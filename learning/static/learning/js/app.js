/* English Daily — toàn bộ phần tương tác phía trình duyệt.
 *
 * Không có đăng nhập: tiến độ, điểm, bài viết lưu trong localStorage (Store),
 * bản ghi âm lưu trong IndexedDB (RecDB). Âm thanh lấy từ /tts/ (giọng neural, cache phía server),
 * nếu lỗi thì dùng giọng đọc có sẵn của trình duyệt.
 */
(function () {
  'use strict';

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const todayISO = () => {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  };
  const addDays = (iso, n) => {
    const d = new Date(iso + 'T00:00:00');
    d.setDate(d.getDate() + n);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  };
  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  const readJSON = (id) => {
    const el = document.getElementById(id);
    return el ? JSON.parse(el.textContent) : null;
  };
  const words = (s) => (s.toLowerCase().replace(/[’‘]/g, "'").match(/[a-z0-9']+/g) || []);

  function toast(msg, icon = 'bi-check-circle-fill') {
    let t = $('.toast-x');
    if (!t) {
      t = document.createElement('div');
      t.className = 'toast-x';
      t.setAttribute('role', 'status');
      document.body.appendChild(t);
    }
    t.innerHTML = `<i class="bi ${icon}"></i><span></span>`;
    $('span', t).textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2200);
  }

  /* =========================================================
   * Store — tiến độ học trong localStorage
   * ========================================================= */
  const STORE_KEY = 'englishDaily:v1';
  const Store = {
    data: null,
    load() {
      try {
        this.data = JSON.parse(localStorage.getItem(STORE_KEY)) || {};
      } catch (e) {
        this.data = {};
      }
      const d = this.data;
      d.days = d.days || {};
      d.quiz = d.quiz || {};
      d.writing = d.writing || {};
      d.srs = d.srs || {};
      d.weeks = d.weeks || {};
      d.rubric = d.rubric || {};
      d.activity = d.activity || {};
      d.settings = d.settings || {};
      return d;
    },
    save() {
      try {
        localStorage.setItem(STORE_KEY, JSON.stringify(this.data));
      } catch (e) {
        toast('Không lưu được tiến độ (bộ nhớ trình duyệt bị chặn?)');
      }
      document.dispatchEvent(new CustomEvent('store:change'));
    },
    day(n) {
      const key = String(n);
      this.data.days[key] = this.data.days[key] || { sections: {}, products: {} };
      return this.data.days[key];
    },
    touch() {
      this.data.activity[todayISO()] = true;
    },
    setSection(dayNo, sec, on) {
      const d = this.day(dayNo);
      d.sections[sec] = !!on;
      if (on) this.touch();
      this.save();
    },
    isDayDone(n) {
      const d = this.data.days[String(n)];
      return !!(d && d.done);
    },
    dayPartial(n) {
      const d = this.data.days[String(n)];
      return !!(d && !d.done && Object.values(d.sections || {}).some(Boolean));
    },
    doneCount() {
      return Object.values(this.data.days).filter((d) => d.done).length;
    },
    streak() {
      // Số ngày học liên tiếp tính đến hôm nay (Chủ nhật không học không làm đứt chuỗi).
      let count = 0;
      let cur = todayISO();
      if (!this.data.activity[cur]) cur = addDays(cur, -1);
      for (let i = 0; i < 400; i++) {
        const isSunday = new Date(cur + 'T00:00:00').getDay() === 0;
        if (this.data.activity[cur]) count++;
        else if (!isSunday) break;
        cur = addDays(cur, -1);
      }
      return count;
    },
  };
  Store.load();

  /* =========================================================
   * Settings
   * ========================================================= */
  const DEFAULTS = { voice: 'ava', speed: 'normal', shadowSpeed: 'slow', gap: 1.3, theme: 'auto', autoplay: true };
  const Settings = {
    get(key) {
      const v = Store.data.settings[key];
      return v === undefined ? DEFAULTS[key] : v;
    },
    set(key, value) {
      Store.data.settings[key] = value;
      Store.save();
    },
  };

  /* ---------- Theme ---------- */
  function applyTheme() {
    const pref = Settings.get('theme');
    const dark = pref === 'dark' || (pref === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.setAttribute('data-bs-theme', dark ? 'dark' : 'light');
    $$('[data-theme-toggle] i').forEach((icon) => (icon.className = dark ? 'bi bi-sun' : 'bi bi-moon-stars'));
  }
  applyTheme();

  /* ---------- Seg control: <div class="seg" data-value> <button data-v> ---------- */
  const Seg = {
    set(el, v) {
      if (!el) return;
      el.dataset.value = String(v);
      $$(':scope > button', el).forEach((b) => b.classList.toggle('on', b.dataset.v === String(v)));
    },
    init(root = document) {
      $$('.seg', root).forEach((el) => this.set(el, el.dataset.value ?? ''));
    },
  };
  document.addEventListener('click', (e) => {
    const b = e.target.closest('.seg > button');
    if (!b) return;
    const seg = b.parentElement;
    if (seg.dataset.value === b.dataset.v) return;
    Seg.set(seg, b.dataset.v);
    seg.dispatchEvent(new CustomEvent('seg:change', { bubbles: true, detail: b.dataset.v }));
  });

  /** Nút phát chính (.play-main): đổi biểu tượng và nhãn khi đang chạy. */
  function setRunning(btn, running, label) {
    btn.dataset.running = running ? '1' : '0';
    btn.classList.toggle('is-running', running);
    const i = $('i', btn);
    if (i) i.className = running ? 'bi bi-stop-fill' : 'bi bi-play-fill';
    const s = $('span', btn);
    if (s) s.textContent = running ? 'Dừng' : label || btn.dataset.label || s.textContent;
  }

  /** Pháo giấy khi hoàn thành ngày học. */
  function confetti() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const box = document.createElement('div');
    box.className = 'confetti';
    const colors = ['#5b4cf0', '#ff6b3d', '#16a34a', '#f59e0b', '#ec4899', '#0ea5a4', '#3b82f6'];
    for (let i = 0; i < 90; i++) {
      const p = document.createElement('i');
      p.style.left = `${Math.random() * 100}%`;
      p.style.background = colors[i % colors.length];
      p.style.setProperty('--dx', `${(Math.random() - 0.5) * 240}px`);
      p.style.setProperty('--rot', `${Math.random() * 900 - 450}deg`);
      p.style.animationDuration = `${2.2 + Math.random() * 1.8}s`;
      p.style.animationDelay = `${Math.random() * 0.4}s`;
      box.appendChild(p);
    }
    document.body.appendChild(box);
    setTimeout(() => box.remove(), 4600);
  }

  /* =========================================================
   * Speech — phát âm thanh (neural TTS từ server, dự phòng Web Speech)
   * ========================================================= */
  const RATE = { slower: 0.65, slow: 0.8, normal: 1, fast: 1.15 };
  const Speech = {
    audio: new Audio(),
    resolver: null,
    serverDownUntil: 0,
    activeEl: null,
    url(text, voice, speed) {
      return `/tts/?t=${encodeURIComponent(text)}&v=${encodeURIComponent(voice)}&s=${encodeURIComponent(speed)}`;
    },
    prefetch(text, opts = {}) {
      if (Date.now() < this.serverDownUntil || !text) return;
      const voice = opts.voice || Settings.get('voice');
      const speed = opts.speed || Settings.get('speed');
      fetch(this.url(text, voice, speed)).catch(() => {});
    },
    _finish(result) {
      if (this.resolver) {
        const r = this.resolver;
        this.resolver = null;
        r(result);
      }
      if (this.activeEl) {
        this.activeEl.classList.remove('is-playing', 'is-loading');
        this.activeEl = null;
      }
    },
    stop() {
      this.audio.pause();
      this.audio.removeAttribute('src');
      if (window.speechSynthesis) window.speechSynthesis.cancel();
      this._finish(false);
    },
    /** Phát một câu; Promise trả về true nếu phát xong, false nếu bị dừng. */
    play(text, opts = {}) {
      this.stop();
      const voice = opts.voice || Settings.get('voice');
      const speed = opts.speed || Settings.get('speed');
      const el = opts.el || null;
      if (el) {
        this.activeEl = el;
        el.classList.add('is-loading');
      }
      return new Promise((resolve) => {
        this.resolver = resolve;
        const myResolver = resolve;
        const fallback = () => {
          if (this.resolver !== myResolver) return;
          this._speakFallback(text, speed);
        };
        if (Date.now() < this.serverDownUntil) {
          fallback();
          return;
        }
        const a = this.audio;
        a.onplaying = () => {
          if (el && this.resolver === myResolver) {
            el.classList.remove('is-loading');
            el.classList.add('is-playing');
          }
        };
        a.onended = () => {
          if (this.resolver === myResolver) this._finish(true);
        };
        const src = this.url(text, voice, speed);
        a.onerror = () => {
          if (this.resolver !== myResolver || !a.src.endsWith(src)) return;
          this.serverDownUntil = Date.now() + 60000;
          fallback();
        };
        a.src = src;
        a.play().catch((err) => {
          if (this.resolver !== myResolver) return;
          if (err && err.name === 'AbortError') return;
          if (err && err.name === 'NotAllowedError') {
            this._finish(false);
            return;
          }
          fallback();
        });
      });
    },
    _pickVoice() {
      if (!window.speechSynthesis) return null;
      const voices = window.speechSynthesis.getVoices().filter((v) => /^en[-_]/i.test(v.lang));
      const prefer = [/natural/i, /google us english/i, /aria|jenny|ava|emma|samantha/i, /en[-_]us/i];
      for (const re of prefer) {
        const v = voices.find((x) => re.test(x.name) || re.test(x.lang));
        if (v) return v;
      }
      return voices[0] || null;
    },
    _speakFallback(text, speed) {
      if (!window.speechSynthesis) {
        this._finish(false);
        return;
      }
      const u = new SpeechSynthesisUtterance(text);
      const v = this._pickVoice();
      if (v) u.voice = v;
      u.lang = (v && v.lang) || 'en-US';
      u.rate = RATE[speed] || 1;
      const resolver = this.resolver;
      u.onstart = () => {
        if (this.activeEl) {
          this.activeEl.classList.remove('is-loading');
          this.activeEl.classList.add('is-playing');
        }
      };
      u.onend = () => {
        if (this.resolver === resolver) this._finish(true);
      };
      u.onerror = () => {
        if (this.resolver === resolver) this._finish(false);
      };
      window.speechSynthesis.speak(u);
    },
  };
  if (window.speechSynthesis) window.speechSynthesis.onvoiceschanged = () => {};

  /* ---------- Tải trước âm thanh của trang trong nền để bấm là nghe ngay ---------- */
  const Prefetch = {
    queue: [],
    seen: new Set(),
    running: 0,
    add(text, opts = {}) {
      if (!text) return;
      const key = `${opts.voice || ''}|${opts.speed || ''}|${text}`;
      if (this.seen.has(key)) return;
      this.seen.add(key);
      this.queue.push([text, opts]);
    },
    start(delay = 1200) {
      setTimeout(() => this._pump(), delay);
    },
    _pump() {
      while (this.running < 2 && this.queue.length) {
        if (Date.now() < Speech.serverDownUntil) {
          this.queue = [];
          return;
        }
        const [text, opts] = this.queue.shift();
        const voice = opts.voice || Settings.get('voice');
        const speed = opts.speed || Settings.get('speed');
        this.running++;
        fetch(Speech.url(text, voice, speed))
          .then((r) => r.ok && r.blob())
          .catch(() => {})
          .finally(() => {
            this.running--;
            this._pump();
          });
      }
    },
  };

  /* ---------- Sequence: chuỗi phát dài (shadowing, hội thoại) có thể dừng ---------- */
  const Seq = {
    token: 0,
    label: '',
    start(label, onStop) {
      this.cancel();
      this.token++;
      this.label = label;
      this.onStop = onStop || null;
      const pill = $('#now-playing');
      if (pill) {
        $('.txt', pill).textContent = label;
        pill.classList.add('show');
      }
      return this.token;
    },
    alive(tok) {
      return tok === this.token;
    },
    cancel() {
      if (this.onStop) {
        const f = this.onStop;
        this.onStop = null;
        f();
      }
      this.token++;
      Speech.stop();
      const pill = $('#now-playing');
      if (pill) pill.classList.remove('show');
    },
    end(tok) {
      if (tok !== this.token) return;
      if (this.onStop) {
        const f = this.onStop;
        this.onStop = null;
        f();
      }
      const pill = $('#now-playing');
      if (pill) pill.classList.remove('show');
    },
    /** Chờ ms mili-giây, cập nhật thanh tiến trình (nếu có); trả về false nếu bị hủy. */
    async wait(tok, ms, bar) {
      const t0 = performance.now();
      while (performance.now() - t0 < ms) {
        if (!this.alive(tok)) return false;
        if (bar) bar.style.width = `${Math.min(100, ((performance.now() - t0) / ms) * 100)}%`;
        await sleep(60);
      }
      if (bar) bar.style.width = '100%';
      return this.alive(tok);
    },
  };

  /* ---------- Nút phát nhanh: [data-say] và các đoạn tiếng Anh trong bài học ---------- */
  function sayButton(text, speed, cls = '') {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = `say-btn sm ${cls}`.trim();
    b.dataset.say = text;
    if (speed && speed !== 'normal') b.dataset.speed = speed;
    b.title = speed === 'slow' ? 'Nghe chậm' : 'Nghe';
    b.innerHTML = speed === 'slow' ? '<i class="bi bi-hourglass-split"></i>' : '<i class="bi bi-volume-up"></i>';
    return b;
  }

  function enhanceLesson(root = document) {
    $$('.lesson .say', root).forEach((el) => {
      el.classList.add('say-inline');
      el.dataset.say = el.textContent.trim();
      el.setAttribute('role', 'button');
      el.title = 'Bấm để nghe';
    });
    $$('.lesson .ex .en, .lesson .fix .en', root).forEach((el) => {
      if (el.querySelector('.say-btn')) return;
      const text = el.textContent.trim();
      el.appendChild(sayButton(text, 'normal'));
      el.appendChild(sayButton(text, 'slow', 'slow'));
    });
    $$('.lesson table', root).forEach((t) => {
      if (t.parentElement.classList.contains('table-wrap')) return;
      const w = document.createElement('div');
      w.className = 'table-wrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }

  document.addEventListener('click', (e) => {
    const el = e.target.closest('[data-say]');
    if (!el) return;
    e.preventDefault();
    e.stopPropagation();
    if (el.classList.contains('is-playing') || el.classList.contains('is-loading')) {
      Seq.cancel();
      return;
    }
    Seq.cancel();
    Speech.play(el.dataset.say, { speed: el.dataset.speed, voice: el.dataset.voice, el });
  });

  /* =========================================================
   * Pron — chấm phát âm bằng nhận dạng giọng nói (Chrome/Edge)
   * ========================================================= */
  const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const Pron = {
    supported: !!Recognition,
    listen() {
      return new Promise((resolve, reject) => {
        const rec = new Recognition();
        rec.lang = 'en-US';
        rec.interimResults = false;
        rec.maxAlternatives = 3;
        let done = false;
        rec.onresult = (ev) => {
          done = true;
          resolve(Array.from(ev.results[0]).map((a) => a.transcript));
        };
        rec.onerror = (ev) => {
          done = true;
          reject(ev.error);
        };
        rec.onend = () => {
          if (!done) resolve([]);
        };
        rec.start();
      });
    },
    compare(target, heardList) {
      const t = words(target);
      let best = { score: 0, heard: '', marks: t.map(() => false) };
      heardList.forEach((h) => {
        const hw = words(h);
        const pool = hw.slice();
        const marks = t.map((w) => {
          const i = pool.indexOf(w);
          if (i >= 0) {
            pool.splice(i, 1);
            return true;
          }
          return false;
        });
        const score = t.length ? Math.round((marks.filter(Boolean).length / t.length) * 100) : 0;
        if (score >= best.score) best = { score, heard: h, marks };
      });
      const shown = target.split(/\s+/);
      let wi = 0;
      const html = shown
        .map((tok) => {
          const has = words(tok).length > 0;
          const ok = has ? best.marks[wi++] : true;
          return `<span class="${ok ? 'w-ok' : 'w-miss'}">${esc(tok)}</span>`;
        })
        .join(' ');
      return { ...best, html };
    },
    async check(target, out, btn) {
      if (!this.supported) {
        toast('Trình duyệt chưa hỗ trợ nhận dạng giọng nói. Dùng Chrome hoặc Edge.');
        return;
      }
      Seq.cancel();
      btn && btn.classList.add('is-playing');
      out.innerHTML = '<span class="muted"><i class="bi bi-mic"></i> Đang nghe… hãy đọc câu.</span>';
      try {
        const heard = await this.listen();
        if (!heard.length) {
          out.innerHTML = '<span class="muted">Không nghe thấy gì. Thử lại nhé.</span>';
          return;
        }
        const r = this.compare(target, heard);
        const emoji = r.score >= 90 ? '🎉' : r.score >= 70 ? '👍' : '💪';
        out.innerHTML = `<div><b>${emoji} ${r.score}%</b> · ${r.html}</div><div class="muted small">Máy nghe được: “${esc(r.heard)}”</div>`;
      } catch (err) {
        out.innerHTML = `<span class="muted">Không dùng được micro (${esc(err)}).</span>`;
      } finally {
        btn && btn.classList.remove('is-playing');
      }
    },
  };

  /* =========================================================
   * RecDB — lưu bản ghi âm trong IndexedDB
   * ========================================================= */
  const RecDB = {
    db: null,
    open() {
      if (this.db) return Promise.resolve(this.db);
      return new Promise((resolve, reject) => {
        const req = indexedDB.open('englishDaily', 1);
        req.onupgradeneeded = () => {
          const store = req.result.createObjectStore('recordings', { keyPath: 'id', autoIncrement: true });
          store.createIndex('key', 'key');
          store.createIndex('day', 'day');
        };
        req.onsuccess = () => {
          this.db = req.result;
          resolve(this.db);
        };
        req.onerror = () => reject(req.error);
      });
    },
    async tx(mode, fn) {
      const db = await this.open();
      return new Promise((resolve, reject) => {
        const t = db.transaction('recordings', mode);
        const store = t.objectStore('recordings');
        const out = fn(store);
        t.oncomplete = () => resolve(out && 'result' in out ? out.result : undefined);
        t.onerror = () => reject(t.error);
      });
    },
    add(rec) {
      return this.tx('readwrite', (s) => s.add(rec));
    },
    remove(id) {
      return this.tx('readwrite', (s) => s.delete(id));
    },
    byKey(key) {
      return this.tx('readonly', (s) => s.index('key').getAll(key));
    },
    all() {
      return this.tx('readonly', (s) => s.getAll());
    },
  };

  const Mic = {
    stream: null,
    async get() {
      if (this.stream && this.stream.active) return this.stream;
      this.stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true } });
      return this.stream;
    },
    release() {
      if (this.stream) this.stream.getTracks().forEach((t) => t.stop());
      this.stream = null;
    },
    async record(onTick) {
      const stream = await this.get();
      const mime = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4', 'audio/ogg'].find((m) => window.MediaRecorder && MediaRecorder.isTypeSupported(m)) || '';
      const mr = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
      const chunks = [];
      const t0 = Date.now();
      const timer = setInterval(() => onTick && onTick((Date.now() - t0) / 1000), 250);
      mr.ondataavailable = (e) => e.data.size && chunks.push(e.data);
      const done = new Promise((resolve) => {
        mr.onstop = () => {
          clearInterval(timer);
          this.release();
          resolve({ blob: new Blob(chunks, { type: mr.mimeType || 'audio/webm' }), duration: (Date.now() - t0) / 1000 });
        };
      });
      mr.start();
      return { stop: () => mr.state !== 'inactive' && mr.stop(), done };
    },
  };

  const fmtTime = (sec) => `${Math.floor(sec / 60)}:${String(Math.floor(sec % 60)).padStart(2, '0')}`;
  const fmtDate = (ts) => new Date(ts).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });

  function takeRow(rec, onDelete) {
    const row = document.createElement('div');
    row.className = 'take';
    const url = URL.createObjectURL(rec.blob);
    row.innerHTML = `<span class="chip sm tabular"><i class="bi bi-mic-fill"></i> ${fmtTime(rec.duration || 0)}</span>
      <span class="faint">${fmtDate(rec.created)}</span>
      <audio controls preload="metadata" src="${url}"></audio>
      <a class="icon-btn" download="${esc((rec.label || 'recording').replace(/[^\w\- ]+/g, ''))}.webm" href="${url}" title="Tải về" aria-label="Tải về"><i class="bi bi-download"></i></a>
      <button type="button" class="icon-btn btn-danger-quiet" title="Xóa" aria-label="Xóa bản ghi"><i class="bi bi-trash"></i></button>`;
    $('button', row).addEventListener('click', async () => {
      if (!confirm('Xóa bản ghi này?')) return;
      await RecDB.remove(rec.id);
      URL.revokeObjectURL(url);
      row.remove();
      onDelete && onDelete();
    });
    return row;
  }

  /** Widget ghi âm: <div class="recorder" data-key data-day data-label data-seconds> */
  function initRecorder(el) {
    const key = el.dataset.key;
    const target = Number(el.dataset.seconds || 0);
    el.innerHTML = `<div class="rec-top">
        <button type="button" class="rec-btn" aria-label="Bắt đầu ghi âm"><i class="bi bi-mic-fill"></i></button>
        <div class="rec-info">
          <div class="t">Bấm để ghi âm</div>
          <div class="d-flex align-items-baseline gap-2"><span class="rec-timer">0:00</span>${target ? `<span class="s">/ mục tiêu ${fmtTime(target)}</span>` : ''}</div>
          ${target ? '<div class="bar thin mt-2"><span></span></div>' : ''}
        </div>
      </div>
      <div class="takes"></div>`;
    const btn = $('.rec-btn', el);
    const label = $('.rec-info .t', el);
    const timerEl = $('.rec-timer', el);
    const bar = $('.bar span', el);
    const takes = $('.takes', el);
    let session = null;

    const refresh = async () => {
      try {
        const list = (await RecDB.byKey(key)).sort((a, b) => b.created - a.created);
        takes.innerHTML = '';
        label.textContent = list.length ? `Bấm để ghi âm · đã có ${list.length} bản` : 'Bấm để ghi âm';
        list.forEach((r) => takes.appendChild(takeRow(r, refresh)));
      } catch (e) {
        takes.innerHTML = '<div class="faint" style="font-size:.84rem">Trình duyệt không cho lưu bản ghi (IndexedDB bị chặn).</div>';
      }
    };

    btn.addEventListener('click', async () => {
      if (session) {
        session.stop();
        return;
      }
      Seq.cancel();
      try {
        session = await Mic.record((sec) => {
          timerEl.textContent = fmtTime(sec);
          if (bar) bar.style.width = `${Math.min(100, (sec / target) * 100)}%`;
        });
      } catch (e) {
        toast('Không mở được micro. Hãy cho phép quyền micro cho trang này.', 'bi-mic-mute-fill');
        return;
      }
      btn.classList.add('is-recording');
      btn.setAttribute('aria-label', 'Dừng và lưu');
      label.textContent = 'Đang ghi… bấm để dừng & lưu';
      $('i', btn).className = 'bi bi-stop-fill';
      const { blob, duration } = await session.done;
      session = null;
      btn.classList.remove('is-recording');
      btn.setAttribute('aria-label', 'Bắt đầu ghi âm');
      $('i', btn).className = 'bi bi-mic-fill';
      if (duration < 1) {
        refresh();
        return;
      }
      await RecDB.add({ key, day: Number(el.dataset.day || 0), week: Number(el.dataset.week || 0), label: el.dataset.label || key, created: Date.now(), duration, blob });
      Store.touch();
      Store.save();
      toast('Đã lưu bản ghi âm');
      refresh();
    });
    refresh();
  }

  /* ---------- Ghi âm nhanh để so sánh (không lưu): dùng trong shadowing ---------- */
  const QuickRec = {
    session: null,
    async toggle(btn, modelText, opts) {
      if (this.session) {
        this.session.stop();
        return;
      }
      Seq.cancel();
      try {
        this.session = await Mic.record();
      } catch (e) {
        toast('Không mở được micro.');
        return;
      }
      btn.classList.add('is-playing');
      btn.title = 'Dừng';
      const { blob } = await this.session.done;
      this.session = null;
      btn.classList.remove('is-playing');
      btn.title = 'Ghi âm & so sánh';
      // Phát giọng mẫu rồi tới giọng của bạn
      const tok = Seq.start('So sánh: giọng mẫu → giọng bạn');
      await Speech.play(modelText, opts);
      if (!Seq.alive(tok)) return;
      await sleep(350);
      const a = new Audio(URL.createObjectURL(blob));
      await new Promise((r) => {
        a.onended = r;
        a.onerror = r;
        a.play().catch(r);
      });
      Seq.end(tok);
    },
  };

  /* =========================================================
   * Shadowing player
   * ========================================================= */
  function initShadow(el) {
    const items = $$('.shadow-item', el);
    if (!items.length) return;
    const bar = $('.player-bar', el);
    const playBtn = $('[data-act="play"]', bar);
    const speedSeg = $('[data-opt="speed"]', bar);
    const repSeg = $('[data-opt="reps"]', bar);
    const pauseSeg = $('[data-opt="pause"]', bar);
    const speed = () => speedSeg.dataset.value;
    Seg.set(speedSeg, Settings.get('shadowSpeed'));
    speedSeg.addEventListener('seg:change', () => Settings.set('shadowSpeed', speed()));

    $('[data-act="hide-text"]', bar)?.addEventListener('click', (e) => {
      el.classList.toggle('hide-text');
      e.currentTarget.classList.toggle('active');
    });
    $('[data-act="hide-vi"]', bar)?.addEventListener('click', (e) => {
      el.classList.toggle('hide-vi');
      e.currentTarget.classList.toggle('active');
    });

    items.forEach((it) => {
      const text = it.dataset.text;
      const tools = $('.tools', it);
      const voice = it.dataset.voice || undefined;
      tools.innerHTML = '';
      const b1 = sayButton(text, 'normal');
      if (voice) b1.dataset.voice = voice;
      const b2 = sayButton(text, 'slow', 'slow');
      if (voice) b2.dataset.voice = voice;
      const rec = document.createElement('button');
      rec.type = 'button';
      rec.className = 'say-btn sm';
      rec.title = 'Ghi âm & so sánh với giọng mẫu';
      rec.innerHTML = '<i class="bi bi-mic"></i>';
      rec.addEventListener('click', (e) => {
        e.stopPropagation();
        QuickRec.toggle(rec, text, { speed: speed(), voice });
      });
      tools.append(b1, b2, rec);
      if (Pron.supported) {
        const chk = document.createElement('button');
        chk.type = 'button';
        chk.className = 'say-btn sm';
        chk.title = 'Chấm phát âm (máy nghe bạn đọc)';
        chk.innerHTML = '<i class="bi bi-patch-check"></i>';
        chk.addEventListener('click', (e) => {
          e.stopPropagation();
          Pron.check(text, $('.pron-result', it), chk);
        });
        tools.append(chk);
      }
      it.addEventListener('click', () => it.classList.toggle('revealed'));
    });

    const stopUI = () => {
      setRunning(playBtn, false);
      items.forEach((i) => i.classList.remove('is-current', 'is-your-turn'));
    };

    playBtn.addEventListener('click', async () => {
      if (playBtn.dataset.running === '1') {
        Seq.cancel();
        return;
      }
      const tok = Seq.start('Shadowing — nghe rồi nhắc lại', stopUI);
      setRunning(playBtn, true);
      const reps = Number(repSeg.dataset.value);
      const pauseMul = Number(pauseSeg.dataset.value);
      const startAt = Math.max(0, items.findIndex((i) => i.classList.contains('is-current')));
      for (let i = startAt; i < items.length; i++) {
        const it = items[i];
        items.forEach((x) => x.classList.remove('is-current'));
        it.classList.add('is-current');
        it.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        if (items[i + 1]) Speech.prefetch(items[i + 1].dataset.text, { speed: speed(), voice: items[i + 1].dataset.voice });
        for (let r = 0; r < reps; r++) {
          const t0 = performance.now();
          const ok = await Speech.play(it.dataset.text, { speed: speed(), voice: it.dataset.voice });
          if (!Seq.alive(tok)) return;
          if (!ok) break;
          const dur = performance.now() - t0;
          if (pauseMul > 0) {
            it.classList.add('is-your-turn');
            const turnBar = $('.turn-bar span', it);
            const alive = await Seq.wait(tok, dur * pauseMul + 700, turnBar);
            it.classList.remove('is-your-turn');
            if (!alive) return;
          } else {
            if (!(await Seq.wait(tok, 500))) return;
          }
        }
      }
      items.forEach((x) => x.classList.remove('is-current'));
      Seq.end(tok);
      toast('Xong một lượt shadowing 👏', 'bi-stars');
    });
  }

  /* =========================================================
   * Dialogue player (nghe hội thoại, đóng vai)
   * ========================================================= */
  function initDialogue(el) {
    const lines = $$('.line', el);
    const bar = $('.player-bar', el);
    const playBtn = $('[data-act="play"]', bar);
    const speedSeg = $('[data-opt="speed"]', bar);
    const speed = () => speedSeg.dataset.value;
    const roleSeg = $('[data-opt="role"]', bar);
    const role = () => (roleSeg ? roleSeg.dataset.value : '');
    const scriptBtn = $('[data-act="script"]', bar);
    const viBtn = $('[data-act="vi"]', bar);

    scriptBtn.addEventListener('click', () => {
      el.classList.toggle('hide-script');
      scriptBtn.classList.toggle('active', !el.classList.contains('hide-script'));
      const hidden = el.classList.contains('hide-script');
      scriptBtn.innerHTML = hidden ? '<i class="bi bi-eye"></i> Hiện lời' : '<i class="bi bi-eye-slash"></i> Ẩn lời';
    });
    viBtn.addEventListener('click', () => {
      el.classList.toggle('show-vi');
      viBtn.classList.toggle('active');
    });
    const applyRole = () => {
      lines.forEach((ln) => ln.classList.toggle('is-mine', role() !== '' && ln.dataset.speaker === role()));
    };
    roleSeg?.addEventListener('seg:change', applyRole);

    lines.forEach((ln) => {
      ln.addEventListener('click', (e) => {
        if (e.target.closest('button')) return;
        Seq.cancel();
        lines.forEach((x) => x.classList.remove('is-current'));
        ln.classList.add('is-current');
        Speech.play(ln.dataset.text, { voice: ln.dataset.voice, speed: speed() });
      });
    });

    const stopUI = () => {
      setRunning(playBtn, false, 'Phát cả bài');
      lines.forEach((x) => x.classList.remove('is-current', 'is-your-turn'));
    };

    playBtn.addEventListener('click', async () => {
      if (playBtn.dataset.running === '1') {
        Seq.cancel();
        return;
      }
      const tok = Seq.start(role() ? 'Đóng vai — đến lượt bạn thì nói' : 'Đang phát hội thoại', stopUI);
      setRunning(playBtn, true);
      for (let i = 0; i < lines.length; i++) {
        const ln = lines[i];
        lines.forEach((x) => x.classList.remove('is-current'));
        ln.classList.add('is-current');
        ln.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        const next = lines[i + 1];
        if (next) Speech.prefetch(next.dataset.text, { voice: next.dataset.voice, speed: speed() });
        if (role() && ln.dataset.speaker === role()) {
          ln.classList.add('is-your-turn');
          const ms = Math.max(2200, words(ln.dataset.text).length * 520 + 1200);
          const alive = await Seq.wait(tok, ms, $('.turn-bar span', ln));
          ln.classList.remove('is-your-turn');
          if (!alive) return;
        } else {
          const ok = await Speech.play(ln.dataset.text, { voice: ln.dataset.voice, speed: speed() });
          if (!Seq.alive(tok)) return;
          if (!ok) break;
          if (!(await Seq.wait(tok, 380))) return;
        }
      }
      Seq.end(tok);
    });
  }

  /* =========================================================
   * Quiz
   * ========================================================= */
  function initQuiz(el) {
    const key = el.dataset.key;
    const qs = $$('.q', el);
    const result = $('.quiz-result', el);
    const letters = 'ABCDEFGH';

    qs.forEach((q) => {
      const answer = Number(q.dataset.answer);
      const opts = $$('.opt', q);
      opts.forEach((o, i) => {
        if (!$('.k', o)) o.insertAdjacentHTML('afterbegin', `<span class="k">${letters[i]}</span>`);
        o.addEventListener('click', () => {
          if (q.classList.contains('answered')) return;
          q.classList.add('answered');
          q.dataset.correct = i === answer ? '1' : '0';
          opts.forEach((x, j) => {
            x.disabled = true;
            if (j === answer) x.classList.add('is-right');
          });
          if (i !== answer) o.classList.add('is-wrong');
          check();
        });
      });
    });

    const check = () => {
      const answered = qs.filter((q) => q.classList.contains('answered'));
      const right = answered.filter((q) => q.dataset.correct === '1').length;
      $$('[data-quiz-progress]', el).forEach((p) => (p.textContent = `${answered.length}/${qs.length}`));
      if (answered.length < qs.length) return;
      el.classList.add('finished');
      const pct = Math.round((right / qs.length) * 100);
      $('.score-big', result).textContent = `${right}/${qs.length}`;
      const ring = $('[data-quiz-ring]', result);
      if (ring) {
        ring.style.setProperty('--p', pct);
        ring.style.setProperty('--fill', pct >= 70 ? 'var(--ok)' : pct >= 50 ? 'var(--warn)' : 'var(--bad)');
      }
      $('.score-msg', result).textContent = pct >= 90 ? 'Xuất sắc! 🎉' : pct >= 70 ? 'Tốt lắm! Xem lại các câu sai nhé.' : 'Cần ôn thêm — đọc kỹ giải thích các câu sai rồi làm lại.';
      if (key) {
        const prev = Store.data.quiz[key];
        Store.data.quiz[key] = { score: right, total: qs.length, at: Date.now(), best: Math.max(right, prev ? prev.best || prev.score : 0) };
        if (el.dataset.section && el.dataset.day) Store.day(el.dataset.day).sections[el.dataset.section] = true;
        Store.touch();
        Store.save();
      }
      result.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    };

    $('[data-act="retry"]', el)?.addEventListener('click', () => {
      el.classList.remove('finished');
      qs.forEach((q) => {
        q.classList.remove('answered');
        delete q.dataset.correct;
        $$('.opt', q).forEach((o) => {
          o.disabled = false;
          o.classList.remove('is-right', 'is-wrong');
        });
      });
      check();
      el.scrollIntoView({ behavior: 'smooth' });
    });

    const prev = key && Store.data.quiz[key];
    if (prev) {
      const info = $('.quiz-prev', el);
      if (info) info.textContent = `Lần trước: ${prev.score}/${prev.total} · cao nhất ${prev.best ?? prev.score}/${prev.total}`;
    }
    check();
  }

  /* =========================================================
   * Dictation — nghe và chép chính tả
   * ========================================================= */
  function lcsDiff(target, typed) {
    const a = words(target);
    const b = words(typed);
    const dp = Array.from({ length: a.length + 1 }, () => new Array(b.length + 1).fill(0));
    for (let i = a.length - 1; i >= 0; i--) for (let j = b.length - 1; j >= 0; j--) dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    const out = [];
    let i = 0;
    let j = 0;
    while (i < a.length || j < b.length) {
      if (i < a.length && j < b.length && a[i] === b[j]) {
        out.push(`<span class="ok">${esc(a[i])}</span>`);
        i++;
        j++;
      } else if (j < b.length && (i >= a.length || dp[i][j + 1] >= dp[i + 1][j])) {
        out.push(`<span class="bad">${esc(b[j])}</span>`);
        j++;
      } else {
        out.push(`<span class="miss">${esc(a[i])}</span>`);
        i++;
      }
    }
    return { html: out.join(' '), score: a.length ? Math.round((dp[0][0] / a.length) * 100) : 0 };
  }

  function initDictation(el) {
    const speed = el.dataset.speed || 'normal';
    $$('.dict-item', el).forEach((it) => {
      const text = it.dataset.text;
      const input = $('input', it);
      const out = $('.dict-diff', it);
      $('[data-act="play"]', it).addEventListener('click', () => Speech.play(text, { speed }));
      $('[data-act="slow"]', it).addEventListener('click', () => Speech.play(text, { speed: 'slower' }));
      const check = () => {
        const r = lcsDiff(text, input.value);
        out.innerHTML = `<b>${r.score}%</b> · ${r.html}<div class="muted small mt-1">Đáp án: ${esc(text)}</div>`;
      };
      $('[data-act="check"]', it).addEventListener('click', check);
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          check();
        }
      });
    });
  }

  /* =========================================================
   * Writing — tự lưu bản nháp, đếm từ, nghe lại bài viết
   * ========================================================= */
  function initWriting(el) {
    const key = el.dataset.key;
    const ta = $('textarea', el);
    const count = $('.wc', el);
    const min = Number(el.dataset.min || 0);
    ta.value = Store.data.writing[key] || '';
    let timer;
    const update = () => {
      const n = words(ta.value).length;
      count.textContent = `${n} từ${min ? ` / tối thiểu ${min}` : ''}`;
      count.style.color = min && n >= min ? 'var(--ok)' : '';
      const wb = $('[data-wc-bar]', el);
      if (wb) {
        wb.style.width = `${min ? Math.min(100, (n / min) * 100) : n ? 100 : 0}%`;
        wb.style.background = min && n >= min ? 'var(--ok)' : '';
      }
    };
    ta.addEventListener('input', () => {
      update();
      clearTimeout(timer);
      timer = setTimeout(() => {
        Store.data.writing[key] = ta.value;
        Store.touch();
        Store.save();
        const s = $('.saved', el);
        if (s) {
          s.innerHTML = '<i class="bi bi-cloud-check"></i> Đã lưu';
          setTimeout(() => (s.textContent = ''), 1500);
        }
      }, 600);
    });
    $('[data-act="listen-mine"]', el)?.addEventListener('click', (e) => {
      const txt = ta.value.trim();
      if (!txt) return toast('Bạn chưa viết gì.');
      Seq.cancel();
      Speech.play(txt.slice(0, 1500), { el: e.currentTarget });
    });
    $('[data-act="model"]', el)?.addEventListener('click', (e) => {
      $('.model-wrap', el).classList.toggle('hidden');
      e.currentTarget.classList.toggle('active');
    });
    update();
  }

  /* =========================================================
   * Rubric (tự chấm 4 tiêu chí) & tự đánh giá tuần
   * ========================================================= */
  function initRating(el, getObj, onSave) {
    $$('.rate', el).forEach((group) => {
      const field = group.dataset.field;
      const btns = $$('button', group);
      const paint = () => {
        const v = (getObj() || {})[field];
        btns.forEach((b) => b.classList.toggle('on', Number(b.dataset.v) <= (v || 0)));
      };
      btns.forEach((b) =>
        b.addEventListener('click', () => {
          onSave(field, Number(b.dataset.v));
          paint();
        })
      );
      paint();
    });
  }

  function initRubric(el) {
    const key = el.dataset.key;
    initRating(el, () => Store.data.rubric[key], (field, v) => {
      Store.data.rubric[key] = { ...(Store.data.rubric[key] || {}), [field]: v, at: Date.now() };
      Store.save();
      showAvg();
    });
    const showAvg = () => {
      const r = Store.data.rubric[key];
      const out = $('.rubric-avg', el);
      if (!r || !out) return;
      const vals = ['fluency', 'vocab', 'grammar', 'pron'].map((k) => r[k]).filter(Boolean);
      if (vals.length) out.textContent = `Trung bình: ${(vals.reduce((a, b) => a + b, 0) / vals.length).toFixed(1)} / 5`;
    };
    showAvg();
  }

  function initWeekAssess(el) {
    const w = el.dataset.week;
    const get = () => Store.data.weeks[w];
    initRating(el, get, (field, v) => {
      Store.data.weeks[w] = { ...(get() || {}), [field]: v };
      Store.save();
    });
    const ta = $('textarea', el);
    if (ta) {
      ta.value = (get() || {}).note || '';
      ta.addEventListener('input', () => {
        Store.data.weeks[w] = { ...(get() || {}), note: ta.value };
        Store.save();
      });
    }
  }

  /* =========================================================
   * Day page — đánh dấu phần đã xong, sản phẩm, hoàn thành ngày
   * ========================================================= */
  function addWordsToSRS(list) {
    const today = todayISO();
    let added = 0;
    list.forEach((w) => {
      const k = w.word.toLowerCase();
      if (!Store.data.srs[k]) {
        Store.data.srs[k] = { box: 0, due: today, day: w.day };
        added++;
      }
    });
    return added;
  }

  function initDayPage(root) {
    const dayNo = root.dataset.day;
    const vocab = readJSON('vocab-data') || [];

    const paint = () => {
      const d = Store.day(dayNo);
      $$('.sec-done').forEach((b) => {
        const on = !!d.sections[b.dataset.sec];
        b.classList.toggle('is-on', on);
        b.innerHTML = on ? '<i class="bi bi-check-circle-fill"></i> Đã xong' : '<i class="bi bi-circle"></i> Đánh dấu xong';
      });
      $$('[data-toc]').forEach((a) => a.classList.toggle('done', !!d.sections[a.dataset.toc]));
      const total = $$('.sec-done').length;
      const done = $$('.sec-done').filter((b) => d.sections[b.dataset.sec]).length;
      const pct = d.done ? 100 : total ? Math.round((done / total) * 100) : 0;
      $$('[data-day-progress]').forEach((p) => (p.style.width = `${pct}%`));
      $$('[data-day-progress-text]').forEach((p) => (p.textContent = `${done}/${total}`));
      $$('[data-day-progress-label]').forEach((p) => (p.textContent = d.done ? 'Đã hoàn thành' : `${done}/${total} phần · ${pct}%`));
      $$('[data-day-ring]').forEach((r) => r.style.setProperty('--p', pct));
      const start = $('[data-act="start-day"] span');
      if (start) start.textContent = d.done ? 'Ôn lại bài' : done ? 'Học tiếp' : 'Bắt đầu học';
      const fin = $('#finish-day');
      if (fin) {
        fin.classList.toggle('done', !!d.done);
        fin.innerHTML = d.done ? `<i class="bi bi-trophy-fill"></i> Đã hoàn thành ngày ${dayNo}${d.doneAt ? ' · ' + d.doneAt.split('-').reverse().join('/') : ''}` : `<i class="bi bi-flag-fill"></i> Hoàn thành ngày ${dayNo}`;
      }
    };
    // Nút "Học tiếp" nhảy tới phần đầu tiên chưa xong
    $('[data-act="start-day"]')?.addEventListener('click', (e) => {
      const d = Store.day(dayNo);
      const first = $$('.sec-done').find((b) => !d.sections[b.dataset.sec]);
      if (first && !d.done) {
        e.preventDefault();
        document.getElementById(first.dataset.sec)?.scrollIntoView({ behavior: 'smooth' });
      }
    });

    $$('.sec-done').forEach((b) =>
      b.addEventListener('click', () => {
        const d = Store.day(dayNo);
        const on = !d.sections[b.dataset.sec];
        if (b.dataset.sec === 'vocab' && on) {
          const n = addWordsToSRS(vocab);
          if (n) toast(`Đã thêm ${n} từ vào lịch ôn tập`);
        }
        Store.setSection(dayNo, b.dataset.sec, on);
        paint();
      })
    );

    // Sản phẩm kiểm tra
    $$('.products input[type=checkbox]').forEach((cb) => {
      const d = Store.day(dayNo);
      cb.checked = !!d.products[cb.dataset.i];
      cb.addEventListener('change', () => {
        Store.day(dayNo).products[cb.dataset.i] = cb.checked;
        Store.touch();
        Store.save();
      });
    });
    const notes = $('#day-notes');
    if (notes) {
      notes.value = Store.day(dayNo).notes || '';
      notes.addEventListener('input', () => {
        Store.day(dayNo).notes = notes.value;
        Store.save();
      });
    }

    $('#finish-day')?.addEventListener('click', () => {
      const d = Store.day(dayNo);
      if (d.done) {
        if (!confirm('Bỏ đánh dấu hoàn thành ngày này?')) return;
        d.done = false;
        Store.save();
        paint();
        return;
      }
      d.done = true;
      d.doneAt = todayISO();
      addWordsToSRS(vocab);
      Store.touch();
      Store.save();
      paint();
      confetti();
      toast(`Tuyệt vời! Đã xong ngày ${dayNo} 🎉`, 'bi-trophy-fill');
    });

    // Mục lục: tô sáng phần đang đọc
    const secs = $$('.section');
    if ('IntersectionObserver' in window && secs.length) {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((en) => {
            if (!en.isIntersecting) return;
            $$('[data-toc]').forEach((a) => a.classList.toggle('current', a.dataset.toc === en.target.dataset.section));
            const pill = $(`.chipnav [data-toc="${en.target.dataset.section}"]`);
            const nav = pill && pill.parentElement;
            if (nav && nav.scrollWidth > nav.clientWidth) nav.scrollTo({ left: pill.offsetLeft - nav.clientWidth / 2 + pill.clientWidth / 2, behavior: 'smooth' });
          });
        },
        { rootMargin: '-30% 0px -60% 0px' }
      );
      secs.forEach((s) => io.observe(s));
    }

    // Từ vựng: ẩn nghĩa để tự kiểm tra, nghe tất cả
    $('[data-act="hide-meaning"]')?.addEventListener('click', (e) => {
      $('#vocab-list').classList.toggle('hide-meaning');
      e.currentTarget.classList.toggle('active');
    });
    $$('#vocab-list .vcard').forEach((c) => c.addEventListener('click', (e) => !e.target.closest('button') && c.classList.toggle('peek')));
    $('[data-act="play-vocab"]')?.addEventListener('click', async (e) => {
      const btn = e.currentTarget;
      if (btn.dataset.running === '1') return Seq.cancel();
      const cards = $$('#vocab-list .vcard');
      const tok = Seq.start('Đang đọc từ vựng (từ chậm → câu ví dụ)', () => {
        setRunning(btn, false, 'Nghe tất cả');
        cards.forEach((c) => c.classList.remove('is-current'));
      });
      setRunning(btn, true);
      for (const c of cards) {
        cards.forEach((x) => x.classList.remove('is-current'));
        c.classList.add('is-current');
        c.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        for (const [text, speed] of [[c.dataset.word, 'slow'], [c.dataset.word, 'normal'], [c.dataset.ex, 'normal']]) {
          const ok = await Speech.play(text, { speed });
          if (!Seq.alive(tok) || !ok) return Seq.end(tok);
          if (!(await Seq.wait(tok, 700))) return;
        }
        if (!(await Seq.wait(tok, 600))) return;
      }
      Seq.end(tok);
    });

    paint();
    document.addEventListener('store:change', paint);

    // Tải trước âm thanh: câu khởi động, từ vựng, ví dụ
    const shadowSpeed = Settings.get('shadowSpeed');
    $$('#warmup .shadow-item').forEach((it) => Prefetch.add(it.dataset.text, { speed: shadowSpeed }));
    vocab.forEach((w) => {
      Prefetch.add(w.word);
      Prefetch.add(w.word, { speed: 'slow' });
      Prefetch.add(w.ex);
    });
    Prefetch.start();
  }

  /* =========================================================
   * Practice — thẻ từ & các dạng bài tự sinh từ danh sách từ vựng
   * ========================================================= */
  function initPractice(root) {
    const vocab = readJSON('vocab-data') || [];
    const pool = readJSON('pool-data') || vocab;
    const stage = $('#practice-stage', root);
    const progress = $('#practice-progress', root);
    const scoreEl = $('#practice-score', root);
    let mode = 'cards';
    let queue = [];
    let idx = 0;
    let score = 0;

    const others = (w, field, n = 3) => shuffle(pool.filter((x) => x[field] !== w[field] && x.word !== w.word)).slice(0, n).map((x) => x[field]);
    const blankOut = (w) => {
      const base = w.word.replace(/\(.*?\)/g, '').trim();
      const re = new RegExp(`\\b${base.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\w*`, 'i');
      return re.test(w.ex) ? w.ex.replace(re, '_____') : null;
    };

    const pbar = $('#practice-bar', root);
    const setProgress = (finished = false) => {
      progress.textContent = `${Math.min(idx + 1, queue.length)}/${queue.length}`;
      scoreEl.innerHTML = mode === 'cards' ? '' : `<i class="bi bi-check2"></i> ${score}`;
      scoreEl.classList.toggle('hidden', mode === 'cards');
      if (pbar) pbar.style.width = `${queue.length ? ((finished ? queue.length : idx) / queue.length) * 100 : 0}%`;
    };

    const finish = () => {
      Seq.cancel();
      const total = queue.length;
      setProgress(true);
      const pct = total ? Math.round((score / total) * 100) : 0;
      stage.innerHTML = `<div class="done-state fade-in">
          <div class="emoji">${mode === 'cards' || pct >= 80 ? '🎉' : pct >= 50 ? '👍' : '💪'}</div>
          <h3 class="fw-800 mt-3 mb-1">Xong lượt luyện!</h3>
          ${mode === 'cards' ? `<p class="muted">Bạn đã xem ${total} thẻ. Thử tiếp dạng “Chọn nghĩa” nhé.</p>` : `<div class="score-big my-2">${score}/${total}</div><p class="muted">${pct >= 80 ? 'Rất tốt!' : 'Luyện lại một lượt nữa sẽ nhớ hơn.'}</p>`}
          <button class="btn btn-brand mt-2" data-act="again"><i class="bi bi-arrow-repeat"></i> Luyện lại</button>
        </div>`;
      $('[data-act="again"]', stage).addEventListener('click', () => start(mode));
      if (mode !== 'cards' && root.dataset.day) {
        Store.data.quiz[`practice-${root.dataset.day}-${mode}`] = { score, total, at: Date.now() };
      }
      addWordsToSRS(vocab);
      Store.touch();
      Store.save();
    };

    const next = () => {
      idx++;
      if (idx >= queue.length) return finish();
      render();
    };

    const choiceUI = (promptHTML, choices, correct, onAfter) => {
      stage.innerHTML = `<div class="py-3 fade-in">${promptHTML}</div><div class="choice-grid"></div><div class="feedback"></div>`;
      const grid = $('.choice-grid', stage);
      choices.forEach((c) => {
        const b = document.createElement('button');
        b.className = 'choice';
        b.textContent = c;
        b.addEventListener('click', () => {
          const ok = c === correct;
          if (ok) score++;
          $$('.choice', grid).forEach((x) => {
            x.disabled = true;
            if (x.textContent === correct) x.classList.add('is-right');
          });
          if (!ok) b.classList.add('is-wrong');
          $('.feedback', stage).innerHTML = `<div class="mb-1">${ok ? '<span class="chip ok"><i class="bi bi-check-lg"></i> Chính xác</span>' : '<span class="chip" style="background:var(--bad-soft);color:var(--bad)"><i class="bi bi-x-lg"></i> Chưa đúng</span>'}</div>`;
          onAfter && onAfter(ok);
          $('.feedback', stage).insertAdjacentHTML('beforeend', `<div class="mt-3"><button class="btn btn-brand" data-act="next">Tiếp <i class="bi bi-arrow-right"></i></button> <span class="faint ms-2" style="font-size:.8rem"><span class="kbd">Enter</span></span></div>`);
          $('[data-act="next"]', stage).addEventListener('click', next);
          setProgress();
        });
        grid.appendChild(b);
      });
    };

    const wordInfo = (w) => `<div><div class="word-info"><b>${esc(w.word)}</b> <span class="faint">${esc(w.ipa)}</span> — ${esc(w.vi)}<div class="mt-1 en-text" style="color:var(--ink-2)">${esc(w.ex)}</div></div></div>`;

    const render = () => {
      const w = queue[idx];
      setProgress();
      if (mode === 'cards') {
        stage.innerHTML = `<div class="flash fade-in" tabindex="0">
            <div class="flash-inner">
              <div class="flash-face flash-front">
                <div class="big-word en-text">${esc(w.word)}</div>
                <div class="ipa-line">${esc(w.ipa)} · ${esc(w.pos)}</div>
                <div class="d-flex gap-2 mt-3 say-slot"></div>
                <div class="hint"><i class="bi bi-arrow-repeat"></i> Bấm vào thẻ để lật</div>
              </div>
              <div class="flash-face flash-back">
                <div class="meaning">${esc(w.vi)}</div>
                <div class="ex"><span class="ex-btn"></span><div><div class="en-text">${esc(w.ex)}</div><div class="faint mt-1" style="font-size:.86rem">${esc(w.ex_vi)}</div></div></div>
              </div>
            </div>
          </div>
          <div class="card-actions">
            <button class="btn btn-ghost" data-act="prev" aria-label="Thẻ trước"><i class="bi bi-arrow-left"></i></button>
            <button class="btn btn-danger-quiet" data-act="again-card"><i class="bi bi-x-lg"></i> Chưa nhớ</button>
            <button class="btn btn-brand" data-act="know"><i class="bi bi-check-lg"></i> Đã nhớ</button>
          </div>
          <div class="text-center faint mt-3 d-none d-md-block" style="font-size:.8rem"><span class="kbd">Space</span> lật · <span class="kbd">←</span> <span class="kbd">→</span> chuyển · <span class="kbd">P</span> nghe</div>`;
        const front = $('.flash-front .say-slot', stage);
        front.append(sayButton(w.word, 'normal'), sayButton(w.word, 'slow', 'slow'));
        $('.ex-btn', stage).append(sayButton(w.ex, 'normal'));
        const card = $('.flash', stage);
        card.addEventListener('click', (e) => !e.target.closest('button') && card.classList.toggle('flipped'));
        $('[data-act="prev"]', stage).addEventListener('click', () => {
          idx = Math.max(0, idx - 1);
          render();
        });
        $('[data-act="again-card"]', stage).addEventListener('click', () => {
          queue.push(w);
          next();
        });
        $('[data-act="know"]', stage).addEventListener('click', next);
        if (Settings.get('autoplay')) Speech.play(w.word);
      } else if (mode === 'meaning') {
        choiceUI(
          `<div class="prompt-big en-text">${esc(w.word)} <span class="say-slot"></span></div><div class="text-center faint" style="font-family:var(--font-ipa)">${esc(w.ipa)}</div><p class="text-center mt-2 muted" style="font-size:.88rem">Chọn nghĩa đúng</p>`,
          shuffle([w.vi, ...others(w, 'vi')]),
          w.vi,
          () => $('.feedback', stage).insertAdjacentHTML('beforeend', wordInfo(w))
        );
        $('.say-slot', stage).append(sayButton(w.word, 'normal'));
        if (Settings.get('autoplay')) Speech.play(w.word);
      } else if (mode === 'listen') {
        choiceUI(
          `<div class="text-center"><button class="say-btn xl" data-say="${esc(w.word)}" aria-label="Nghe lại"><i class="bi bi-volume-up-fill"></i></button><p class="muted mt-3" style="font-size:.88rem">Nghe và chọn từ đúng</p></div>`,
          shuffle([w.word, ...others(w, 'word')]),
          w.word,
          () => $('.feedback', stage).insertAdjacentHTML('beforeend', wordInfo(w))
        );
        Speech.play(w.word);
      } else if (mode === 'type') {
        stage.innerHTML = `<div class="text-center py-3 fade-in">
            <div class="d-inline-flex align-items-center gap-2"><button class="say-btn xl" data-say="${esc(w.word)}" aria-label="Nghe lại"><i class="bi bi-volume-up-fill"></i></button>
            <button class="say-btn lg slow" data-say="${esc(w.word)}" data-speed="slower" aria-label="Nghe rất chậm"><i class="bi bi-hourglass-split"></i></button></div>
            <p class="muted mt-3" style="font-size:.88rem">Nghe và gõ lại từ/cụm từ · gợi ý: <b>${esc(w.vi)}</b></p>
          </div>
          <div class="d-flex gap-2 justify-content-center mx-auto" style="max-width:460px"><input class="form-control form-control-lg en-text" autocomplete="off" autocapitalize="off" spellcheck="false" lang="en" placeholder="Gõ từ bạn nghe được…"><button class="btn btn-brand" data-act="check">Kiểm tra</button></div>
          <div class="feedback"></div>`;
        const input = $('input', stage);
        input.focus();
        let checked = false;
        const check = () => {
          if (checked) return next();
          checked = true;
          const norm = (s) => words(s).join(' ');
          const ok = norm(input.value) === norm(w.word);
          if (ok) score++;
          $('.feedback', stage).innerHTML = `${ok ? '<span class="chip ok"><i class="bi bi-check-lg"></i> Chính xác</span>' : `<span class="chip" style="background:var(--bad-soft);color:var(--bad)"><i class="bi bi-x-lg"></i> Chưa đúng</span>`}${wordInfo(w)}<div class="mt-3"><button class="btn btn-brand" data-act="next">Tiếp <i class="bi bi-arrow-right"></i></button></div>`;
          $('[data-act="next"]', stage).addEventListener('click', next);
          setProgress();
        };
        $('[data-act="check"]', stage).addEventListener('click', check);
        input.addEventListener('keydown', (e) => e.key === 'Enter' && (e.preventDefault(), check()));
        Speech.play(w.word);
      } else if (mode === 'gap') {
        const sentence = blankOut(w);
        choiceUI(
          `<div class="text-center en-text mx-auto" style="font-size:1.3rem;font-weight:600;max-width:620px;line-height:1.5">${esc(sentence)}</div><p class="text-center muted mt-2" style="font-size:.88rem">${esc(w.ex_vi)}</p>`,
          shuffle([w.word, ...others(w, 'word')]),
          w.word,
          () => {
            $('.feedback', stage).insertAdjacentHTML('beforeend', wordInfo(w));
            Speech.play(w.ex);
          }
        );
      }
    };

    const start = (m) => {
      mode = m;
      score = 0;
      idx = 0;
      let list = shuffle(vocab);
      if (m === 'gap') list = list.filter(blankOut);
      queue = list;
      Seg.set($('.mode-tabs', root), m);
      if (!queue.length) {
        stage.innerHTML = '<div class="empty"><div class="emoji">🤔</div>Không đủ dữ liệu cho dạng bài này.</div>';
        return;
      }
      render();
    };

    $('.mode-tabs', root)?.addEventListener('seg:change', (e) => start(e.detail));
    document.addEventListener('keydown', (e) => {
      if (e.target.closest && e.target.closest('input, textarea, select')) return;
      if (e.key === 'Enter') $('[data-act="next"]', stage)?.click();
      if (mode !== 'cards') return;
      if (e.key === ' ') {
        e.preventDefault();
        $('.flash', stage)?.classList.toggle('flipped');
      } else if (e.key === 'ArrowRight') $('[data-act="know"]', stage)?.click();
      else if (e.key === 'ArrowLeft') $('[data-act="prev"]', stage)?.click();
      else if (e.key.toLowerCase() === 'p' && queue[idx]) Speech.play(queue[idx].word);
    });
    start('cards');
  }

  /* =========================================================
   * SRS — ôn tập ngắt quãng kiểu Leitner
   * ========================================================= */
  const SRS_INTERVALS = [0, 1, 3, 7, 14, 30, 60];
  const TOTAL_DAYS = 72;
  const SRS = {
    dueList(today = todayISO()) {
      return Object.entries(Store.data.srs).filter(([, c]) => c.due <= today).map(([k]) => k);
    },
    grade(key, grade) {
      const c = Store.data.srs[key];
      if (!c) return;
      if (grade === 0) c.box = 0;
      else if (grade === 2) c.box = Math.min(SRS_INTERVALS.length - 1, c.box + 1);
      c.due = addDays(todayISO(), grade === 0 ? 0 : grade === 1 ? 1 : SRS_INTERVALS[c.box]);
      c.seen = (c.seen || 0) + 1;
      Store.touch();
      Store.save();
    },
    stats() {
      const cards = Object.values(Store.data.srs);
      return { total: cards.length, mastered: cards.filter((c) => c.box >= 4).length, due: this.dueList().length };
    },
  };

  function initReview(root) {
    const all = readJSON('vocab-data') || [];
    const byKey = {};
    all.forEach((w) => (byKey[w.word.toLowerCase()] = w));
    const stage = $('#review-stage', root);
    let queue = shuffle(SRS.dueList().filter((k) => byKey[k]));
    let done = 0;

    const paintStats = () => {
      const s = SRS.stats();
      $('#srs-total').textContent = s.total;
      $('#srs-mastered').textContent = s.mastered;
      $('#srs-due').textContent = queue.length;
      $('#srs-done').textContent = done;
    };

    const render = () => {
      paintStats();
      if (!queue.length) {
        const has = SRS.stats().total;
        stage.innerHTML = `<div class="done-state fade-in"><div class="emoji">${has ? '✅' : '🌱'}</div><h3 class="fw-800 mt-3 mb-1">${has ? 'Hết thẻ cần ôn hôm nay!' : 'Lịch ôn đang trống'}</h3>
          <p class="muted mx-auto" style="max-width:440px">${has ? 'Quay lại vào ngày mai nhé. Từ mới sẽ được thêm khi bạn học xong phần Từ vựng mỗi ngày.' : 'Hãy học phần Từ vựng của một ngày và bấm “Đánh dấu xong” — từ sẽ tự vào lịch ôn.'}</p>
          <a href="/hom-nay/" class="btn btn-brand mt-2"><i class="bi bi-play-fill"></i> Vào bài hôm nay</a></div>`;
        return;
      }
      const key = queue[0];
      const w = byKey[key];
      const card = Store.data.srs[key];
      const nextIv = SRS_INTERVALS[Math.min(SRS_INTERVALS.length - 1, card.box + 1)];
      stage.innerHTML = `<div class="flash fade-in" tabindex="0"><div class="flash-inner">
          <div class="flash-face flash-front"><div class="big-word en-text">${esc(w.word)}</div><div class="ipa-line">${esc(w.ipa)}</div><div class="d-flex gap-2 mt-3 say-slot"></div><div class="hint">Nhớ nghĩa rồi bấm để lật · hộp ${card.box}/6</div></div>
          <div class="flash-face flash-back"><div class="meaning">${esc(w.vi)}</div><div class="ex"><span class="ex-btn"></span><div><div class="en-text">${esc(w.ex)}</div><div class="faint mt-1" style="font-size:.86rem">${esc(w.ex_vi)}</div></div></div><a class="chip sm mt-3" href="/ngay/${w.day}/">Ngày ${w.day} <i class="bi bi-arrow-up-right"></i></a></div>
        </div></div>
        <div class="grade-bar hidden">
          <button type="button" data-g="0"><span>Quên</span><small>ôn lại ngay · <span class="kbd">1</span></small></button>
          <button type="button" data-g="1"><span>Mang máng</span><small>ngày mai · <span class="kbd">2</span></small></button>
          <button type="button" data-g="2"><span>Nhớ rõ</span><small>sau ${nextIv} ngày · <span class="kbd">3</span></small></button>
        </div>
        <div class="card-actions flip-hint"><button class="btn btn-brand btn-lg" data-act="flip"><i class="bi bi-arrow-repeat"></i> Lật thẻ <span class="kbd ms-1">Space</span></button></div>`;
      $('.say-slot', stage).append(sayButton(w.word, 'normal'), sayButton(w.word, 'slow', 'slow'));
      $('.ex-btn', stage).append(sayButton(w.ex, 'normal'));
      const flash = $('.flash', stage);
      const flip = () => {
        flash.classList.add('flipped');
        $('.grade-bar', stage).classList.remove('hidden');
        $('.flip-hint', stage).classList.add('hidden');
      };
      flash.addEventListener('click', (e) => !e.target.closest('button, a') && flip());
      $('[data-act="flip"]', stage).addEventListener('click', flip);
      $$('[data-g]', stage).forEach((b) =>
        b.addEventListener('click', () => {
          const g = Number(b.dataset.g);
          SRS.grade(key, g);
          queue.shift();
          if (g === 0) queue.splice(Math.min(queue.length, 3), 0, key);
          else done++;
          render();
        })
      );
      if (Settings.get('autoplay')) Speech.play(w.word);
    };

    document.addEventListener('keydown', (e) => {
      if (e.target.closest && e.target.closest('input, textarea, select')) return;
      if (e.key === ' ') {
        e.preventDefault();
        $('[data-act="flip"]', stage)?.click();
      } else if (['1', '2', '3'].includes(e.key)) {
        const b = $(`[data-g="${Number(e.key) - 1}"]`, stage);
        if (b && !$('.grade-bar', stage).classList.contains('hidden')) b.click();
      }
    });

    $('#srs-add-all')?.addEventListener('click', () => {
      const days = Object.entries(Store.data.days).filter(([, d]) => d.done).map(([n]) => Number(n));
      const n = addWordsToSRS(all.filter((w) => days.includes(w.day)));
      Store.save();
      queue = shuffle(SRS.dueList().filter((k) => byKey[k]));
      toast(n ? `Đã thêm ${n} từ của các ngày đã hoàn thành` : 'Không có từ mới để thêm', n ? 'bi-check-circle-fill' : 'bi-info-circle');
      render();
    });
    render();
  }

  /* =========================================================
   * Trạng thái ngày trên roadmap / trang chủ / trang tuần
   * ========================================================= */
  function paintDayStatus() {
    $$('[data-day-status]').forEach((el) => {
      const n = el.dataset.dayStatus;
      el.classList.toggle('is-done', Store.isDayDone(n));
      el.classList.toggle('is-partial', Store.dayPartial(n));
    });
    $$('[data-week-done]').forEach((el) => {
      const days = el.dataset.weekDone.split(',');
      el.textContent = `${days.filter((n) => Store.isDayDone(n)).length}/${days.length}`;
    });
    const due = SRS.dueList().length;
    $$('.srs-due-badge').forEach((b) => (b.textContent = due ? String(due > 99 ? '99+' : due) : ''));

    // Thống kê chung trên mọi trang (thanh bên, trang chủ, lộ trình)
    const total = TOTAL_DAYS;
    const done = Store.doneCount();
    const pct = Math.round((done / total) * 100);
    const streak = Store.streak();
    $$('[data-streak]').forEach((el) => (el.textContent = streak));
    $$('[data-done-count]').forEach((el) => (el.textContent = `${done}/${total}`));
    $$('[data-overall-bar]').forEach((el) => (el.style.width = `${pct}%`));
    $$('[data-overall-ring]').forEach((el) => el.style.setProperty('--p', pct));
    $$('[data-overall-pct]').forEach((el) => (el.textContent = `${pct}%`));
    $$('[data-week-bar]').forEach((el) => {
      const days = el.dataset.weekBar.split(',');
      el.style.width = `${(days.filter((n) => Store.isDayDone(n)).length / days.length) * 100}%`;
    });

    // Lịch học dạng heatmap
    const hm = $('[data-heatmap]');
    if (hm) {
      const today = hm.dataset.today || todayISO();
      $$('span', hm).forEach((c) => {
        c.classList.toggle('today', c.dataset.date === today);
        if (!c.dataset.day) return;
        const isDone = Store.isDayDone(c.dataset.day);
        c.classList.toggle('done', isDone);
        c.classList.toggle('act', !isDone && (Store.dayPartial(c.dataset.day) || !!Store.data.activity[c.dataset.date]));
      });
    }

    // Vòng tiến độ bài hôm nay (trang chủ)
    const tr = $('[data-today-ring]');
    if (tr) {
      const d = Store.data.days[tr.dataset.day] || { sections: {} };
      const n = Object.values(d.sections || {}).filter(Boolean).length;
      const p = d.done ? 100 : Math.min(95, Math.round((n / Number(tr.dataset.sections || 8)) * 100));
      tr.style.setProperty('--p', p);
      $$('[data-today-pct]').forEach((el) => (el.textContent = `${p}%`));
      $$('[data-today-cta]').forEach((el) => (el.textContent = d.done ? 'Ôn lại bài hôm nay' : n ? 'Học tiếp' : 'Bắt đầu học'));
    }
  }

  function initHome() {
    const total = TOTAL_DAYS;
    const done = Store.doneCount();
    const s = SRS.stats();
    const set = (id, v) => {
      const el = document.getElementById(id);
      if (el) el.textContent = v;
    };
    set('stat-done', `${done}/${total}`);
    set('stat-streak', Store.streak());
    set('stat-words', s.total);
    set('stat-due', s.due);
    const h = new Date().getHours();
    $$('[data-greeting]').forEach((el) => (el.textContent = h < 11 ? 'Chào buổi sáng ☀️' : h < 14 ? 'Chào buổi trưa 🌤️' : h < 18 ? 'Chào buổi chiều 🌇' : 'Chào buổi tối 🌙'));
    // Bài tiếp theo chưa hoàn thành
    let nextDay = 1;
    while (nextDay <= total && Store.isDayDone(nextDay)) nextDay++;
    const cont = $('#continue-link');
    if (cont && done > 0 && nextDay <= total) {
      cont.href = `/ngay/${nextDay}/`;
      $('.n', cont).textContent = nextDay;
      cont.classList.remove('hidden');
    }
  }

  /* =========================================================
   * Trang bản ghi âm
   * ========================================================= */
  async function initRecordings(root) {
    const list = $('#rec-list', root);
    const titles = readJSON('day-titles') || {};
    let recs = [];
    try {
      recs = (await RecDB.all()).sort((a, b) => a.created - b.created);
    } catch (e) {
      list.innerHTML = '<div class="panel empty"><div class="emoji">🚫</div>Trình duyệt không hỗ trợ lưu bản ghi.</div>';
      return;
    }
    if (!recs.length) {
      list.innerHTML = '<div class="panel empty"><div class="emoji">🎙️</div><div class="fw-800 mb-1" style="color:var(--ink)">Chưa có bản ghi nào</div>Các bản ghi ở phần <b>Nói</b> mỗi ngày sẽ hiện ở đây.<div class="mt-3"><a href="/hom-nay/" class="btn btn-brand btn-sm">Vào bài hôm nay</a></div></div>';
    }
    const groups = {};
    recs.forEach((r) => (groups[r.day] = groups[r.day] || []).push(r));
    Object.keys(groups)
      .sort((a, b) => a - b)
      .forEach((day) => {
        const box = document.createElement('div');
        box.className = 'panel panel-pad mb-3';
        box.innerHTML = `<a class="d-flex align-items-center gap-2 mb-1" style="color:var(--ink)" href="/ngay/${day}/"><span class="chip brand">Ngày ${day}</span><span class="fw-800">${esc(titles[day] || '')}</span><i class="bi bi-arrow-up-right ms-auto faint"></i></a>`;
        groups[day].forEach((r) => {
          const lab = document.createElement('div');
          lab.className = 'faint fw-700 mt-3 mb-1';
          lab.style.fontSize = '.8rem';
          lab.textContent = r.label;
          box.appendChild(lab);
          box.appendChild(takeRow(r, () => {}));
        });
        list.appendChild(box);
      });

    // So sánh 2 bản ghi
    const a = $('#cmp-a', root);
    const b = $('#cmp-b', root);
    if (a && b && recs.length) {
      recs.forEach((r, i) => {
        const opt = `<option value="${i}">${esc(r.label)} · ${fmtDate(r.created)}</option>`;
        a.insertAdjacentHTML('beforeend', opt);
        b.insertAdjacentHTML('beforeend', opt);
      });
      b.value = String(recs.length - 1);
      $('#cmp-wrap', root).classList.remove('hidden');
      const cmpBtn = $('#cmp-play', root);
      cmpBtn.addEventListener('click', async () => {
        if (cmpBtn.dataset.running === '1') return Seq.cancel();
        const tok = Seq.start('So sánh 2 bản ghi');
        setRunning(cmpBtn, true);
        for (const sel of [a, b]) {
          const r = recs[Number(sel.value)];
          const au = new Audio(URL.createObjectURL(r.blob));
          const stop = () => au.pause();
          Seq.onStop = stop;
          await new Promise((res) => {
            au.onended = res;
            au.onerror = res;
            au.play().catch(res);
          });
          if (!Seq.alive(tok)) break;
          await sleep(600);
        }
        setRunning(cmpBtn, false, 'Phát lần lượt');
        Seq.end(tok);
      });
    }

    // Bảng tự chấm
    const rb = $('#rubric-history', root);
    if (rb) {
      const rows = Object.entries(Store.data.rubric).sort((x, y) => (x[1].at || 0) - (y[1].at || 0));
      rb.innerHTML = rows.length
        ? rows.map(([k, r]) => `<tr><td class="fw-700">${esc(k.replace('day-', 'Ngày '))}</td>${['fluency', 'vocab', 'grammar', 'pron'].map((f) => `<td>${r[f] ? `<span class="chip sm ${r[f] >= 4 ? 'ok' : r[f] >= 3 ? 'warn' : ''}">${r[f]}/5</span>` : '–'}</td>`).join('')}<td class="faint" style="font-size:.8rem">${r.at ? fmtDate(r.at) : ''}</td></tr>`).join('')
        : '<tr><td colspan="6" class="faint">Chưa có. Tự chấm ở Ngày 1, 18, 67…</td></tr>';
    }
  }

  /* =========================================================
   * Cài đặt: giọng đọc, tốc độ, giao diện, sao lưu
   * ========================================================= */
  function initSettings(root) {
    const saved = (key, val) => {
      Settings.set(key, val);
      if (key === 'theme') applyTheme();
      toast('Đã lưu cài đặt');
    };
    $$('[data-setting]', root).forEach((input) => {
      const key = input.dataset.setting;
      const v = Settings.get(key);
      if (input.classList.contains('seg')) {
        Seg.set(input, v);
        input.addEventListener('seg:change', (e) => saved(key, e.detail));
        return;
      }
      if (input.type === 'checkbox') input.checked = !!v;
      else if (input.type === 'radio') input.checked = input.value === String(v);
      else input.value = String(v);
      input.addEventListener('change', () => saved(key, input.type === 'checkbox' ? input.checked : input.value));
    });
    $$('[data-test-voice]', root).forEach((b) =>
      b.addEventListener('click', (e) => {
        e.preventDefault();
        if (b.classList.contains('is-playing') || b.classList.contains('is-loading')) return Speech.stop();
        Speech.play('Hello! This is how I sound. I hope you enjoy learning English with me.', { voice: b.dataset.testVoice, el: b });
      })
    );
    $('#free-say')?.addEventListener('click', (e) => {
      const txt = $('#free-text').value.trim();
      if (!txt) return toast('Hãy dán một câu tiếng Anh trước', 'bi-info-circle');
      Seq.cancel();
      Speech.play(txt.slice(0, 1500), { speed: $('#free-speed').dataset.value, el: e.currentTarget });
    });
    $('#export-btn')?.addEventListener('click', () => {
      const blob = new Blob([JSON.stringify(Store.data, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `english-daily-backup-${todayISO()}.json`;
      a.click();
    });
    $('#import-file')?.addEventListener('change', async (e) => {
      const f = e.target.files[0];
      if (!f) return;
      try {
        const data = JSON.parse(await f.text());
        if (typeof data !== 'object' || !data.days) throw new Error('bad');
        if (!confirm('Thay toàn bộ tiến độ hiện tại bằng bản sao lưu này?')) return;
        localStorage.setItem(STORE_KEY, JSON.stringify(data));
        Store.load();
        toast('Đã khôi phục tiến độ ✓');
        setTimeout(() => location.reload(), 600);
      } catch (err) {
        toast('File sao lưu không hợp lệ');
      }
    });
    $('#reset-btn')?.addEventListener('click', () => {
      if (!confirm('Xóa TOÀN BỘ tiến độ, điểm và bài viết? (Bản ghi âm không bị xóa.)')) return;
      localStorage.removeItem(STORE_KEY);
      Store.load();
      toast('Đã xóa tiến độ');
      setTimeout(() => location.reload(), 600);
    });
  }

  /* =========================================================
   * Kho từ vựng: tìm kiếm & đánh dấu từ đã thuộc
   * ========================================================= */
  function initVocabBank(root) {
    const input = $('#vocab-search', root);
    const rows = $$('.vrow', root);
    const count = $('#vocab-count', root);
    let week = '';
    const paintKnown = () =>
      rows.forEach((r) => {
        const c = Store.data.srs[r.dataset.word.toLowerCase()];
        const badge = $('.known', r);
        if (badge) badge.classList.toggle('hidden', !(c && c.box >= 3));
      });
    const filter = () => {
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      $$('.week-block', root).forEach((b) => {
        const inWeek = !week || b.dataset.week === week;
        let any = 0;
        $$('.day-block', b).forEach((d) => {
          let n = 0;
          $$('.vrow', d).forEach((r) => {
            const ok = inWeek && (!q || r.dataset.search.includes(q));
            r.classList.toggle('hidden', !ok);
            if (ok) n++;
          });
          d.classList.toggle('hidden', !n);
          any += n;
        });
        b.classList.toggle('hidden', !any);
        shown += any;
      });
      if (count) count.textContent = shown;
      $('#vocab-empty', root)?.classList.toggle('hidden', shown > 0);
    };
    input?.addEventListener('input', filter);
    $$('#week-filter button', root).forEach((b) =>
      b.addEventListener('click', () => {
        week = b.dataset.week;
        $$('#week-filter button', root).forEach((x) => x.classList.toggle('on', x === b));
        filter();
      })
    );
    paintKnown();
  }

  function initPhraseBank(root) {
    const input = $('#phrase-search', root);
    input?.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      $$('.phrase-group', root).forEach((g) => {
        let n = 0;
        $$('.phrase', g).forEach((p) => {
          const ok = !q || p.dataset.search.includes(q);
          p.classList.toggle('hidden', !ok);
          if (ok) n++;
        });
        g.classList.toggle('hidden', !n);
        shown += n;
      });
      $('#phrase-empty', root)?.classList.toggle('hidden', shown > 0);
    });
  }

  /* =========================================================
   * Khởi động
   * ========================================================= */
  document.addEventListener('DOMContentLoaded', () => {
    Seg.init();
    enhanceLesson();
    $$('.shadow-player').forEach(initShadow);
    $$('.dialogue').forEach(initDialogue);
    $$('.quiz').forEach(initQuiz);
    $$('.dictation').forEach(initDictation);
    $$('.writing').forEach(initWriting);
    $$('.recorder').forEach(initRecorder);
    $$('.rubric').forEach(initRubric);
    $$('.week-assess').forEach(initWeekAssess);
    const dayPage = $('#day-page');
    if (dayPage) initDayPage(dayPage);
    const practice = $('#practice');
    if (practice) initPractice(practice);
    const review = $('#review');
    if (review) initReview(review);
    const recs = $('#recordings');
    if (recs) initRecordings(recs);
    const settings = $('#settings');
    if (settings) initSettings(settings);
    const bank = $('#vocab-bank');
    if (bank) initVocabBank(bank);
    const phrases = $('#phrase-bank');
    if (phrases) initPhraseBank(phrases);
    if ($('#home-stats')) initHome();
    paintDayStatus();
    document.addEventListener('store:change', paintDayStatus);

    $$('[data-theme-toggle]').forEach((b) =>
      b.addEventListener('click', () => {
        const dark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
        Settings.set('theme', dark ? 'light' : 'dark');
        applyTheme();
      })
    );
    applyTheme();
    $('#now-playing button')?.addEventListener('click', () => Seq.cancel());
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') Seq.cancel();
    });
  });

  window.EnglishDaily = { Store, Speech, Seq, SRS, RecDB };
})();
