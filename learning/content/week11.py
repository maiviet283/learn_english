"""Tuần 11 — Xử lý tình huống khó."""

DAY1 = {
    'title': 'Khi không hiểu câu hỏi',
    'title_en': "When You Don't Understand",
    'goal': 'Xử lý bình tĩnh khi không nghe rõ hoặc không hiểu: xin nhắc lại, kiểm tra lại ý, hỏi nghĩa từ, xử lý sự cố kết nối — với 10 câu mẫu phản xạ.',
    'tasks': [
        'Học 14 cụm từ cho tình huống không nghe rõ/không hiểu.',
        'Học 4 nhóm chiến lược: nhắc lại – chậm lại – giải thích – kiểm tra.',
        'Nghe một cuộc gọi khó với khách hàng nói nhanh và mạng kém.',
        'Luyện phản xạ: nghe 10 tình huống, nói ngay câu phù hợp.',
    ],
    'product': '10 câu mẫu xử lý khi không hiểu',
    'warmup': [
        ('Sorry, I missed that. Could you say it again?', 'Xin lỗi, tôi lỡ mất. Bạn nói lại được không?'),
        ("I didn't catch the last part.", 'Tôi không nghe kịp phần cuối.'),
        ('Do you mean the mobile app or the website?', 'Ý bạn là ứng dụng di động hay website?'),
        ("You're cutting out a bit.", 'Tiếng bạn bị ngắt quãng.'),
        ("I think you've frozen.", 'Tôi nghĩ hình của bạn bị đứng.'),
        ('Could you spell that for me?', 'Bạn đánh vần giúp tôi được không?'),
    ],
    'vocab': [
        ("didn't catch", '/ˈdɪdnt kætʃ/', 'phrase', 'không nghe kịp', "Sorry, I didn't catch your name.", 'Xin lỗi, tôi không nghe kịp tên bạn.'),
        ('missed', '/mɪst/', 'verb (past)', 'lỡ mất (không nghe được)', 'Sorry, I missed the last sentence.', 'Xin lỗi, tôi lỡ mất câu cuối.'),
        ('lagging', '/ˈlæɡɪŋ/', 'adj', 'bị trễ, giật (kết nối)', 'The video is lagging a lot.', 'Video bị giật nhiều.'),
        ('cut out', '/kʌt aʊt/', 'phrasal verb', '(tiếng) bị mất quãng', 'Your audio keeps cutting out.', 'Tiếng của bạn cứ bị mất quãng.'),
        ('frozen', '/ˈfrəʊzn/', 'adj', '(hình) bị đứng', "Your screen has frozen.", 'Màn hình của bạn bị đứng.'),
        ('echo', '/ˈekəʊ/', 'n', 'tiếng vọng', "There's an echo. Could you use headphones?", 'Có tiếng vọng. Bạn dùng tai nghe được không?'),
        ('background noise', '/ˈbækɡraʊnd nɔɪz/', 'n', 'tiếng ồn xung quanh', "There's a lot of background noise on your side.", 'Phía bạn có nhiều tiếng ồn.'),
        ('unmute', '/ʌnˈmjuːt/', 'verb', 'bật mic', 'Please unmute yourself to speak.', 'Vui lòng bật mic để nói.'),
        ('mishear', '/ˌmɪsˈhɪə/', 'verb', 'nghe nhầm (misheard)', 'Sorry, I misheard. I thought you said fifteen.', 'Xin lỗi, tôi nghe nhầm. Tôi tưởng bạn nói mười lăm.'),
        ('lose track', '/luːz træk/', 'phrase', 'mất dấu, không theo kịp', 'Sorry, I lost track. Which slide are we on?', 'Xin lỗi, tôi không theo kịp. Chúng ta đang ở slide nào?'),
        ('come again', '/kʌm əˈɡen/', 'phrase', 'nói lại? (thân mật)', 'Come again? I didn\'t hear you.', 'Nói lại xem? Tôi không nghe thấy.'),
        ('spell out', '/spel aʊt/', 'phrasal verb', 'đánh vần; nói rõ ràng từng chi tiết', 'Could you spell out the company name?', 'Bạn đánh vần tên công ty được không?'),
        ('speak up', '/spiːk ʌp/', 'phrasal verb', 'nói to lên', "Could you speak up a little? You're very quiet.", 'Bạn nói to hơn một chút được không? Tiếng bạn rất nhỏ.'),
        ('repeat', '/rɪˈpiːt/', 'verb', 'nhắc lại', 'Would you mind repeating the question?', 'Bạn có phiền nhắc lại câu hỏi không?'),
    ],
    'lesson': """
<h3>1. Bốn chiến lược khi không hiểu</h3>
<table class="table">
<tr><th>Chiến lược</th><th>Khi nào</th><th>Câu</th></tr>
<tr><td><b>Nhắc lại</b></td><td>Không nghe rõ</td><td><span class="say">Sorry, I didn't catch that. Could you say it again?</span></td></tr>
<tr><td><b>Chậm lại / to lên</b></td><td>Nói nhanh, nhỏ</td><td><span class="say">Could you speak a bit more slowly?</span> · <span class="say">Could you speak up a little?</span></td></tr>
<tr><td><b>Giải thích</b></td><td>Nghe rõ nhưng không hiểu từ/ý</td><td><span class="say">What do you mean by "rollout"?</span> · <span class="say">Could you give me an example?</span></td></tr>
<tr><td><b>Kiểm tra</b></td><td>Hiểu một phần</td><td><span class="say">Do you mean…?</span> · <span class="say">So you're saying that…, right?</span></td></tr>
</table>

<h3>2. Hỏi lại một phần cụ thể (rất tự nhiên)</h3>
<p>Thay vì "Sorry?" chung chung, hãy hỏi lại <b>đúng phần</b> bạn bị lỡ — người nói chỉ cần nhắc một từ:</p>
<div class="ex"><span class="en">Sorry, the meeting is on… which day?</span></div>
<div class="ex"><span class="en">You need it by when?</span></div>
<div class="ex"><span class="en">Did you say fifteen or fifty?</span><span class="vi">Cặp số hay nhầm: 13/30, 14/40, 15/50… (fifTEEN nhấn sau, FIFty nhấn trước).</span></div>

<h3>3. Sự cố kết nối</h3>
<table class="table">
<tr><th>Vấn đề</th><th>Câu</th></tr>
<tr><td>Mất tiếng</td><td><span class="say">You're cutting out. Could you repeat that?</span></td></tr>
<tr><td>Hình đứng</td><td><span class="say">I think you've frozen.</span></td></tr>
<tr><td>Mạng của bạn kém</td><td><span class="say">My connection is unstable. I'll turn off my camera.</span></td></tr>
<tr><td>Ồn</td><td><span class="say">There's some background noise. Could you mute when you're not speaking?</span></td></tr>
<tr><td>Rớt mạng</td><td><span class="say">Sorry, I dropped out for a minute. What did I miss?</span></td></tr>
</table>
<div class="note"><b>Đừng xin lỗi quá nhiều.</b> Một "Sorry" là đủ. Người bản xứ cũng hỏi lại liên tục — đó là giao tiếp bình thường, không phải lỗi của bạn.</div>
""",
    'phrases': [
        ('Sorry, I dropped out for a minute. What did I miss?', 'Xin lỗi, tôi bị rớt mạng một phút. Tôi đã lỡ gì?'),
        ('You need it by when?', 'Bạn cần nó trước khi nào?'),
        ('Did you say fifteen or fifty?', 'Bạn nói mười lăm hay năm mươi?'),
        ('So you\'re saying that…, right?', 'Vậy ý bạn là…, đúng không?'),
    ],
    'listening': {
        'title': 'A difficult client call',
        'intro': 'Khách hàng nói nhanh, mạng kém và dùng từ lạ. Chú ý cách Huy xử lý từng tình huống mà không hoảng.',
        'speakers': {'A': ('Mr. Collins (client)', 'ryan'), 'B': ('Huy', 'andrew')},
        'lines': [
            ('A', "Right, so for the rollout, we're thinking we kick it off mid-month, phase one in the north, and then…", 'Được rồi, về việc triển khai, chúng tôi nghĩ sẽ bắt đầu giữa tháng, giai đoạn một ở miền bắc, rồi sau đó…'),
            ('B', "Sorry, Mr. Collins, could you speak a bit more slowly? I want to make sure I get the details right.", 'Xin lỗi ông Collins, ông nói chậm hơn một chút được không? Tôi muốn chắc chắn nắm đúng chi tiết.'),
            ('A', "Of course. We want to start the rollout in the middle of the month, in our northern stores first.", 'Dĩ nhiên. Chúng tôi muốn bắt đầu triển khai vào giữa tháng, ở các cửa hàng miền bắc trước.'),
            ('B', "Thanks. What do you mean by 'rollout' exactly? Installing the app in the stores, or training the staff?", 'Cảm ơn. Chính xác thì "rollout" nghĩa là gì ạ? Cài ứng dụng ở cửa hàng hay đào tạo nhân viên?'),
            ('A', "Both. And we need everything ready by the… [audio cuts out] …of March.", 'Cả hai. Và chúng tôi cần mọi thứ sẵn sàng trước… [mất tiếng] …tháng Ba.'),
            ('B', "Sorry, you're cutting out. You need everything ready by… which date in March?", 'Xin lỗi, tiếng ông bị mất. Ông cần mọi thứ sẵn sàng trước… ngày nào của tháng Ba?'),
            ('A', "The fifteenth.", 'Ngày mười lăm.'),
            ('B', "Did you say the fifteenth or the fiftieth… sorry, the fifth?", 'Ông nói ngày mười lăm hay… xin lỗi, ngày năm?'),
            ('A', "Ha, fifteen. One five.", 'Ha, mười lăm. Một năm.'),
            ('B', "Perfect. So just to confirm: you'd like the app installed and the staff trained in the northern stores by March fifteenth. Is that right?", 'Hoàn hảo. Vậy xin xác nhận: ông muốn ứng dụng được cài và nhân viên được đào tạo ở các cửa hàng miền bắc trước ngày mười lăm tháng Ba. Đúng không ạ?'),
            ('A', "Exactly right. Great, you've got it.", 'Chính xác. Tuyệt, anh nắm được rồi.'),
        ],
        'questions': [
            ('What is Huy\'s first request?', ['To speak more slowly', 'To turn on the camera', 'To send an email', 'To end the call'], 0, '"could you speak a bit more slowly?"'),
            ('What does "rollout" mean for the client?', ['Only installing the app', 'Only training staff', 'Both installing the app and training staff', 'Building new stores'], 2, '"Both."'),
            ('What happened when the client said the date?', ['He was on mute.', 'His audio cut out.', 'He left.', 'He spoke Vietnamese.'], 1, '[audio cuts out].'),
            ('What is the deadline?', ['March 5th', 'March 15th', 'March 50th', 'Mid-February'], 1, '"fifteen. One five."'),
            ('How does Huy finish?', ['He asks for the money.', 'He confirms everything in one sentence.', 'He says goodbye.', 'He asks the client to write it down.'], 1, '"So just to confirm…"'),
        ],
    },
    'speaking': {
        'tips': ['Bấm nghe từng tình huống, trả lời NGAY trong 3 giây bằng câu phù hợp.', 'Lặp lại cả bộ 2 lần cho đến khi phản xạ tự nhiên.'],
        'prompts': [
            ('Your manager speaks very fast and you miss everything.', 'Could you speak a bit more slowly?'),
            ('You hear "We need it by the …teen". You\'re not sure of the number.', 'Did you say…?'),
            ('A colleague uses a word you don\'t know: "Let\'s timebox this".', 'What do you mean by…?'),
            ('The client\'s audio keeps cutting out.', 'You\'re cutting out…'),
            ('You lost your connection for one minute.', 'Sorry, I dropped out…'),
            ('You understood half of a long explanation.', 'So you\'re saying that…, right?'),
        ],
        'model': (
            "Sorry, could you speak a bit more slowly? I want to make sure I get the details right. "
            "Did you say thirteen or thirty? "
            "Sorry, what do you mean by 'timebox'? "
            "You're cutting out a bit. Could you repeat the last part? "
            "Sorry, I dropped out for a minute. What did I miss? "
            "So you're saying that we should finish the API first and do the design later, right?",
            'Xin lỗi, bạn nói chậm hơn một chút được không? Tôi muốn chắc chắn nắm đúng chi tiết. '
            'Bạn nói mười ba hay ba mươi? '
            'Xin lỗi, "timebox" nghĩa là gì? '
            'Tiếng bạn hơi bị mất. Bạn nhắc lại phần cuối được không? '
            'Xin lỗi, tôi bị rớt mạng một phút. Tôi đã lỡ gì? '
            'Vậy ý bạn là chúng ta nên làm xong API trước và làm thiết kế sau, đúng không?'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'It\'s okay not to understand',
        'text': [
            'Many non-native speakers pretend to understand because they are embarrassed to ask again. They nod, say "okay", and hope the meaning will become clear later. Often it does not, and the misunderstanding appears days later as the wrong feature or a missed deadline.',
            'Native speakers ask for repetition all the time, especially on video calls with bad connections or strong accents. Nobody thinks it is strange. What people do find strange is when someone says "yes, got it" and then does something completely different.',
            'A useful rule: if a detail affects your work, such as a date, a number, a name or a requirement, never guess. Ask, or confirm in writing after the call. It takes ten seconds and can save ten days.',
        ],
        'vi': 'Nhiều người không phải bản xứ giả vờ hiểu vì ngại hỏi lại; họ gật đầu, nói "okay" và hy vọng sẽ hiểu sau. Thường thì không, và hiểu lầm lộ ra vài ngày sau thành tính năng sai hay trễ hạn. Người bản xứ hỏi lại suốt, nhất là trên cuộc gọi mạng kém; không ai thấy lạ. Điều người ta thấy lạ là ai đó nói "vâng, hiểu rồi" rồi làm khác hẳn. Quy tắc: nếu chi tiết ảnh hưởng công việc (ngày, số, tên, yêu cầu), đừng bao giờ đoán — hỏi lại hoặc xác nhận bằng văn bản. Mất mười giây, có thể tiết kiệm mười ngày.',
        'questions': [
            ('Why do some non-native speakers pretend to understand?', ['They are lazy.', 'They are embarrassed to ask again.', 'They understand everything.', 'They don\'t care.'], 1, 'Đoạn 1.'),
            ('What do people find strange, according to the text?', ['Asking for repetition', 'Saying "got it" and then doing something different', 'Bad connections', 'Accents'], 1, 'Đoạn 2.'),
            ('Which details should you never guess?', ['Jokes', 'Dates, numbers, names and requirements', 'Small talk', 'Greetings'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 10 câu mẫu bạn sẽ dùng khi không hiểu, chia theo 4 nhóm chiến lược (nhắc lại, chậm/to lên, giải thích, kiểm tra) + 2 câu cho sự cố kết nối. Học thuộc chúng.',
        'tips': ['Ưu tiên câu hỏi lại một phần cụ thể: "You need it by when?"'],
        'model': "Repeat:\n1. Sorry, I didn't catch that. Could you say it again?\n2. Sorry, the deadline is… which day?\n\nSlow down / speak up:\n3. Could you speak a bit more slowly? I want to get the details right.\n4. Could you speak up a little? You're quite quiet.\n\nExplain:\n5. What do you mean by \"rollout\"?\n6. Could you give me an example?\n\nCheck:\n7. Did you say fifteen or fifty?\n8. So you're saying that we should start with the API, right?\n\nConnection:\n9. You're cutting out. Could you repeat the last part?\n10. Sorry, I dropped out for a minute. What did I miss?",
        'min_words': 80,
    },
    'quiz': [
        ('"Sorry, I didn\'t ___ that." (nghe kịp)', ['catch', 'take', 'hold', 'get on'], 0, "didn't catch."),
        ('The audio stops and starts: it\'s ___.', ['cutting out', 'cutting off up', 'breaking in', 'falling'], 0, 'cut out.'),
        ('The video doesn\'t move: it has ___.', ['frozen', 'freezed', 'froze up', 'fried'], 0, 'freeze – froze – frozen.'),
        ('Hỏi lại một phần cụ thể:', ['What?', 'You need it by when?', 'Huh?', 'Repeat all.'], 1, 'Hỏi đúng phần bị lỡ.'),
        ('"fifteen" nhấn trọng âm ở:', ['fif-', '-teen'], 1, 'fifTEEN; FIFty.', 'fifteen'),
        ('Nghe và chọn số bạn nghe được.', ['13', '30'], 1, 'THIR-ty: nhấn âm đầu.', 'thirty'),
        ('Could you ___ up a little? You\'re very quiet.', ['speak', 'talk', 'say', 'tell'], 0, 'speak up.'),
        ('"Sorry, I ___ out for a minute. What did I miss?"', ['dropped', 'fell', 'went', 'got'], 0, 'drop out (rớt mạng).'),
        ('Khi một chi tiết (ngày, số) ảnh hưởng công việc, bạn nên:', ['Đoán', 'Hỏi lại hoặc xác nhận bằng văn bản', 'Bỏ qua', 'Hỏi người khác sau'], 1, 'Không bao giờ đoán.'),
        ('"I thought you said fifty. I ___." (nghe nhầm)', ['misheard', 'mistook up', 'misread', 'misspoke'], 0, 'mishear – misheard.'),
    ],
}

DAY2 = {
    'title': 'Làm rõ yêu cầu',
    'title_en': 'Clarifying Requirements',
    'goal': 'Hỏi lại yêu cầu mơ hồ, xác định tiêu chí chấp nhận và xác nhận deadline; viết một đoạn hội thoại làm rõ yêu cầu mẫu.',
    'tasks': [
        'Học 14 từ về yêu cầu và phạm vi.',
        'Học bộ câu hỏi làm rõ: ai, cái gì, khi nào, như thế nào là xong.',
        'Nghe developer làm rõ một yêu cầu mơ hồ với PM.',
        'Viết một đoạn hội thoại mẫu làm rõ yêu cầu.',
    ],
    'product': 'Đoạn hội thoại làm rõ yêu cầu mẫu',
    'warmup': [
        ("Could you walk me through the use case?", 'Bạn có thể đi qua trường hợp sử dụng cho tôi không?'),
        ('What are the acceptance criteria?', 'Tiêu chí chấp nhận là gì?'),
        ('This requirement is a bit vague.', 'Yêu cầu này hơi mơ hồ.'),
        ("When you say 'fast', how fast exactly?", 'Khi bạn nói "nhanh", chính xác là nhanh bao nhiêu?'),
        ("Is mobile in scope, or out of scope?", 'Mobile nằm trong hay ngoài phạm vi?'),
        ("I'll confirm everything in writing after the call.", 'Tôi sẽ xác nhận mọi thứ bằng văn bản sau cuộc gọi.'),
    ],
    'vocab': [
        ('acceptance criteria', '/əkˈseptəns kraɪˈtɪəriə/', 'n', 'tiêu chí chấp nhận', 'Every ticket needs clear acceptance criteria.', 'Mỗi ticket cần tiêu chí chấp nhận rõ ràng.'),
        ('ambiguous', '/æmˈbɪɡjuəs/', 'adj', 'mơ hồ, có thể hiểu nhiều cách', 'The word "recent" is ambiguous. Last week or last month?', 'Từ "gần đây" mơ hồ. Tuần trước hay tháng trước?'),
        ('vague', '/veɪɡ/', 'adj', 'chung chung, không rõ', '"Make it better" is too vague.', '"Làm nó tốt hơn" quá chung chung.'),
        ('specify', '/ˈspesɪfaɪ/', 'verb', 'nêu cụ thể', 'Could you specify the file format?', 'Bạn có thể nêu cụ thể định dạng file không?'),
        ('spec', '/spek/', 'n', 'bản đặc tả (specification)', 'The spec says the button should be blue.', 'Bản đặc tả nói nút phải màu xanh.'),
        ('mockup', '/ˈmɒkʌp/', 'n', 'bản thiết kế mẫu', 'Is there a mockup for this screen?', 'Có bản thiết kế mẫu cho màn hình này không?'),
        ('use case', '/ˈjuːs keɪs/', 'n', 'trường hợp sử dụng', 'What is the main use case for this feature?', 'Trường hợp sử dụng chính của tính năng này là gì?'),
        ('definition of done', '/ˌdefɪˈnɪʃn əv dʌn/', 'n', 'định nghĩa "hoàn thành"', 'Our definition of done includes tests and docs.', 'Định nghĩa hoàn thành của chúng tôi gồm test và tài liệu.'),
        ('walk through', '/wɔːk θruː/', 'phrasal verb', 'đi qua, giải thích từng bước', 'Could you walk me through the flow?', 'Bạn có thể giải thích luồng từng bước cho tôi không?'),
        ('double-check', '/ˌdʌbl ˈtʃek/', 'verb', 'kiểm tra lại', 'Let me double-check the deadline.', 'Để tôi kiểm tra lại hạn chót.'),
        ('expectation', '/ˌekspekˈteɪʃn/', 'n', 'kỳ vọng', 'Let\'s align our expectations early.', 'Hãy thống nhất kỳ vọng sớm.'),
        ('in writing', '/ɪn ˈraɪtɪŋ/', 'phrase', 'bằng văn bản', 'Please confirm the new date in writing.', 'Vui lòng xác nhận ngày mới bằng văn bản.'),
        ('out of scope', '/aʊt əv skəʊp/', 'phrase', 'ngoài phạm vi', 'The mobile version is out of scope for now.', 'Bản di động hiện nằm ngoài phạm vi.'),
        ('confirm', '/kənˈfɜːm/', 'verb', 'xác nhận', 'Can you confirm the deadline is Friday?', 'Bạn xác nhận hạn chót là thứ Sáu được không?'),
    ],
    'lesson': """
<h3>1. Yêu cầu mơ hồ → câu hỏi cụ thể</h3>
<table class="table">
<tr><th>Yêu cầu mơ hồ</th><th>Câu hỏi làm rõ</th></tr>
<tr><td>"Make the page faster."</td><td><span class="say">How fast exactly? Is under two seconds okay?</span></td></tr>
<tr><td>"Add an export."</td><td><span class="say">Which format: CSV, Excel or PDF? Which columns?</span></td></tr>
<tr><td>"Users should be notified."</td><td><span class="say">By email, push notification, or both? Which users?</span></td></tr>
<tr><td>"It should be secure."</td><td><span class="say">Are there specific requirements, like two-factor authentication?</span></td></tr>
<tr><td>"We need it soon."</td><td><span class="say">What date do you have in mind?</span></td></tr>
</table>

<h3>2. Bộ câu hỏi 5W + Done</h3>
<ul>
<li><b>Who:</b> <span class="say">Who will use this feature?</span></li>
<li><b>What:</b> <span class="say">What problem are we solving?</span></li>
<li><b>Why:</b> <span class="say">Why is this important now?</span></li>
<li><b>When:</b> <span class="say">When do you need it, and is that date flexible?</span></li>
<li><b>Scope:</b> <span class="say">Is mobile in scope?</span></li>
<li><b>Done:</b> <span class="say">How will we know it's done? What are the acceptance criteria?</span></li>
</ul>

<h3>3. Xác nhận lại (closing the loop)</h3>
<div class="ex"><span class="en">So, to summarise: a CSV export of all orders, for admins only, on the website, by the 20th. Mobile is out of scope. Is that correct?</span></div>
<div class="ex"><span class="en">I'll send a short summary in writing after this call, so we're all on the same page.</span></div>
<div class="note"><b>Hỏi "Why?" giúp bạn đề xuất giải pháp tốt hơn.</b> Đôi khi khách hàng xin "một nút xuất Excel" nhưng thật ra họ chỉ cần một email báo cáo hằng tuần.</div>
""",
    'phrases': [
        ('What problem are we trying to solve?', 'Chúng ta đang cố giải quyết vấn đề gì?'),
        ('How will we know it\'s done?', 'Làm sao biết là đã xong?'),
        ('Is that date flexible?', 'Ngày đó có linh hoạt không?'),
        ("So we're all on the same page.", 'Để mọi người cùng hiểu như nhau.'),
    ],
    'listening': {
        'title': '"Can you add a report?"',
        'intro': 'PM gửi một yêu cầu mơ hồ. Developer hỏi lại từng điểm để tránh làm sai.',
        'speakers': {'A': ('Julia (PM)', 'emma'), 'B': ('Son', 'brian')},
        'lines': [
            ('A', "Hi Son. The sales team wants a report of recent orders. Can you add it to the admin page?", 'Chào Sơn. Đội kinh doanh muốn một báo cáo các đơn hàng gần đây. Em thêm vào trang quản trị được không?'),
            ('B', "Sure. I have a few questions so I build the right thing. First, what problem are they trying to solve?", 'Vâng. Em có vài câu hỏi để làm đúng. Đầu tiên, họ đang cố giải quyết vấn đề gì?'),
            ('A', "They want to see which products are selling well, so they can plan promotions.", 'Họ muốn xem sản phẩm nào bán chạy để lên kế hoạch khuyến mãi.'),
            ('B', "Got it. When you say 'recent', how recent? The last seven days, the last month?", 'Em hiểu. Khi chị nói "gần đây", là gần bao nhiêu? Bảy ngày qua, hay tháng qua?'),
            ('A', "Hmm, good question. Let's say they can choose a date range, with the last thirty days as the default.", 'Hừm, câu hỏi hay. Cứ để họ chọn khoảng ngày, mặc định là ba mươi ngày gần nhất.'),
            ('B', "Okay. Should the report show the data on the screen, or do they need to download it?", 'Được. Báo cáo hiển thị dữ liệu trên màn hình, hay họ cần tải về?'),
            ('A', "Both would be nice, but the download is more important. They use Excel.", 'Cả hai thì tốt, nhưng tải về quan trọng hơn. Họ dùng Excel.'),
            ('B', "Then a CSV file should work, because it opens in Excel. Is the mobile app in scope, or just the website?", 'Vậy file CSV là được, vì nó mở được bằng Excel. App di động có trong phạm vi không, hay chỉ website?'),
            ('A', "Just the website. Mobile is out of scope.", 'Chỉ website. Di động ngoài phạm vi.'),
            ('B', "And when do they need it? Is the date flexible?", 'Và họ cần khi nào ạ? Ngày đó có linh hoạt không?'),
            ('A', "Before their planning meeting on the twentieth. That's not very flexible.", 'Trước buổi họp kế hoạch ngày hai mươi. Không linh hoạt lắm.'),
            ('B', "Okay. So, to summarise: a downloadable CSV of orders by product, with a date range defaulting to thirty days, website only, by the twentieth. I'll write the acceptance criteria in the ticket and send it to you to double-check.", 'Được. Vậy tóm lại: file CSV tải về các đơn theo sản phẩm, có khoảng ngày mặc định ba mươi ngày, chỉ website, trước ngày hai mươi. Em sẽ viết tiêu chí chấp nhận vào ticket và gửi chị kiểm tra lại.'),
            ('A', "Perfect. That's exactly what they need.", 'Hoàn hảo. Đó đúng là thứ họ cần.'),
        ],
        'questions': [
            ('What problem does the sales team want to solve?', ['Find slow servers', 'See which products sell well to plan promotions', 'Track employees', 'Delete old orders'], 1, '"so they can plan promotions".'),
            ('What does "recent" mean in the end?', ['Last seven days only', 'A date range, defaulting to the last 30 days', 'Last year', 'Today'], 1, 'Khoảng ngày, mặc định 30 ngày.'),
            ('Why is CSV a good format?', ['It is smaller.', 'It opens in Excel.', 'It is more secure.', 'Mobile needs it.'], 1, '"because it opens in Excel".'),
            ('What is out of scope?', ['The website', 'The download', 'The mobile app', 'The date range'], 2, '"Mobile is out of scope."'),
            ('What will Son do next?', ['Start coding immediately', 'Write acceptance criteria and send them to Julia to double-check', 'Call the sales team', 'Wait until the 20th'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Đóng vai Sơn ở phần Nghe.', 'Luyện hỏi làm rõ cho các yêu cầu mơ hồ bên dưới — mỗi yêu cầu ít nhất 3 câu hỏi.'],
        'prompts': [
            ('"Can you make the app faster?"', 'How fast? Which part? Why now?'),
            ('"We need notifications for users."', 'Which users? Email or push? When?'),
            ('"Add a search to the website, ASAP."', 'Search what? Filters? What date exactly?'),
        ],
        'model': (
            "Sure, I can look into search. I have a few questions so I build the right thing. "
            "First, what do users need to search for: products, orders, or both? "
            "Second, do they need filters, for example by price or category? "
            "And when you say ASAP, what date do you have in mind? Is it flexible? "
            "Also, is the mobile app in scope, or just the website? "
            "Once I have the answers, I'll write the acceptance criteria in the ticket and send them to you to double-check, so we're all on the same page.",
            'Vâng, tôi có thể xem phần tìm kiếm. Tôi có vài câu hỏi để làm đúng. '
            'Đầu tiên, người dùng cần tìm gì: sản phẩm, đơn hàng hay cả hai? '
            'Thứ hai, họ có cần bộ lọc không, ví dụ theo giá hay danh mục? '
            'Và khi bạn nói càng sớm càng tốt, bạn nghĩ đến ngày nào? Có linh hoạt không? '
            'Ngoài ra, app di động có trong phạm vi không, hay chỉ website? '
            'Khi có câu trả lời, tôi sẽ viết tiêu chí chấp nhận vào ticket và gửi bạn kiểm tra lại, để mọi người cùng hiểu như nhau.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'The most expensive question is the one you didn\'t ask',
        'text': [
            'Studies of software projects consistently show that fixing a misunderstanding gets more expensive the later it is discovered. A wrong assumption that takes five minutes to clarify during planning can take five days to fix after the feature has been built and tested.',
            'Developers often skip clarifying questions because they want to start coding, or because they do not want to look slow or inexperienced. In reality, good questions are a sign of seniority. Junior developers build exactly what they are told; senior developers make sure they understand what is actually needed.',
            'A simple habit helps: before you start any task larger than a day, write three to five acceptance criteria and ask the person who requested it to confirm them. If they disagree with one, you have just saved yourself a lot of work.',
        ],
        'vi': 'Hiểu lầm càng phát hiện muộn càng tốn kém: giả định sai mất năm phút để làm rõ khi lập kế hoạch có thể mất năm ngày để sửa sau khi đã làm và test xong. Dev hay bỏ qua câu hỏi làm rõ vì muốn bắt tay code ngay hoặc sợ trông chậm chạp. Thực ra câu hỏi tốt là dấu hiệu của sự giàu kinh nghiệm: junior làm đúng những gì được bảo, senior đảm bảo hiểu điều thực sự cần. Thói quen đơn giản: trước mọi việc lớn hơn một ngày, viết 3–5 tiêu chí chấp nhận và nhờ người yêu cầu xác nhận.',
        'questions': [
            ('What happens to the cost of a misunderstanding over time?', ['It goes down.', 'It gets more expensive the later it is found.', 'It stays the same.', 'It disappears.'], 1, 'Đoạn 1.'),
            ('According to the text, good questions are a sign of…', ['weakness', 'seniority', 'laziness', 'confusion'], 1, 'Đoạn 2.'),
            ('What should you write before any task larger than a day?', ['A blog post', '3–5 acceptance criteria', 'A full spec', 'A test plan only'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết một đoạn hội thoại mẫu (10–14 lượt lời) giữa bạn và PM/khách hàng để làm rõ một yêu cầu mơ hồ (bạn tự chọn). Kết thúc bằng câu tóm tắt và danh sách 3–5 tiêu chí chấp nhận.',
        'tips': ['Dùng bộ 5W + Done.', 'Câu cuối: tóm tắt + "I\'ll confirm in writing".'],
        'model': "PM: Can you add notifications for users?\nMe: Sure. What problem are we trying to solve?\nPM: Customers miss their appointments.\nMe: I see. So, reminders before an appointment?\nPM: Exactly.\nMe: By email, SMS, or push notification?\nPM: SMS and email. Most customers don't install the app.\nMe: How long before the appointment?\nPM: Twenty-four hours, and maybe one hour before.\nMe: Is the app in scope?\nPM: No, just SMS and email for now.\nMe: When do you need it? Is that flexible?\nPM: End of the month, but a week later is okay.\nMe: So, to summarise: SMS and email reminders 24 hours and 1 hour before each appointment, no app notifications, by the end of the month. I'll confirm in writing.\n\nAcceptance criteria:\n1. Customer receives an SMS and email 24 hours before the appointment.\n2. Customer receives an SMS 1 hour before.\n3. No reminder is sent for cancelled appointments.\n4. Admins can turn reminders off for a customer.",
        'min_words': 120,
    },
    'quiz': [
        ('Conditions that must be met for a task to be "done" = ___.', ['acceptance criteria', 'action items', 'agenda', 'assumptions'], 0, 'acceptance criteria.'),
        ('"Make it better" is too ___.', ['vague', 'vogue', 'valid', 'vain'], 0, 'vague.'),
        ('A word that can be understood in two ways is ___.', ['ambiguous', 'ambitious', 'anonymous', 'amazing'], 0, 'ambiguous.'),
        ('"Could you ___ me through the flow?"', ['walk', 'run', 'take on', 'go'], 0, 'walk somebody through.'),
        ('A visual design of a screen before coding = a ___.', ['mockup', 'make-up', 'mock test', 'markup'], 0, 'mockup.'),
        ('Câu hỏi làm rõ tốt cho "Make the page faster":', ['Okay.', 'How fast exactly? Is under two seconds okay?', 'Why?', 'No.'], 1, 'Hỏi con số cụ thể.'),
        ('"Mobile is ___ of scope for now."', ['out', 'off', 'outside of up', 'over'], 0, 'out of scope.'),
        ('"Please confirm the new date ___ writing."', ['in', 'on', 'by', 'with'], 0, 'in writing.'),
        ('Hỏi "Why?" khi làm rõ yêu cầu giúp:', ['Làm chậm dự án', 'Hiểu vấn đề thật và đề xuất giải pháp tốt hơn', 'Gây khó chịu', 'Không có tác dụng'], 1, 'Hiểu vấn đề thật.'),
        ('"Let me ___ the deadline." (kiểm tra lại)', ['double-check', 'double-take', 'check-double', 'twice-check'], 0, 'double-check.'),
    ],
}

DAY3 = {
    'title': 'Từ chối và thương lượng',
    'title_en': 'Saying No and Negotiating',
    'goal': 'Từ chối lịch sự ("I\'m afraid that\'s not possible, but…") và luôn đề xuất phương án thay thế; tìm điểm thỏa hiệp khi thương lượng.',
    'tasks': [
        'Học 14 cụm từ từ chối và thương lượng.',
        'Học công thức từ chối: ghi nhận – lý do – không – phương án.',
        'Nghe cuộc thương lượng giữa dev và khách hàng.',
        'Viết 5 mẫu câu từ chối kèm phương án thay thế.',
    ],
    'product': '5 mẫu câu từ chối kèm phương án thay thế',
    'warmup': [
        ("I'm afraid that's not possible, but here's what we can do.", 'Tôi e là không được, nhưng đây là điều chúng tôi có thể làm.'),
        ("We don't have the capacity this month.", 'Tháng này chúng tôi không đủ nguồn lực.'),
        ('As an alternative, we could deliver it in two phases.', 'Thay vào đó, chúng tôi có thể bàn giao theo hai giai đoạn.'),
        ("Let's try to find a middle ground.", 'Hãy cố tìm điểm chung.'),
        ('Could we meet halfway?', 'Chúng ta có thể nhượng bộ mỗi bên một nửa không?'),
        ('Security is non-negotiable.', 'Bảo mật là điều không thể thương lượng.'),
    ],
    'vocab': [
        ("I'm afraid", '/aɪm əˈfreɪd/', 'phrase', 'tôi e là (mở đầu tin không vui)', "I'm afraid we can't add that before Friday.", 'Tôi e là chúng tôi không thể thêm việc đó trước thứ Sáu.'),
        ('alternative', '/ɔːlˈtɜːnətɪv/', 'n', 'phương án thay thế', 'Can I suggest an alternative?', 'Tôi có thể đề xuất phương án khác không?'),
        ('compromise', '/ˈkɒmprəmaɪz/', 'n / verb', 'sự thỏa hiệp; thỏa hiệp', 'We reached a compromise on the deadline.', 'Chúng tôi đạt được thỏa hiệp về hạn chót.'),
        ('capacity', '/kəˈpæsəti/', 'n', 'năng lực, nguồn lực (có thể đảm nhận)', "We don't have the capacity for a new project.", 'Chúng tôi không đủ nguồn lực cho dự án mới.'),
        ('decline', '/dɪˈklaɪn/', 'verb', 'từ chối (trang trọng)', 'We have to decline this request.', 'Chúng tôi phải từ chối yêu cầu này.'),
        ('counteroffer', '/ˈkaʊntərɒfə/', 'n', 'đề nghị đáp lại', 'They made a counteroffer with a lower price.', 'Họ đưa ra đề nghị đáp lại với giá thấp hơn.'),
        ('middle ground', '/ˈmɪdl ɡraʊnd/', 'n', 'điểm chung, giải pháp dung hòa', "Let's find a middle ground that works for both teams.", 'Hãy tìm giải pháp dung hòa cho cả hai team.'),
        ('meet halfway', '/miːt ˌhɑːfˈweɪ/', 'phrase', 'mỗi bên nhượng bộ một nửa', "I'll meet you halfway: two weeks instead of three.", 'Tôi nhượng bộ một nửa: hai tuần thay vì ba.'),
        ('non-negotiable', '/ˌnɒn nɪˈɡəʊʃiəbl/', 'adj', 'không thể thương lượng', 'Data security is non-negotiable.', 'Bảo mật dữ liệu là không thể thương lượng.'),
        ('concession', '/kənˈseʃn/', 'n', 'sự nhượng bộ', 'We made one concession: free support for three months.', 'Chúng tôi nhượng bộ một điều: hỗ trợ miễn phí ba tháng.'),
        ('on the table', '/ɒn ðə ˈteɪbl/', 'phrase', 'đang được xem xét', 'Several options are still on the table.', 'Một số phương án vẫn đang được xem xét.'),
        ('workable', '/ˈwɜːkəbl/', 'adj', 'khả thi, làm được', "That's a workable solution for both sides.", 'Đó là giải pháp khả thi cho cả hai bên.'),
        ('push for', '/pʊʃ fɔː/', 'phrasal verb', 'thúc ép, đòi hỏi', 'The client is pushing for an earlier launch.', 'Khách hàng đang thúc ép ra mắt sớm hơn.'),
        ('firm', '/fɜːm/', 'adj', 'cố định, chắc chắn (không đổi)', 'Is the deadline firm, or is there some flexibility?', 'Hạn chót có cố định không, hay có linh hoạt?'),
    ],
    'lesson': """
<h3>1. Công thức từ chối 4 bước</h3>
<table class="table">
<tr><th>Bước</th><th>Mẫu câu</th></tr>
<tr><td>1. Ghi nhận</td><td><span class="say">I understand this is important for your launch.</span></td></tr>
<tr><td>2. Lý do ngắn</td><td><span class="say">The team is fully booked with the payment integration this month.</span></td></tr>
<tr><td>3. Nói "không" rõ ràng</td><td><span class="say">So I'm afraid we can't add it before the 15th.</span></td></tr>
<tr><td>4. Phương án thay thế</td><td><span class="say">But here's what we can do: we can deliver a simple version by the 15th and the full version by the end of the month.</span></td></tr>
</table>

<h3>2. Từ chối mạnh và nhẹ</h3>
<table class="table">
<tr><th>Mức độ</th><th>Câu</th></tr>
<tr><td>Nhẹ nhàng</td><td><span class="say">That might be difficult, because…</span> · <span class="say">I'm not sure we can manage that by Friday.</span></td></tr>
<tr><td>Rõ ràng</td><td><span class="say">I'm afraid that's not possible, but…</span> · <span class="say">Unfortunately, we don't have the capacity.</span></td></tr>
<tr><td>Dứt khoát (nguyên tắc)</td><td><span class="say">I'm sorry, but security testing is non-negotiable.</span></td></tr>
</table>
<div class="warn"><b>Cẩn thận "That might be difficult":</b> với người Việt nghe như "có thể làm được", nhưng người bản xứ thường hiểu là "không". Nếu thật sự là không — hãy nói rõ "I'm afraid we can't…" kèm phương án.</div>

<h3>3. Thương lượng: tìm điểm chung</h3>
<div class="ex"><span class="en">What if we meet halfway: we deliver the report this week, and the dashboard next week?</span></div>
<div class="ex"><span class="en">If you can give us the designs by Monday, we can commit to Friday.</span><span class="vi">Đổi điều kiện: "If you…, we can…"</span></div>
<div class="ex"><span class="en">Which is more important to you: the date or the full feature set?</span></div>
""",
    'phrases': [
        ("Here's what we can do.", 'Đây là điều chúng tôi có thể làm.'),
        ('If you can…, we can…', 'Nếu bạn có thể…, chúng tôi có thể…'),
        ('Which is more important to you?', 'Điều gì quan trọng hơn với bạn?'),
        ("I'm sorry, but that's non-negotiable.", 'Xin lỗi, nhưng điều đó không thể thương lượng.'),
    ],
    'listening': {
        'title': 'Negotiating with a client',
        'intro': 'Khách hàng muốn thêm tính năng và giảm thời gian. Trưởng nhóm Quân từ chối lịch sự và tìm điểm chung.',
        'speakers': {'A': ('Ms. Taylor (client)', 'sonia'), 'B': ('Quan', 'guy')},
        'lines': [
            ('A', "Quan, we'd like to add a loyalty program to the app, and we still want to launch on March first.", 'Quân, chúng tôi muốn thêm chương trình khách hàng thân thiết vào app, và vẫn muốn ra mắt ngày một tháng Ba.'),
            ('B', "I understand the loyalty program is important for your marketing. But our team is fully booked with the payment work until the end of February.", 'Tôi hiểu chương trình thân thiết quan trọng cho marketing của bà. Nhưng team chúng tôi kín lịch với phần thanh toán đến hết tháng Hai.'),
            ('B', "So I'm afraid we can't add the full loyalty program and still launch on March first.", 'Nên tôi e là chúng tôi không thể thêm toàn bộ chương trình thân thiết mà vẫn ra mắt ngày một tháng Ba.'),
            ('A', "That's disappointing. The launch date is very important to us.", 'Thật đáng thất vọng. Ngày ra mắt rất quan trọng với chúng tôi.'),
            ('B', "Of course. Here's what we can do. We launch on March first with a simple version: customers can collect points. Then we add rewards and the points history two weeks later.", 'Dĩ nhiên. Đây là điều chúng tôi có thể làm. Chúng tôi ra mắt ngày một tháng Ba với bản đơn giản: khách tích điểm được. Rồi hai tuần sau thêm phần đổi thưởng và lịch sử điểm.'),
            ('A', "Hmm. Could you do the rewards as well by March first if we pay for an extra developer?", 'Hừm. Nếu chúng tôi trả thêm tiền cho một lập trình viên nữa, các anh có làm được cả phần đổi thưởng trước ngày một không?'),
            ('B', "I'm afraid adding someone new this late would slow us down at first. But let's meet halfway: if you can approve the designs by this Friday, we can include rewards and leave only the history page for later.", 'Tôi e là thêm người mới vào lúc muộn thế này ban đầu sẽ làm chúng tôi chậm hơn. Nhưng hãy nhượng bộ một nửa: nếu bà duyệt thiết kế trước thứ Sáu này, chúng tôi có thể đưa cả phần đổi thưởng vào và chỉ để trang lịch sử làm sau.'),
            ('A', "That sounds workable. And testing? Can we skip some of it to save time?", 'Nghe có vẻ khả thi. Còn kiểm thử? Có thể bỏ bớt để tiết kiệm thời gian không?'),
            ('B', "I'm sorry, but security testing for payments is non-negotiable. It protects your customers and your brand.", 'Xin lỗi, nhưng kiểm thử bảo mật cho thanh toán là không thể thương lượng. Nó bảo vệ khách hàng và thương hiệu của bà.'),
            ('A', "Fair enough. Let's go with your plan. I'll send the design approval by Friday.", 'Hợp lý. Hãy làm theo kế hoạch của anh. Tôi sẽ gửi duyệt thiết kế trước thứ Sáu.'),
        ],
        'questions': [
            ('Why can\'t the team add the full loyalty program by March 1st?', ['They don\'t know how.', 'They are fully booked with payment work.', 'The client has no budget.', 'The designs are bad.'], 1, '"fully booked with the payment work".'),
            ('What is Quan\'s first alternative?', ['Cancel the launch', 'Launch a simple version, add rewards two weeks later', 'Hire ten developers', 'Skip testing'], 1, 'Bản đơn giản trước.'),
            ('Why doesn\'t Quan want an extra developer?', ['Too expensive', 'Adding someone new this late would slow them down at first', 'No desks', 'The client is lying'], 1, 'Người mới làm chậm lúc đầu.'),
            ('What is the condition for including rewards by March 1st?', ['More money', 'Design approval by Friday', 'Skipping tests', 'Working weekends'], 1, '"if you can approve the designs by this Friday".'),
            ('What is non-negotiable?', ['The launch date', 'Security testing for payments', 'The price', 'The history page'], 1, '"security testing for payments is non-negotiable".'),
        ],
    },
    'speaking': {
        'tips': ['Mỗi tình huống: ghi nhận – lý do – không – phương án.', 'Dùng ít nhất một câu "If you…, we can…".'],
        'prompts': [
            ('A client wants three new features by next Monday. You can do one.', 'I\'m afraid… Here\'s what we can do…'),
            ('Your manager asks you to join a second project, but you\'re overloaded.', 'I don\'t have the capacity…'),
            ('A colleague wants to skip code review to save time.', 'non-negotiable…'),
        ],
        'model': (
            "I understand why you need these features before the trade fair. But our team is already working on the payment update, so I'm afraid we can't deliver all three by Monday. "
            "Here's what we can do: we can deliver the product catalogue by Monday, because that's the most important one for the fair. The other two can follow the week after. "
            "If you can send us the final product photos by Thursday, we can commit to Monday for the catalogue. "
            "Which is more important to you: having all three later, or the catalogue on time?",
            'Tôi hiểu vì sao bạn cần các tính năng này trước hội chợ. Nhưng team chúng tôi đang làm bản cập nhật thanh toán, nên tôi e là không thể bàn giao cả ba trước thứ Hai. '
            'Đây là điều chúng tôi có thể làm: bàn giao danh mục sản phẩm trước thứ Hai, vì đó là thứ quan trọng nhất cho hội chợ. Hai cái còn lại có thể theo sau một tuần. '
            'Nếu bạn gửi ảnh sản phẩm cuối cùng trước thứ Năm, chúng tôi cam kết thứ Hai cho phần danh mục. '
            'Điều gì quan trọng hơn với bạn: có cả ba nhưng muộn hơn, hay danh mục đúng hạn?'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Why "yes" can be dangerous',
        'text': [
            'In many Asian cultures, saying "no" directly to a client or a senior person feels impolite. Developers may say "I\'ll try" or "it might be difficult" when they really mean "this is impossible". International clients often hear these phrases as "yes".',
            'The result is a broken promise, which damages trust much more than an honest "no" would have. A client who hears "I\'m afraid we can\'t do all of it by Friday, but we can do this part" can plan around it. A client who hears "we\'ll try" and then gets nothing cannot.',
            'Being clear is not the same as being rude. You can say no politely, explain the reason briefly and, most importantly, offer an alternative. Clients rarely remember the no; they remember that you helped them find a solution.',
        ],
        'vi': 'Ở nhiều nền văn hóa châu Á, nói "không" thẳng với khách hàng hay cấp trên có vẻ bất lịch sự; dev nói "tôi sẽ cố" hay "có thể khó" khi thật ra là "không thể". Khách quốc tế thường hiểu những câu này là "có". Kết quả là lời hứa bị phá vỡ, gây mất lòng tin hơn nhiều so với một câu "không" thành thật. Rõ ràng không có nghĩa là thô lỗ: bạn có thể từ chối lịch sự, giải thích ngắn gọn và quan trọng nhất là đưa phương án thay thế. Khách hiếm khi nhớ lời từ chối; họ nhớ bạn đã giúp tìm ra giải pháp.',
        'questions': [
            ('How do international clients often hear "I\'ll try"?', ['As "no"', 'As "yes"', 'As a joke', 'As a question'], 1, 'Đoạn 1.'),
            ('What damages trust more?', ['An honest no', 'A broken promise', 'A long email', 'A phone call'], 1, 'Đoạn 2.'),
            ('What do clients remember, according to the text?', ['The no', 'That you helped them find a solution', 'The price', 'Your English'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 5 mẫu câu từ chối (mỗi mẫu 2–3 câu) cho 5 tình huống khác nhau trong công việc, mỗi mẫu đều có phương án thay thế.',
        'tips': ['Đủ 4 bước: ghi nhận – lý do – không – phương án.'],
        'model': "1. (Extra feature) I understand the export is important, but we're focused on the payment release this week. I'm afraid we can't add it now. We could start on Monday and deliver it by Wednesday.\n2. (Second project) Thanks for thinking of me. I don't have the capacity right now because of the migration, but I could join from the next sprint, or review their designs for an hour this week.\n3. (Skip testing) I know we're short on time, but testing the payment flow is non-negotiable. What we can do is skip the nice-to-have animations instead.\n4. (Weekend work) I'm afraid I can't work this weekend. However, I can start earlier on Monday and send you an update by noon.\n5. (Lower price) Unfortunately, we can't lower the price for the full scope. If you remove the admin dashboard, we can reduce it by 20%.",
        'min_words': 120,
    },
    'quiz': [
        ('"___, but that\'s not possible." (tôi e là)', ["I'm afraid", "I'm scared", "I'm fear", "I worry"], 0, "I'm afraid…"),
        ('Công thức từ chối:', ['Không – hết', 'Ghi nhận – lý do – không – phương án', 'Im lặng', 'Nói "I\'ll try"'], 1, '4 bước.'),
        ('"That might be difficult" thường được người bản xứ hiểu là:', ['Chắc chắn làm được', 'Có lẽ là không', 'Sẽ làm ngay', 'Rất dễ'], 1, 'Thường mang nghĩa "không".'),
        ('"We don\'t have the ___ this month." (nguồn lực)', ['capacity', 'capability up', 'capital', 'caption'], 0, 'capacity.'),
        ('Each side gives up half: let\'s ___ halfway.', ['meet', 'go', 'come', 'walk'], 0, 'meet halfway.'),
        ('Something you will not change under any condition is ___.', ['non-negotiable', 'negotiable', 'flexible', 'optional'], 0, 'non-negotiable.'),
        ('A solution both sides can accept is a ___.', ['compromise', 'complaint', 'compliment', 'component'], 0, 'compromise.'),
        ('"If you can approve the designs by Friday, we ___ commit to Monday."', ['can', 'could have', 'will be', 'are'], 0, 'If you can…, we can…'),
        ('"Several options are still on the ___."', ['table', 'desk', 'board', 'floor'], 0, 'on the table.'),
        ('Vì sao "yes" có thể nguy hiểm?', ['Vì khách không thích', 'Vì lời hứa bị phá vỡ làm mất lòng tin', 'Vì quá ngắn', 'Vì sai ngữ pháp'], 1, 'Broken promise.'),
    ],
}

DAY4 = {
    'title': 'Báo trễ deadline',
    'title_en': 'Reporting a Delay',
    'goal': 'Viết email/tin nhắn báo trễ hạn chuyên nghiệp: báo sớm, lý do ngắn gọn, thời gian mới cụ thể, kế hoạch giảm thiểu ảnh hưởng.',
    'tasks': [
        'Học 14 từ về chậm trễ và kế hoạch xử lý.',
        'Học khung email báo trễ 5 phần.',
        'Nghe cuộc gọi báo trễ với quản lý.',
        'Viết 1 email báo trễ mẫu.',
    ],
    'product': '1 email báo trễ mẫu',
    'warmup': [
        ("I'm writing to let you know about a delay.", 'Tôi viết để báo về một sự chậm trễ.'),
        ('Due to an unforeseen issue, the release will move to Thursday.', 'Do một vấn đề không lường trước, bản phát hành sẽ dời sang thứ Năm.'),
        ('Here is our revised timeline.', 'Đây là tiến độ đã điều chỉnh.'),
        ('To mitigate the impact, we will release the core features first.', 'Để giảm thiểu ảnh hưởng, chúng tôi sẽ phát hành tính năng cốt lõi trước.'),
        ('I apologise for the inconvenience.', 'Tôi xin lỗi vì sự bất tiện.'),
        ("I'll keep you updated every day until it's done.", 'Tôi sẽ cập nhật cho bạn mỗi ngày cho đến khi xong.'),
    ],
    'vocab': [
        ('delay', '/dɪˈleɪ/', 'n / verb', 'sự chậm trễ; trì hoãn', 'Sorry for the delay in getting back to you.', 'Xin lỗi vì trả lời chậm.'),
        ('revised timeline', '/rɪˈvaɪzd ˈtaɪmlaɪn/', 'n', 'tiến độ đã điều chỉnh', 'Please see the revised timeline below.', 'Vui lòng xem tiến độ đã điều chỉnh bên dưới.'),
        ('unforeseen', '/ˌʌnfɔːˈsiːn/', 'adj', 'không lường trước', 'We ran into an unforeseen problem with the data.', 'Chúng tôi gặp một vấn đề không lường trước với dữ liệu.'),
        ('apologise', '/əˈpɒlədʒaɪz/', 'verb', 'xin lỗi (trang trọng)', 'I apologise for any inconvenience this may cause.', 'Tôi xin lỗi vì mọi bất tiện có thể gây ra.'),
        ('mitigate', '/ˈmɪtɪɡeɪt/', 'verb', 'giảm thiểu (tác hại)', 'To mitigate the risk, we added extra testing.', 'Để giảm thiểu rủi ro, chúng tôi thêm kiểm thử.'),
        ('buffer', '/ˈbʌfə/', 'n', 'thời gian dự phòng', 'Always add a buffer of a few days.', 'Luôn thêm vài ngày dự phòng.'),
        ('inconvenience', '/ˌɪnkənˈviːniəns/', 'n', 'sự bất tiện', 'We apologise for the inconvenience.', 'Chúng tôi xin lỗi vì sự bất tiện.'),
        ('contingency plan', '/kənˈtɪndʒənsi plæn/', 'n', 'kế hoạch dự phòng', 'What is our contingency plan if the API is not ready?', 'Kế hoạch dự phòng của ta là gì nếu API chưa sẵn sàng?'),
        ('transparent', '/trænsˈpærənt/', 'adj', 'minh bạch', "I want to be transparent about the risks.", 'Tôi muốn minh bạch về các rủi ro.'),
        ('slippage', '/ˈslɪpɪdʒ/', 'n', 'sự trượt tiến độ', 'There has been some slippage in the schedule.', 'Tiến độ đã bị trượt một chút.'),
        ('recovery plan', '/rɪˈkʌvəri plæn/', 'n', 'kế hoạch khắc phục', "Here's our recovery plan to get back on track.", 'Đây là kế hoạch khắc phục để quay lại đúng tiến độ.'),
        ('ahead of time', '/əˈhed əv taɪm/', 'phrase', 'trước (thời hạn)', 'Thanks for letting me know ahead of time.', 'Cảm ơn đã báo trước cho tôi.'),
        ('underestimate', '/ˌʌndərˈestɪmeɪt/', 'verb', 'đánh giá thấp', 'We underestimated the complexity of the migration.', 'Chúng tôi đã đánh giá thấp độ phức tạp của việc chuyển đổi.'),
        ('knock-on effect', '/ˈnɒk ɒn ɪˈfekt/', 'n', 'hiệu ứng dây chuyền', 'The delay will have a knock-on effect on the marketing campaign.', 'Sự chậm trễ sẽ gây hiệu ứng dây chuyền lên chiến dịch marketing.'),
    ],
    'lesson': """
<h3>1. Khung email báo trễ 5 phần</h3>
<table class="table">
<tr><th>Phần</th><th>Mẫu câu</th></tr>
<tr><td>1. Tin chính (đầu email)</td><td><span class="say">I'm writing to let you know that the release will move from Tuesday to Thursday.</span></td></tr>
<tr><td>2. Lý do (1–2 câu, không đổ lỗi)</td><td><span class="say">During final testing, we found an issue with large file uploads, and we want to fix it properly.</span></td></tr>
<tr><td>3. Ảnh hưởng</td><td><span class="say">The rest of the features are ready, and the delay does not affect the March launch.</span></td></tr>
<tr><td>4. Kế hoạch / giảm thiểu</td><td><span class="say">To mitigate the impact, we can release everything except uploads on Tuesday.</span></td></tr>
<tr><td>5. Xin lỗi + cập nhật tiếp</td><td><span class="say">I apologise for the inconvenience. I'll send you an update on Wednesday afternoon.</span></td></tr>
</table>

<h3>2. Nguyên tắc</h3>
<ul>
<li><b>Báo sớm</b> — ngay khi biết, không đợi đến hạn chót.</li>
<li><b>Ngày mới cụ thể</b> — "Thursday the 12th", không phải "soon" hay "next week".</li>
<li><b>Chịu trách nhiệm</b> — "We underestimated…" thay vì đổ lỗi cho người khác.</li>
<li><b>Có thêm dự phòng</b> — hứa ngày mà bạn chắc chắn làm được (có buffer).</li>
<li><b>Xin lỗi một lần</b> — đủ chân thành, không lặp lại nhiều lần.</li>
</ul>

<h3>3. Câu tránh và câu nên dùng</h3>
<div class="fix"><s>Sorry, it's not finished. Maybe next week.</s><span class="en">The feature will be ready on Thursday the 12th instead of Tuesday the 10th.</span></div>
<div class="fix"><s>The backend team was too slow, so we are late.</s><span class="en">We underestimated the time needed to integrate the new API.</span></div>
<div class="fix"><s>Sorry sorry, very sorry for the late.</s><span class="en">I apologise for the inconvenience.</span></div>
""",
    'phrases': [
        ("I wanted to flag this as early as possible.", 'Tôi muốn báo việc này sớm nhất có thể.'),
        ('This does not affect the launch date.', 'Việc này không ảnh hưởng đến ngày ra mắt.'),
        ("I'll send you an update on…", 'Tôi sẽ gửi cập nhật cho bạn vào…'),
        ('We underestimated…', 'Chúng tôi đã đánh giá thấp…'),
    ],
    'listening': {
        'title': 'Calling the manager about a delay',
        'intro': 'Developer Tâm gọi cho quản lý ngay khi nhận ra sẽ trễ hạn.',
        'speakers': {'A': ('Tam', 'ava'), 'B': ('Steve (manager)', 'ryan')},
        'lines': [
            ('A', "Hi Steve, do you have five minutes? I wanted to flag something as early as possible.", 'Chào Steve, anh có năm phút không? Em muốn báo một việc sớm nhất có thể.'),
            ('B', "Sure, what's up?", 'Chắc chắn, có chuyện gì?'),
            ('A', "The data migration won't be ready on Friday. I think we need until Wednesday next week.", 'Việc chuyển đổi dữ liệu sẽ không xong vào thứ Sáu. Em nghĩ cần đến thứ Tư tuần sau.'),
            ('B', "Okay. What happened?", 'Được. Chuyện gì đã xảy ra?'),
            ('A', "We underestimated the old data. About fifteen percent of the records have missing fields, so the import fails. We need to write rules to clean them first.", 'Bọn em đánh giá thấp dữ liệu cũ. Khoảng mười lăm phần trăm bản ghi bị thiếu trường, nên việc nhập bị lỗi. Cần viết quy tắc làm sạch chúng trước.'),
            ('B', "I see. Does this affect the launch?", 'Anh hiểu. Việc này có ảnh hưởng đến ngày ra mắt không?'),
            ('A', "Not if we're careful. The launch is in three weeks, so we still have a buffer. But there's a knock-on effect on testing: QA will start two days later.", 'Không, nếu cẩn thận. Còn ba tuần nữa mới ra mắt nên vẫn có thời gian dự phòng. Nhưng có hiệu ứng dây chuyền lên kiểm thử: QA sẽ bắt đầu muộn hai ngày.'),
            ('B', "What's your plan to mitigate that?", 'Kế hoạch giảm thiểu của em là gì?'),
            ('A', "We can migrate the clean records first, on Friday, so QA can start testing with them. The difficult fifteen percent will follow on Wednesday.", 'Bọn em có thể chuyển các bản ghi sạch trước, vào thứ Sáu, để QA bắt đầu kiểm thử với chúng. Mười lăm phần trăm khó sẽ theo sau vào thứ Tư.'),
            ('B', "That's a good contingency plan. Thanks for telling me ahead of time. Can you put it in an email so I can share it with the client?", 'Kế hoạch dự phòng tốt đấy. Cảm ơn em đã báo trước. Em viết thành email để anh chia sẻ với khách hàng được không?'),
            ('A', "Of course. I'll send it within the hour.", 'Dĩ nhiên. Em sẽ gửi trong vòng một giờ.'),
        ],
        'questions': [
            ('When will the migration be ready now?', ['Friday', 'Monday', 'Wednesday next week', 'In three weeks'], 2, '"until Wednesday next week".'),
            ('What was the cause of the delay?', ['A sick developer', '15% of old records have missing fields', 'The server crashed', 'The client changed the design'], 1, '"About fifteen percent of the records have missing fields".'),
            ('What is the knock-on effect?', ['The launch moves.', 'QA will start two days later.', 'The client leaves.', 'Costs double.'], 1, '"QA will start two days later".'),
            ('What is Tam\'s mitigation plan?', ['Skip testing', 'Migrate the clean records first so QA can start', 'Hire more people', 'Cancel the migration'], 1, 'Chuyển bản ghi sạch trước.'),
            ('What does Steve ask Tam to do?', ['Work at the weekend', 'Put it in an email to share with the client', 'Call the client', 'Fix it today'], 1, 'Viết email.'),
        ],
    },
    'speaking': {
        'tips': ['Đóng vai Tâm ở phần Nghe.', 'Báo trễ bằng lời trong 1 phút: tin chính → lý do → ảnh hưởng → kế hoạch → cập nhật tiếp.'],
        'prompts': [
            ('Call your manager: your feature will be three days late because an external API changed.', 'I wanted to flag…'),
            ('Tell a client the release is moving by one week. Stay calm and offer a plan.', 'I\'m writing/calling to let you know…'),
        ],
        'model': (
            "Hi Anna, do you have a minute? I wanted to flag something as early as possible. The booking feature will be three days late: Friday instead of Tuesday. "
            "The reason is that the payment provider changed their API last week, and we need to update our integration. "
            "The good news is that the rest of the feature is finished, and the launch date isn't affected, because we have a one-week buffer. "
            "To mitigate the impact, QA can start testing the booking flow tomorrow with a test payment. "
            "I'm sorry about this. I'll send you a short written update every afternoon until it's done.",
            'Chào Anna, chị có một phút không? Em muốn báo một việc sớm nhất có thể. Tính năng đặt chỗ sẽ trễ ba ngày: thứ Sáu thay vì thứ Ba. '
            'Lý do là bên cung cấp thanh toán đã đổi API tuần trước và bọn em cần cập nhật phần tích hợp. '
            'Tin tốt là phần còn lại của tính năng đã xong, và ngày ra mắt không bị ảnh hưởng vì có một tuần dự phòng. '
            'Để giảm thiểu ảnh hưởng, QA có thể bắt đầu kiểm thử luồng đặt chỗ từ mai với thanh toán thử. '
            'Em xin lỗi về chuyện này. Em sẽ gửi cập nhật ngắn bằng văn bản mỗi chiều cho đến khi xong.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Bad news early is good news',
        'text': [
            'There is an old saying among project managers: "Bad news early is good news." A delay reported three weeks before a deadline is a planning problem. The same delay reported on the morning of the deadline is a crisis.',
            'When people hear about a problem early, they have options. They can move resources, change the scope, inform customers or adjust a marketing campaign. When they hear about it late, the only option left is disappointment.',
            'This is why the best engineers are not the ones who never have delays. Everyone has delays. The best engineers are the ones whose managers are never surprised.',
        ],
        'vi': 'Câu nói quen thuộc của quản lý dự án: "Tin xấu đến sớm là tin tốt." Trễ hạn được báo ba tuần trước hạn chót là vấn đề kế hoạch; cùng sự chậm trễ đó báo vào sáng ngày hạn chót là khủng hoảng. Khi biết sớm, người ta có lựa chọn: điều chỉnh nguồn lực, phạm vi, báo khách hàng, đổi chiến dịch marketing. Khi biết muộn, chỉ còn thất vọng. Kỹ sư giỏi nhất không phải người không bao giờ trễ — ai cũng trễ — mà là người khiến quản lý không bao giờ bị bất ngờ.',
        'questions': [
            ('What is a delay reported on the morning of the deadline?', ['A planning problem', 'A crisis', 'Good news', 'Normal'], 1, 'Đoạn 1.'),
            ('Why is early bad news useful?', ['People have options.', 'It is cheaper to send.', 'Managers like emails.', 'It sounds better.'], 0, 'Đoạn 2.'),
            ('Who are the best engineers, according to the text?', ['Those who never have delays', 'Those whose managers are never surprised', 'The fastest coders', 'The most senior'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 1 email báo trễ (120–160 từ) gửi khách hàng hoặc quản lý theo khung 5 phần, dựa trên tình huống thật hoặc giả định.',
        'tips': ['Ngày mới cụ thể. Một lời xin lỗi. Có kế hoạch giảm thiểu.', 'Dùng: I\'m writing to let you know…, We underestimated…, To mitigate…'],
        'model': "Subject: Update: data migration moved to Wednesday 14th\n\nDear Ms. Johnson,\n\nI'm writing to let you know that the data migration will be completed on Wednesday the 14th instead of Friday the 9th.\n\nDuring the final checks, we found that about 15% of the old customer records have missing fields. We underestimated how much cleaning this data would need, and we want to make sure nothing is lost.\n\nThis does not affect the launch date on the 30th. To mitigate the impact, we will migrate all complete records this Friday, so your team can start testing on Monday as planned. The remaining records will follow on Wednesday.\n\nI apologise for the inconvenience. I will send you a short progress update every afternoon until the migration is complete.\n\nKind regards,\nTam Nguyen",
        'min_words': 110,
    },
    'quiz': [
        ('Câu mở email báo trễ tốt nhất:', ['Sorry, sorry, sorry.', "I'm writing to let you know that the release will move from Tuesday to Thursday.", 'Bad news!', 'Maybe late.'], 1, 'Tin chính ngay đầu.'),
        ('Ngày mới nên được nêu:', ['soon', 'next week maybe', 'Thursday the 12th', 'when possible'], 2, 'Cụ thể.'),
        ('"We ___ the complexity of the migration." (đánh giá thấp)', ['underestimated', 'overestimated', 'understood', 'undertook'], 0, 'underestimate.'),
        ('Extra time added to a plan for safety = a ___.', ['buffer', 'butter', 'border', 'bumper'], 0, 'buffer.'),
        ('"To ___ the impact, we will release core features first."', ['mitigate', 'migrate', 'motivate', 'mediate'], 0, 'mitigate.'),
        ('A problem nobody expected is ___.', ['unforeseen', 'unforgiven', 'unfounded', 'unseen up'], 0, 'unforeseen.'),
        ('A delay that causes other delays has a ___ effect.', ['knock-on', 'knock-out', 'knock-off', 'knock-down'], 0, 'knock-on effect.'),
        ('Plan B if things go wrong = a ___ plan.', ['contingency', 'continuity', 'content', 'continent'], 0, 'contingency plan.'),
        ('Câu chịu trách nhiệm (không đổ lỗi):', ['The other team was too slow.', 'We underestimated the time needed.', 'It\'s not my fault.', 'The client is difficult.'], 1, 'Nhận trách nhiệm.'),
        ('"Bad news early is ___ news."', ['good', 'bad', 'old', 'fake'], 0, 'Tin xấu sớm là tin tốt.'),
    ],
}

DAY5 = {
    'title': 'Đóng vai tình huống bất ngờ',
    'title_en': 'Role-play: Unexpected Situations',
    'goal': 'Phản ứng ngay trong 3 tình huống bất ngờ: sự cố production, khách hàng tức giận, bị hỏi bất ngờ trước cả nhóm — giữ bình tĩnh và dùng câu phù hợp.',
    'tasks': [
        'Học 14 từ về sự cố và xử lý khủng hoảng.',
        'Học công thức xử lý: Acknowledge – Reassure – Act – Update.',
        'Nghe cuộc gọi với khách hàng đang tức giận vì sự cố.',
        'Đóng vai 3 tình huống bất ngờ ở phần Nói (trả lời ngay, không chuẩn bị).',
        'Ghi chú phản ứng của bạn và cách làm tốt hơn.',
    ],
    'product': 'Bản ghi 3 tình huống; Ghi chú phản ứng',
    'warmup': [
        ("I completely understand your frustration.", 'Tôi hoàn toàn hiểu sự bực bội của bạn.'),
        ("We're aware of the outage and we're working on it.", 'Chúng tôi biết về sự cố và đang xử lý.'),
        ("I'll escalate this to our senior engineer right now.", 'Tôi sẽ chuyển việc này lên kỹ sư cấp cao ngay bây giờ.'),
        ('Let me check and come back to you in fifteen minutes.', 'Để tôi kiểm tra và quay lại với bạn sau mười lăm phút.'),
        ("I take full responsibility for this mistake.", 'Tôi hoàn toàn chịu trách nhiệm về lỗi này.'),
        ("You've put me on the spot, but let me try.", 'Bạn hỏi bất ngờ quá, nhưng để tôi thử.'),
    ],
    'vocab': [
        ('incident', '/ˈɪnsɪdənt/', 'n', 'sự cố', 'We had a major incident last night.', 'Tối qua chúng tôi gặp sự cố lớn.'),
        ('outage', '/ˈaʊtɪdʒ/', 'n', 'sự ngừng hoạt động (dịch vụ)', 'The outage lasted forty minutes.', 'Sự cố ngừng hoạt động kéo dài bốn mươi phút.'),
        ('escalate', '/ˈeskəleɪt/', 'verb', 'chuyển lên cấp cao hơn; leo thang', "If it's not fixed in an hour, escalate it to the CTO.", 'Nếu một giờ chưa sửa được, chuyển lên CTO.'),
        ('de-escalate', '/ˌdiːˈeskəleɪt/', 'verb', 'làm dịu (tình huống căng thẳng)', 'A calm voice helps de-escalate the situation.', 'Giọng bình tĩnh giúp làm dịu tình huống.'),
        ('stay calm', '/steɪ kɑːm/', 'phrase', 'giữ bình tĩnh', 'Stay calm and focus on the facts.', 'Giữ bình tĩnh và tập trung vào sự thật.'),
        ('take responsibility', '/teɪk rɪˌspɒnsəˈbɪləti/', 'phrase', 'nhận trách nhiệm', 'I take responsibility for the mistake.', 'Tôi nhận trách nhiệm về sai sót.'),
        ('put on the spot', '/pʊt ɒn ðə spɒt/', 'phrase', 'hỏi bất ngờ khiến lúng túng', 'The CEO put me on the spot with a question about costs.', 'CEO hỏi bất ngờ tôi về chi phí khiến tôi lúng túng.'),
        ('irate', '/aɪˈreɪt/', 'adj', 'giận dữ', 'An irate customer called the support line.', 'Một khách hàng giận dữ gọi đường dây hỗ trợ.'),
        ('reassure', '/ˌriːəˈʃʊə/', 'verb', 'trấn an', 'I reassured the client that no data was lost.', 'Tôi trấn an khách hàng rằng không mất dữ liệu.'),
        ('acknowledge', '/əkˈnɒlɪdʒ/', 'verb', 'thừa nhận, ghi nhận', 'First, acknowledge the problem.', 'Đầu tiên, hãy thừa nhận vấn đề.'),
        ('status page', '/ˈsteɪtəs peɪdʒ/', 'n', 'trang trạng thái dịch vụ', 'Check our status page for live updates.', 'Xem trang trạng thái để cập nhật trực tiếp.'),
        ('on call', '/ɒn kɔːl/', 'phrase', 'trực (sẵn sàng xử lý sự cố)', "I'm on call this weekend.", 'Cuối tuần này tôi trực.'),
        ('triage', '/ˈtriːɑːʒ/', 'n / verb', 'phân loại mức ưu tiên', "Let's triage the bugs: critical ones first.", 'Hãy phân loại lỗi: lỗi nghiêm trọng trước.'),
        ('post-mortem', '/ˌpəʊst ˈmɔːtəm/', 'n', 'bản phân tích sau sự cố', "We'll write a post-mortem by Friday.", 'Chúng tôi sẽ viết phân tích sau sự cố trước thứ Sáu.'),
    ],
    'lesson': """
<h3>1. Công thức xử lý tình huống căng thẳng: A-R-A-U</h3>
<table class="table">
<tr><th>Bước</th><th>Mẫu câu</th></tr>
<tr><td><b>Acknowledge</b> — ghi nhận</td><td><span class="say">I completely understand your frustration, and I'm sorry this happened.</span></td></tr>
<tr><td><b>Reassure</b> — trấn an (bằng sự thật)</td><td><span class="say">Your data is safe. Nothing has been lost.</span></td></tr>
<tr><td><b>Act</b> — hành động cụ thể</td><td><span class="say">Our team is restoring the service right now, and I've escalated it to our senior engineer.</span></td></tr>
<tr><td><b>Update</b> — hẹn cập nhật</td><td><span class="say">I'll call you back in thirty minutes, even if we don't have a fix yet.</span></td></tr>
</table>

<h3>2. Ba tình huống thường gặp</h3>
<h4>a) Sự cố production</h4>
<div class="ex"><span class="en">We're aware of the issue and we're investigating. I'll post an update on the status page every thirty minutes.</span></div>
<h4>b) Khách hàng tức giận</h4>
<div class="ex"><span class="en">I hear you, and you're right to be upset. Let me tell you exactly what we're doing to fix it.</span></div>
<p>Không ngắt lời, không tranh cãi, không đổ lỗi. Nói chậm và thấp giọng hơn bình thường.</p>
<h4>c) Bị hỏi bất ngờ trước cả nhóm</h4>
<div class="ex"><span class="en">That's a good question. I don't have the full picture right now, but here's what I know so far… I'll confirm the details after the meeting.</span></div>

<h3>3. Những câu nên tránh</h3>
<div class="fix"><s>It's not my fault.</s><span class="en">Let me look into what happened.</span></div>
<div class="fix"><s>Calm down!</s><span class="en">I understand this is really frustrating.</span></div>
<div class="fix"><s>I have no idea.</s><span class="en">I don't know yet, but I'll find out and get back to you by 3 p.m.</span></div>
""",
    'phrases': [
        ("I completely understand your frustration.", 'Tôi hoàn toàn hiểu sự bực bội của bạn.'),
        ("Here's what we're doing right now.", 'Đây là những gì chúng tôi đang làm ngay lúc này.'),
        ("I'll call you back in thirty minutes, even if we don't have a fix yet.", 'Tôi sẽ gọi lại sau ba mươi phút, kể cả khi chưa sửa xong.'),
        ("I don't have the full picture yet.", 'Tôi chưa nắm toàn bộ tình hình.'),
    ],
    'listening': {
        'title': 'An angry client during an outage',
        'intro': 'Trang web bán hàng của khách sập đúng ngày khuyến mãi. Khách gọi đến rất giận. Chú ý cách Ngân giữ bình tĩnh.',
        'speakers': {'A': ('Mr. Brooks (client)', 'guy'), 'B': ('Ngan', 'jenny')},
        'lines': [
            ('A', "This is unacceptable! It's our biggest sale of the year and the website has been down for twenty minutes! We're losing thousands of dollars!", 'Không thể chấp nhận được! Đây là đợt sale lớn nhất năm mà website đã sập hai mươi phút! Chúng tôi đang mất hàng nghìn đô!'),
            ('B', "Mr. Brooks, I completely understand your frustration, and you're right to be upset. I'm sorry this is happening today of all days.", 'Ông Brooks, tôi hoàn toàn hiểu sự bực bội của ông, và ông giận là đúng. Tôi rất tiếc chuyện này xảy ra đúng vào hôm nay.'),
            ('A', "Sorry doesn't help me. When will it be back?", 'Xin lỗi chẳng giúp được gì. Khi nào nó chạy lại?'),
            ('B', "Let me tell you exactly what we know and what we're doing. The problem is that the traffic was five times higher than expected, and the database couldn't handle it.", 'Để tôi nói chính xác những gì chúng tôi biết và đang làm. Vấn đề là lưu lượng cao gấp năm lần dự kiến, và cơ sở dữ liệu không chịu nổi.'),
            ('B', "First, I want to reassure you: no orders or customer data have been lost. Second, our on-call team is adding more database capacity right now, and I've escalated it to our CTO.", 'Trước hết, tôi muốn trấn an ông: không có đơn hàng hay dữ liệu khách hàng nào bị mất. Thứ hai, đội trực đang tăng năng lực cơ sở dữ liệu ngay lúc này, và tôi đã báo lên CTO.'),
            ('A', "How long will that take?", 'Việc đó mất bao lâu?'),
            ('B', "Our estimate is about fifteen minutes. In the meantime, we've put a message on the website so customers know the sale will be extended.", 'Ước tính khoảng mười lăm phút. Trong lúc đó, chúng tôi đã đặt thông báo trên website để khách biết đợt sale sẽ được kéo dài.'),
            ('A', "Extended? Who decided that?", 'Kéo dài? Ai quyết định vậy?'),
            ('B', "That's only a suggestion. If you agree, we can extend the sale by two hours at no cost to you. It's your decision.", 'Đó chỉ là đề xuất. Nếu ông đồng ý, chúng tôi có thể kéo dài sale thêm hai giờ mà ông không mất chi phí. Quyết định là của ông.'),
            ('A', "Okay… that would help. Fine, do it.", 'Được… điều đó có ích. Ừ, làm đi.'),
            ('B', "Thank you. I'll call you back in fifteen minutes, even if we're not fully back yet. And after this, we'll send you a full post-mortem explaining what happened and how we'll prevent it.", 'Cảm ơn ông. Tôi sẽ gọi lại sau mười lăm phút, kể cả khi chưa chạy lại hoàn toàn. Và sau việc này, chúng tôi sẽ gửi ông bản phân tích đầy đủ về chuyện đã xảy ra và cách ngăn chặn.'),
        ],
        'questions': [
            ('Why is the client so angry?', ['His order was wrong.', 'The website went down during his biggest sale.', 'The price went up.', 'Ngan was late.'], 1, 'Sập trong đợt sale lớn nhất năm.'),
            ('What caused the outage?', ['A hacker', 'Traffic five times higher than expected', 'A power cut', 'A bad design'], 1, '"the traffic was five times higher than expected".'),
            ('How does Ngan reassure him?', ['She says it is not her fault.', 'She says no orders or data have been lost.', 'She offers a discount.', 'She asks him to calm down.'], 1, '"no orders or customer data have been lost".'),
            ('What does Ngan suggest?', ['Cancel the sale', 'Extend the sale by two hours at no cost', 'Move to another company', 'Wait until tomorrow'], 1, 'Kéo dài sale hai giờ.'),
            ('What will Ngan send after the incident?', ['An invoice', 'A post-mortem', 'A gift', 'Nothing'], 1, '"a full post-mortem".'),
        ],
    },
    'speaking': {
        'tips': ['Bấm nghe từng tình huống và phản ứng NGAY, không chuẩn bị. Ghi âm cả 3.', 'Dùng A-R-A-U. Nói chậm, giọng thấp, bình tĩnh.', 'Sau đó ghi chú: câu nào tốt, câu nào nên đổi.'],
        'prompts': [
            ('[Situation 1] It\'s 9 a.m. Users can\'t log in. Your manager calls: "What\'s going on?"', 'We\'re aware… Here\'s what we know… I\'ll update you in…'),
            ('[Situation 2] A client shouts: "You promised this feature last week! Why isn\'t it ready?"', 'I understand your frustration… Here\'s what happened… Here\'s the new plan…'),
            ('[Situation 3] In a big meeting, the CEO suddenly asks you: "How much will the new system cost us per month?"', 'I don\'t have the exact number… what I know so far… I\'ll confirm…'),
        ],
        'model': (
            "Situation two: I completely understand your frustration, and you're right. We told you it would be ready last week, and it isn't. I'm sorry about that. "
            "Here's what happened: during testing, we found a problem with how payments are saved, and we decided not to release something that could lose your customers' money. "
            "The fix is finished, and it's being tested now. The new date is this Thursday, and I'm confident about that date. "
            "I'll send you a short update every afternoon until then, so you're never left wondering.",
            'Tình huống hai: Tôi hoàn toàn hiểu sự bực bội của bạn, và bạn nói đúng. Chúng tôi đã nói tuần trước sẽ xong, và nó chưa xong. Tôi xin lỗi về điều đó. '
            'Đây là chuyện đã xảy ra: trong lúc kiểm thử, chúng tôi phát hiện vấn đề trong cách lưu thanh toán, và quyết định không phát hành thứ có thể làm mất tiền của khách hàng bạn. '
            'Bản sửa đã xong và đang được kiểm thử. Ngày mới là thứ Năm này, và tôi tự tin về ngày đó. '
            'Tôi sẽ gửi bạn cập nhật ngắn mỗi chiều cho đến lúc đó, để bạn không phải băn khoăn.'
        ),
        'seconds': 240,
    },
    'reading': {
        'title': 'Communication during an incident',
        'text': [
            'During an outage, engineers naturally focus on fixing the problem. But for customers and managers, silence is often worse than the outage itself. When nobody is giving updates, people imagine the worst.',
            'Many companies therefore separate two roles during a serious incident. One person, the incident commander, coordinates the technical work. Another person handles communication: updating the status page, answering the support team and calling key clients.',
            'Good incident updates are short and regular, even when there is no news: "We are still working on the database issue. Next update at 10:30." This tells people that someone is in control, which reduces panic and saves the engineers from being interrupted every five minutes.',
        ],
        'vi': 'Khi có sự cố, kỹ sư tập trung sửa lỗi, nhưng với khách hàng và quản lý, sự im lặng thường tệ hơn chính sự cố — không ai cập nhật thì người ta tưởng tượng điều tồi tệ nhất. Vì vậy nhiều công ty tách hai vai trò: người chỉ huy sự cố điều phối kỹ thuật, và người phụ trách giao tiếp cập nhật trang trạng thái, trả lời đội hỗ trợ, gọi khách hàng quan trọng. Cập nhật tốt ngắn và đều đặn, kể cả khi chưa có tin mới, để mọi người biết có người đang kiểm soát — giảm hoảng loạn và để kỹ sư không bị làm phiền liên tục.',
        'questions': [
            ('What is often worse than the outage itself?', ['The cost', 'Silence', 'The fix', 'The post-mortem'], 1, 'Đoạn 1.'),
            ('What does the second person do during an incident?', ['Writes code', 'Handles communication', 'Calls the police', 'Goes home'], 1, 'Đoạn 2.'),
            ('Why send updates even when there is no news?', ['To fill time', 'To show someone is in control and reduce panic', 'Managers require long emails', 'To blame others'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Ghi chú cho 3 tình huống bạn vừa đóng vai: bạn đã nói gì, câu nào tốt, câu nào nên đổi. Sau đó viết một thông báo cập nhật sự cố ngắn (3–4 câu) cho trang trạng thái.',
        'tips': ['Thông báo sự cố: chuyện gì, ảnh hưởng gì, đang làm gì, cập nhật tiếp khi nào.'],
        'model': "Situation 1 (login outage): I started well (\"We're aware of the issue\"), but I forgot to say when I'd update my manager. Next time: \"I'll update you in 20 minutes.\"\nSituation 2 (angry client): I said \"It's not only our fault\" — too defensive. Better: \"You're right to be upset. Here's what happened.\"\nSituation 3 (CEO question): I panicked and gave a random number. Better: \"I don't have the exact figure, but it's roughly 2,000 dollars a month. I'll confirm today.\"\n\nStatus page update:\n10:05 – We are aware that some users cannot log in. Your data is safe, and no payments have been affected. Our engineers are working on a fix. Next update at 10:30.",
        'min_words': 80,
    },
    'quiz': [
        ('Công thức xử lý tình huống căng thẳng:', ['Acknowledge – Reassure – Act – Update', 'Argue – Refuse – Avoid – Undo', 'Apologise – Run – Ask – Under', 'Answer – Reply – Agree – Unmute'], 0, 'A-R-A-U.'),
        ('Câu tốt nhất với khách đang giận:', ['Calm down!', "It's not my fault.", 'I completely understand your frustration.', 'Whatever.'], 2, 'Ghi nhận cảm xúc.'),
        ('A period when a service is not working = an ___.', ['outage', 'outrage', 'output', 'outlet'], 0, 'outage.'),
        ('To pass a problem to someone more senior = to ___.', ['escalate', 'evaluate', 'estimate', 'elevate up'], 0, 'escalate.'),
        ('To make a tense situation calmer = to ___.', ['de-escalate', 'escalate', 'deactivate', 'decrease up'], 0, 'de-escalate.'),
        ('Asked a hard question suddenly in front of others = put ___ the spot.', ['on', 'in', 'at', 'to'], 0, 'put on the spot.'),
        ('Bị hỏi điều chưa biết, câu tốt nhất:', ['I have no idea.', "I don't know yet, but I'll find out and get back to you by 3 p.m.", 'Ask someone else.', 'Silence.'], 1, 'Thành thật + hẹn giờ.'),
        ('A web page showing live service status = a ___ page.', ['status', 'state', 'station', 'stats up'], 0, 'status page.'),
        ('Sorting bugs by urgency = ___.', ['triage', 'trial', 'tribute', 'trigger'], 0, 'triage.'),
        ('Cập nhật sự cố khi chưa có tin mới nên:', ['Im lặng', 'Vẫn gửi cập nhật ngắn kèm giờ cập nhật tiếp', 'Chờ đến khi sửa xong', 'Đổ lỗi'], 1, 'Ngắn, đều đặn.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 11',
    'title_en': 'Week 11 Review: Diplomatic Language',
    'goal': 'Ghi âm một tình huống khó 3 phút và so sánh với bản ghi tuần đầu; học ngôn ngữ ngoại giao để bất đồng mà vẫn giữ quan hệ tốt.',
    'tasks': [
        'Học 14 cụm từ ngoại giao.',
        'Ôn 5 kỹ năng xử lý tình huống của tuần.',
        'Nghe hai đồng nghiệp bất đồng một cách văn minh.',
        'Ghi âm một tình huống 3 phút (tự chọn) và so sánh với bản ghi Ngày 1.',
    ],
    'product': 'Bản ghi âm tình huống 3 phút',
    'rubric': True,
    'warmup': [
        ("I see where you're coming from.", 'Tôi hiểu quan điểm của bạn.'),
        ('I understand your concern, but…', 'Tôi hiểu mối lo của bạn, nhưng…'),
        ("With all due respect, I don't think that will work.", 'Với tất cả sự tôn trọng, tôi không nghĩ cách đó hiệu quả.'),
        ('Point taken. Let me think about it.', 'Tôi ghi nhận. Để tôi suy nghĩ.'),
        ("Let's agree to disagree on that one.", 'Chuyện đó hãy chấp nhận mỗi người một ý.'),
        ("I think we have more common ground than it seems.", 'Tôi nghĩ chúng ta có nhiều điểm chung hơn vẻ ngoài.'),
    ],
    'vocab': [
        ("I see where you're coming from", "/aɪ siː weə jʊə ˈkʌmɪŋ frɒm/", 'phrase', 'tôi hiểu quan điểm của bạn', "I see where you're coming from, but the data says otherwise.", 'Tôi hiểu quan điểm của bạn, nhưng dữ liệu nói khác.'),
        ('I understand your concern', '/aɪ ˌʌndəˈstænd jɔː kənˈsɜːn/', 'phrase', 'tôi hiểu mối lo của bạn', 'I understand your concern about security.', 'Tôi hiểu mối lo của bạn về bảo mật.'),
        ('with all due respect', '/wɪð ɔːl djuː rɪˈspekt/', 'phrase', 'với tất cả sự tôn trọng (trước khi phản đối)', "With all due respect, that deadline isn't realistic.", 'Với tất cả sự tôn trọng, hạn chót đó không thực tế.'),
        ('I hear you', '/aɪ hɪə juː/', 'phrase', 'tôi hiểu (ghi nhận cảm xúc)', 'I hear you. It has been a stressful week.', 'Tôi hiểu. Tuần này thật căng thẳng.'),
        ("that's understandable", '/ðæts ˌʌndəˈstændəbl/', 'phrase', 'điều đó dễ hiểu', "You're disappointed, and that's understandable.", 'Bạn thất vọng, và điều đó dễ hiểu.'),
        ('point taken', '/pɔɪnt ˈteɪkən/', 'phrase', 'tôi ghi nhận ý đó', 'Point taken. We will add more tests.', 'Ghi nhận. Chúng tôi sẽ thêm test.'),
        ('agree to disagree', '/əˈɡriː tə ˌdɪsəˈɡriː/', 'phrase', 'chấp nhận bất đồng', "On tabs versus spaces, let's agree to disagree.", 'Chuyện tab hay dấu cách, hãy chấp nhận bất đồng.'),
        ('common ground', '/ˈkɒmən ɡraʊnd/', 'n', 'điểm chung', "Let's start from our common ground: we both want a stable release.", 'Hãy bắt đầu từ điểm chung: cả hai ta đều muốn bản phát hành ổn định.'),
        ('tactful', '/ˈtæktfl/', 'adj', 'khéo léo', 'Be tactful when you give feedback to a senior colleague.', 'Hãy khéo léo khi góp ý cho đồng nghiệp cấp cao.'),
        ('diplomatic', '/ˌdɪpləˈmætɪk/', 'adj', 'ngoại giao, tế nhị', 'She gave a very diplomatic answer.', 'Cô ấy trả lời rất tế nhị.'),
        ('tone down', '/təʊn daʊn/', 'phrasal verb', 'làm dịu giọng, bớt gay gắt', 'You might want to tone down that email.', 'Có lẽ bạn nên làm dịu giọng email đó.'),
        ('sensitive topic', '/ˈsensətɪv ˈtɒpɪk/', 'n', 'chủ đề nhạy cảm', 'Salary is a sensitive topic in many teams.', 'Lương là chủ đề nhạy cảm ở nhiều team.'),
        ('frame', '/freɪm/', 'verb', 'diễn đạt, đặt vấn đề (theo cách nào đó)', 'Frame your feedback as a suggestion.', 'Hãy diễn đạt góp ý như một gợi ý.'),
        ('defuse', '/ˌdiːˈfjuːz/', 'verb', 'xoa dịu (căng thẳng)', 'A little humour can defuse a tense meeting.', 'Chút hài hước có thể xoa dịu cuộc họp căng thẳng.'),
    ],
    'lesson': """
<h3>1. Bất đồng văn minh: Ghi nhận → Nhưng → Lý do → Đề xuất</h3>
<div class="ex"><span class="en">I see where you're coming from — the old code is hard to work with. But a full rewrite would take at least three months. What if we refactor the worst module first and see how it goes?</span></div>

<h3>2. Bảng ngôn ngữ ngoại giao</h3>
<table class="table">
<tr><th>Thay vì</th><th>Nói</th></tr>
<tr><td>You're wrong.</td><td><span class="say">I see it a bit differently.</span></td></tr>
<tr><td>That's a bad idea.</td><td><span class="say">I'm not sure that would work, because…</span></td></tr>
<tr><td>You don't understand.</td><td><span class="say">Maybe I didn't explain it clearly.</span></td></tr>
<tr><td>No.</td><td><span class="say">I understand your concern, but I'd suggest…</span></td></tr>
<tr><td>Fine, whatever.</td><td><span class="say">Let's agree to disagree and move forward with option A.</span></td></tr>
</table>

<h3>3. Ôn tuần 11</h3>
<table class="table">
<tr><th>Tình huống</th><th>Công cụ</th></tr>
<tr><td>Không hiểu</td><td>Hỏi lại phần cụ thể · "So you're saying…, right?"</td></tr>
<tr><td>Yêu cầu mơ hồ</td><td>5W + Done · acceptance criteria · xác nhận bằng văn bản</td></tr>
<tr><td>Từ chối</td><td>Ghi nhận – lý do – không – phương án · "If you…, we can…"</td></tr>
<tr><td>Trễ hạn</td><td>Báo sớm · ngày mới cụ thể · giảm thiểu · cập nhật</td></tr>
<tr><td>Sự cố / khách giận</td><td>Acknowledge – Reassure – Act – Update</td></tr>
<tr><td>Bất đồng</td><td>Ghi nhận – nhưng – lý do – đề xuất</td></tr>
</table>
<div class="note"><b>Ghi âm hôm nay:</b> chọn 1 tình huống (khách giận, báo trễ, từ chối…) và nói liền 3 phút như đang trong cuộc gọi thật. Sau đó mở trang <a href="/ghi-am/">Ghi âm</a>, so sánh với bản Ngày 1 và tự chấm.</div>
""",
    'listening': {
        'title': 'A respectful disagreement',
        'intro': 'Hai kỹ sư bất đồng về việc viết lại hệ thống. Họ không đồng ý hoàn toàn nhưng vẫn tìm ra hướng đi.',
        'speakers': {'A': ('Raj', 'brian'), 'B': ('Lien', 'ava')},
        'lines': [
            ('A', "Honestly, Lien, I think we should rewrite the whole billing service. The code is a mess, and every change takes forever.", 'Thật lòng, Liên, mình nghĩ nên viết lại toàn bộ dịch vụ thanh toán. Code lộn xộn, sửa gì cũng mất cả đời.'),
            ('B', "I see where you're coming from. I've also spent days fighting that code. But I'm worried about the risk.", 'Mình hiểu quan điểm của cậu. Mình cũng từng mất nhiều ngày vật lộn với đống code đó. Nhưng mình lo về rủi ro.'),
            ('A', "What risk? We know the system better than anyone.", 'Rủi ro gì? Bọn mình hiểu hệ thống hơn ai hết.'),
            ('B', "With all due respect, nobody fully understands it. It has eight years of special cases for different clients. A rewrite could easily take six months and introduce new bugs in billing, which is very sensitive.", 'Với tất cả sự tôn trọng, chẳng ai hiểu hết nó. Nó có tám năm các trường hợp đặc biệt cho từng khách hàng. Viết lại có thể dễ dàng mất sáu tháng và sinh lỗi mới trong thanh toán, vốn rất nhạy cảm.'),
            ('A', "Point taken. But if we don't do something, we'll be slow forever.", 'Ghi nhận. Nhưng nếu không làm gì, bọn mình sẽ chậm mãi.'),
            ('B', "I agree with that completely. That's our common ground: we both want to move faster. What if we start by rewriting just the invoice module, the part that changes most often?", 'Mình hoàn toàn đồng ý điều đó. Đó là điểm chung: cả hai đều muốn nhanh hơn. Hay là bắt đầu bằng việc viết lại chỉ module hóa đơn, phần thay đổi thường xuyên nhất?'),
            ('A', "Hmm. I still think a full rewrite is better in the long run.", 'Hừm. Mình vẫn nghĩ viết lại toàn bộ tốt hơn về lâu dài.'),
            ('B', "That's fair. Let's agree to disagree on the long term. But can we agree to start with the invoice module and review after a month?", 'Hợp lý. Về lâu dài thì hãy chấp nhận mỗi người một ý. Nhưng có thể thống nhất bắt đầu với module hóa đơn và đánh giá lại sau một tháng không?'),
            ('A', "Yes, that I can agree to. If it goes well, it's also evidence for a bigger rewrite.", 'Được, cái đó mình đồng ý. Nếu thuận lợi, nó cũng là bằng chứng cho việc viết lại lớn hơn.'),
            ('B', "Exactly. Let's present it together to the team.", 'Chính xác. Cùng trình bày với team nhé.'),
        ],
        'questions': [
            ('What does Raj want to do?', ['Rewrite the whole billing service', 'Delete the billing service', 'Hire a new team', 'Do nothing'], 0, '"rewrite the whole billing service".'),
            ('Why is Lien worried?', ['She likes the old code.', 'A rewrite could take six months and introduce new bugs in billing.', 'She is busy.', 'Raj is junior.'], 1, 'Rủi ro thời gian và lỗi mới.'),
            ('What is their common ground?', ['They both want to move faster.', 'They both love the old code.', 'They both want a new job.', 'They both hate billing.'], 0, '"we both want to move faster".'),
            ('What do they finally agree on?', ['A full rewrite now', 'Start with the invoice module and review after a month', 'Do nothing', 'Ask the CEO'], 1, 'Bắt đầu với module hóa đơn.'),
            ('What do they "agree to disagree" on?', ['The long-term plan', 'The invoice module', 'The team meeting', 'The deadline'], 0, '"Let\'s agree to disagree on the long term."'),
        ],
    },
    'speaking': {
        'tips': ['Chọn một tình huống khó (khách giận, báo trễ, từ chối, bất đồng) và nói liền 3 phút như trong cuộc gọi thật.', 'Dùng ít nhất 4 cụm ngoại giao hôm nay.', 'Sau đó so sánh với bản ghi Ngày 1 ở trang Ghi âm và tự chấm.'],
        'prompts': [
            ('A senior colleague wants to skip testing to meet a deadline. Disagree diplomatically and propose an alternative. (3 minutes)', 'I see where you\'re coming from… With all due respect… What if…'),
            ('Or: Call a client to say the project will be one week late, then handle their frustration. (3 minutes)', 'A-R-A-U + báo trễ.'),
        ],
        'model': (
            "I see where you're coming from, and I know how important this deadline is for the client. Nobody wants to miss it. "
            "But with all due respect, I don't think skipping testing is a good idea for the payment module. If something goes wrong there, customers could be charged twice, and that would cost us much more than a two-day delay. "
            "That said, I think we have common ground: we both want to deliver on time. So here's what I'd suggest. We test the payment flow fully, because that's non-negotiable, but we skip the manual tests for the profile pages, which are low risk. "
            "And if we still need more time, we could release the payment update on Friday and the profile changes on Monday. "
            "What do you think? If you still disagree, let's bring both options to the team lead and let them decide.",
            'Tôi hiểu quan điểm của anh, và tôi biết hạn chót này quan trọng thế nào với khách hàng. Không ai muốn lỡ nó. '
            'Nhưng với tất cả sự tôn trọng, tôi không nghĩ bỏ kiểm thử là ý hay với module thanh toán. Nếu có gì sai ở đó, khách có thể bị trừ tiền hai lần, và điều đó tốn kém hơn nhiều so với trễ hai ngày. '
            'Dù vậy, tôi nghĩ chúng ta có điểm chung: cả hai đều muốn bàn giao đúng hạn. Nên tôi đề xuất thế này. Chúng ta kiểm thử đầy đủ luồng thanh toán, vì đó là điều không thể thương lượng, nhưng bỏ kiểm thử thủ công cho các trang hồ sơ, vốn ít rủi ro. '
            'Và nếu vẫn cần thêm thời gian, có thể phát hành bản cập nhật thanh toán vào thứ Sáu và thay đổi trang hồ sơ vào thứ Hai. '
            'Anh thấy sao? Nếu anh vẫn không đồng ý, hãy đưa cả hai phương án lên trưởng nhóm để họ quyết định.'
        ),
        'seconds': 180,
    },
    'reading': {
        'title': 'Disagree and commit',
        'text': [
            'Some technology companies use a principle called "disagree and commit". It means that during a discussion, everyone should share their honest opinion, even if they disagree with the manager. But once a decision is made, everyone commits to it fully, including the people who disagreed.',
            'This principle solves two common problems. In some teams, people never disagree openly, so bad ideas go ahead without challenge. In other teams, people keep arguing after a decision, and nothing moves forward.',
            'For people from cultures where open disagreement feels uncomfortable, the first part is the hardest. Diplomatic phrases make it easier: you can challenge an idea while showing respect for the person. And remember that a well-argued "I see it differently" is often exactly what a good manager wants to hear.',
        ],
        'vi': 'Một số công ty công nghệ áp dụng nguyên tắc "disagree and commit": khi thảo luận, mọi người nói thật quan điểm kể cả khi bất đồng với quản lý; nhưng khi đã ra quyết định thì ai cũng cam kết thực hiện hết mình, kể cả người từng phản đối. Nguyên tắc này giải quyết hai vấn đề: team không ai dám phản đối nên ý tưởng tồi vẫn được làm; và team cứ tranh cãi mãi sau khi đã quyết. Với người từ văn hóa ngại phản đối công khai, phần đầu khó nhất; ngôn ngữ ngoại giao giúp bạn phản biện ý tưởng mà vẫn tôn trọng người nói.',
        'questions': [
            ('What does "disagree and commit" mean?', ['Never disagree', 'Share honest opinions, then fully support the final decision', 'Keep arguing until you win', 'Leave if you disagree'], 1, 'Đoạn 1.'),
            ('Which problem does it solve?', ['Too many meetings', 'Bad ideas going ahead without challenge', 'Low salaries', 'Slow computers'], 1, 'Đoạn 2.'),
            ('What makes open disagreement easier, according to the text?', ['Shouting', 'Diplomatic phrases', 'Writing anonymously', 'Avoiding meetings'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết lại tình huống bạn vừa ghi âm thành đoạn hội thoại hoặc email ngắn (100–150 từ) dùng ít nhất 5 cụm ngoại giao. Thêm 2 câu so sánh bản ghi hôm nay với bản Ngày 1.',
        'tips': ['Ghi nhận – nhưng – lý do – đề xuất.'],
        'model': "Hi David,\n\nThanks for sharing your idea about skipping the regression tests this sprint. I see where you're coming from — the deadline is tight, and the tests take almost a day. However, with all due respect, I don't think it's worth the risk for the payment module, which is a sensitive area for our clients. That said, I think we have a lot of common ground: we both want to deliver on Friday. What if we run the full tests only for payments and a short smoke test for everything else? If you still see it differently, I'm happy to agree to disagree and let Sarah make the final call.\n\nBest,\nMinh\n\nCompared with Day 1: I spoke for three minutes with only a few short pauses, and my structure was much clearer. My pronunciation of final sounds is better, but I still say \"um\" too often.",
        'min_words': 110,
    },
    'quiz': [
        ('Thay cho "You\'re wrong.", nói:', ['I see it a bit differently.', 'You are stupid.', 'No way.', 'Wrong!'], 0, 'Ngoại giao.'),
        ('"I see where you\'re ___ from."', ['coming', 'going', 'looking', 'running'], 0, "I see where you're coming from."),
        ('"___ all due respect, I disagree."', ['With', 'For', 'By', 'In'], 0, 'With all due respect.'),
        ('When you accept someone\'s point: "Point ___."', ['taken', 'took', 'take', 'taking'], 0, 'Point taken.'),
        ('Accepting that you will not agree: let\'s agree to ___.', ['disagree', 'dislike', 'discuss', 'differ up'], 0, 'agree to disagree.'),
        ('Things both sides agree on = ___ ground.', ['common', 'middle up', 'shared up', 'same'], 0, 'common ground.'),
        ('To make an email less aggressive = to ___ it down.', ['tone', 'turn', 'calm', 'break'], 0, 'tone down.'),
        ('Careful and polite when saying difficult things = ___.', ['tactful', 'tactical', 'tasteful', 'tactile'], 0, 'tactful.'),
        ('Cấu trúc bất đồng văn minh:', ['Ghi nhận → Nhưng → Lý do → Đề xuất', 'Không → Không → Không', 'Im lặng', 'Đồng ý rồi làm khác'], 0, 'Ghi nhận – nhưng – lý do – đề xuất.'),
        ('"Disagree and commit" nghĩa là:', ['Không bao giờ phản đối', 'Nói thật quan điểm, rồi cam kết với quyết định cuối', 'Phản đối mãi', 'Nghỉ việc'], 1, 'Nguyên tắc disagree and commit.'),
    ],
}

WEEK = {
    'title': 'Xử lý tình huống khó',
    'title_en': 'Handling Difficult Situations',
    'goal': 'Làm rõ yêu cầu, từ chối lịch sự, báo trễ deadline và xử lý tình huống bất ngờ.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
