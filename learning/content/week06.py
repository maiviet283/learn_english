"""Tuần 6 — Nói trong công việc."""

DAY1 = {
    'title': 'Daily standup',
    'title_en': 'The Daily Stand-up',
    'goal': 'Báo cáo standup gọn trong 1 phút theo cấu trúc Yesterday – Today – Blockers với các mẫu câu chuẩn ("I\'m blocked by…", "I\'ll pick up…").',
    'tasks': [
        'Học 14 cụm từ dùng trong standup.',
        'Nghe một buổi standup của team 3 người.',
        'Viết kịch bản standup 1 phút cho công việc thật của bạn.',
        'Đọc to kịch bản 3 lần, ghi âm lần cuối.',
    ],
    'product': 'Kịch bản standup 1 phút',
    'warmup': [
        ('Yesterday, I wrapped up the login page.', 'Hôm qua tôi hoàn tất trang đăng nhập.'),
        ("Today, I'll pick up the password reset ticket.", 'Hôm nay tôi sẽ nhận ticket đặt lại mật khẩu.'),
        ("I'm blocked by the API changes.", 'Tôi đang bị chặn bởi thay đổi API.'),
        ("I'm still on track for Friday.", 'Tôi vẫn đúng tiến độ cho thứ Sáu.'),
        ('No blockers for me.', 'Tôi không có vướng mắc gì.'),
        ("Just a heads-up: I'm out of office on Thursday.", 'Báo trước: thứ Năm tôi nghỉ.'),
    ],
    'vocab': [
        ('wrap up', '/ræp ʌp/', 'phrasal verb', 'hoàn tất, kết thúc', 'I wrapped up the report yesterday afternoon.', 'Chiều qua tôi đã hoàn tất báo cáo.'),
        ('pick up', '/pɪk ʌp/', 'phrasal verb', 'nhận làm (một việc)', "I'll pick up the next ticket in the backlog.", 'Tôi sẽ nhận ticket tiếp theo trong backlog.'),
        ('be blocked by', '/biː blɒkt baɪ/', 'phrase', 'bị chặn/vướng bởi', "I'm blocked by a missing API key.", 'Tôi bị vướng vì thiếu API key.'),
        ('on track', '/ɒn træk/', 'phrase', 'đúng tiến độ', "We're on track to finish by Friday.", 'Chúng ta đúng tiến độ để xong trước thứ Sáu.'),
        ('in progress', '/ɪn ˈprəʊɡres/', 'phrase', 'đang làm dở', 'The migration is still in progress.', 'Migration vẫn đang thực hiện.'),
        ('pair with', '/peə wɪð/', 'verb', 'làm cặp với (lập trình đôi)', "I'll pair with Minh on the payment bug.", 'Tôi sẽ làm cặp với Minh xử lý lỗi thanh toán.'),
        ('ETA', '/ˌiː tiː ˈeɪ/', 'n', 'thời gian dự kiến xong', "What's the ETA for the fix?", 'Dự kiến khi nào sửa xong?'),
        ('heads-up', '/ˈhedz ʌp/', 'n', 'lời báo trước', "Just a heads-up: the staging server will be down tonight.", 'Báo trước: tối nay server staging sẽ tạm dừng.'),
        ('carry over', '/ˈkæri ˈəʊvə/', 'phrasal verb', 'chuyển sang (sprint/ngày sau)', 'Two tickets will carry over to the next sprint.', 'Hai ticket sẽ chuyển sang sprint sau.'),
        ('unblock', '/ʌnˈblɒk/', 'verb', 'gỡ vướng cho ai', 'Can someone unblock me? I need database access.', 'Ai có thể gỡ vướng cho tôi không? Tôi cần quyền vào cơ sở dữ liệu.'),
        ('out of office', '/aʊt əv ˈɒfɪs/', 'phrase', 'vắng mặt, nghỉ (OOO)', "I'll be out of office on Friday.", 'Thứ Sáu tôi sẽ nghỉ.'),
        ('almost done', '/ˈɔːlməʊst dʌn/', 'phrase', 'gần xong', 'The new design is almost done.', 'Thiết kế mới gần xong rồi.'),
        ('take a look', '/teɪk ə lʊk/', 'phrase', 'xem qua', "Could you take a look at my PR?", 'Bạn xem qua PR của tôi được không?'),
        ('nothing new', '/ˈnʌθɪŋ njuː/', 'phrase', 'không có gì mới', 'Nothing new from my side.', 'Phía tôi không có gì mới.'),
    ],
    'lesson': """
<h3>1. Cấu trúc 3 phần (≤ 1 phút)</h3>
<table class="table">
<tr><th>Phần</th><th>Thì</th><th>Mẫu câu</th></tr>
<tr><td><b>Yesterday</b></td><td>Quá khứ đơn</td><td><span class="say">Yesterday, I finished the login page and opened a PR.</span></td></tr>
<tr><td><b>Today</b></td><td>will / going to / hiện tại tiếp diễn</td><td><span class="say">Today, I'll pick up the password reset ticket.</span></td></tr>
<tr><td><b>Blockers</b></td><td>Hiện tại</td><td><span class="say">I'm blocked by the API changes.</span> / <span class="say">No blockers.</span></td></tr>
</table>

<h3>2. Mẫu câu theo tình huống</h3>
<table class="table">
<tr><th>Tình huống</th><th>Câu</th></tr>
<tr><td>Việc chưa xong</td><td><span class="say">I'm still working on the search page. It's taking longer than expected.</span></td></tr>
<tr><td>Cần người review</td><td><span class="say">My PR is ready for review. Could someone take a look today?</span></td></tr>
<tr><td>Bị vướng</td><td><span class="say">I'm waiting on the design team for the final mockups.</span></td></tr>
<tr><td>Cần giúp</td><td><span class="say">I might need to pair with someone on the deployment.</span></td></tr>
<tr><td>Báo trước</td><td><span class="say">Just a heads-up: I'm out of office tomorrow afternoon.</span></td></tr>
<tr><td>Bàn sau</td><td><span class="say">Let's take that offline.</span> (bàn riêng sau buổi họp)</td></tr>
</table>

<h3>3. Lỗi hay gặp ở standup</h3>
<ul>
<li><b>Quá chi tiết kỹ thuật</b> — standup không phải nơi giải quyết vấn đề. Nói <i>"Let's take that offline"</i> và bàn sau.</li>
<li><b>Chỉ nói "I worked on ticket 123"</b> — nói kết quả: <span class="say">I finished the export feature; it's on staging now.</span></li>
<li><b>Giấu vướng mắc</b> — nói sớm để được giúp sớm.</li>
</ul>
<div class="note"><b>Câu "đinh":</b> <span class="say">Yesterday I…, today I'm going to…, and I have no blockers.</span> — học thuộc như một câu thần chú, mỗi sáng chỉ cần thay nội dung.</div>
""",
    'phrases': [
        ("Let's take that offline.", 'Chúng ta bàn riêng sau nhé.'),
        ('My PR is ready for review.', 'PR của tôi sẵn sàng để review.'),
        ("It's taking longer than expected.", 'Nó tốn thời gian hơn dự kiến.'),
        ("That's it from me.", 'Phía tôi chỉ có vậy.'),
    ],
    'listening': {
        'title': 'Monday stand-up',
        'intro': 'Buổi standup sáng thứ Hai của một team 3 người. Mỗi người nói chưa đến 1 phút.',
        'speakers': {'A': ('Sarah (lead)', 'jenny'), 'B': ('Long', 'brian'), 'C': ('Ivy', 'emma')},
        'lines': [
            ('A', "Morning everyone. Let's keep it quick. Long, do you want to start?", 'Chào buổi sáng mọi người. Làm nhanh nhé. Long bắt đầu nhé?'),
            ('B', "Sure. On Friday, I wrapped up the order history page and opened a PR. It's ready for review, so if someone could take a look today, that would be great.", 'Vâng. Thứ Sáu em hoàn tất trang lịch sử đơn hàng và mở PR. Nó sẵn sàng để review, nếu hôm nay có ai xem giúp thì tuyệt quá.'),
            ('B', "Today, I'll pick up the CSV export ticket. No blockers.", 'Hôm nay em sẽ nhận ticket xuất CSV. Không có vướng mắc.'),
            ('A', "Thanks, Long. I'll review it after lunch. Ivy?", 'Cảm ơn Long. Chị sẽ review sau bữa trưa. Ivy?'),
            ('C', "On Friday, I kept working on the payment integration. It's still in progress, and honestly it's taking longer than expected.", 'Thứ Sáu em tiếp tục phần tích hợp thanh toán. Vẫn đang làm, và thật lòng thì nó lâu hơn dự kiến.'),
            ('C', "I'm blocked by the sandbox account. The payment provider hasn't sent us the test keys yet.", 'Em đang bị vướng tài khoản sandbox. Bên cung cấp thanh toán vẫn chưa gửi key test.'),
            ('A', "Okay, I'll email their support right after this and try to unblock you. What's your ETA if you get the keys today?", 'Được, chị sẽ email bộ phận hỗ trợ của họ ngay sau buổi này để gỡ vướng cho em. Nếu có key hôm nay thì dự kiến khi nào xong?'),
            ('C', "Probably Wednesday. Also, just a heads-up: I'm out of office on Thursday afternoon.", 'Chắc thứ Tư ạ. Ngoài ra, báo trước: chiều thứ Năm em nghỉ.'),
            ('A', "Noted. From my side, I'm finishing the sprint report and I'll be in client meetings most of the afternoon. That's it. Thanks everyone!", 'Đã ghi nhận. Về phía chị, chị đang hoàn thành báo cáo sprint và chiều nay phần lớn là họp khách hàng. Vậy thôi. Cảm ơn mọi người!'),
        ],
        'questions': [
            ('What did Long finish on Friday?', ['The CSV export', 'The order history page', 'The payment integration', 'The sprint report'], 1, '"I wrapped up the order history page".'),
            ('What is Ivy blocked by?', ['A code review', 'Missing test keys from the payment provider', 'A server crash', 'The design team'], 1, '"The payment provider hasn\'t sent us the test keys yet."'),
            ('What will Sarah do to unblock Ivy?', ['Pair with her', 'Email the provider\'s support', 'Give her new tasks', 'Cancel the integration'], 1, '"I\'ll email their support right after this".'),
            ('When will Ivy be out of office?', ['Wednesday', 'Thursday afternoon', 'Friday', 'All week'], 1, '"I\'m out of office on Thursday afternoon."'),
        ],
    },
    'speaking': {
        'tips': ['Viết kịch bản trước (phần Viết), đọc to 3 lần, rồi nói KHÔNG nhìn giấy.', 'Đúng 3 phần, dưới 1 phút.'],
        'prompts': [
            ('Give your stand-up update for today: yesterday, today, blockers.', 'Dùng công việc thật của bạn.'),
            ('Imagine you are blocked. Ask the team for help in one sentence.', 'I\'m blocked by… Could someone…?'),
            ('Give a heads-up about a day off next week.', 'Just a heads-up…'),
        ],
        'model': (
            "Yesterday, I finished the email notification feature and fixed two small bugs from QA. The PR is ready for review, so if someone could take a look today, that would be great. "
            "Today, I'm going to pick up the ticket for the new dashboard filters. "
            "I'm a bit blocked by the analytics API, because the endpoint I need isn't deployed on staging yet. I'll check with the backend team after this. "
            "Just a heads-up: I'll be out of office on Friday morning. That's it from me.",
            'Hôm qua tôi làm xong tính năng thông báo email và sửa hai lỗi nhỏ từ QA. PR đã sẵn sàng review, nếu hôm nay có ai xem giúp thì tuyệt. '
            'Hôm nay tôi sẽ nhận ticket bộ lọc mới cho dashboard. '
            'Tôi hơi bị vướng API analytics, vì endpoint tôi cần chưa được triển khai lên staging. Sau buổi này tôi sẽ hỏi team backend. '
            'Báo trước: sáng thứ Sáu tôi nghỉ. Phía tôi chỉ có vậy.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Async stand-ups',
        'text': [
            'Many remote teams have replaced the daily video stand-up with an "async stand-up": every morning, each person writes a short update in a chat channel. This saves time and works better across time zones.',
            'A good async update follows the same structure as a spoken one, but it can include links: the pull request that needs review, the ticket that is blocked, the document that needs feedback. It should take less than a minute to read.',
            'The risk is that people stop reading each other\'s updates, and blockers are ignored. Successful teams solve this with a simple rule: if someone mentions a blocker, the team lead must reply within two hours.',
        ],
        'vi': 'Nhiều team remote thay standup video bằng "standup không đồng bộ": mỗi sáng mỗi người viết cập nhật ngắn trong kênh chat — tiết kiệm thời gian và hợp với nhiều múi giờ. Cập nhật tốt có cùng cấu trúc với bản nói nhưng có thể kèm link (PR cần review, ticket bị chặn) và đọc dưới một phút. Rủi ro là mọi người ngừng đọc và vướng mắc bị bỏ qua; team thành công đặt quy tắc: ai nhắc đến vướng mắc thì trưởng nhóm phải trả lời trong hai giờ.',
        'questions': [
            ('What is an async stand-up?', ['A meeting at night', 'Written updates in a chat channel', 'A weekly video call', 'A meeting without a manager'], 1, 'Đoạn 1.'),
            ('What can a written update include that a spoken one can\'t easily?', ['Jokes', 'Links', 'Feelings', 'Questions'], 1, 'Đoạn 2.'),
            ('What rule helps successful teams?', ['Everyone must write 500 words.', 'The lead replies to blockers within two hours.', 'No updates on Fridays.', 'Only managers write updates.'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết kịch bản standup 1 phút cho công việc thật của bạn (Yesterday / Today / Blockers), sau đó viết lại thành bản cập nhật async ngắn trên Slack.',
        'tips': ['Nói kết quả, không chỉ nói "worked on".', 'Bản Slack: gạch đầu dòng, có thể thêm link.'],
        'model': "Spoken script:\nYesterday, I finished the search filters and opened a PR. Today, I'll fix the two bugs QA found on staging and then pick up the CSV export. I'm blocked by the analytics API — the endpoint isn't on staging yet. Just a heads-up: I'm out of office Friday morning.\n\nSlack update:\n✅ Yesterday: finished search filters — PR ready for review (link)\n🔨 Today: fix 2 QA bugs, then start CSV export\n🚧 Blocker: analytics endpoint not deployed on staging yet\n📅 Heads-up: OOO Friday morning",
        'min_words': 60,
    },
    'quiz': [
        ('Yesterday, I ___ the login page. (hoàn tất)', ['wrapped up', 'picked up', 'carried over', 'took offline'], 0, 'wrap up = hoàn tất.'),
        ("Today, I'll ___ the next ticket.", ['pick up', 'wrap up', 'pair up', 'look up'], 0, 'pick up = nhận làm.'),
        ("I'm ___ by the missing test keys.", ['blocked', 'blocking', 'block', 'blocker'], 0, 'be blocked by.'),
        ("What's the ___ for the fix?", ['ETA', 'API', 'PR', 'OOO'], 0, 'ETA = estimated time of arrival/thời gian dự kiến.'),
        ('"Just a ___: the server will be down tonight."', ['heads-up', 'head-on', 'headline', 'head start'], 0, 'heads-up = báo trước.'),
        ('A detailed technical discussion during stand-up? Say:', ["Let's take that offline.", "Let's talk now for 30 minutes.", 'Stop talking.', 'I don\'t care.'], 0, 'Bàn riêng sau buổi họp.'),
        ('Thì dùng cho phần "Yesterday":', ['Hiện tại đơn', 'Quá khứ đơn', 'Tương lai', 'Hiện tại hoàn thành tiếp diễn'], 1, 'Quá khứ đơn.'),
        ('Câu standup tốt hơn:', ['I worked on ticket 512.', 'I finished the export feature; it\'s on staging now.', 'I did things.', 'Same as yesterday.'], 1, 'Nói kết quả cụ thể.'),
        ("The migration is still ___.", ['in progress', 'on progress', 'at progress', 'progressing in'], 0, 'in progress.'),
        ("Two tickets will ___ to the next sprint.", ['carry over', 'carry on', 'carry out', 'carry up'], 0, 'carry over = chuyển sang.'),
    ],
}

DAY2 = {
    'title': 'Đóng vai standup',
    'title_en': 'Stand-up Role-play',
    'goal': 'Nói standup trôi chảy không nhìn giấy, kể cả khi bị hỏi thêm; báo cáo tiến độ chính xác (halfway through, behind schedule, waiting on…).',
    'tasks': [
        'Học 14 cụm từ báo cáo tiến độ.',
        'Nghe standup có câu hỏi bất ngờ từ quản lý.',
        'Đóng vai: chọn "Bạn là Phong" và trả lời quản lý.',
        'Đọc kịch bản hôm qua 1 lần, rồi nói lại không nhìn giấy. Ghi âm lần 2.',
        'Trả lời 4 câu hỏi follow-up của quản lý.',
    ],
    'product': 'Bản ghi âm standup không nhìn giấy',
    'warmup': [
        ("I'm about halfway through the migration.", 'Tôi làm được khoảng một nửa migration.'),
        ("We're slightly behind schedule.", 'Chúng ta hơi chậm tiến độ.'),
        ("I'm still waiting on feedback from design.", 'Tôi vẫn đang chờ phản hồi từ team thiết kế.'),
        ('The release might slip to next week.', 'Bản phát hành có thể lùi sang tuần sau.'),
        ("It's ready for review, pending QA sign-off.", 'Nó sẵn sàng để review, chờ QA duyệt.'),
        ("I'll tackle the hardest part first.", 'Tôi sẽ xử lý phần khó nhất trước.'),
    ],
    'vocab': [
        ('halfway through', '/ˌhɑːfweɪ ˈθruː/', 'phrase', 'được một nửa', "I'm halfway through the code review.", 'Tôi review code được một nửa.'),
        ('ahead of schedule', '/əˈhed əv ˈʃedjuːl/', 'phrase', 'vượt tiến độ', "We're two days ahead of schedule.", 'Chúng ta vượt tiến độ hai ngày.'),
        ('behind schedule', '/bɪˈhaɪnd ˈʃedjuːl/', 'phrase', 'chậm tiến độ', 'The project is a week behind schedule.', 'Dự án chậm một tuần.'),
        ('slip', '/slɪp/', 'verb', '(thời hạn) bị lùi', 'The launch date slipped by two weeks.', 'Ngày ra mắt bị lùi hai tuần.'),
        ('pending', '/ˈpendɪŋ/', 'adj / prep', 'đang chờ; chờ đến khi', 'The release is pending approval from the client.', 'Bản phát hành đang chờ khách hàng duyệt.'),
        ('waiting on', '/ˈweɪtɪŋ ɒn/', 'phrase', 'đang chờ (ai/cái gì)', "I'm waiting on the final copy from marketing.", 'Tôi đang chờ nội dung cuối từ marketing.'),
        ('finalize', '/ˈfaɪnəlaɪz/', 'verb', 'hoàn thiện, chốt', "We'll finalize the design on Tuesday.", 'Thứ Ba chúng ta sẽ chốt thiết kế.'),
        ('sign-off', '/ˈsaɪn ɒf/', 'n', 'sự phê duyệt cuối', 'We need sign-off from the client before we launch.', 'Chúng ta cần khách hàng duyệt trước khi ra mắt.'),
        ('ready for review', '/ˈredi fə rɪˈvjuː/', 'phrase', 'sẵn sàng để review', 'The PR is ready for review.', 'PR đã sẵn sàng để review.'),
        ('get through', '/ɡet θruː/', 'phrasal verb', 'xử lý xong (nhiều việc)', "I got through most of my emails this morning.", 'Sáng nay tôi xử lý xong phần lớn email.'),
        ('on hold', '/ɒn həʊld/', 'phrase', 'tạm dừng', 'The mobile project is on hold until January.', 'Dự án mobile tạm dừng đến tháng Giêng.'),
        ('tackle', '/ˈtækl/', 'verb', 'xử lý, giải quyết (việc khó)', "Let's tackle the performance issues first.", 'Hãy xử lý các vấn đề hiệu năng trước.'),
        ('knock out', '/nɒk aʊt/', 'phrasal verb', 'làm xong nhanh (thân mật)', 'I knocked out three small tickets before lunch.', 'Tôi làm xong nhanh ba ticket nhỏ trước bữa trưa.'),
        ('reprioritize', '/ˌriːpraɪˈɒrətaɪz/', 'verb', 'sắp xếp lại ưu tiên', 'We had to reprioritize after the outage.', 'Chúng tôi phải sắp xếp lại ưu tiên sau sự cố.'),
    ],
    'lesson': """
<h3>1. Báo cáo tiến độ chính xác</h3>
<table class="table">
<tr><th>Mức tiến độ</th><th>Câu</th></tr>
<tr><td>Mới bắt đầu</td><td><span class="say">I've just started on the export feature.</span></td></tr>
<tr><td>Một nửa</td><td><span class="say">I'm about halfway through.</span></td></tr>
<tr><td>Gần xong</td><td><span class="say">It's almost done. I just need to add tests.</span></td></tr>
<tr><td>Xong, chờ duyệt</td><td><span class="say">It's ready for review, pending QA sign-off.</span></td></tr>
<tr><td>Nhanh hơn kế hoạch</td><td><span class="say">We're a day ahead of schedule.</span></td></tr>
<tr><td>Chậm</td><td><span class="say">I'm a bit behind schedule because of the API changes.</span></td></tr>
<tr><td>Bị lùi</td><td><span class="say">The release might slip to Monday.</span></td></tr>
</table>

<h3>2. Trả lời câu hỏi follow-up của quản lý</h3>
<table class="table">
<tr><th>Câu hỏi</th><th>Trả lời mẫu</th></tr>
<tr><td><span class="say">When do you think it'll be done?</span></td><td><span class="say">If everything goes well, by Thursday. Worst case, Friday morning.</span></td></tr>
<tr><td><span class="say">What's slowing you down?</span></td><td><span class="say">Mainly the test data. Setting it up takes a while.</span></td></tr>
<tr><td><span class="say">Do you need any help?</span></td><td><span class="say">Actually, yes. It would help to pair with someone for an hour.</span></td></tr>
<tr><td><span class="say">Is it still on track for the release?</span></td><td><span class="say">Yes, as long as the design is finalized by Tuesday.</span></td></tr>
</table>

<h3>3. Từ kịch bản đến nói tự nhiên</h3>
<ol>
<li>Đọc kịch bản to 1 lần.</li>
<li>Gạch hết, chỉ giữ <b>từ khóa</b>: <i>export – halfway – waiting on design – Thursday</i>.</li>
<li>Nói lại chỉ nhìn từ khóa.</li>
<li>Nói lại không nhìn gì. Câu có thể khác kịch bản — <b>đó là điều tốt</b>.</li>
</ol>
""",
    'phrases': [
        ('Worst case, Friday morning.', 'Trường hợp xấu nhất là sáng thứ Sáu.'),
        ('If everything goes well, by Thursday.', 'Nếu suôn sẻ thì trước thứ Năm.'),
        ("It would help to pair with someone.", 'Sẽ có ích nếu được làm cặp với ai đó.'),
        ("I'll keep you posted.", 'Tôi sẽ cập nhật cho bạn.'),
    ],
    'listening': {
        'title': 'Stand-up with follow-up questions',
        'intro': 'Quản lý hỏi thêm sau phần báo cáo của Phong. Sau khi nghe, chọn "Bạn là Phong" để đóng vai.',
        'speakers': {'A': ('Daniel (manager)', 'guy'), 'B': ('Phong', 'andrew')},
        'lines': [
            ('A', "Phong, how's the reporting module going?", 'Phong, module báo cáo thế nào rồi?'),
            ('B', "I'm about halfway through. The charts are done, but the PDF export is taking longer than expected.", 'Em làm được khoảng một nửa. Biểu đồ xong rồi, nhưng phần xuất PDF tốn thời gian hơn dự kiến.'),
            ('A', "What's slowing you down?", 'Điều gì làm em chậm lại?'),
            ('B', "Mainly the fonts. Vietnamese characters don't display correctly in the PDF library we're using.", 'Chủ yếu là font chữ. Ký tự tiếng Việt không hiển thị đúng trong thư viện PDF mình đang dùng.'),
            ('A', "I see. When do you think it'll be done?", 'Anh hiểu. Em nghĩ khi nào xong?'),
            ('B', "If I can fix the fonts today, by Thursday. Worst case, Friday morning.", 'Nếu hôm nay sửa được font thì trước thứ Năm. Trường hợp xấu nhất là sáng thứ Sáu.'),
            ('A', "Is it still on track for the release next week?", 'Vẫn kịp cho bản phát hành tuần sau chứ?'),
            ('B', "Yes, as long as the client signs off on the design by Wednesday. I'm still waiting on their feedback.", 'Vâng, miễn là khách hàng duyệt thiết kế trước thứ Tư. Em vẫn đang chờ phản hồi của họ.'),
            ('A', "Okay. Do you need any help?", 'Được. Em có cần giúp gì không?'),
            ('B', "Actually, yes. Mai solved a similar font problem last year. It would help to pair with her for an hour.", 'Thực ra có ạ. Năm ngoái chị Mai đã giải quyết một vấn đề font tương tự. Sẽ có ích nếu được làm cặp với chị ấy một tiếng.'),
            ('A', "Good idea. I'll ask her after the stand-up. Keep me posted.", 'Ý hay. Anh sẽ hỏi chị ấy sau standup. Nhớ cập nhật cho anh.'),
        ],
        'questions': [
            ('How far is Phong with the reporting module?', ['Just started', 'About halfway', 'Almost done', 'Finished'], 1, '"I\'m about halfway through."'),
            ('What is the problem with the PDF export?', ['It is too slow.', 'Vietnamese characters don\'t display correctly.', 'The charts are wrong.', 'The client doesn\'t want it.'], 1, '"Vietnamese characters don\'t display correctly".'),
            ('What is the worst-case finish time?', ['Wednesday', 'Thursday', 'Friday morning', 'Next week'], 2, '"Worst case, Friday morning."'),
            ('What is the release on track for, as long as…?', ['Mai helps', 'The client signs off on the design by Wednesday', 'The fonts are fixed', 'Daniel agrees'], 1, '"as long as the client signs off on the design by Wednesday".'),
            ('What help does Phong ask for?', ['More time', 'To pair with Mai', 'A new library', 'A day off'], 1, '"It would help to pair with her for an hour."'),
        ],
    },
    'speaking': {
        'tips': ['Đóng vai Phong ở phần Nghe 2 lần.', 'Sau đó nói standup của bạn không nhìn giấy, rồi trả lời 4 câu hỏi follow-up bên dưới (bấm nghe từng câu).'],
        'prompts': [
            ("How's your main task going?", 'halfway through / almost done / behind schedule'),
            ("What's slowing you down?", 'Nêu nguyên nhân cụ thể.'),
            ('When do you think it\'ll be done?', 'If…, by…. Worst case, …'),
            ('Do you need any help?', 'It would help to… / No, I\'m fine, thanks.'),
        ],
        'model': (
            "It's going okay, but I'm a bit behind schedule. I'm about halfway through the new dashboard. "
            "What's slowing me down is the data. The numbers from the analytics service don't match the old reports, so I'm checking them one by one. "
            "If I can find the difference today, I should be done by Thursday. Worst case, Friday afternoon. "
            "Actually, it would help to have thirty minutes with someone from the data team. Could you introduce me to the right person? I'll keep you posted.",
            'Mọi thứ ổn nhưng tôi hơi chậm tiến độ. Tôi làm được khoảng một nửa dashboard mới. '
            'Điều làm tôi chậm là dữ liệu. Số liệu từ dịch vụ analytics không khớp với báo cáo cũ nên tôi đang kiểm tra từng cái. '
            'Nếu hôm nay tìm ra chỗ khác biệt, tôi sẽ xong trước thứ Năm. Trường hợp xấu nhất là chiều thứ Sáu. '
            'Thực ra sẽ có ích nếu được gặp ai đó trong team dữ liệu ba mươi phút. Bạn giới thiệu giúp tôi đúng người được không? Tôi sẽ cập nhật cho bạn.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'How to give bad news in a stand-up',
        'text': [
            'Nobody likes saying "I\'m behind schedule" in front of the team. Many developers wait, hoping they can catch up. Usually they cannot, and the bad news arrives at the worst possible moment.',
            'Experienced engineers share bad news early and with a plan. Instead of "the export is late", they say: "The export is two days behind because of a font issue. I\'m pairing with Mai today, and I expect to finish on Friday. If that changes, I\'ll let you know tomorrow."',
            'This version contains four things: the facts, the reason, the plan and the next update. Managers can work with that. What they cannot work with is surprise.',
        ],
        'vi': 'Không ai thích nói "tôi bị chậm" trước cả team, nên nhiều dev chờ đợi mong bắt kịp — thường là không kịp và tin xấu đến vào lúc tệ nhất. Kỹ sư giàu kinh nghiệm báo tin xấu sớm kèm kế hoạch: sự thật, lý do, kế hoạch và lần cập nhật tiếp theo. Quản lý làm việc được với điều đó; thứ họ không xử lý được là sự bất ngờ.',
        'questions': [
            ('Why do many developers wait before sharing bad news?', ['They forget.', 'They hope to catch up.', 'Managers don\'t listen.', 'They are not sure.'], 1, 'Đoạn 1.'),
            ('Which is NOT one of the four things in a good update?', ['The facts', 'The reason', 'Who to blame', 'The next update'], 2, 'Đoạn 3.'),
            ('What can managers not work with?', ['Bad news', 'Surprise', 'Delays', 'Plans'], 1, 'Câu cuối.'),
        ],
    },
    'writing': {
        'task': 'Viết bản cập nhật cho một tình huống chậm tiến độ (thật hoặc giả định) gồm đủ 4 phần: sự thật, lý do, kế hoạch, lần cập nhật tiếp theo.',
        'tips': ['Dùng: behind schedule, because of, I\'m going to, I expect to, I\'ll let you know.'],
        'model': "Quick update on the search feature: I'm about two days behind schedule. The main reason is that the new search API returns results in a different format, so I had to rewrite the filters. I've already finished the basic search, and today I'm going to pair with Quang on the filters. I expect to have everything ready for review on Friday morning. If anything changes, I'll let you know at tomorrow's stand-up.",
        'min_words': 60,
    },
    'quiz': [
        ("I'm ___ through the migration. (một nửa)", ['halfway', 'half', 'middle', 'mid'], 0, 'halfway through.'),
        ("We're two days ___ schedule. (vượt)", ['ahead of', 'behind', 'before of', 'in front'], 0, 'ahead of schedule.'),
        ('The launch date ___ by a week.', ['slipped', 'slept', 'slapped', 'skipped'], 0, 'slip = (thời hạn) bị lùi.'),
        ("I'm still ___ feedback from the client.", ['waiting on', 'waiting at', 'waiting with', 'waiting'], 0, 'waiting on/for.'),
        ('The project is ___ until next year.', ['on hold', 'in hold', 'at hold', 'holding'], 0, 'on hold.'),
        ('We need the client\'s ___ before launch.', ['sign-off', 'sign-up', 'sign-in', 'signal'], 0, 'sign-off = phê duyệt cuối.'),
        ("When do you think it'll be done? — If all goes well, Thursday. ___, Friday.", ['Worst case', 'Bad case', 'Worse case', 'Worst time'], 0, 'Worst case.'),
        ("Let's ___ the hardest problem first.", ['tackle', 'tickle', 'tackled', 'tack'], 0, 'tackle.'),
        ('Báo tin chậm tiến độ tốt nhất là:', ['Đợi đến hạn chót', 'Báo sớm, kèm lý do và kế hoạch', 'Không nói gì', 'Đổ lỗi cho người khác'], 1, 'Sớm + lý do + kế hoạch.'),
        ("I'll keep you ___.", ['posted', 'post', 'posting', 'to post'], 0, 'keep somebody posted = cập nhật cho ai.'),
    ],
}

DAY3 = {
    'title': 'Code review bằng tiếng Anh',
    'title_en': 'Code Review in English',
    'goal': 'Viết và nói nhận xét code review lịch sự, rõ ràng: đặt câu hỏi thay vì ra lệnh, phân biệt nit với vấn đề quan trọng, biết LGTM, request changes, follow-up PR.',
    'tasks': [
        'Học 14 thuật ngữ code review.',
        'Học công thức nhận xét lịch sự.',
        'Nghe hai dev trao đổi về một PR.',
        'Viết 10 câu nhận xét review mẫu.',
    ],
    'product': '10 câu nhận xét code review mẫu',
    'warmup': [
        ('Could you clarify why we need this check?', 'Bạn giải thích giúp vì sao cần kiểm tra này?'),
        ("I'd suggest extracting this into a separate function.", 'Tôi đề xuất tách cái này thành một hàm riêng.'),
        ('Nit: there is a typo in the variable name.', 'Chi tiết nhỏ: có lỗi chính tả ở tên biến.'),
        ('What happens if the list is empty?', 'Chuyện gì xảy ra nếu danh sách rỗng?'),
        ('LGTM with minor comments.', 'Ổn rồi, chỉ vài góp ý nhỏ.'),
        ("Let's handle that in a follow-up PR.", 'Hãy xử lý việc đó trong một PR tiếp theo.'),
    ],
    'vocab': [
        ('readability', '/ˌriːdəˈbɪləti/', 'n', 'tính dễ đọc', 'This change improves readability a lot.', 'Thay đổi này giúp code dễ đọc hơn nhiều.'),
        ('edge case', '/ˈedʒ keɪs/', 'n', 'trường hợp biên', "Don't forget the edge case where the user has no orders.", 'Đừng quên trường hợp biên khi người dùng không có đơn nào.'),
        ('naming', '/ˈneɪmɪŋ/', 'n', 'cách đặt tên', 'Naming is one of the hardest things in programming.', 'Đặt tên là một trong những việc khó nhất khi lập trình.'),
        ('nit', '/nɪt/', 'n', 'góp ý nhỏ, không quan trọng', 'Nit: missing space after the comma.', 'Góp ý nhỏ: thiếu dấu cách sau dấu phẩy.'),
        ('duplication', '/ˌdjuːplɪˈkeɪʃn/', 'n', 'sự trùng lặp (code)', "There's some duplication between these two functions.", 'Có chút trùng lặp giữa hai hàm này.'),
        ('LGTM', '/ˌel dʒiː tiː ˈem/', 'abbr', 'Looks good to me — ổn rồi', 'LGTM, ship it!', 'Ổn rồi, phát hành thôi!'),
        ('request changes', '/rɪˈkwest ˈtʃeɪndʒɪz/', 'phrase', 'yêu cầu sửa (trước khi duyệt)', 'I requested changes because the tests are missing.', 'Tôi yêu cầu sửa vì thiếu test.'),
        ('suggestion', '/səˈdʒestʃən/', 'n', 'gợi ý', 'This is just a suggestion, feel free to ignore it.', 'Đây chỉ là gợi ý, bạn cứ bỏ qua nếu muốn.'),
        ('follow-up PR', '/ˈfɒləʊ ʌp ˌpiː ˈɑː/', 'n', 'PR tiếp theo (làm sau)', "Let's fix the naming in a follow-up PR.", 'Hãy sửa cách đặt tên trong một PR sau.'),
        ('maintainable', '/meɪnˈteɪnəbl/', 'adj', 'dễ bảo trì', 'Smaller functions are more maintainable.', 'Hàm nhỏ dễ bảo trì hơn.'),
        ('test coverage', '/test ˈkʌvərɪdʒ/', 'n', 'độ bao phủ test', 'Our test coverage is around eighty percent.', 'Độ bao phủ test của chúng tôi khoảng tám mươi phần trăm.'),
        ('hard-coded', '/ˌhɑːd ˈkəʊdɪd/', 'adj', 'viết cứng trong code', 'The API URL is hard-coded; move it to the config.', 'URL API bị viết cứng; hãy chuyển vào file cấu hình.'),
        ('magic number', '/ˈmædʒɪk ˈnʌmbə/', 'n', 'số "ma thuật" (không rõ ý nghĩa)', 'What does 86400 mean? Avoid magic numbers.', '86400 nghĩa là gì? Tránh số không rõ ý nghĩa.'),
        ('clarify', '/ˈklærəfaɪ/', 'verb', 'làm rõ', 'Could you clarify what this function returns?', 'Bạn làm rõ giúp hàm này trả về gì?'),
    ],
    'lesson': """
<h3>1. Nguyên tắc vàng: nhận xét code, không nhận xét người</h3>
<table class="table">
<tr><th>Tránh</th><th>Nên viết</th></tr>
<tr><td>You forgot to handle errors.</td><td><span class="say">What happens if the request fails here?</span></td></tr>
<tr><td>This is wrong.</td><td><span class="say">I think this might cause a problem when the list is empty.</span></td></tr>
<tr><td>Rename this.</td><td><span class="say">What do you think about renaming this to user_count?</span></td></tr>
<tr><td>Why did you do this?</td><td><span class="say">Could you clarify why we need this extra check?</span></td></tr>
</table>

<h3>2. Bộ mẫu câu code review</h3>
<table class="table">
<tr><th>Mục đích</th><th>Mẫu câu</th></tr>
<tr><td>Hỏi để hiểu</td><td><span class="say">Could you clarify why…?</span> · <span class="say">Is there a reason we…?</span></td></tr>
<tr><td>Đề xuất</td><td><span class="say">I'd suggest…</span> · <span class="say">What about…?</span> · <span class="say">Have you considered…?</span></td></tr>
<tr><td>Góp ý nhỏ</td><td><span class="say">Nit: …</span> · <span class="say">Minor: …</span> · <span class="say">Optional: …</span></td></tr>
<tr><td>Vấn đề quan trọng</td><td><span class="say">This might break when…</span> · <span class="say">I think we need a test for this.</span></td></tr>
<tr><td>Để sau</td><td><span class="say">Not blocking, but…</span> · <span class="say">Could we do this in a follow-up PR?</span></td></tr>
<tr><td>Khen</td><td><span class="say">Nice, this is much cleaner.</span> · <span class="say">Great catch!</span></td></tr>
<tr><td>Duyệt</td><td><span class="say">LGTM.</span> · <span class="say">LGTM with minor comments.</span> · <span class="say">Approved, ship it!</span></td></tr>
</table>

<h3>3. Trả lời review của người khác</h3>
<div class="ex"><span class="en">Good catch, thanks! Fixed in the latest commit.</span></div>
<div class="ex"><span class="en">I did it this way because the API sometimes returns null. Happy to change it if you have a better idea.</span></div>
<div class="ex"><span class="en">Agreed, but I'd prefer to do it in a follow-up PR to keep this one small.</span></div>
<div class="note"><b>Nit</b> (từ "nitpick" — bắt bẻ chi tiết) báo cho tác giả biết đây là góp ý nhỏ, không bắt buộc sửa. Dùng nó giúp review của bạn nghe nhẹ nhàng hơn rất nhiều.</div>
""",
    'phrases': [
        ('Good catch, thanks!', 'Phát hiện hay, cảm ơn!'),
        ('Fixed in the latest commit.', 'Đã sửa trong commit mới nhất.'),
        ('Not blocking, but…', 'Không bắt buộc, nhưng…'),
        ('Have you considered…?', 'Bạn đã cân nhắc… chưa?'),
        ('Happy to change it if you prefer.', 'Tôi sẵn sàng đổi nếu bạn muốn.'),
    ],
    'listening': {
        'title': 'Talking through a pull request',
        'intro': 'Hai lập trình viên gọi nhanh để bàn về các nhận xét trên một pull request.',
        'speakers': {'A': ('Marco', 'ryan'), 'B': ('Thuy', 'ava')},
        'lines': [
            ('A', "Hi Thuy, thanks for reviewing my PR. I saw your comments. Do you have a few minutes to go through them?", 'Chào Thủy, cảm ơn đã review PR của mình. Mình thấy nhận xét rồi. Bạn có vài phút để cùng xem không?'),
            ('B', "Sure. Overall, it looks really good. The new structure is much cleaner. I just had a few questions.", 'Chắc chắn. Nhìn chung rất tốt. Cấu trúc mới gọn hơn nhiều. Mình chỉ có vài câu hỏi.'),
            ('A', "Great. The first one was about the discount function?", 'Tuyệt. Câu đầu về hàm giảm giá phải không?'),
            ('B', "Yes. Could you clarify what happens if the cart is empty? I think the function might divide by zero.", 'Đúng. Bạn làm rõ giúp chuyện gì xảy ra nếu giỏ hàng trống? Mình nghĩ hàm có thể chia cho không.'),
            ('A', "Oh, good catch. I didn't think about that edge case. I'll add a check and a test for it.", 'Ồ, phát hiện hay. Mình không nghĩ đến trường hợp biên đó. Mình sẽ thêm kiểm tra và một test cho nó.'),
            ('B', "Thanks. The second comment is about the number 0.15. It's a bit of a magic number. I'd suggest moving it to a constant with a clear name.", 'Cảm ơn. Nhận xét thứ hai về con số 0.15. Hơi giống số ma thuật. Mình đề xuất chuyển nó thành hằng số có tên rõ ràng.'),
            ('A', "Makes sense. Something like MEMBER DISCOUNT RATE?", 'Hợp lý. Kiểu như MEMBER DISCOUNT RATE?'),
            ('B', "Perfect. The rest are just nits, like a few long lines. Not blocking.", 'Hoàn hảo. Còn lại chỉ là góp ý nhỏ, như vài dòng quá dài. Không bắt buộc.'),
            ('A', "What about the duplication with the old checkout code? Should I clean that up too?", 'Còn phần trùng lặp với code thanh toán cũ? Mình có nên dọn luôn không?'),
            ('B', "I'd prefer to do that in a follow-up PR. This one is already big, and it's easier to review small changes.", 'Mình muốn làm việc đó trong một PR sau. PR này đã lớn rồi, và thay đổi nhỏ thì dễ review hơn.'),
            ('A', "Agreed. I'll push the fixes in an hour.", 'Đồng ý. Một tiếng nữa mình đẩy bản sửa.'),
            ('B', "Sounds good. Once the empty cart test is in, it's LGTM from me.", 'Ổn. Khi có test giỏ hàng trống thì mình duyệt.'),
        ],
        'questions': [
            ('What is Thuy\'s overall opinion of the PR?', ['It needs a full rewrite.', 'It looks really good.', 'It is too small.', 'She hasn\'t read it.'], 1, '"Overall, it looks really good."'),
            ('What edge case did Thuy find?', ['A very large cart', 'An empty cart', 'A negative price', 'A missing user'], 1, '"what happens if the cart is empty?"'),
            ('What does Thuy suggest for 0.15?', ['Delete it', 'Move it to a named constant', 'Change it to 0.2', 'Add a comment'], 1, '"moving it to a constant with a clear name".'),
            ('What will happen to the code duplication?', ['It will be fixed now.', 'It will be fixed in a follow-up PR.', 'It will be ignored forever.', 'Thuy will fix it.'], 1, '"I\'d prefer to do that in a follow-up PR."'),
            ('When will Thuy approve the PR?', ['Now', 'Once the empty cart test is added', 'Next week', 'Never'], 1, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to các mẫu câu, nhấn nhẹ nhàng (không ra lệnh).', 'Đóng vai Thủy: đưa nhận xét lịch sự cho đồng đội.'],
        'prompts': [
            ('Give spoken feedback on a PR: one question, one suggestion, one nit, and approval with conditions.', 'Could you clarify… / I\'d suggest… / Nit: … / LGTM once…'),
            ('Respond to a reviewer who asked why you used a global variable.', 'I did it this way because… Happy to change it…'),
        ],
        'model': (
            "Thanks for the PR, it's a really nice improvement. I have a few comments. "
            "First, could you clarify why we call the API twice in the save function? I might be missing something. "
            "Second, I'd suggest moving the timeout value to the config file, because it's hard-coded at the moment. "
            "There's also a small nit: the variable name data is a bit vague. Maybe something like order items? "
            "None of this is blocking, except the API call. Once that's clarified, it's LGTM from me.",
            'Cảm ơn PR nhé, cải thiện rất tốt. Mình có vài nhận xét. '
            'Thứ nhất, bạn làm rõ giúp vì sao mình gọi API hai lần trong hàm save? Có thể mình bỏ sót gì đó. '
            'Thứ hai, mình đề xuất chuyển giá trị timeout vào file cấu hình, vì hiện nó bị viết cứng. '
            'Còn một góp ý nhỏ: tên biến data hơi mơ hồ. Có lẽ kiểu như order items? '
            'Không có gì bắt buộc, trừ chỗ gọi API. Khi chỗ đó được làm rõ thì mình duyệt.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'A code review checklist',
        'text': [
            'Good reviewers do not only look for typos. They read the code in order of importance. First: does it do what the ticket asks? Second: is it correct, including edge cases and error handling? Third: is it tested? Only after that do they look at naming, style and small improvements.',
            'They also keep their comments kind and specific. "This is confusing" is not helpful. "I found this loop hard to follow. Could we split it into two functions?" tells the author exactly what the problem is and suggests a solution.',
            'Finally, they respond quickly. A pull request that waits three days for review slows down the whole team. Many teams agree that every review should start within one working day.',
        ],
        'vi': 'Người review giỏi đọc code theo thứ tự ưu tiên: (1) có làm đúng yêu cầu ticket không, (2) có đúng không — kể cả trường hợp biên và xử lý lỗi, (3) có test không; sau đó mới đến tên biến, style. Nhận xét phải tử tế và cụ thể: thay vì "khó hiểu", hãy nói rõ vấn đề và gợi ý cách sửa. Cuối cùng, phản hồi nhanh: PR chờ ba ngày làm chậm cả team; nhiều team thống nhất mọi review bắt đầu trong vòng một ngày làm việc.',
        'questions': [
            ('What do good reviewers check FIRST?', ['Naming', 'Whether it does what the ticket asks', 'Typos', 'Style'], 1, 'Đoạn 1.'),
            ('Why is "This is confusing" not a helpful comment?', ['It is rude.', 'It does not explain the problem or suggest a solution.', 'It is too long.', 'It uses slang.'], 1, 'Đoạn 2.'),
            ('Many teams agree that reviews should start within…', ['one hour', 'one working day', 'three days', 'one week'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 10 câu nhận xét code review mẫu cho các tình huống: thiếu xử lý lỗi, tên biến mơ hồ, số ma thuật, trùng lặp code, thiếu test, URL viết cứng, khen một thay đổi tốt, góp ý nhỏ về format, đề nghị PR sau, và duyệt có điều kiện.',
        'tips': ['Dùng câu hỏi và "I\'d suggest" thay vì câu mệnh lệnh.', 'Đánh dấu "Nit:" cho góp ý nhỏ.'],
        'model': "1. What happens if the payment API times out here?\n2. Could we rename 'tmp' to something more descriptive, like 'pending_orders'?\n3. What does 3600 represent? I'd suggest a named constant like ONE_HOUR_IN_SECONDS.\n4. This block looks very similar to the one in invoice.py. Have you considered extracting a helper?\n5. I think we need a test for the case where the user has no address.\n6. The base URL is hard-coded. Could we move it to the settings file?\n7. Nice refactor! This is much easier to read now.\n8. Nit: extra blank line at the end of the file.\n9. Not blocking, but we could clean up the old export code in a follow-up PR.\n10. LGTM once the timeout case is handled.",
        'min_words': 90,
    },
    'quiz': [
        ('Câu review lịch sự nhất:', ['You forgot error handling.', 'What happens if the request fails here?', 'Wrong.', 'Fix this now.'], 1, 'Đặt câu hỏi thay vì chỉ trích.'),
        ('"LGTM" nghĩa là:', ['Let\'s go to meeting', 'Looks good to me', 'Light green test mode', 'Long gap time missing'], 1, 'Looks good to me.'),
        ('A small, non-important comment usually starts with:', ['Nit:', 'Bug:', 'Urgent:', 'Stop:'], 0, 'Nit:'),
        ('A case at the boundary, like an empty list, is an ___.', ['edge case', 'end case', 'side case', 'test case'], 0, 'edge case.'),
        ('86400 without explanation is a ___.', ['magic number', 'hard number', 'secret number', 'nit'], 0, 'magic number.'),
        ('Responding to a good comment from a reviewer:', ['Good catch, thanks! Fixed.', 'No.', 'Whatever.', 'I know.'], 0, 'Good catch, thanks!'),
        ("Let's do the clean-up in a ___ to keep this PR small.", ['follow-up PR', 'follow PR', 'next PR up', 'PR follow'], 0, 'follow-up PR.'),
        ('A URL written directly in the code is ___.', ['hard-coded', 'hard-written', 'fixed-coded', 'deep-coded'], 0, 'hard-coded.'),
        ('"Could you ___ why we need this check?"', ['clarify', 'clear', 'clean', 'claim'], 0, 'clarify.'),
        ('Smaller, well-named functions are more ___.', ['maintainable', 'maintained', 'maintaining', 'maintenance'], 0, 'maintainable.'),
    ],
}

DAY4 = {
    'title': 'Làm rõ trong cuộc họp',
    'title_en': 'Clarifying in Meetings',
    'goal': 'Dùng thành thạo 15 cụm từ để xác nhận, hỏi lại, xin thời gian trả lời và tóm tắt trong cuộc họp online.',
    'tasks': [
        'Học 14 từ/cụm về cuộc họp.',
        'Nghe một cuộc họp online có nhiều tình huống cần làm rõ.',
        'Đóng vai người tham gia họp.',
        'Lập danh sách 15 cụm từ làm rõ của riêng bạn.',
    ],
    'product': 'Danh sách 15 cụm từ làm rõ',
    'warmup': [
        ('Just to confirm, the deadline is Friday, right?', 'Xin xác nhận, hạn chót là thứ Sáu đúng không?'),
        ('Sorry, could you repeat that?', 'Xin lỗi, bạn nhắc lại được không?'),
        ("Let me get back to you on that.", 'Để tôi trả lời bạn sau về việc đó.'),
        ("I think you're on mute.", 'Tôi nghĩ bạn đang tắt mic.'),
        ('Can everyone see my screen?', 'Mọi người thấy màn hình của tôi không?'),
        ("Let me quickly recap the action items.", 'Để tôi tóm tắt nhanh các việc cần làm.'),
    ],
    'vocab': [
        ('agenda', '/əˈdʒendə/', 'n', 'chương trình họp', "Let's stick to the agenda.", 'Hãy bám theo chương trình họp.'),
        ('action item', '/ˈækʃn ˈaɪtəm/', 'n', 'việc cần làm (sau họp)', 'Each action item needs an owner and a date.', 'Mỗi việc cần làm cần có người phụ trách và ngày hạn.'),
        ('take notes', '/teɪk nəʊts/', 'phrase', 'ghi chép', 'Could someone take notes today?', 'Hôm nay ai ghi chép được không?'),
        ('minutes', '/ˈmɪnɪts/', 'n (pl)', 'biên bản họp', "I'll send the minutes after the meeting.", 'Tôi sẽ gửi biên bản sau cuộc họp.'),
        ('circle back', '/ˈsɜːkl bæk/', 'phrasal verb', 'quay lại (bàn) sau', "Let's circle back to this next week.", 'Hãy quay lại chuyện này tuần sau.'),
        ('sync', '/sɪŋk/', 'n / verb', 'buổi trao đổi nhanh; đồng bộ', "Let's have a quick sync tomorrow.", 'Mai mình trao đổi nhanh nhé.'),
        ('align', '/əˈlaɪn/', 'verb', 'thống nhất (quan điểm)', 'We need to align on the priorities.', 'Chúng ta cần thống nhất về các ưu tiên.'),
        ('on mute', '/ɒn mjuːt/', 'phrase', 'đang tắt mic', "Sorry, I was on mute.", 'Xin lỗi, tôi đang tắt mic.'),
        ('share screen', '/ʃeə skriːn/', 'phrase', 'chia sẻ màn hình', 'Let me share my screen.', 'Để tôi chia sẻ màn hình.'),
        ('just to confirm', '/dʒʌst tə kənˈfɜːm/', 'phrase', 'xin xác nhận lại', 'Just to confirm, you need the report by Monday?', 'Xin xác nhận, bạn cần báo cáo trước thứ Hai?'),
        ('get back to', '/ɡet bæk tuː/', 'phrasal verb', 'trả lời lại sau', "I'll get back to you by the end of the day.", 'Tôi sẽ trả lời bạn trước cuối ngày.'),
        ('recap', '/ˈriːkæp/', 'n / verb', 'tóm tắt lại', 'Here\'s a quick recap of what we decided.', 'Đây là tóm tắt nhanh những gì ta đã quyết định.'),
        ('attendee', '/ˌætenˈdiː/', 'n', 'người tham dự', 'All attendees received the slides.', 'Mọi người tham dự đã nhận được slide.'),
        ('break up', '/breɪk ʌp/', 'phrasal verb', '(âm thanh) bị rè, đứt quãng', "Sorry, you're breaking up a bit.", 'Xin lỗi, tiếng bạn bị rè.'),
    ],
    'lesson': """
<h3>1. 15 cụm từ "cứu nguy" trong cuộc họp</h3>
<table class="table">
<tr><th>Tình huống</th><th>Cụm từ</th></tr>
<tr><td>Xác nhận</td><td><span class="say">Just to confirm, …?</span> · <span class="say">So if I understand correctly, …</span> · <span class="say">Just to be clear, …</span></td></tr>
<tr><td>Không nghe rõ</td><td><span class="say">Sorry, could you repeat that?</span> · <span class="say">You're breaking up a bit.</span> · <span class="say">Sorry, I missed the last part.</span></td></tr>
<tr><td>Không hiểu</td><td><span class="say">Could you give me an example?</span> · <span class="say">What do you mean by…?</span></td></tr>
<tr><td>Chưa trả lời được</td><td><span class="say">Let me get back to you on that.</span> · <span class="say">I'll need to check and confirm.</span></td></tr>
<tr><td>Hoãn bàn</td><td><span class="say">Can we circle back to this later?</span> · <span class="say">Maybe we can take this offline.</span></td></tr>
<tr><td>Tóm tắt</td><td><span class="say">Let me quickly recap.</span> · <span class="say">So the action items are…</span></td></tr>
</table>

<h3>2. Câu chuyên dụng cho họp online</h3>
<div class="ex"><span class="en">I think you're on mute.</span><span class="vi">Bạn đang tắt mic.</span></div>
<div class="ex"><span class="en">Can everyone see my screen?</span></div>
<div class="ex"><span class="en">Sorry, go ahead.</span><span class="vi">Khi hai người cùng nói một lúc — nhường lời.</span></div>
<div class="ex"><span class="en">Sorry, you're breaking up. Could you say that again?</span></div>
<div class="ex"><span class="en">I need to drop off in five minutes.</span><span class="vi">Tôi phải rời cuộc họp sau năm phút.</span></div>

<h3>3. Kỹ thuật "nói lại bằng lời mình" (paraphrase)</h3>
<p>Khi không chắc mình hiểu đúng, đừng hỏi "Can you repeat?" lần thứ ba. Hãy <b>tóm tắt lại điều bạn hiểu</b> và để người kia sửa:</p>
<div class="ex"><span class="en">So if I understand correctly, you want the report to include only active users, not everyone. Is that right?</span></div>
<p>Cách này cho thấy bạn đang lắng nghe, và người nói chỉ cần trả lời "yes" hoặc sửa một chi tiết.</p>
""",
    'phrases': [
        ('So if I understand correctly, …', 'Vậy nếu tôi hiểu đúng thì…'),
        ('Sorry, go ahead.', 'Xin lỗi, bạn nói trước đi.'),
        ('I need to drop off in five minutes.', 'Năm phút nữa tôi phải rời họp.'),
        ('What do you mean by…?', '… nghĩa là gì vậy?'),
        ('Sorry, I missed the last part.', 'Xin lỗi, tôi lỡ mất phần cuối.'),
    ],
    'listening': {
        'title': 'A client call with technical problems',
        'intro': 'Một cuộc gọi với khách hàng có đủ tình huống: tắt mic, rè tiếng, yêu cầu mơ hồ. Chú ý cách Hà làm rõ.',
        'speakers': {'A': ('Mr. Davis (client)', 'guy'), 'B': ('Ha', 'jenny')},
        'lines': [
            ('B', "Good morning, Mr. Davis. Can you hear me okay?", 'Chào buổi sáng, ông Davis. Ông nghe tôi rõ không?'),
            ('A', "Yes, perfectly. Before we start, I'd like to add one thing to the agenda: the new reports.", 'Có, rất rõ. Trước khi bắt đầu, tôi muốn thêm một mục vào chương trình họp: các báo cáo mới.'),
            ('B', "Of course. Let me share my screen first. Can you see the dashboard?", 'Dĩ nhiên. Để tôi chia sẻ màn hình trước. Ông có thấy dashboard không?'),
            ('A', "Yes. So, for the reports, we need… [silence]", 'Có. Vậy, về báo cáo, chúng tôi cần… [im lặng]'),
            ('B', "Sorry, Mr. Davis, I think you're on mute.", 'Xin lỗi ông Davis, tôi nghĩ ông đang tắt mic.'),
            ('A', "Oh, sorry about that. I said we need the reports to show weekly data, and also the… numbers for the… region.", 'Ồ, xin lỗi. Tôi nói chúng tôi cần báo cáo hiển thị dữ liệu theo tuần, và cả… số liệu cho… khu vực.'),
            ('B', "Sorry, you're breaking up a bit. I missed the last part. Could you repeat that?", 'Xin lỗi, tiếng ông bị rè. Tôi lỡ phần cuối. Ông nhắc lại được không?'),
            ('A', "Sure. The sales numbers for each region.", 'Được. Số liệu bán hàng cho từng khu vực.'),
            ('B', "Got it. So if I understand correctly, you want weekly reports with sales numbers broken down by region. Is that right?", 'Đã rõ. Vậy nếu tôi hiểu đúng, ông muốn báo cáo hằng tuần có số liệu bán hàng chia theo khu vực. Đúng không ạ?'),
            ('A', "Exactly. And can we have it before the end of the month?", 'Chính xác. Và chúng tôi có thể có nó trước cuối tháng không?'),
            ('B', "I'll need to check with the team before I can promise a date. Let me get back to you on that by tomorrow.", 'Tôi cần kiểm tra với team trước khi hứa ngày cụ thể. Để tôi trả lời ông về việc đó trước ngày mai.'),
            ('A', "That's fine. Oh, and what about the mobile version we discussed last time?", 'Được. À, còn phiên bản di động chúng ta bàn lần trước thì sao?'),
            ('B', "That's a bigger topic. Can we circle back to it next week, so we have enough time?", 'Đó là chủ đề lớn hơn. Chúng ta quay lại vào tuần sau được không, để có đủ thời gian?'),
            ('A', "Good idea.", 'Ý hay.'),
            ('B', "Great. Let me quickly recap. Action items: I'll confirm the date for the regional reports by tomorrow, and we'll schedule a sync about the mobile version next week. I'll send the minutes after this call.", 'Tuyệt. Để tôi tóm tắt nhanh. Việc cần làm: tôi sẽ xác nhận ngày cho báo cáo theo khu vực trước ngày mai, và chúng ta sẽ hẹn một buổi trao đổi về bản di động tuần sau. Tôi sẽ gửi biên bản sau cuộc gọi.'),
        ],
        'questions': [
            ('What did Mr. Davis add to the agenda?', ['The mobile version', 'The new reports', 'The budget', 'A new team member'], 1, '"I\'d like to add one thing to the agenda: the new reports."'),
            ('Why didn\'t Ha hear him the first time?', ['He was on mute.', 'She was late.', 'He spoke Spanish.', 'The meeting ended.'], 0, '"I think you\'re on mute."'),
            ('What exactly does Mr. Davis want?', ['Daily reports for all users', 'Weekly reports with sales numbers by region', 'Monthly reports for the mobile app', 'A new dashboard design'], 1, 'Hà tóm tắt lại.'),
            ('Why doesn\'t Ha promise a date immediately?', ['She doesn\'t want to do it.', 'She needs to check with the team.', 'The client is rude.', 'It is impossible.'], 1, '"I\'ll need to check with the team before I can promise a date."'),
            ('What will happen with the mobile version topic?', ['It is cancelled.', 'They will discuss it next week.', 'Ha will decide alone.', 'They discussed it fully.'], 1, '"Can we circle back to it next week".'),
        ],
    },
    'speaking': {
        'tips': ['Đóng vai Hà ở phần Nghe.', 'Luyện từng tình huống bên dưới: nói ngay cụm từ phù hợp, không suy nghĩ quá 3 giây.'],
        'prompts': [
            ('The client says something important, but the audio cuts out. What do you say?', 'You\'re breaking up…'),
            ('Your manager gives a long, unclear explanation. Check your understanding.', 'So if I understand correctly, …'),
            ('Someone asks you for a date you can\'t promise yet.', 'Let me get back to you…'),
            ('The meeting is ending. Recap the action items.', 'Let me quickly recap…'),
        ],
        'model': (
            "Sorry, you're breaking up a bit. Could you repeat the last part? "
            "Okay, so if I understand correctly, you'd like us to add a filter for date ranges, and the default should be the last thirty days. Is that right? "
            "In terms of timing, I'll need to check with the team before I can promise a date. Let me get back to you on that by Thursday. "
            "Great. Let me quickly recap. Action items: I'll confirm the timeline by Thursday, and Lisa will send the updated designs. I'll send the minutes after the call.",
            'Xin lỗi, tiếng bạn hơi rè. Bạn nhắc lại phần cuối được không? '
            'Được, vậy nếu tôi hiểu đúng, bạn muốn chúng tôi thêm bộ lọc theo khoảng ngày, và mặc định là ba mươi ngày gần nhất. Đúng không? '
            'Về thời gian, tôi cần kiểm tra với team trước khi hứa ngày cụ thể. Để tôi trả lời bạn trước thứ Năm. '
            'Tuyệt. Để tôi tóm tắt nhanh. Việc cần làm: tôi xác nhận tiến độ trước thứ Năm, và Lisa gửi thiết kế cập nhật. Tôi sẽ gửi biên bản sau cuộc gọi.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Why you should always send meeting notes',
        'text': [
            'Two people can leave the same meeting with completely different ideas about what was decided. One thinks the deadline is the end of the month; the other thinks it is the middle. Nobody notices until it is too late.',
            'A short written summary prevents this. It does not need to be long: three or four bullet points with the decisions, the action items, the owner of each item and the due date. Send it within an hour of the meeting, while everyone still remembers the discussion.',
            'For non-native speakers, meeting notes have an extra benefit. If you misunderstood something, people will correct you in writing, which is much less stressful than being corrected in front of the whole team.',
        ],
        'vi': 'Hai người có thể rời cùng một cuộc họp với hiểu biết hoàn toàn khác nhau về điều đã quyết định. Một bản tóm tắt ngắn ngăn chặn điều này: 3–4 gạch đầu dòng gồm quyết định, việc cần làm, người phụ trách và hạn chót, gửi trong vòng một giờ sau họp. Với người không phải bản xứ, biên bản họp còn có lợi ích thêm: nếu bạn hiểu sai, mọi người sẽ sửa bằng văn bản — đỡ căng thẳng hơn nhiều so với bị sửa trước cả team.',
        'questions': [
            ('What problem do meeting notes prevent?', ['Long meetings', 'Different understandings of decisions', 'Bad audio', 'Late attendees'], 1, 'Đoạn 1.'),
            ('When should you send the summary?', ['The next week', 'Within an hour of the meeting', 'Before the meeting', 'Only if asked'], 1, 'Đoạn 2.'),
            ('What extra benefit do notes have for non-native speakers?', ['They improve grammar.', 'Corrections come in writing, which is less stressful.', 'They make meetings shorter.', 'They replace speaking.'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Phần A: Viết danh sách 15 cụm từ làm rõ của bạn (chia theo tình huống). Phần B: Viết biên bản ngắn cho cuộc gọi ở bài nghe (quyết định, việc cần làm, người phụ trách, hạn).',
        'tips': ['Biên bản dùng gạch đầu dòng, câu ngắn.'],
        'model': "Meeting notes – Call with Mr. Davis (Tuesday)\n\nDecisions:\n• The new reports will show weekly data with sales numbers by region.\n• The mobile version will be discussed separately next week.\n\nAction items:\n• Ha – confirm the delivery date for the regional reports – by Wednesday.\n• Ha – schedule a sync about the mobile version – next week.\n\nPlease let me know if I missed or misunderstood anything.",
        'min_words': 60,
    },
    'quiz': [
        ('"___, the deadline is Friday, right?"', ['Just to confirm', 'Just in case', 'Just for fun', 'Just about'], 0, 'Just to confirm.'),
        ('The audio keeps cutting out. You say:', ["You're breaking up a bit.", "You're breaking down.", "You're broken.", "You break."], 0, 'break up = rè, đứt quãng.'),
        ('You can\'t answer now. You say:', ['Let me get back to you on that.', 'I don\'t know, sorry.', 'Ask someone else.', 'No comment.'], 0, 'get back to somebody.'),
        ('"Let\'s ___ back to this topic next week."', ['circle', 'turn', 'go round', 'come'], 0, 'circle back.'),
        ('The written record of a meeting is the ___.', ['minutes', 'hours', 'seconds', 'notes up'], 0, 'minutes.'),
        ('A task that someone must do after a meeting is an ___.', ['action item', 'agenda', 'attendee', 'apology'], 0, 'action item.'),
        ('Nobody can hear Tom. You say:', ["I think you're on mute.", "You're off mute.", "Your sound is mute.", "Turn your mute."], 0, 'on mute.'),
        ('Checking understanding by paraphrasing:', ['So if I understand correctly, …', 'Repeat please.', 'What?', 'Okay okay.'], 0, 'Paraphrase.'),
        ('"We need to ___ on the priorities before we start."', ['align', 'aline', 'line', 'assign'], 0, 'align on.'),
        ('Two people start talking at the same time. You say:', ['Sorry, go ahead.', 'Stop.', 'Me first.', 'Wait me.'], 0, 'Sorry, go ahead.'),
    ],
}

DAY5 = {
    'title': 'Mô phỏng họp với PM',
    'title_en': 'Simulated Meeting with a Project Manager',
    'goal': 'Xử lý một cuộc họp với PM: báo cáo tiến độ, phản hồi yêu cầu thay đổi, thương lượng phạm vi và thời hạn một cách lịch sự nhưng rõ ràng.',
    'tasks': [
        'Học 14 từ về phạm vi, thời hạn và thương lượng.',
        'Nghe cuộc họp mẫu giữa PM và developer.',
        'Đóng vai developer (chọn "Bạn là Tuấn") ít nhất 2 lần.',
        'Trả lời 6 câu hỏi của PM ở phần Nói và ghi âm cả buổi.',
        'Ghi 5 lỗi nổi bật sau khi nghe lại.',
    ],
    'product': 'Bản ghi âm buổi họp mô phỏng; Ghi chú 5 lỗi',
    'warmup': [
        ("I'd like to push back on that timeline a little.", 'Tôi muốn phản đối nhẹ về tiến độ đó.'),
        ("Is that deadline realistic?", 'Hạn chót đó có thực tế không?'),
        ('If we descope the reports, we can make it.', 'Nếu cắt bớt phần báo cáo, chúng ta kịp.'),
        ("What's the priority: speed or features?", 'Ưu tiên là tốc độ hay tính năng?'),
        ("It's feasible, but it's tight.", 'Khả thi, nhưng sít sao.'),
        ("That's a nice-to-have, not a must-have.", 'Đó là thứ nên có, không phải bắt buộc phải có.'),
    ],
    'vocab': [
        ('push back', '/pʊʃ bæk/', 'phrasal verb', 'phản đối (lịch sự); lùi lịch', "I had to push back on the new deadline.", 'Tôi phải phản đối hạn chót mới.'),
        ('realistic', '/ˌriːəˈlɪstɪk/', 'adj', 'thực tế', "Two weeks isn't realistic for this feature.", 'Hai tuần không thực tế cho tính năng này.'),
        ('timeline', '/ˈtaɪmlaɪn/', 'n', 'tiến độ, mốc thời gian', "Let's agree on a timeline.", 'Hãy thống nhất tiến độ.'),
        ('commit to', '/kəˈmɪt tuː/', 'verb', 'cam kết', "I can't commit to Friday yet.", 'Tôi chưa thể cam kết thứ Sáu.'),
        ('descope', '/diːˈskəʊp/', 'verb', 'cắt bớt phạm vi', 'We descoped the admin panel to launch on time.', 'Chúng tôi cắt bớt trang quản trị để ra mắt đúng hạn.'),
        ('prioritize', '/praɪˈɒrətaɪz/', 'verb', 'ưu tiên', 'We need to prioritize security over new features.', 'Chúng ta cần ưu tiên bảo mật hơn tính năng mới.'),
        ('feasible', '/ˈfiːzəbl/', 'adj', 'khả thi', 'Is it technically feasible?', 'Về kỹ thuật có khả thi không?'),
        ('change request', '/tʃeɪndʒ rɪˈkwest/', 'n', 'yêu cầu thay đổi', 'Every change request must be estimated first.', 'Mọi yêu cầu thay đổi phải được ước lượng trước.'),
        ('flexibility', '/ˌfleksəˈbɪləti/', 'n', 'sự linh hoạt', 'Is there any flexibility on the date?', 'Ngày có linh hoạt được không?'),
        ('quick win', '/kwɪk wɪn/', 'n', 'kết quả nhanh, dễ đạt', 'Fixing the search speed is a quick win.', 'Tăng tốc tìm kiếm là việc dễ mà hiệu quả nhanh.'),
        ('nice-to-have', '/ˌnaɪs tə ˈhæv/', 'n', 'thứ nên có (không bắt buộc)', 'Dark mode is a nice-to-have.', 'Chế độ tối là thứ nên có.'),
        ('must-have', '/ˈmʌst hæv/', 'n', 'thứ bắt buộc phải có', 'Secure login is a must-have.', 'Đăng nhập an toàn là bắt buộc.'),
        ('phase', '/feɪz/', 'n / verb', 'giai đoạn; chia giai đoạn', "Let's phase the release: core features first.", 'Hãy chia giai đoạn phát hành: tính năng cốt lõi trước.'),
        ('bandwidth', '/ˈbændwɪdθ/', 'n', 'thời gian/khả năng làm thêm việc', "I don't have the bandwidth for another project.", 'Tôi không còn sức để nhận thêm dự án.'),
    ],
    'lesson': """
<h3>1. Khi PM yêu cầu thêm việc: công thức "Yes, and…/Yes, but…"</h3>
<p>Đừng nói "No" thẳng thừng, cũng đừng nói "Yes" rồi làm không kịp. Hãy cho PM thấy <b>sự đánh đổi</b>:</p>
<div class="ex"><span class="en">Yes, we can add the export feature, but the release would move to next Friday.</span></div>
<div class="ex"><span class="en">We can keep the date if we descope the reports to phase two.</span></div>
<div class="ex"><span class="en">Which is more important for you: the date or the full feature set?</span></div>

<h3>2. Bộ câu thương lượng</h3>
<table class="table">
<tr><th>Mục đích</th><th>Câu</th></tr>
<tr><td>Phản đối nhẹ</td><td><span class="say">I'd like to push back a little on that.</span> · <span class="say">I'm not sure that's realistic.</span></td></tr>
<tr><td>Hỏi ưu tiên</td><td><span class="say">What's the priority here?</span> · <span class="say">Is this a must-have or a nice-to-have?</span></td></tr>
<tr><td>Đưa phương án</td><td><span class="say">What if we phase it? Core features first, the rest in two weeks.</span></td></tr>
<tr><td>Hỏi linh hoạt</td><td><span class="say">Is there any flexibility on the deadline?</span></td></tr>
<tr><td>Chưa thể hứa</td><td><span class="say">I can't commit to that until I've looked at the code.</span></td></tr>
<tr><td>Đồng ý có điều kiện</td><td><span class="say">That's feasible, as long as the designs are final by Monday.</span></td></tr>
</table>

<h3>3. Cấu trúc trả lời một yêu cầu thay đổi</h3>
<ol>
<li><b>Ghi nhận:</b> <span class="say">I understand why that's important.</span></li>
<li><b>Tác động:</b> <span class="say">It would add about three days of work.</span></li>
<li><b>Phương án:</b> <span class="say">We could either move the date, or drop the PDF export for now.</span></li>
<li><b>Hỏi quyết định:</b> <span class="say">Which option works better for you?</span></li>
</ol>
<div class="note"><b>Mẹo:</b> Nói con số (số ngày, số giờ) giúp cuộc thương lượng khách quan, không mang tính cá nhân.</div>
""",
    'phrases': [
        ('I understand why that\'s important.', 'Tôi hiểu vì sao điều đó quan trọng.'),
        ('Which option works better for you?', 'Phương án nào phù hợp với bạn hơn?'),
        ('That would add about three days.', 'Việc đó sẽ thêm khoảng ba ngày.'),
        ("I don't have the bandwidth right now.", 'Hiện tôi không còn thời gian cho việc đó.'),
    ],
    'listening': {
        'title': 'Meeting with the PM',
        'intro': 'PM Rebecca họp với developer Tuấn: hỏi tiến độ, đưa thêm yêu cầu và muốn dời hạn chót sớm hơn. Sau khi nghe, đóng vai Tuấn.',
        'speakers': {'A': ('Rebecca (PM)', 'sonia'), 'B': ('Tuan', 'brian')},
        'lines': [
            ('A', "Hi Tuan, thanks for joining. How's the booking feature coming along?", 'Chào Tuấn, cảm ơn đã tham gia. Tính năng đặt lịch tiến triển thế nào?'),
            ('B', "It's going well. The booking flow is done, and I'm about halfway through the payment step. We're on track for the twentieth.", 'Ổn ạ. Luồng đặt lịch xong rồi, phần thanh toán em làm được khoảng một nửa. Chúng ta đúng tiến độ cho ngày hai mươi.'),
            ('A', "Great. Now, I've got some news. The client wants to launch on the fifteenth instead, because of a marketing campaign.", 'Tuyệt. Giờ chị có tin này. Khách hàng muốn ra mắt vào ngày mười lăm, vì một chiến dịch marketing.'),
            ('B', "Five days earlier? I understand why that's important, but I'd like to push back a little. I don't think it's realistic with the current scope.", 'Sớm hơn năm ngày ạ? Em hiểu vì sao điều đó quan trọng, nhưng em muốn phản đối nhẹ. Em không nghĩ là thực tế với phạm vi hiện tại.'),
            ('A', "What would we need to change?", 'Chúng ta cần thay đổi gì?'),
            ('B', "We could phase it. The booking and payment are must-haves, so we launch those on the fifteenth. The calendar sync and the reminder emails could come a week later.", 'Mình có thể chia giai đoạn. Đặt lịch và thanh toán là bắt buộc, nên ra mắt chúng vào ngày mười lăm. Đồng bộ lịch và email nhắc nhở có thể ra sau một tuần.'),
            ('A', "Hmm. The client really likes the reminders.", 'Hừm. Khách hàng rất thích tính năng nhắc nhở.'),
            ('B', "Then another option is to keep the reminders but descope the calendar sync. The reminders are a quick win, maybe one day of work.", 'Vậy một phương án khác là giữ nhắc nhở nhưng cắt đồng bộ lịch. Nhắc nhở làm nhanh, chắc một ngày.'),
            ('A', "That could work. One more thing: they also asked for an admin report of all bookings. Can we add that?", 'Có thể được. Thêm một việc: họ cũng yêu cầu báo cáo quản trị cho tất cả lịch đặt. Mình thêm được không?'),
            ('B', "That's a new change request. It would add about three days. I'd suggest we treat it as a nice-to-have for phase two. Is there any flexibility on that?", 'Đó là một yêu cầu thay đổi mới. Nó sẽ thêm khoảng ba ngày. Em đề xuất coi nó là thứ nên có cho giai đoạn hai. Phần đó có linh hoạt được không ạ?'),
            ('A', "I think so. I'll check with them. So, to summarise: booking, payment and reminders on the fifteenth; calendar sync and reports in phase two.", 'Chắc là được. Chị sẽ hỏi họ. Vậy tóm lại: đặt lịch, thanh toán và nhắc nhở vào ngày mười lăm; đồng bộ lịch và báo cáo ở giai đoạn hai.'),
            ('B', "Exactly. I can commit to that, as long as the payment provider gives us the live keys by the tenth.", 'Chính xác. Em có thể cam kết điều đó, miễn là bên thanh toán đưa key thật trước ngày mười.'),
            ('A', "Perfect. I'll send a summary to the client today. Thanks, Tuan.", 'Hoàn hảo. Hôm nay chị sẽ gửi bản tóm tắt cho khách hàng. Cảm ơn Tuấn.'),
        ],
        'questions': [
            ('What was the original launch date?', ['The tenth', 'The fifteenth', 'The twentieth', 'Next month'], 2, '"We\'re on track for the twentieth."'),
            ('Why does the client want to launch earlier?', ['Because of a marketing campaign', 'Because of a competitor', 'Because the CEO is leaving', 'No reason'], 0, '"because of a marketing campaign".'),
            ('What is Tuan\'s first suggestion?', ['Work at weekends', 'Phase the release', 'Cancel the project', 'Hire more developers'], 1, '"We could phase it."'),
            ('Why does Tuan suggest keeping the reminders?', ['They are a quick win (about one day).', 'They are the hardest part.', 'The calendar sync is broken.', 'Rebecca insists.'], 0, '"The reminders are a quick win, maybe one day of work."'),
            ('What is Tuan\'s condition for committing to the fifteenth?', ['More money', 'Live payment keys by the tenth', 'A new designer', 'No more meetings'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Đóng vai Tuấn ở phần Nghe ít nhất 2 lần (không nhìn lời ở lần 2).', 'Sau đó trả lời 6 câu hỏi của PM bên dưới — bấm nghe từng câu, trả lời ngay, ghi âm cả buổi.'],
        'prompts': [
            ("How's your current task going?", 'Tiến độ cụ thể.'),
            ('The client wants it a week earlier. Is that possible?', 'push back + phương án.'),
            ('Can we add a dark mode before launch?', 'nice-to-have / phase two.'),
            ('What do you need from me to stay on track?', 'Nêu điều kiện.'),
            ('Why did the last feature take longer than planned?', 'Lý do + bài học.'),
            ('Can you commit to Friday?', 'I can commit to… as long as…'),
        ],
        'model': (
            "I understand the client wants it a week earlier, and I see why. But honestly, I don't think that's realistic with the current scope. "
            "We still need about eight days for payment and testing. "
            "What I'd suggest is to phase it. We launch the must-haves, booking and payment, on the new date, and move the dashboard to phase two. "
            "Dark mode is a nice-to-have, so I'd also keep it for later. "
            "If we go with that plan, I can commit to the new date, as long as I get the final designs by Monday.",
            'Tôi hiểu khách hàng muốn sớm hơn một tuần và tôi hiểu lý do. Nhưng thật lòng, tôi không nghĩ là thực tế với phạm vi hiện tại. '
            'Chúng ta vẫn cần khoảng tám ngày cho thanh toán và kiểm thử. '
            'Tôi đề xuất chia giai đoạn. Ra mắt những thứ bắt buộc là đặt lịch và thanh toán vào ngày mới, chuyển dashboard sang giai đoạn hai. '
            'Chế độ tối là thứ nên có, nên tôi cũng để sau. '
            'Nếu theo kế hoạch đó, tôi có thể cam kết ngày mới, miễn là tôi nhận thiết kế cuối trước thứ Hai.'
        ),
        'seconds': 240,
    },
    'reading': {
        'title': 'Saying no without saying no',
        'text': [
            'Developers are often asked to do more in less time. Saying "no" can feel rude, especially in cultures where people avoid direct conflict. But saying "yes" to everything leads to missed deadlines and tired teams.',
            'The solution is to answer with options instead of a simple yes or no. "We can do A by Friday, or A and B by next Wednesday. Which do you prefer?" This puts the decision back with the person who owns the priorities, usually the product manager.',
            'Options work because they show that you want to help, they make the cost of each request visible, and they turn a conflict into a shared problem. Most managers respect this much more than a silent yes.',
        ],
        'vi': 'Dev thường bị yêu cầu làm nhiều hơn trong thời gian ít hơn. Nói "không" có vẻ bất lịch sự, nhưng nói "có" với mọi thứ dẫn đến trễ hạn và team kiệt sức. Giải pháp: trả lời bằng các phương án ("A trước thứ Sáu, hoặc A và B trước thứ Tư tuần sau — bạn chọn cái nào?") để quyết định quay về người nắm ưu tiên. Phương án cho thấy bạn muốn giúp, làm rõ chi phí của mỗi yêu cầu và biến xung đột thành vấn đề chung.',
        'questions': [
            ('What happens if you say yes to everything?', ['You get promoted.', 'Missed deadlines and tired teams', 'Better products', 'Happier clients'], 1, 'Đoạn 1.'),
            ('What does the writer suggest instead of yes or no?', ['Silence', 'Options', 'Asking another developer', 'Working overtime'], 1, 'Đoạn 2.'),
            ('Who should usually make the decision between options?', ['The developer', 'The product manager', 'The tester', 'The CEO'], 1, '"the person who owns the priorities, usually the product manager".'),
        ],
    },
    'writing': {
        'task': 'Viết tin nhắn (6–8 câu) trả lời PM khi họ yêu cầu thêm một tính năng mà vẫn giữ nguyên hạn chót. Dùng cấu trúc: ghi nhận – tác động – 2 phương án – hỏi quyết định.',
        'tips': ['Có con số (số ngày).', 'Dùng: I understand…, It would add…, We could either… or…, Which option works better for you?'],
        'model': "Hi Rebecca,\n\nThanks for passing on the request for the admin report. I understand why it's important for the client. It would add about three days of work, mainly for the filters and the export. We could either keep the launch on the 15th and deliver the report in phase two, or include the report and move the launch to the 18th. Personally, I'd recommend the first option, because the booking and payment flows are the real must-haves. Which option works better for you and the client?\n\nThanks,\nTuan",
        'min_words': 70,
    },
    'quiz': [
        ('"I\'d like to ___ back on that deadline a little."', ['push', 'pull', 'put', 'pay'], 0, 'push back = phản đối lịch sự.'),
        ('Something essential for launch is a ___.', ['must-have', 'nice-to-have', 'quick win', 'phase'], 0, 'must-have.'),
        ('Something good but not essential is a ___.', ['nice-to-have', 'must-have', 'blocker', 'deadline'], 0, 'nice-to-have.'),
        ('Removing features to meet a date = to ___.', ['descope', 'escape', 'describe', 'deploy'], 0, 'descope.'),
        ('"Is there any ___ on the date?"', ['flexibility', 'flexible', 'flex', 'flexing'], 0, 'flexibility (danh từ).'),
        ('"I can\'t ___ to Friday until I check the code."', ['commit', 'commute', 'comment', 'complete'], 0, 'commit to.'),
        ('A small task with big impact is a ___.', ['quick win', 'fast win', 'easy go', 'short hit'], 0, 'quick win.'),
        ('"I don\'t have the ___ for another project."', ['bandwidth', 'broadband', 'bandage', 'bond'], 0, 'bandwidth = khả năng nhận thêm việc.'),
        ('Câu trả lời tốt nhất cho yêu cầu thêm việc:', ['No.', 'Yes, sure! (rồi làm không kịp)', 'We can add it, but the launch would move by three days. Which do you prefer?', 'Ask the client.'], 2, 'Đưa phương án + đánh đổi.'),
        ('"That\'s technically ___, but the timeline is tight."', ['feasible', 'feasibility', 'fees', 'favourable'], 0, 'feasible = khả thi.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 6',
    'title_en': 'Week 6 Review: Sounding Natural',
    'goal': 'Nghe lại bản ghi âm trong tuần, sửa 5 câu nói chưa tự nhiên; học cách làm mềm câu (I was wondering if…, would you mind…) để nghe lịch sự và chuyên nghiệp.',
    'tasks': [
        'Học 14 cụm từ làm mềm câu.',
        'So sánh câu "thẳng" và câu "mềm" trong bài học.',
        'Nghe hội thoại công sở lịch sự.',
        'Nghe lại bản ghi tuần này, chọn 5 câu chưa tự nhiên và sửa lại.',
        'Ghi âm lại 5 câu đã sửa.',
    ],
    'product': 'Bản ghi cuối tuần; 5 câu đã sửa',
    'warmup': [
        ('I was wondering if you could help me with this.', 'Không biết bạn có thể giúp tôi việc này không.'),
        ('Would you mind taking a look at my PR?', 'Bạn có phiền xem PR của tôi không?'),
        ('It might be worth checking the logs first.', 'Có lẽ nên kiểm tra log trước.'),
        ('Maybe we could move the meeting to Thursday?', 'Có lẽ chúng ta dời họp sang thứ Năm?'),
        ("I'm happy to help if you need anything.", 'Tôi sẵn lòng giúp nếu bạn cần gì.'),
        ('Just wanted to check if you saw my email.', 'Tôi chỉ muốn hỏi xem bạn đã thấy email của tôi chưa.'),
    ],
    'vocab': [
        ('I was wondering if', '/aɪ wəz ˈwʌndərɪŋ ɪf/', 'phrase', 'không biết liệu… (nhờ vả lịch sự)', 'I was wondering if you had time for a quick call.', 'Không biết bạn có thời gian cho một cuộc gọi nhanh không.'),
        ('would you mind', '/wʊd juː maɪnd/', 'phrase', 'bạn có phiền… (+ V-ing)', 'Would you mind sending me the file again?', 'Bạn có phiền gửi lại file cho tôi không?'),
        ('it might be worth', '/ɪt maɪt biː wɜːθ/', 'phrase', 'có lẽ đáng để… (+ V-ing)', 'It might be worth asking the client first.', 'Có lẽ nên hỏi khách hàng trước.'),
        ('perhaps', '/pəˈhæps/', 'adv', 'có lẽ', 'Perhaps we should wait until Monday.', 'Có lẽ chúng ta nên đợi đến thứ Hai.'),
        ('could we possibly', '/kʊd wiː ˈpɒsəbli/', 'phrase', 'liệu chúng ta có thể (rất lịch sự)', 'Could we possibly start ten minutes later?', 'Liệu chúng ta có thể bắt đầu muộn mười phút không?'),
        ('happy to', '/ˈhæpi tuː/', 'phrase', 'sẵn lòng', "I'm happy to explain it again.", 'Tôi sẵn lòng giải thích lại.'),
        ('if possible', '/ɪf ˈpɒsəbl/', 'phrase', 'nếu có thể', 'Please reply by Friday, if possible.', 'Vui lòng trả lời trước thứ Sáu, nếu có thể.'),
        ('maybe we could', '/ˈmeɪbi wiː kʊd/', 'phrase', 'có lẽ chúng ta có thể (gợi ý)', 'Maybe we could try a different approach.', 'Có lẽ chúng ta có thể thử cách khác.'),
        ("I'd rather", '/aɪd ˈrɑːðə/', 'phrase', 'tôi muốn… hơn', "I'd rather fix it properly than rush it.", 'Tôi muốn sửa cho đúng hơn là làm vội.'),
        ('do you think we could', '/duː juː θɪŋk wiː kʊd/', 'phrase', 'bạn nghĩ chúng ta có thể…?', 'Do you think we could extend the deadline?', 'Bạn nghĩ chúng ta có thể gia hạn không?'),
        ('feel free to', '/fiːl friː tuː/', 'phrase', 'cứ tự nhiên', 'Feel free to ask me anything.', 'Cứ tự nhiên hỏi tôi bất cứ điều gì.'),
        ('no worries', '/nəʊ ˈwʌriz/', 'phrase', 'không sao đâu', '"Sorry I\'m late." — "No worries!"', '"Xin lỗi tôi đến muộn." — "Không sao đâu!"'),
        ('just wanted to', '/dʒʌst ˈwɒntɪd tuː/', 'phrase', 'chỉ muốn (làm nhẹ lời nhắc)', 'Just wanted to follow up on my last message.', 'Tôi chỉ muốn nhắc lại tin nhắn trước.'),
        ('a quick question', '/ə kwɪk ˈkwestʃən/', 'phrase', 'một câu hỏi nhanh', 'Hi Anna, a quick question about the API.', 'Chào Anna, một câu hỏi nhanh về API.'),
    ],
    'lesson': """
<h3>1. Vì sao câu đúng ngữ pháp vẫn nghe "cộc"?</h3>
<p>Tiếng Việt lịch sự nhờ từ như "ạ", "giúp", "nhé". Tiếng Anh lịch sự nhờ <b>cấu trúc gián tiếp</b>: lùi thì, dùng câu hỏi, thêm từ làm mềm. Người Việt hay dịch thẳng nên dễ nghe như ra lệnh.</p>
<table class="table">
<tr><th>Thẳng (nghe cộc)</th><th>Mềm (tự nhiên, chuyên nghiệp)</th></tr>
<tr><td>Send me the file.</td><td><span class="say">Could you send me the file when you get a chance?</span></td></tr>
<tr><td>Review my code.</td><td><span class="say">Would you mind reviewing my code today?</span></td></tr>
<tr><td>I want to ask you something.</td><td><span class="say">I was wondering if I could ask you a quick question.</span></td></tr>
<tr><td>Your idea is bad.</td><td><span class="say">I'm not sure that would work. Maybe we could try…</span></td></tr>
<tr><td>Why didn't you reply?</td><td><span class="say">Just wanted to check if you saw my email.</span></td></tr>
<tr><td>You must check the logs.</td><td><span class="say">It might be worth checking the logs first.</span></td></tr>
</table>

<h3>2. Bốn kỹ thuật làm mềm</h3>
<ol>
<li><b>Câu hỏi thay mệnh lệnh:</b> Could you…? Would you mind…?</li>
<li><b>Lùi thì:</b> I <b>was</b> wondering… / I <b>wanted</b> to ask… (lịch sự hơn I wonder / I want).</li>
<li><b>Từ giảm nhẹ:</b> just, a bit, perhaps, maybe, possibly, slightly.</li>
<li><b>Ghi nhận trước khi phản đối:</b> <span class="say">That's a good point, but…</span> · <span class="say">I see what you mean. However…</span></li>
</ol>
<div class="warn"><b>Would you mind + V-ing:</b> <span class="say">Would you mind closing the door?</span> — trả lời đồng ý là <b>"No, not at all."</b> (= không phiền gì).</div>

<h3>3. Tổng kết tuần 6</h3>
<table class="table">
<tr><th>Tình huống</th><th>Câu quan trọng nhất</th></tr>
<tr><td>Standup</td><td><span class="say">Yesterday I…, today I'll…, no blockers.</span></td></tr>
<tr><td>Báo cáo tiến độ</td><td><span class="say">I'm about halfway through. Worst case, Friday.</span></td></tr>
<tr><td>Code review</td><td><span class="say">Could you clarify why…? Nit: … LGTM.</span></td></tr>
<tr><td>Họp</td><td><span class="say">Just to confirm… Let me get back to you on that.</span></td></tr>
<tr><td>Thương lượng</td><td><span class="say">We could either… or… Which works better for you?</span></td></tr>
</table>
""",
    'listening': {
        'title': 'Polite requests at work',
        'intro': 'Ba tình huống ngắn trong một ngày làm việc. Chú ý cách hai người làm mềm câu.',
        'speakers': {'A': ('Olivia', 'emma'), 'B': ('Hung', 'andrew')},
        'lines': [
            ('B', "Hi Olivia, a quick question. Do you have a minute?", 'Chào Olivia, một câu hỏi nhanh. Bạn có một phút không?'),
            ('A', "Sure, what's up?", 'Chắc chắn, có chuyện gì vậy?'),
            ('B', "I was wondering if you could take a look at my PR before lunch. It's quite small.", 'Không biết bạn có thể xem PR của mình trước bữa trưa không. Nó khá nhỏ.'),
            ('A', "Happy to. Would you mind sending me the link? I can't find it.", 'Sẵn lòng. Bạn có phiền gửi link cho mình không? Mình không tìm thấy.'),
            ('B', "Not at all. I'll send it now. Thanks a lot.", 'Không phiền gì. Mình gửi ngay. Cảm ơn nhiều.'),
            ('A', "Oh, and Hung, about the database change you mentioned yesterday. It might be worth running it on staging first. The data there is much bigger.", 'À Hùng, về thay đổi cơ sở dữ liệu bạn nói hôm qua. Có lẽ nên chạy nó trên staging trước. Dữ liệu ở đó lớn hơn nhiều.'),
            ('B', "That's a good point. I was planning to run it directly, but I'd rather be safe.", 'Ý hay. Mình định chạy trực tiếp, nhưng mình muốn an toàn hơn.'),
            ('A', "Also, do you think we could move our sync to three o'clock? I have a client call at two.", 'Thêm nữa, bạn nghĩ chúng ta có thể dời buổi trao đổi sang ba giờ không? Hai giờ mình có cuộc gọi với khách.'),
            ('B', "No worries, three is fine. I'll update the invite.", 'Không sao, ba giờ được. Mình sẽ cập nhật lời mời.'),
            ('A', "Perfect. And feel free to ping me if you get stuck with the migration.", 'Hoàn hảo. Và cứ nhắn mình nếu bạn bị bí với migration nhé.'),
        ],
        'questions': [
            ('What does Hung ask Olivia to do?', ['Write a PR', 'Review his PR before lunch', 'Run a migration', 'Call a client'], 1, '"I was wondering if you could take a look at my PR before lunch."'),
            ('What does "Not at all" mean in this conversation?', ['He refuses.', 'He doesn\'t mind at all.', 'He is angry.', 'He didn\'t hear.'], 1, 'Trả lời "Would you mind…?" bằng "Not at all" = sẵn lòng.'),
            ('What does Olivia suggest about the database change?', ['Cancel it', 'Run it on staging first', 'Ask the client', 'Do it at night'], 1, '"It might be worth running it on staging first."'),
            ('Why does Olivia want to move the sync?', ['She is tired.', 'She has a client call at two.', 'Hung is busy.', 'The room is booked.'], 1, '"I have a client call at two."'),
        ],
    },
    'speaking': {
        'tips': ['Nghe lại các bản ghi tuần 6 (trang Ghi âm). Chọn 5 câu nghe cộc hoặc sai.', 'Sửa lại theo bảng "thẳng → mềm", rồi ghi âm 5 câu mới.'],
        'prompts': [
            ('Make these polite: "Send me the report." / "Explain this to me." / "Why is it late?"', 'Could you… / Would you mind… / Just wanted to check…'),
            ('Disagree politely with a colleague who wants to rewrite the whole app.', 'I see what you mean. However… Maybe we could…'),
            ('Ask your manager for a day off next Friday.', 'I was wondering if…'),
        ],
        'model': (
            "Hi Minh, could you send me the latest report when you get a chance? "
            "Also, would you mind explaining the new caching logic to me? I'm not sure I understand it fully. "
            "And just wanted to check on the invoice feature. Is it still on track for Friday? "
            "About the rewrite: I see what you mean, the old code is messy. However, a full rewrite might take months. Maybe we could start by refactoring the worst module first? "
            "Oh, and I was wondering if I could take next Friday off. I've finished my tasks for the sprint.",
            'Chào Minh, bạn gửi giúp mình báo cáo mới nhất khi rảnh nhé? '
            'Thêm nữa, bạn có phiền giải thích cho mình logic cache mới không? Mình chưa chắc đã hiểu hết. '
            'Và mình chỉ muốn hỏi về tính năng hóa đơn. Vẫn kịp thứ Sáu chứ? '
            'Về việc viết lại: mình hiểu ý bạn, code cũ khá lộn xộn. Tuy nhiên, viết lại toàn bộ có thể mất vài tháng. Có lẽ chúng ta bắt đầu bằng việc tái cấu trúc module tệ nhất trước? '
            'À, không biết mình có thể nghỉ thứ Sáu tuần sau không. Mình đã xong việc của sprint rồi.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Direct vs indirect communication',
        'text': [
            'Cultures differ in how directly people say things. In some countries, such as the Netherlands or Germany, colleagues often give very direct feedback: "This doesn\'t work." In others, including Vietnam, Japan and the UK, people tend to be more indirect: "It might be worth having another look at this."',
            'Neither style is wrong, but misunderstandings happen when the two meet. A direct speaker may sound rude to an indirect listener. An indirect speaker may sound unclear, and the important message may be missed completely.',
            'In international teams, a good rule is to be polite in form but clear in content. Use softeners like "could you" or "I was wondering", but make sure the key information is impossible to misunderstand: the problem, the deadline, the decision you need.',
        ],
        'vi': 'Các nền văn hóa khác nhau về mức độ nói thẳng. Ở Hà Lan, Đức, đồng nghiệp hay góp ý rất thẳng; ở Việt Nam, Nhật, Anh, người ta gián tiếp hơn. Không kiểu nào sai, nhưng hiểu lầm xảy ra khi hai kiểu gặp nhau: người nói thẳng có vẻ thô lỗ, người nói gián tiếp có vẻ mơ hồ và thông điệp chính bị bỏ lỡ. Quy tắc trong team quốc tế: lịch sự về hình thức nhưng rõ ràng về nội dung.',
        'questions': [
            ('Which countries are described as more indirect?', ['The Netherlands and Germany', 'Vietnam, Japan and the UK', 'Only Vietnam', 'All countries'], 1, 'Đoạn 1.'),
            ('What problem can an indirect speaker have?', ['Sounding rude', 'The key message may be missed', 'Talking too much', 'Using slang'], 1, 'Đoạn 2.'),
            ('What is the "good rule" for international teams?', ['Always be direct', 'Polite in form, clear in content', 'Never give feedback', 'Only write, never speak'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 5 câu bạn đã nói chưa tự nhiên trong tuần (từ bản ghi âm) và bản đã sửa bên cạnh. Sau đó viết lại 3 tin nhắn "cộc" sau cho lịch sự: "Fix this bug today." / "I need the password." / "Why no reply?"',
        'tips': ['Dạng: Tôi nói → Tự nhiên hơn.'],
        'model': "My 5 sentences:\n1. \"I am finish the page yesterday\" → \"I finished the page yesterday.\"\n2. \"Give me more time\" → \"Is there any flexibility on the deadline?\"\n3. \"You must review my code\" → \"Would you mind reviewing my PR today?\"\n4. \"I don't understand what you say\" → \"Sorry, could you clarify what you mean by…?\"\n5. \"This is impossible\" → \"I'm not sure that's realistic. Maybe we could phase it?\"\n\nRewritten messages:\n• \"Fix this bug today.\" → \"Would it be possible to fix this bug today? The client is waiting for it.\"\n• \"I need the password.\" → \"Could you send me the password for the staging server when you get a chance?\"\n• \"Why no reply?\" → \"Just wanted to follow up on my message from Monday.\"",
        'min_words': 80,
    },
    'quiz': [
        ('Lịch sự nhất:', ['Send me the file.', 'Could you send me the file when you get a chance?', 'File, please now.', 'I want the file.'], 1, 'Câu hỏi + "when you get a chance".'),
        ('"Would you mind ___ the door?"', ['close', 'closing', 'to close', 'closed'], 1, 'Would you mind + V-ing.'),
        ('"Would you mind helping me?" — Đồng ý giúp, bạn trả lời:', ['Yes, I mind.', 'No, not at all.', 'Yes, I would.', 'I mind not.'], 1, '"No, not at all" = không phiền gì.'),
        ('"I ___ wondering if you could help."', ['am', 'was', 'were', 'be'], 1, 'Lùi thì "was wondering" lịch sự hơn.'),
        ('"It might be worth ___ the logs."', ['check', 'checking', 'to check', 'checked'], 1, 'worth + V-ing.'),
        ('"Sorry I\'m late!" — "___!"', ['No worries', 'No worry', 'Not worries', 'Don\'t worries'], 0, 'No worries.'),
        ('Nhắc lịch sự khi chưa được trả lời:', ['Why no reply?', 'Just wanted to follow up on my email.', 'Answer me.', 'Hello???'], 1, 'Just wanted to…'),
        ('Phản đối lịch sự:', ['Your idea is bad.', "I see what you mean. However, maybe we could…", 'No way.', 'Wrong.'], 1, 'Ghi nhận rồi đề xuất.'),
        ('"I\'d ___ fix it properly than rush it."', ['rather', 'better', 'prefer', 'like'], 0, "I'd rather… than…"),
        ('Quy tắc giao tiếp trong team quốc tế:', ['Luôn nói thẳng', 'Lịch sự về hình thức, rõ ràng về nội dung', 'Tránh mọi góp ý', 'Chỉ dùng email'], 1, 'Polite in form, clear in content.'),
    ],
}

WEEK = {
    'title': 'Nói trong công việc',
    'title_en': 'Speaking at Work',
    'goal': 'Tham gia daily standup, code review và họp nhóm bằng tiếng Anh một cách tự tin.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
