"""Tuần 2 — Thì nâng cao và câu phức."""

DAY1 = {
    'title': 'Câu điều kiện loại 1 và 2',
    'title_en': 'First and Second Conditionals',
    'goal': 'Dùng câu điều kiện để nói về tình huống có thật trong công việc (loại 1) và tình huống giả định (loại 2); biết dùng unless, in case, otherwise.',
    'tasks': [
        'Học 14 từ về xử lý sự cố.',
        'Ôn cấu trúc câu điều kiện loại 0, 1, 2 và các từ thay thế "if".',
        'Nghe hội thoại "Friday deployment" và trả lời câu hỏi.',
        'Trả lời 3 câu hỏi "What would you do if…?" và ghi âm.',
        'Viết 6 câu điều kiện loại 1 và 4 câu loại 2.',
    ],
    'product': '6 câu điều kiện loại 1; 4 câu điều kiện loại 2; Bản ghi âm trả lời câu hỏi giả định',
    'warmup': [
        ('If the build fails, I will check the logs.', 'Nếu bản build lỗi, tôi sẽ kiểm tra log.'),
        ('If I had more time, I would write more tests.', 'Nếu có nhiều thời gian hơn, tôi sẽ viết thêm test.'),
        ("We won't release it unless the tests pass.", 'Chúng ta sẽ không phát hành trừ khi test chạy qua.'),
        ('What would you do if the server went down?', 'Bạn sẽ làm gì nếu máy chủ bị sập?'),
        ("Let's make a backup in case something goes wrong.", 'Hãy sao lưu phòng khi có gì trục trặc.'),
        ('If you heat ice, it melts.', 'Nếu bạn làm nóng đá, nó tan chảy.'),
    ],
    'vocab': [
        ('fail', '/feɪl/', 'verb', 'thất bại, bị lỗi', 'The payment request failed three times.', 'Yêu cầu thanh toán thất bại ba lần.'),
        ('crash', '/kræʃ/', 'verb / n', 'bị sập, treo; sự cố sập', 'The app crashes when you upload a large file.', 'Ứng dụng bị sập khi bạn tải lên file lớn.'),
        ('issue', '/ˈɪʃuː/', 'n', 'vấn đề, lỗi', "We're looking into the login issue.", 'Chúng tôi đang xem xét vấn đề đăng nhập.'),
        ('retry', '/ˌriːˈtraɪ/', 'verb', 'thử lại', 'The system will retry after five seconds.', 'Hệ thống sẽ thử lại sau năm giây.'),
        ('backup', '/ˈbækʌp/', 'n', 'bản sao lưu', 'Do we have a backup of the database?', 'Chúng ta có bản sao lưu cơ sở dữ liệu không?'),
        ('solution', '/səˈluːʃn/', 'n', 'giải pháp', "I think I've found a better solution.", 'Tôi nghĩ tôi đã tìm ra giải pháp tốt hơn.'),
        ('risk', '/rɪsk/', 'n', 'rủi ro', 'Deploying on Friday is a big risk.', 'Triển khai vào thứ Sáu là một rủi ro lớn.'),
        ('prevent', '/prɪˈvent/', 'verb', 'ngăn chặn, phòng ngừa', 'Code reviews help prevent bugs.', 'Review code giúp phòng ngừa lỗi.'),
        ('handle', '/ˈhændl/', 'verb', 'xử lý, đảm đương', 'Our server can handle a thousand requests per second.', 'Máy chủ của chúng tôi xử lý được một nghìn request mỗi giây.'),
        ('workaround', '/ˈwɜːkəraʊnd/', 'n', 'cách xử lý tạm, đi vòng', "There's no fix yet, but there is a workaround.", 'Chưa có bản sửa, nhưng có cách xử lý tạm.'),
        ('unless', '/ənˈles/', 'conj', 'trừ khi', "Don't call me unless it's urgent.", 'Đừng gọi tôi trừ khi có việc gấp.'),
        ('in case', '/ɪn keɪs/', 'conj', 'phòng khi', 'Take an umbrella in case it rains.', 'Mang ô phòng khi trời mưa.'),
        ('otherwise', '/ˈʌðəwaɪz/', 'adv', 'nếu không thì', 'Save your work often; otherwise, you might lose it.', 'Hãy lưu bài thường xuyên; nếu không, bạn có thể mất nó.'),
        ('as long as', '/æz lɒŋ æz/', 'conj', 'miễn là', "You can work from home as long as you join the stand-up.", 'Bạn có thể làm ở nhà miễn là bạn tham gia stand-up.'),
    ],
    'lesson': """
<h3>1. Ba loại câu điều kiện hay dùng nhất</h3>
<table class="table">
<tr><th>Loại</th><th>Cấu trúc</th><th>Dùng khi</th><th>Ví dụ</th></tr>
<tr><td><b>0</b></td><td>If + hiện tại đơn, hiện tại đơn</td><td>Sự thật, quy luật luôn đúng</td><td><span class="say">If you press this button, the app restarts.</span></td></tr>
<tr><td><b>1</b></td><td>If + hiện tại đơn, <b>will</b> + V</td><td>Có thể xảy ra thật ở hiện tại/tương lai</td><td><span class="say">If the build fails, I will check the logs.</span></td></tr>
<tr><td><b>2</b></td><td>If + quá khứ đơn, <b>would</b> + V</td><td>Giả định, không có thật hoặc khó xảy ra</td><td><span class="say">If I had more time, I would write tests.</span></td></tr>
</table>
<div class="note"><b>Mẹo nhớ:</b> loại 1 = "chuyện thật, sắp tới" → <i>will</i>. Loại 2 = "giá mà / giả sử" → lùi thì về quá khứ + <i>would</i>. Với "be" ở loại 2, văn viết dùng <b>were</b> cho mọi ngôi: <span class="say">If I were you, I would ask for help.</span></div>

<h3>2. Không dùng "will" trong mệnh đề If</h3>
<div class="fix"><s>If it will rain tomorrow, we will cancel the trip.</s><span class="en">If it rains tomorrow, we will cancel the trip.</span></div>
<div class="fix"><s>If I would have money, I would buy a new laptop.</s><span class="en">If I had money, I would buy a new laptop.</span></div>

<h3>3. Những từ thay thế "if"</h3>
<table class="table">
<tr><th>Từ</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>unless</b></td><td>trừ khi (= if … not)</td><td><span class="say">We won't merge it unless someone reviews it.</span></td></tr>
<tr><td><b>as long as</b></td><td>miễn là</td><td><span class="say">It's fine as long as the tests pass.</span></td></tr>
<tr><td><b>in case</b></td><td>phòng khi</td><td><span class="say">I'll save a copy in case the upload fails.</span></td></tr>
<tr><td><b>otherwise</b></td><td>nếu không thì</td><td><span class="say">Fix it today. Otherwise, the client will complain.</span></td></tr>
<tr><td><b>What if…?</b></td><td>Nếu… thì sao?</td><td><span class="say">What if the API is down during the demo?</span></td></tr>
</table>

<h3>4. Câu điều kiện trong công việc hằng ngày</h3>
<div class="ex"><span class="en">If you have any questions, just let me know.</span><span class="vi">Câu kết email cực kỳ phổ biến.</span></div>
<div class="ex"><span class="en">If we cut this feature, we will finish on time.</span><span class="vi">Đề xuất phương án khi thương lượng deadline.</span></div>
<div class="ex"><span class="en">If I were in your position, I would talk to the client first.</span><span class="vi">Cho lời khuyên một cách lịch sự.</span></div>
<div class="ex"><span class="en">It would be great if you could review my PR today.</span><span class="vi">Nhờ vả lịch sự bằng loại 2.</span></div>
""",
    'phrases': [
        ('If you have any questions, feel free to ask.', 'Nếu có câu hỏi gì, cứ thoải mái hỏi nhé.'),
        ('It would be great if you could…', 'Sẽ rất tốt nếu bạn có thể…'),
        ('If I were you, I would…', 'Nếu tôi là bạn, tôi sẽ…'),
        ("What if we try a different approach?", 'Nếu ta thử một cách khác thì sao?'),
        ("Just in case, let's keep a backup.", 'Để phòng hờ, hãy giữ một bản sao lưu.'),
    ],
    'listening': {
        'title': 'Friday deployment',
        'intro': 'Chiều thứ Sáu, hai lập trình viên bàn xem có nên triển khai bản cập nhật lớn lên production hay không.',
        'speakers': {'A': ('Kevin', 'guy'), 'B': ('Hana', 'emma')},
        'lines': [
            ('A', 'Hana, the new checkout is ready. Should we deploy it today?', 'Hana, trang thanh toán mới xong rồi. Mình triển khai luôn hôm nay nhé?'),
            ('B', "It's four o'clock on a Friday. If something breaks, nobody will be here to fix it.", 'Bốn giờ chiều thứ Sáu rồi. Nếu có gì hỏng, chẳng ai ở đây để sửa đâu.'),
            ('A', 'But the client wants it before the weekend sale.', 'Nhưng khách hàng muốn có nó trước đợt sale cuối tuần.'),
            ('B', 'I understand. What if we deploy it behind a feature flag?', 'Mình hiểu. Hay là triển khai nhưng ẩn sau feature flag?'),
            ('A', 'Good idea. If we turn the flag on for just ten percent of users, the risk will be much lower.', 'Ý hay. Nếu bật flag cho mười phần trăm người dùng thôi thì rủi ro sẽ thấp hơn nhiều.'),
            ('B', "Exactly. And we should make a database backup first, just in case.", 'Chính xác. Và nên sao lưu cơ sở dữ liệu trước, để phòng hờ.'),
            ('A', "Okay. But honestly, if I were the manager, I wouldn't allow Friday releases at all.", 'Được. Nhưng thật lòng, nếu mình là quản lý, mình sẽ không cho phát hành vào thứ Sáu luôn.'),
            ('B', "Ha, me neither. If we had more people on call, it would be different.", 'Ha, mình cũng vậy. Nếu có nhiều người trực hơn thì đã khác.'),
            ('A', "So, we'll deploy at four thirty unless the tests fail. Agreed?", 'Vậy bốn rưỡi mình triển khai, trừ khi test lỗi. Đồng ý chứ?'),
            ('B', "Agreed. And if there are any errors, we'll turn the flag off immediately.", 'Đồng ý. Và nếu có lỗi, mình tắt flag ngay lập tức.'),
        ],
        'questions': [
            ("Why is Hana worried about deploying today?", ['The tests are failing.', 'Nobody will be there if something breaks.', 'The client does not want it.', 'The feature is not finished.'], 1, '"If something breaks, nobody will be here to fix it."'),
            ('What does Hana suggest?', ['Waiting until Monday', 'Deploying behind a feature flag', 'Asking the client', 'Hiring more people'], 1, '"What if we deploy it behind a feature flag?"'),
            ('What will they do first?', ['Call the manager', 'Make a database backup', 'Turn off the flag', 'Write more tests'], 1, '"we should make a database backup first, just in case."'),
            ('When will they NOT deploy?', ['If the tests fail', 'If the client calls', 'If it is after five', 'If the manager is away'], 0, '"…unless the tests fail" = trừ khi test lỗi.'),
        ],
    },
    'speaking': {
        'tips': ['Loại 1 cho kế hoạch thật, loại 2 cho giả định. Nhớ: If + quá khứ → would.', 'Mỗi câu trả lời: câu điều kiện + 2 câu giải thích lý do.'],
        'prompts': [
            ('What will you do if you finish all your tasks early this week?', 'Loại 1: kế hoạch thật.'),
            ('What would you do if your code broke production at midnight?', 'Loại 2: giả định.'),
            ('If you could work for any company in the world, which one would you choose and why?', 'Loại 2: mơ ước.'),
            ('If you had one extra hour every day, how would you use it?', 'Loại 2.'),
        ],
        'model': (
            "If I could work for any company in the world, I would probably choose a small product company rather than a big tech giant. "
            "If I worked in a small team, I would have more responsibility and I would learn faster. "
            "I would also like a company that allows remote work, because if I didn't have to commute, I would have more time for my family. "
            "Of course, if I joined a startup, the salary might be lower. But if the product were interesting, I wouldn't mind. "
            "For now, if I finish my tasks early this week, I will spend the extra time preparing for interviews.",
            'Nếu được làm cho bất kỳ công ty nào trên thế giới, có lẽ tôi sẽ chọn một công ty sản phẩm nhỏ thay vì một ông lớn công nghệ. '
            'Nếu làm trong một team nhỏ, tôi sẽ có nhiều trách nhiệm hơn và học nhanh hơn. '
            'Tôi cũng thích công ty cho làm từ xa, vì nếu không phải đi lại, tôi sẽ có nhiều thời gian cho gia đình hơn. '
            'Dĩ nhiên, nếu vào startup, lương có thể thấp hơn. Nhưng nếu sản phẩm thú vị thì tôi không ngại. '
            'Còn hiện tại, nếu tuần này xong việc sớm, tôi sẽ dành thời gian dư để chuẩn bị phỏng vấn.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Planning for failure',
        'text': [
            'Good engineering teams do not only ask, "Will this work?" They also ask, "What will happen if it fails?" This simple question has saved many companies from disaster.',
            'Before a big release, some teams hold a short meeting called a "pre-mortem". They imagine that the release has already failed, and they try to explain why. If the database migration takes too long, what will we do? If users cannot log in, who will be called?',
            'For each risk, the team writes down a plan. If the plan is simple, such as turning off a feature flag, it can be done in seconds. If there is no plan, people usually panic and make the problem worse.',
            'A pre-mortem takes about thirty minutes. Compared with the hours that a real incident can cost, it is one of the cheapest investments a team can make.',
        ],
        'vi': 'Các team giỏi không chỉ hỏi "Cái này có chạy không?" mà còn hỏi "Nếu nó lỗi thì sao?". Trước khi phát hành lớn, một số team họp "pre-mortem": tưởng tượng bản phát hành đã thất bại và tìm lý do. Với mỗi rủi ro, họ viết sẵn kế hoạch xử lý. Có kế hoạch đơn giản như tắt feature flag thì xử lý trong vài giây; không có kế hoạch thì mọi người dễ hoảng và làm mọi chuyện tệ hơn. Một buổi pre-mortem chỉ mất khoảng 30 phút — rẻ hơn rất nhiều so với hàng giờ xử lý sự cố thật.',
        'questions': [
            ('What do teams imagine in a pre-mortem?', ['That the release was a big success', 'That the release has already failed', 'That users love the feature', 'That the deadline is moved'], 1, 'Đoạn 2: "They imagine that the release has already failed".'),
            ('According to the text, what happens if there is no plan?', ['The release is cancelled.', 'People panic and make it worse.', 'The manager fixes it.', 'Nothing happens.'], 1, 'Đoạn 3: "people usually panic and make the problem worse".'),
            ('How long does a pre-mortem usually take?', ['Five minutes', 'About thirty minutes', 'A few hours', 'A whole day'], 1, 'Đoạn 4.'),
        ],
    },
    'writing': {
        'task': 'Viết 6 câu điều kiện loại 1 về công việc thật của bạn (kế hoạch, rủi ro) và 4 câu loại 2 về các tình huống giả định.',
        'tips': ['Dùng ít nhất một câu với unless và một câu với in case.', 'Không dùng will/would trong mệnh đề If.'],
        'model': "Type 1:\nIf the client approves the design, we will start coding on Monday.\nIf the tests pass, I'll merge the pull request this afternoon.\nI'll ask Minh for help if I can't fix the bug by lunchtime.\nWe won't deploy unless the QA team gives us the green light.\nI'll keep my laptop with me in case there's an urgent issue.\nIf you need the report, I'll send it before five.\n\nType 2:\nIf I had more time, I would learn Rust.\nIf our team were bigger, we would finish the project faster.\nIf I worked remotely, I would move back to my hometown.\nIf I were the CTO, I would ban meetings on Wednesday mornings.",
        'min_words': 80,
    },
    'quiz': [
        ('If the server ___ down, we will lose customers.', ['go', 'goes', 'will go', 'went'], 1, 'Loại 1: If + hiện tại đơn; "the server" số ít → goes.'),
        ('If I ___ you, I would talk to the manager.', ['am', 'was being', 'were', 'will be'], 2, 'Loại 2 với "be": If I were you…'),
        ('We ___ finish on time if we cut this feature.', ['will', 'would have', 'are', 'had'], 0, 'Loại 1 (khả năng có thật): will + V.'),
        ('If I had more money, I ___ a bigger monitor.', ['will buy', 'buy', 'would buy', 'bought'], 2, 'Loại 2: would + V.'),
        ("I won't sign the contract ___ they change the deadline.", ['if', 'unless', 'in case', 'as long as'], 1, '"unless" = trừ khi.'),
        ("Bring your charger ___ the meeting runs late.", ['unless', 'otherwise', 'in case', 'if not'], 2, '"in case" = phòng khi.'),
        ('You can use my laptop ___ you are careful with it.', ['unless', 'as long as', 'in case', 'otherwise'], 1, '"as long as" = miễn là.'),
        ('If you mix red and blue, you ___ purple.', ['get', 'will got', 'would get', 'got'], 0, 'Loại 0: sự thật luôn đúng → hiện tại đơn ở cả hai vế.'),
        ('What would you do if your boss ___ you to work at weekends?', ['asks', 'asked', 'will ask', 'has asked'], 1, 'Loại 2: If + quá khứ đơn.'),
        ('Finish the report today; ___, the client will be upset.', ['unless', 'otherwise', 'in case', 'if'], 1, '"otherwise" = nếu không thì.'),
        ("If it ___ tomorrow, we'll have the team lunch inside.", ['will rain', 'rains', 'rained', 'would rain'], 1, 'Không dùng will sau If.'),
        ('It would be great if you ___ send me the file today.', ['can', 'could', 'will', 'are'], 1, 'Nhờ vả lịch sự: It would be great if you could…'),
    ],
}

DAY2 = {
    'title': 'Mệnh đề quan hệ',
    'title_en': 'Relative Clauses',
    'goal': 'Dùng who, which, that, where, whose để nối câu và mô tả người, sản phẩm, dự án; biết rút gọn mệnh đề quan hệ cho câu gọn hơn.',
    'tasks': [
        'Học 14 từ để mô tả sản phẩm và ứng dụng.',
        'Ôn đại từ quan hệ, mệnh đề xác định và không xác định, cách rút gọn.',
        'Nghe buổi demo sản phẩm và trả lời câu hỏi.',
        'Mô tả bằng lời một ứng dụng bạn dùng hằng ngày.',
        'Viết 8 câu mô tả một dự án bạn đã làm.',
    ],
    'product': '8 câu mô tả một dự án có dùng mệnh đề quan hệ; Bản ghi âm mô tả một ứng dụng',
    'warmup': [
        ('This is the dashboard which shows all our sales.', 'Đây là bảng điều khiển hiển thị toàn bộ doanh số.'),
        ('Anna is the designer who created our new logo.', 'Anna là nhà thiết kế đã tạo logo mới của chúng tôi.'),
        ('That is the office where I had my first job.', 'Đó là văn phòng nơi tôi có công việc đầu tiên.'),
        ('The app that I use most is my calendar.', 'Ứng dụng tôi dùng nhiều nhất là lịch.'),
        ("He's the developer whose code is always clean.", 'Anh ấy là lập trình viên có code luôn sạch sẽ.'),
        ('Users who sign up today get a free month.', 'Người dùng đăng ký hôm nay được miễn phí một tháng.'),
    ],
    'vocab': [
        ('platform', '/ˈplætfɔːm/', 'n', 'nền tảng', "It's a platform that connects drivers with passengers.", 'Đó là nền tảng kết nối tài xế với hành khách.'),
        ('user-friendly', '/ˌjuːzə ˈfrendli/', 'adj', 'dễ sử dụng', 'The new interface is much more user-friendly.', 'Giao diện mới dễ dùng hơn nhiều.'),
        ('dashboard', '/ˈdæʃbɔːd/', 'n', 'bảng điều khiển, trang tổng quan', 'Managers check the dashboard every morning.', 'Các quản lý xem trang tổng quan mỗi sáng.'),
        ('customer', '/ˈkʌstəmə/', 'n', 'khách hàng (mua hàng)', 'Customers can track their orders in real time.', 'Khách hàng có thể theo dõi đơn hàng theo thời gian thực.'),
        ('allow', '/əˈlaʊ/', 'verb', 'cho phép', 'The app allows users to pay by QR code.', 'Ứng dụng cho phép người dùng thanh toán bằng mã QR.'),
        ('enable', '/ɪˈneɪbl/', 'verb', 'giúp có thể, bật (tính năng)', 'This tool enables teams to work faster.', 'Công cụ này giúp các team làm việc nhanh hơn.'),
        ('integrate', '/ˈɪntɪɡreɪt/', 'verb', 'tích hợp', 'We integrated the app with Google Calendar.', 'Chúng tôi đã tích hợp ứng dụng với Google Calendar.'),
        ('notification', '/ˌnəʊtɪfɪˈkeɪʃn/', 'n', 'thông báo', 'Users get a notification when their order ships.', 'Người dùng nhận thông báo khi đơn hàng được gửi đi.'),
        ('subscription', '/səbˈskrɪpʃn/', 'n', 'gói đăng ký (trả phí định kỳ)', 'The monthly subscription costs five dollars.', 'Gói đăng ký hằng tháng giá năm đô la.'),
        ('feedback', '/ˈfiːdbæk/', 'n', 'phản hồi, góp ý', 'We changed the menu based on user feedback.', 'Chúng tôi đổi menu dựa trên phản hồi của người dùng.'),
        ('target user', '/ˈtɑːɡɪt ˈjuːzə/', 'n', 'người dùng mục tiêu', 'Our target users are small business owners.', 'Người dùng mục tiêu của chúng tôi là chủ doanh nghiệp nhỏ.'),
        ('main', '/meɪn/', 'adj', 'chính', 'The main goal is to save people time.', 'Mục tiêu chính là tiết kiệm thời gian cho mọi người.'),
        ('interface', '/ˈɪntəfeɪs/', 'n', 'giao diện', 'The interface works well on small screens.', 'Giao diện hoạt động tốt trên màn hình nhỏ.'),
        ('admin', '/ˈædmɪn/', 'n', 'quản trị viên; trang quản trị', 'Only admins can delete accounts.', 'Chỉ quản trị viên mới xóa được tài khoản.'),
    ],
    'lesson': """
<h3>1. Đại từ quan hệ</h3>
<table class="table">
<tr><th>Từ</th><th>Thay cho</th><th>Ví dụ</th></tr>
<tr><td><b>who</b></td><td>người</td><td><span class="say">She's the engineer who built our API.</span></td></tr>
<tr><td><b>which</b></td><td>vật, sự việc</td><td><span class="say">It's a tool which saves a lot of time.</span></td></tr>
<tr><td><b>that</b></td><td>người hoặc vật (mệnh đề xác định)</td><td><span class="say">The bug that you found is fixed.</span></td></tr>
<tr><td><b>where</b></td><td>nơi chốn</td><td><span class="say">This is the café where we hold our meetups.</span></td></tr>
<tr><td><b>whose</b></td><td>sở hữu (của ai/của cái gì)</td><td><span class="say">That's the client whose website crashed.</span></td></tr>
<tr><td><b>when</b></td><td>thời gian</td><td><span class="say">I remember the day when we launched.</span></td></tr>
</table>

<h3>2. Xác định và không xác định</h3>
<p><b>Mệnh đề xác định</b> (không có dấu phẩy) cho biết ta đang nói về <i>người/vật nào</i>. Thiếu nó câu sẽ không rõ nghĩa.</p>
<div class="ex"><span class="en">The developers who work on the mobile team are in Da Nang.</span><span class="vi">Chỉ những dev ở team mobile (không phải tất cả).</span></div>
<p><b>Mệnh đề không xác định</b> (có dấu phẩy) chỉ thêm thông tin phụ. Không dùng <i>that</i>.</p>
<div class="ex"><span class="en">Our CTO, who has twenty years of experience, joined last month.</span><span class="vi">Bỏ phần giữa hai dấu phẩy câu vẫn đủ nghĩa.</span></div>
<div class="fix"><s>Our app, that has 10,000 users, is free.</s><span class="en">Our app, which has 10,000 users, is free.</span></div>

<h3>3. Lược bỏ đại từ quan hệ</h3>
<p>Khi đại từ quan hệ là <b>tân ngữ</b> (theo sau là một chủ ngữ khác), ta có thể bỏ nó — văn nói rất hay dùng:</p>
<div class="ex"><span class="en">The app I use most is Notion.</span><span class="vi">= The app (that) I use most…</span></div>
<div class="ex"><span class="en">The person you need to talk to is Lan.</span></div>

<h3>4. Rút gọn mệnh đề quan hệ</h3>
<table class="table">
<tr><th>Đầy đủ</th><th>Rút gọn</th></tr>
<tr><td><span class="say">Users who sign up today get a discount.</span></td><td><span class="say">Users signing up today get a discount.</span> (chủ động → V-ing)</td></tr>
<tr><td><span class="say">The report which was sent yesterday has errors.</span></td><td><span class="say">The report sent yesterday has errors.</span> (bị động → V3)</td></tr>
<tr><td><span class="say">He was the first person who arrived.</span></td><td><span class="say">He was the first person to arrive.</span> (sau first/last/only → to V)</td></tr>
</table>
<div class="note"><b>Mô tả dự án:</b> <span class="say">I built a booking app which allows customers to reserve tables. The admin page, where owners manage bookings, was the hardest part.</span></div>
""",
    'phrases': [
        ("It's an app that helps people…", 'Đó là một ứng dụng giúp mọi người…'),
        ('The main feature, which users love, is…', 'Tính năng chính, thứ người dùng rất thích, là…'),
        ('Our target users are people who…', 'Người dùng mục tiêu là những người…'),
        ('The part I am most proud of is…', 'Phần tôi tự hào nhất là…'),
    ],
    'listening': {
        'title': 'A product demo',
        'intro': 'Trưởng nhóm sản phẩm giới thiệu ứng dụng quản lý chi tiêu cho một nhà đầu tư.',
        'speakers': {'A': ('Olivia', 'sonia'), 'B': ('Mr. Grant', 'ryan')},
        'lines': [
            ('A', "Thank you for joining us. Today I'll show you Pocket, an app that helps young people manage their money.", 'Cảm ơn ông đã tham gia. Hôm nay tôi sẽ giới thiệu Pocket, ứng dụng giúp người trẻ quản lý tiền.'),
            ('B', 'Who exactly are your target users?', 'Người dùng mục tiêu của các bạn chính xác là ai?'),
            ('A', 'Mainly students and young workers who have just started earning money.', 'Chủ yếu là sinh viên và người mới đi làm vừa bắt đầu có thu nhập.'),
            ('A', 'This is the home screen, which shows how much you have spent this month.', 'Đây là màn hình chính, hiển thị bạn đã tiêu bao nhiêu trong tháng.'),
            ('B', 'And where does the data come from?', 'Dữ liệu lấy từ đâu?'),
            ('A', 'Users connect their bank accounts, or they can add expenses by taking a photo of the receipt.', 'Người dùng liên kết tài khoản ngân hàng, hoặc thêm chi tiêu bằng cách chụp ảnh hóa đơn.'),
            ('A', 'The feature that users love most is the weekly challenge. For example, "spend less than fifty dollars on coffee".', 'Tính năng người dùng thích nhất là thử thách hằng tuần. Ví dụ: "tiêu dưới năm mươi đô cho cà phê".'),
            ('B', 'Interesting. How do you make money?', 'Thú vị đấy. Các bạn kiếm tiền bằng cách nào?'),
            ('A', 'There is a free version and a premium subscription, which costs three dollars a month.', 'Có bản miễn phí và gói premium giá ba đô mỗi tháng.'),
            ('B', 'And how many users do you have?', 'Các bạn có bao nhiêu người dùng?'),
            ('A', 'About forty thousand, most of whom found us through social media.', 'Khoảng bốn mươi nghìn, phần lớn biết đến chúng tôi qua mạng xã hội.'),
        ],
        'questions': [
            ('Who is the app for?', ['Retired people', 'Students and young workers', 'Bank employees', 'Small business owners'], 1, '"students and young workers who have just started earning money".'),
            ('What does the home screen show?', ['Bank news', 'Monthly spending', 'Weekly challenges', 'Friends\' expenses'], 1, '"which shows how much you have spent this month".'),
            ('Which feature do users love most?', ['Receipt photos', 'Bank connection', 'The weekly challenge', 'The premium version'], 2, '"The feature that users love most is the weekly challenge."'),
            ('How much is the premium subscription?', ['Free', 'Three dollars a month', 'Five dollars a month', 'Fifty dollars a year'], 1, '"…which costs three dollars a month."'),
        ],
    },
    'speaking': {
        'tips': ['Mô tả: Là gì → cho ai → tính năng chính → điều bạn thích/không thích.', 'Cố dùng ít nhất 4 mệnh đề quan hệ.'],
        'prompts': [
            ('Describe an app that you use every day.', 'It\'s an app which… / The feature that I like most is…'),
            ('Describe a person who has helped you in your career.', 'who / whose'),
            ('Describe the place where you usually work.', 'where'),
        ],
        'model': (
            "The app that I use most every day is Google Maps. It's a navigation app which shows you the fastest way to get somewhere. "
            "The feature I like most is the live traffic, which tells me which roads to avoid in the morning. "
            "It's also useful when I travel to cities where I don't know anyone, because it shows restaurants that other people recommend. "
            "The only thing that annoys me is the battery use. People who drive all day probably need a charger in the car.",
            'Ứng dụng tôi dùng nhiều nhất mỗi ngày là Google Maps. Đó là ứng dụng chỉ đường cho bạn biết cách nhanh nhất để đến nơi. '
            'Tính năng tôi thích nhất là tình trạng giao thông trực tiếp, cho tôi biết nên tránh đường nào vào buổi sáng. '
            'Nó cũng hữu ích khi tôi đến những thành phố mà tôi không quen ai, vì nó gợi ý nhà hàng được người khác đánh giá tốt. '
            'Điều duy nhất làm tôi khó chịu là tốn pin. Những người lái xe cả ngày chắc cần sạc trên xe.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Writing a good project description',
        'text': [
            'Recruiters who read hundreds of CVs every week usually spend only a few seconds on each project description. That is why your description needs to be short and clear.',
            'Start with one sentence that explains what the project is and who it is for. For example: "A booking system that helps small clinics manage appointments." Avoid long lists of technologies at the beginning; the reader first needs to understand the problem that you solved.',
            'Next, describe your role. Use action verbs and, if possible, numbers: "Built the REST API, which handles 5,000 bookings a day." Finally, mention one challenge that you overcame. A project which had no problems is not very interesting to read about.',
        ],
        'vi': 'Nhà tuyển dụng chỉ dành vài giây cho mỗi mô tả dự án nên nó cần ngắn và rõ. Câu đầu nêu dự án là gì, cho ai. Đừng mở đầu bằng danh sách công nghệ — người đọc cần hiểu vấn đề bạn giải quyết trước. Sau đó mô tả vai trò bằng động từ hành động và số liệu, rồi nêu một khó khăn bạn đã vượt qua.',
        'questions': [
            ('What should the first sentence of a project description do?', ['List the technologies', 'Explain what the project is and who it is for', 'Describe a challenge', 'Mention your salary'], 1, 'Đoạn 2.'),
            ('Why should you avoid a long list of technologies at the beginning?', ['Recruiters hate technology.', 'The reader first needs to understand the problem.', 'It makes the CV too long.', 'Technologies change quickly.'], 1, '"the reader first needs to understand the problem that you solved".'),
            ('In "a project which had no problems", what does "which" refer to?', ['the reader', 'a project', 'problems', 'a challenge'], 1, '"which" thay cho "a project".'),
        ],
    },
    'writing': {
        'task': 'Viết 8 câu mô tả một dự án bạn đã làm (hoặc một ứng dụng bạn thích), dùng ít nhất 6 mệnh đề quan hệ khác nhau (who, which, that, where, whose, rút gọn).',
        'tips': ['Câu 1: dự án là gì và cho ai.', 'Câu cuối: một khó khăn bạn đã vượt qua.'],
        'model': "Last year I worked on a booking system that helps small clinics manage appointments. The clinics, which are mostly in Hanoi, used to take bookings by phone. Patients who want to see a doctor can now choose a time online. I built the admin page, where receptionists can see all the bookings for the day. The doctor whose idea started the project gave us feedback every week. The feature patients use most is the SMS reminder. Reminders sent the day before reduced missed appointments by 30%. The hardest part was a bug which caused double bookings during busy hours.",
        'min_words': 80,
    },
    'quiz': [
        ('The engineer ___ fixed the bug is on holiday now.', ['which', 'who', 'where', 'whose'], 1, 'Chỉ người → who.'),
        ("This is the laptop ___ I bought last week.", ['who', 'where', 'which', 'whose'], 2, 'Chỉ vật → which/that.'),
        ('That is the café ___ we had our first team meeting.', ['which', 'where', 'who', 'when'], 1, 'Nơi chốn → where.'),
        ("He's the client ___ website we redesigned.", ['who', 'which', 'whose', 'that'], 2, 'Sở hữu (website của khách hàng) → whose.'),
        ('Our CEO, ___ started the company in 2015, will give a talk.', ['that', 'who', 'which', 'whom'], 1, 'Mệnh đề không xác định (có dấu phẩy) → không dùng that; chỉ người → who.'),
        ('Câu nào có thể bỏ đại từ quan hệ?', ['The man who called you is here.', 'The book that I am reading is great.', 'The app which crashed is old.', 'The girl who won is my sister.'], 1, '"that" là tân ngữ của "I am reading" → có thể bỏ: The book I am reading…'),
        ('Rút gọn: "The files which were uploaded yesterday are missing."', ['The files uploading yesterday are missing.', 'The files uploaded yesterday are missing.', 'The files upload yesterday are missing.', 'The files to upload yesterday are missing.'], 1, 'Bị động → dùng V3: uploaded.'),
        ('Rút gọn: "People who work remotely need good internet."', ['People worked remotely…', 'People working remotely…', 'People to work remotely…', 'People work remotely…'], 1, 'Chủ động → V-ing.'),
        ('She was the first person ___ the problem.', ['notice', 'noticed', 'to notice', 'noticing'], 2, 'Sau "the first/last/only" → to V.'),
        ('I still remember the day ___ I got my first salary.', ['which', 'where', 'when', 'who'], 2, 'Thời gian → when.'),
        ('The API, ___ handles all payments, needs to be updated.', ['that', 'which', 'who', 'where'], 1, 'Có dấu phẩy, chỉ vật → which.'),
        ('Everything ___ he said was true.', ['what', 'that', 'who', 'where'], 1, 'Sau everything/something/anything → that (không dùng what).'),
    ],
}

DAY3 = {
    'title': 'Câu bị động',
    'title_en': 'The Passive Voice',
    'goal': 'Dùng câu bị động ở các thì khi mô tả quy trình và tài liệu kỹ thuật; biết khi nào bị động tự nhiên hơn chủ động.',
    'tasks': [
        'Học 14 động từ về quy trình kỹ thuật.',
        'Ôn cấu trúc bị động ở các thì và với động từ khuyết thiếu.',
        'Nghe buổi hướng dẫn quy trình release cho người mới.',
        'Mô tả bằng lời một quy trình ở công ty bạn.',
        'Viết lại 10 câu chủ động thành bị động.',
    ],
    'product': '10 câu chủ động đã chuyển sang bị động; Bản ghi âm mô tả một quy trình',
    'warmup': [
        ('The API is deployed on AWS every Friday.', 'API được triển khai lên AWS vào mỗi thứ Sáu.'),
        ('All passwords are encrypted.', 'Mọi mật khẩu đều được mã hóa.'),
        ('The bug was reported by a customer.', 'Lỗi được một khách hàng báo cáo.'),
        ('The new version has just been released.', 'Phiên bản mới vừa được phát hành.'),
        ('Every pull request must be reviewed by two people.', 'Mọi pull request phải được hai người review.'),
        ('The meeting has been moved to Thursday.', 'Cuộc họp đã được dời sang thứ Năm.'),
    ],
    'vocab': [
        ('deploy', '/dɪˈplɔɪ/', 'verb', 'triển khai (lên máy chủ)', 'The app is deployed automatically after each merge.', 'Ứng dụng được triển khai tự động sau mỗi lần merge.'),
        ('store', '/stɔː/', 'verb', 'lưu trữ', 'User photos are stored in the cloud.', 'Ảnh người dùng được lưu trên đám mây.'),
        ('generate', '/ˈdʒenəreɪt/', 'verb', 'tạo ra, sinh ra', 'The invoices are generated at midnight.', 'Hóa đơn được tạo lúc nửa đêm.'),
        ('trigger', '/ˈtrɪɡə/', 'verb / n', 'kích hoạt; cái kích hoạt', 'The build is triggered by every push.', 'Bản build được kích hoạt bởi mỗi lần push.'),
        ('review', '/rɪˈvjuː/', 'verb / n', 'xem xét, đánh giá; bản review', 'Your code will be reviewed tomorrow.', 'Code của bạn sẽ được review vào ngày mai.'),
        ('approve', '/əˈpruːv/', 'verb', 'phê duyệt', 'The budget was approved last week.', 'Ngân sách đã được phê duyệt tuần trước.'),
        ('encrypt', '/ɪnˈkrɪpt/', 'verb', 'mã hóa', 'All data is encrypted before it is saved.', 'Mọi dữ liệu được mã hóa trước khi lưu.'),
        ('log', '/lɒɡ/', 'verb / n', 'ghi nhật ký; nhật ký (log)', 'Every error is logged with a timestamp.', 'Mọi lỗi đều được ghi lại kèm thời gian.'),
        ('back up', '/bæk ʌp/', 'phrasal verb', 'sao lưu', 'The database is backed up every six hours.', 'Cơ sở dữ liệu được sao lưu mỗi sáu tiếng.'),
        ('require', '/rɪˈkwaɪə/', 'verb', 'yêu cầu, đòi hỏi', 'Two-factor authentication is required for all admins.', 'Xác thực hai lớp là bắt buộc với mọi quản trị viên.'),
        ('maintain', '/meɪnˈteɪn/', 'verb', 'bảo trì, duy trì', 'This library is no longer maintained.', 'Thư viện này không còn được bảo trì nữa.'),
        ('assign', '/əˈsaɪn/', 'verb', 'giao (việc), phân công', 'The ticket was assigned to me this morning.', 'Ticket đã được giao cho tôi sáng nay.'),
        ('process', '/ˈprəʊses/', 'n / verb', 'quy trình; xử lý', 'Orders are processed within 24 hours.', 'Đơn hàng được xử lý trong vòng 24 giờ.'),
        ('update', '/ʌpˈdeɪt/', 'verb', 'cập nhật', 'The documentation is updated with every release.', 'Tài liệu được cập nhật với mỗi lần phát hành.'),
    ],
    'lesson': """
<h3>1. Công thức: be + V3 (past participle)</h3>
<table class="table">
<tr><th>Thì</th><th>Bị động</th><th>Ví dụ</th></tr>
<tr><td>Hiện tại đơn</td><td>am/is/are + V3</td><td><span class="say">The servers are monitored 24/7.</span></td></tr>
<tr><td>Hiện tại tiếp diễn</td><td>am/is/are being + V3</td><td><span class="say">Your request is being processed.</span></td></tr>
<tr><td>Quá khứ đơn</td><td>was/were + V3</td><td><span class="say">The bug was fixed yesterday.</span></td></tr>
<tr><td>Hiện tại hoàn thành</td><td>have/has been + V3</td><td><span class="say">The meeting has been cancelled.</span></td></tr>
<tr><td>Tương lai</td><td>will be + V3</td><td><span class="say">You will be notified by email.</span></td></tr>
<tr><td>Động từ khuyết thiếu</td><td>must/should/can + be + V3</td><td><span class="say">This file should not be deleted.</span></td></tr>
</table>

<h3>2. Khi nào dùng bị động?</h3>
<ul>
<li><b>Không biết hoặc không quan trọng ai làm:</b> <span class="say">The data is backed up every night.</span></li>
<li><b>Tập trung vào hành động/kết quả</b> — rất phổ biến trong tài liệu kỹ thuật: <span class="say">The token is stored in a cookie.</span></li>
<li><b>Lịch sự, tránh đổ lỗi:</b> <span class="say">A mistake was made in the report.</span> nghe nhẹ nhàng hơn <i>You made a mistake.</i></li>
</ul>
<p>Muốn nói ai làm thì thêm <b>by</b>: <span class="say">The app was designed by a team in Berlin.</span></p>

<h3>3. Chuyển chủ động → bị động</h3>
<div class="ex"><span class="en">Active: The QA team tests every release.</span></div>
<div class="ex"><span class="en">Passive: Every release is tested by the QA team.</span><span class="vi">Tân ngữ (every release) lên làm chủ ngữ; động từ thành be + V3, giữ nguyên thì.</span></div>

<h3>4. Lỗi hay gặp</h3>
<div class="fix"><s>The email was send yesterday.</s><span class="en">The email was sent yesterday.</span><span class="vi">Dùng V3, không phải V nguyên mẫu.</span></div>
<div class="fix"><s>The problem was happened last night.</s><span class="en">The problem happened last night.</span><span class="vi">happen, occur, arrive, die… là nội động từ, không có bị động.</span></div>
<div class="fix"><s>The feature is develop by our team.</s><span class="en">The feature is developed by our team.</span></div>

<h3>5. Mẫu câu trong tài liệu</h3>
<div class="ex"><span class="en">It is recommended that you update to the latest version.</span><span class="vi">Khuyến nghị bạn nên cập nhật bản mới nhất.</span></div>
<div class="ex"><span class="en">This method is deprecated and will be removed in version 3.</span><span class="vi">Phương thức này đã lỗi thời và sẽ bị gỡ ở phiên bản 3.</span></div>
""",
    'phrases': [
        ('Your request has been received.', 'Yêu cầu của bạn đã được tiếp nhận.'),
        ('The issue is being investigated.', 'Sự cố đang được điều tra.'),
        ('You will be notified when it is fixed.', 'Bạn sẽ được thông báo khi lỗi được sửa.'),
        ('It is recommended that…', 'Khuyến nghị rằng…'),
        ('This has already been discussed.', 'Việc này đã được bàn rồi.'),
    ],
    'listening': {
        'title': 'How we release software',
        'intro': 'Tech lead Daniel giải thích quy trình phát hành phần mềm cho nhân viên mới tên Vy.',
        'speakers': {'A': ('Daniel', 'andrew'), 'B': ('Vy', 'jenny')},
        'lines': [
            ('A', 'Okay Vy, let me explain how a change gets from your laptop to production.', 'Được rồi Vy, để anh giải thích một thay đổi đi từ laptop của em lên production thế nào.'),
            ('A', 'First, every change is made in a separate branch. Nothing is pushed directly to main.', 'Đầu tiên, mọi thay đổi được làm trên một nhánh riêng. Không có gì được đẩy thẳng lên main.'),
            ('B', 'Got it. And then I open a pull request?', 'Em hiểu. Rồi em mở pull request ạ?'),
            ('A', 'Right. When a pull request is opened, the tests are run automatically. It usually takes about eight minutes.', 'Đúng. Khi pull request được mở, test sẽ tự động chạy. Thường mất khoảng tám phút.'),
            ('B', 'Who reviews the code?', 'Ai review code ạ?'),
            ('A', 'Every pull request must be approved by at least two people. One of them should be a senior developer.', 'Mọi pull request phải được ít nhất hai người phê duyệt. Một trong hai nên là senior.'),
            ('B', 'And after it is approved?', 'Sau khi được duyệt thì sao ạ?'),
            ('A', "It's merged into main and deployed to the staging server. Our QA team checks it there.", 'Nó được merge vào main và triển khai lên máy chủ staging. Đội QA kiểm tra ở đó.'),
            ('A', 'Then, every Tuesday and Thursday, the latest version is released to production.', 'Sau đó, mỗi thứ Ba và thứ Năm, phiên bản mới nhất được phát hành lên production.'),
            ('B', 'What happens if something goes wrong?', 'Nếu có sự cố thì sao ạ?'),
            ('A', 'The previous version can be restored in about two minutes. And everyone on the team is notified in Slack.', 'Phiên bản trước có thể được khôi phục trong khoảng hai phút. Và cả team được thông báo trên Slack.'),
        ],
        'questions': [
            ('Where is every change made first?', ['In the main branch', 'In a separate branch', 'On the staging server', 'In production'], 1, '"every change is made in a separate branch".'),
            ('How many approvals does a pull request need?', ['One', 'At least two', 'Three', 'None'], 1, '"must be approved by at least two people".'),
            ('Where does the QA team check the changes?', ['On the developer\'s laptop', 'In production', 'On the staging server', 'In Slack'], 2, '"deployed to the staging server. Our QA team checks it there."'),
            ('When is new code released to production?', ['Every day', 'Every Friday', 'Tuesdays and Thursdays', 'Once a month'], 2, '"every Tuesday and Thursday, the latest version is released".'),
        ],
    },
    'speaking': {
        'tips': ['Dùng bị động cho các bước: "First, … is …. Then, … are …."', 'Từ nối: first, then, after that, once …, finally.'],
        'prompts': [
            ('Describe how code is released at your company (or a company you know).', 'Bước 1 → bước cuối, dùng bị động.'),
            ('Describe how an online order is processed, from clicking "Buy" to delivery.', 'The order is received… is packed… is shipped…'),
            ('What happens to your data when you sign up for a new app?', 'is stored, is encrypted, is shared…'),
        ],
        'model': (
            "When a customer clicks Buy, the order is sent to our server and the payment is checked by the bank. "
            "If the payment is approved, a confirmation email is generated and sent to the customer. "
            "Then the order is passed to the warehouse, where the items are packed. "
            "After that, the package is picked up by a delivery company, and a tracking number is added to the order. "
            "Most orders are delivered within two days. If a package is lost, a refund is issued automatically.",
            'Khi khách bấm Mua, đơn hàng được gửi lên máy chủ và khoản thanh toán được ngân hàng kiểm tra. '
            'Nếu thanh toán được chấp nhận, một email xác nhận được tạo và gửi cho khách. '
            'Sau đó đơn hàng được chuyển tới kho, nơi hàng được đóng gói. '
            'Tiếp theo, gói hàng được công ty vận chuyển đến lấy, và mã vận đơn được thêm vào đơn hàng. '
            'Phần lớn đơn được giao trong hai ngày. Nếu gói hàng bị thất lạc, tiền sẽ được hoàn tự động.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'README: Backups',
        'text': [
            'This section explains how backups are handled in the Orders service. Please read it carefully before you make any changes to the database.',
            'A full backup of the database is created every night at 2 a.m. (UTC). In addition, changes are recorded every five minutes, so data can be restored to any point in the last seven days. Backups are stored in a separate region and are encrypted with a key that is managed by the security team.',
            'Restoring a backup must be approved by the team lead. The process is documented in the Runbook, and it should be tested at least once a month. Developers are not allowed to download production backups to their personal laptops.',
        ],
        'vi': 'Bản sao lưu đầy đủ được tạo mỗi đêm lúc 2 giờ (UTC); thay đổi được ghi lại mỗi 5 phút nên có thể khôi phục về bất kỳ thời điểm nào trong 7 ngày. Bản sao lưu được lưu ở vùng khác và mã hóa bằng khóa do đội bảo mật quản lý. Việc khôi phục phải được trưởng nhóm duyệt, quy trình nằm trong Runbook và nên được kiểm tra mỗi tháng. Dev không được tải bản sao lưu production về laptop cá nhân.',
        'questions': [
            ('How often is a full backup created?', ['Every five minutes', 'Every night', 'Every week', 'Every month'], 1, '"A full backup… is created every night at 2 a.m."'),
            ('Who must approve restoring a backup?', ['The security team', 'Any developer', 'The team lead', 'The customer'], 2, '"must be approved by the team lead".'),
            ('What are developers NOT allowed to do?', ['Read the Runbook', 'Download production backups to personal laptops', 'Test the process', 'Make database changes'], 1, 'Câu cuối.'),
        ],
    },
    'writing': {
        'task': 'Chuyển 10 câu sau sang bị động (giữ nguyên thì): 1) The team deploys the app every Friday. 2) Someone stole my laptop. 3) They are fixing the bug now. 4) We have released version 2.0. 5) The manager will approve the budget. 6) You must change your password every 90 days. 7) A customer reported the issue. 8) The system generates reports at midnight. 9) They haven\'t paid the invoice yet. 10) Our designer created the new logo.',
        'tips': ['Xác định tân ngữ → đưa lên đầu.', 'Giữ nguyên thì của động từ "be".', 'Bỏ "by someone/they/we" nếu không quan trọng.'],
        'model': "1. The app is deployed every Friday.\n2. My laptop was stolen.\n3. The bug is being fixed now.\n4. Version 2.0 has been released.\n5. The budget will be approved by the manager.\n6. Your password must be changed every 90 days.\n7. The issue was reported by a customer.\n8. Reports are generated at midnight.\n9. The invoice hasn't been paid yet.\n10. The new logo was created by our designer.",
        'min_words': 60,
    },
    'quiz': [
        ('The servers ___ every night.', ['back up', 'are backed up', 'are backing up', 'backed up'], 1, 'Bị động hiện tại đơn: are + V3.'),
        ('The bug ___ by Lan yesterday.', ['fixed', 'is fixed', 'was fixed', 'has fixed'], 2, '"yesterday" → quá khứ; bị động: was fixed.'),
        ('Your application ___ at the moment.', ['is reviewed', 'is being reviewed', 'reviews', 'was reviewing'], 1, '"at the moment" → hiện tại tiếp diễn bị động: is being reviewed.'),
        ('The meeting ___ to next Monday.', ['has moved', 'has been moved', 'have been moved', 'is moving'], 1, 'Hiện tại hoàn thành bị động, chủ ngữ số ít: has been moved.'),
        ('You ___ by email when your order ships.', ['will notify', 'will be notified', 'are notifying', 'notified'], 1, 'Tương lai bị động: will be + V3.'),
        ('Passwords should never ___ in plain text.', ['store', 'be stored', 'stored', 'being stored'], 1, 'Modal + be + V3.'),
        ('The email ___ to all customers last night.', ['was send', 'was sent', 'sent', 'is sending'], 1, 'send – sent – sent.'),
        ('An error ___ while you were sleeping.', ['was occurred', 'occurred', 'is occurred', 'has been occurred'], 1, '"occur" là nội động từ, không có bị động.'),
        ('English ___ in many countries.', ['speaks', 'is spoken', 'is speaking', 'spoke'], 1, 'Sự thật chung → bị động hiện tại đơn.'),
        ('This library ___ anymore. Please use the new one.', ["isn't maintained", "doesn't maintain", "isn't maintaining", "wasn't maintain"], 0, 'Thư viện không được bảo trì → bị động.'),
        ('Câu nào nghe lịch sự, tránh đổ lỗi nhất?', ['You broke the build.', 'The build was broken.', 'You made the build broken.', 'Your build is bad.'], 1, 'Bị động giúp tránh chỉ thẳng vào người.'),
        ('"It is recommended that you ___ your password regularly."', ['changing', 'change', 'changed', 'to change'], 1, 'Sau "It is recommended that + S" dùng động từ nguyên mẫu.'),
    ],
}

DAY4 = {
    'title': 'Phát âm: âm cuối và nối âm',
    'title_en': 'Final Sounds and Linking',
    'goal': 'Phát âm đúng đuôi -s/-es (/s/, /z/, /ɪz/) và -ed (/t/, /d/, /ɪd/); không nuốt phụ âm cuối; nối phụ âm với nguyên âm cho tự nhiên.',
    'tasks': [
        'Học quy tắc đọc đuôi -s/-es và -ed.',
        'Nghe và phân loại 14 từ theo âm cuối.',
        'Làm bài nghe chọn âm cuối.',
        'Đọc 10 câu luyện tập và ghi âm.',
        'Nghe lại: bạn có nuốt âm cuối nào không?',
    ],
    'product': 'Bản ghi âm đọc 10 câu luyện tập; Điểm bài phân loại âm cuối',
    'warmup': [
        ('She works in a big office.', 'Cô ấy làm việc trong một văn phòng lớn.'),
        ('He fixed the bug and pushed the code.', 'Anh ấy sửa lỗi và đẩy code lên.'),
        ('We needed more time, so we started early.', 'Chúng tôi cần thêm thời gian nên bắt đầu sớm.'),
        ('Turn it off and on again.', 'Tắt đi rồi bật lại.'),
        ('Pick it up at eight.', 'Lấy nó lúc tám giờ.'),
        ('The team changes its plans every week.', 'Team thay đổi kế hoạch mỗi tuần.'),
    ],
    'vocab': [
        ('worked', '/wɜːkt/', 'verb (past)', 'đã làm việc — đuôi /t/', 'I worked late last night.', 'Tối qua tôi làm việc muộn.'),
        ('fixed', '/fɪkst/', 'verb (past)', 'đã sửa — đuôi /t/', 'We fixed the problem in ten minutes.', 'Chúng tôi sửa vấn đề trong mười phút.'),
        ('finished', '/ˈfɪnɪʃt/', 'verb (past)', 'đã hoàn thành — đuôi /t/', 'She finished the report before lunch.', 'Cô ấy làm xong báo cáo trước bữa trưa.'),
        ('asked', '/ɑːskt/', 'verb (past)', 'đã hỏi — đuôi /t/', 'He asked a lot of good questions.', 'Anh ấy hỏi nhiều câu hỏi hay.'),
        ('deployed', '/dɪˈplɔɪd/', 'verb (past)', 'đã triển khai — đuôi /d/', 'We deployed the update on Tuesday.', 'Chúng tôi triển khai bản cập nhật vào thứ Ba.'),
        ('planned', '/plænd/', 'verb (past)', 'đã lên kế hoạch — đuôi /d/', 'Everything went as planned.', 'Mọi thứ diễn ra như kế hoạch.'),
        ('changed', '/tʃeɪndʒd/', 'verb (past)', 'đã thay đổi — đuôi /d/', 'The client changed the design again.', 'Khách hàng lại thay đổi thiết kế.'),
        ('solved', '/sɒlvd/', 'verb (past)', 'đã giải quyết — đuôi /d/', 'Have you solved the memory issue?', 'Bạn đã giải quyết vấn đề bộ nhớ chưa?'),
        ('needed', '/ˈniːdɪd/', 'verb (past)', 'đã cần — đuôi /ɪd/', 'We needed two more developers.', 'Chúng tôi đã cần thêm hai lập trình viên.'),
        ('tested', '/ˈtestɪd/', 'verb (past)', 'đã kiểm thử — đuôi /ɪd/', 'Every feature is tested before release.', 'Mọi tính năng đều được kiểm thử trước khi phát hành.'),
        ('updated', '/ʌpˈdeɪtɪd/', 'verb (past)', 'đã cập nhật — đuôi /ɪd/', 'I updated the documentation yesterday.', 'Hôm qua tôi đã cập nhật tài liệu.'),
        ('uses', '/ˈjuːzɪz/', 'verb', 'sử dụng (ngôi 3) — đuôi /ɪz/', 'Our team uses Slack for chat.', 'Team chúng tôi dùng Slack để nhắn tin.'),
        ('pushes', '/ˈpʊʃɪz/', 'verb', 'đẩy (ngôi 3) — đuôi /ɪz/', 'He pushes his code every evening.', 'Anh ấy đẩy code mỗi tối.'),
        ('stops', '/stɒps/', 'verb', 'dừng (ngôi 3) — đuôi /s/', 'The script stops when it finds an error.', 'Script dừng lại khi gặp lỗi.'),
    ],
    'lesson': """
<h3>1. Đuôi -s / -es: 3 cách đọc</h3>
<table class="table">
<tr><th>Đọc</th><th>Khi từ kết thúc bằng âm</th><th>Ví dụ</th></tr>
<tr><td><b>/s/</b></td><td>vô thanh: /p/ /t/ /k/ /f/ /θ/</td><td><span class="say">stops</span>, <span class="say">gets</span>, <span class="say">works</span>, <span class="say">laughs</span>, <span class="say">months</span></td></tr>
<tr><td><b>/ɪz/</b></td><td>/s/ /z/ /ʃ/ /tʃ/ /dʒ/ (s, ss, sh, ch, x, ge, ce)</td><td><span class="say">uses</span>, <span class="say">pushes</span>, <span class="say">watches</span>, <span class="say">changes</span>, <span class="say">fixes</span></td></tr>
<tr><td><b>/z/</b></td><td>các âm còn lại (hữu thanh, nguyên âm)</td><td><span class="say">plays</span>, <span class="say">runs</span>, <span class="say">calls</span>, <span class="say">needs</span>, <span class="say">files</span></td></tr>
</table>

<h3>2. Đuôi -ed: 3 cách đọc</h3>
<table class="table">
<tr><th>Đọc</th><th>Khi động từ kết thúc bằng âm</th><th>Ví dụ</th></tr>
<tr><td><b>/ɪd/</b></td><td>/t/ hoặc /d/</td><td><span class="say">needed</span>, <span class="say">tested</span>, <span class="say">started</span>, <span class="say">updated</span></td></tr>
<tr><td><b>/t/</b></td><td>vô thanh: /p/ /k/ /f/ /s/ /ʃ/ /tʃ/</td><td><span class="say">stopped</span>, <span class="say">worked</span>, <span class="say">fixed</span>, <span class="say">pushed</span>, <span class="say">watched</span></td></tr>
<tr><td><b>/d/</b></td><td>các âm còn lại</td><td><span class="say">played</span>, <span class="say">deployed</span>, <span class="say">changed</span>, <span class="say">planned</span>, <span class="say">called</span></td></tr>
</table>
<div class="warn"><b>Lỗi phổ biến nhất:</b> đọc <i>worked</i> thành "wơ-kết" hay "wơ-kờ-đờ". Chỉ có <b>/ɪd/</b> mới thêm âm tiết! <span class="say">worked</span> vẫn là MỘT âm tiết /wɜːkt/.</div>

<h3>3. Đừng nuốt âm cuối</h3>
<p>Tiếng Việt không có cụm phụ âm cuối như /kst/, /ndʒd/ nên ta hay bỏ qua. Nhưng trong tiếng Anh, âm cuối mang nghĩa: <span class="say">I work</span> khác <span class="say">I worked</span>; <span class="say">one file</span> khác <span class="say">two files</span>.</p>
<p>Mẹo: luyện chậm, phóng đại âm cuối, rồi tăng dần tốc độ: <span class="say">fixed</span> → <span class="say">I fixed it</span> → <span class="say">I fixed it yesterday</span>.</p>

<h3>4. Nối âm (linking)</h3>
<p>Phụ âm cuối của từ trước "chạy" sang nguyên âm đầu của từ sau. Nhờ vậy âm cuối được đọc rõ và câu nghe mượt:</p>
<div class="ex"><span class="en">Turn it off.</span><span class="vi">→ "tur-ni-toff"</span></div>
<div class="ex"><span class="en">Pick it up.</span><span class="vi">→ "pi-ki-tup"</span></div>
<div class="ex"><span class="en">I worked on it all evening.</span><span class="vi">→ "wor-kton-i-tall-evening"</span></div>
<div class="ex"><span class="en">Check it out.</span><span class="vi">→ "che-ki-tout"</span></div>
""",
    'listening': {
        'title': 'What I did last week',
        'intro': 'Peter tóm tắt công việc tuần trước trong buổi họp. Chú ý đuôi -ed và nối âm.',
        'speakers': {'A': ('Peter', 'ryan')},
        'lines': [
            ('A', 'Last week was busy, but I think it went quite well.', 'Tuần trước khá bận nhưng tôi nghĩ mọi thứ khá ổn.'),
            ('A', 'On Monday, I finished the new login page and pushed it for review.', 'Thứ Hai, tôi làm xong trang đăng nhập mới và đẩy lên để review.'),
            ('A', 'On Tuesday, the client asked for some changes, so I updated the design.', 'Thứ Ba, khách hàng yêu cầu vài thay đổi nên tôi cập nhật thiết kế.'),
            ('A', 'On Wednesday, we tested everything on staging and found two small bugs.', 'Thứ Tư, chúng tôi kiểm thử mọi thứ trên staging và phát hiện hai lỗi nhỏ.'),
            ('A', 'I fixed both of them on Thursday morning.', 'Tôi sửa cả hai vào sáng thứ Năm.'),
            ('A', 'Then we deployed the new version on Thursday afternoon, as planned.', 'Sau đó chúng tôi triển khai phiên bản mới vào chiều thứ Năm, đúng kế hoạch.'),
            ('A', 'On Friday, I worked on the documentation and helped Lisa with her tests.', 'Thứ Sáu, tôi làm tài liệu và giúp Lisa viết test.'),
            ('A', 'This week, I need to look into a performance problem that a customer reported.', 'Tuần này, tôi cần xem xét một vấn đề hiệu năng mà khách hàng báo cáo.'),
        ],
        'questions': [
            ('What did Peter do on Monday?', ['Tested on staging', 'Finished the login page', 'Fixed two bugs', 'Wrote documentation'], 1, '"I finished the new login page…" — finished đọc /t/.'),
            ('Why did Peter update the design?', ['It had bugs.', 'The client asked for changes.', 'Lisa asked him.', 'It was too slow.'], 1, '"the client asked for some changes".'),
            ('When was the new version deployed?', ['Monday', 'Wednesday', 'Thursday afternoon', 'Friday'], 2, '"we deployed the new version on Thursday afternoon".'),
            ('What will Peter work on this week?', ['A new login page', 'A performance problem', 'Lisa\'s tests', 'The client\'s design'], 1, '"look into a performance problem".'),
        ],
    },
    'speaking': {
        'tips': ['Đọc chậm, phóng đại âm cuối, sau đó đọc lại ở tốc độ bình thường.', 'Ghi âm và kiểm tra: có nghe rõ /t/ /d/ /s/ /z/ ở cuối không?'],
        'prompts': [
            ('1. She works and he plays. 2. The script stops and starts again. 3. He fixes bugs and watches the logs.', 'Đuôi -s: /s/, /z/, /ɪz/'),
            ('4. I worked, fixed and pushed the code. 5. We planned and deployed it. 6. They needed and tested it.', 'Đuôi -ed: /t/, /d/, /ɪd/'),
            ('7. Turn it off. 8. Pick it up. 9. Check it out. 10. I asked about it again.', 'Nối âm'),
            ('Tell me what you did yesterday, from morning to evening.', 'Dùng thật nhiều động từ -ed; nhấn rõ âm cuối.'),
        ],
        'model': (
            "Yesterday I started work at eight. I checked my emails and joined the stand-up. "
            "After that, I worked on a bug that a customer reported. It looked simple, but it took me two hours. "
            "I fixed it, tested it and pushed the code before lunch. "
            "In the afternoon, I reviewed two pull requests and updated the documentation. "
            "I finished at six, walked home and cooked dinner. Then I watched an episode of a podcast and relaxed.",
            'Hôm qua tôi bắt đầu làm lúc tám giờ. Tôi kiểm tra email và tham gia stand-up. '
            'Sau đó tôi xử lý một lỗi khách hàng báo cáo. Nó trông đơn giản nhưng mất hai tiếng. '
            'Tôi sửa nó, kiểm thử và đẩy code trước bữa trưa. '
            'Buổi chiều, tôi review hai pull request và cập nhật tài liệu. '
            'Tôi xong việc lúc sáu giờ, đi bộ về nhà và nấu bữa tối. Sau đó tôi nghe một tập podcast và thư giãn.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Why final sounds matter',
        'text': [
            'Many Asian languages, including Vietnamese, have few consonant sounds at the end of words. As a result, learners often drop final sounds in English without noticing. They say "I work yesterday" instead of "I worked yesterday", or "two file" instead of "two files".',
            'For native speakers, these small sounds carry a lot of information. The final /d/ tells them the action is in the past. The final /s/ tells them there is more than one thing. When the sounds are missing, listeners have to guess, and conversations become tiring.',
            'The good news is that final sounds are easy to improve with practice. Read short sentences slowly and exaggerate the endings. Record yourself, and listen only to the ends of the words. After two or three weeks, the endings will start to come naturally.',
        ],
        'vi': 'Tiếng Việt có ít phụ âm cuối nên người học hay bỏ âm cuối tiếng Anh mà không biết (I work yesterday, two file). Với người bản xứ, âm cuối mang nhiều thông tin: /d/ cho biết quá khứ, /s/ cho biết số nhiều. Thiếu chúng, người nghe phải đoán và nhanh mệt. Tin tốt là có thể cải thiện: đọc chậm câu ngắn, phóng đại âm cuối, ghi âm và chỉ nghe phần cuối từ. Sau 2–3 tuần sẽ tự nhiên hơn.',
        'questions': [
            ('Why do Vietnamese learners often drop final sounds?', ['They speak too slowly.', 'Vietnamese has few final consonant sounds.', 'Native speakers do it too.', 'Final sounds are not important.'], 1, 'Đoạn 1.'),
            ('What does a final /s/ often tell the listener?', ['The action is in the past.', 'There is more than one thing.', 'It is a question.', 'The speaker is polite.'], 1, 'Đoạn 2.'),
            ('What should you listen to in your recordings?', ['Your intonation', 'The ends of the words', 'Your speed', 'The first word of each sentence'], 1, '"listen only to the ends of the words".'),
        ],
    },
    'writing': {
        'task': 'Viết 6 câu kể lại những gì bạn làm hôm qua, dùng ít nhất 8 động từ có đuôi -ed. Ghi cách đọc đuôi bên cạnh mỗi động từ: /t/, /d/ hoặc /ɪd/. Sau đó đọc to.',
        'tips': ['Ví dụ: "I worked /t/ from home and attended /ɪd/ two meetings."'],
        'model': "Yesterday I worked /t/ from home and attended /ɪd/ two meetings.\nIn the morning, I fixed /t/ a bug and pushed /t/ the code.\nThe tests failed /d/ at first, so I checked /t/ the logs.\nI realized /d/ that I needed /ɪd/ to update the config.\nAfter lunch, I reviewed /d/ a pull request and suggested /ɪd/ some changes.\nIn the evening, I cooked /t/ dinner and watched /t/ a movie.",
        'min_words': 50,
    },
    'quiz': [
        ('Đuôi -ed trong "worked" đọc là:', ['/t/', '/d/', '/ɪd/'], 0, '/k/ là âm vô thanh → /t/.', 'worked'),
        ('Đuôi -ed trong "needed" đọc là:', ['/t/', '/d/', '/ɪd/'], 2, 'Kết thúc bằng /d/ → /ɪd/.', 'needed'),
        ('Đuôi -ed trong "planned" đọc là:', ['/t/', '/d/', '/ɪd/'], 1, '/n/ hữu thanh → /d/.', 'planned'),
        ('Đuôi -ed trong "pushed" đọc là:', ['/t/', '/d/', '/ɪd/'], 0, '/ʃ/ vô thanh → /t/.', 'pushed'),
        ('Đuôi -ed trong "started" đọc là:', ['/t/', '/d/', '/ɪd/'], 2, 'Kết thúc bằng /t/ → /ɪd/.', 'started'),
        ('Đuôi -s trong "changes" đọc là:', ['/s/', '/z/', '/ɪz/'], 2, 'Kết thúc bằng /dʒ/ → /ɪz/.', 'changes'),
        ('Đuôi -s trong "stops" đọc là:', ['/s/', '/z/', '/ɪz/'], 0, '/p/ vô thanh → /s/.', 'stops'),
        ('Đuôi -s trong "calls" đọc là:', ['/s/', '/z/', '/ɪz/'], 1, '/l/ hữu thanh → /z/.', 'calls'),
        ('Từ nào có đuôi -ed đọc /ɪd/?', ['asked', 'tested', 'played', 'watched'], 1, 'test kết thúc bằng /t/ → tested /ɪd/.'),
        ('Từ nào có đuôi -s đọc /ɪz/?', ['works', 'fixes', 'runs', 'gets'], 1, 'fix kết thúc /s/ (x = /ks/) → fixes /ɪz/.'),
        ('"worked" có mấy âm tiết?', ['1', '2', '3'], 0, '/wɜːkt/ — chỉ một âm tiết. Chỉ đuôi /ɪd/ mới thêm âm tiết.'),
        ('Nghe và chọn câu bạn nghe được.', ['I work at home.', 'I worked at home.'], 1, 'Có âm /t/ nối sang "at": "wor-ktat home".', 'I worked at home.'),
    ],
}

DAY5 = {
    'title': 'Shadowing 2 và tóm tắt podcast',
    'title_en': 'Shadowing 2: Podcast Summary',
    'goal': 'Nghe hiểu một tập podcast ngắn kiểu "6 Minute English", shadow các câu quan trọng và tóm tắt nội dung chính bằng lời trong 1 phút không nhìn lời thoại.',
    'tasks': [
        'Học 14 từ về làm việc từ xa và năng suất.',
        'Nghe podcast 2 lần không nhìn lời, ghi 3 ý chính.',
        'Trả lời câu hỏi, sau đó hiện lời và nghe lại.',
        'Shadow 6 câu quan trọng nhất.',
        'Tóm tắt podcast bằng lời trong 1 phút và ghi âm.',
    ],
    'product': 'Bản ghi âm tóm tắt 1 phút; 3 ý chính của podcast',
    'warmup': [
        ('Working from home can be great for focus.', 'Làm việc ở nhà có thể rất tốt cho sự tập trung.'),
        ('But some people feel isolated.', 'Nhưng một số người cảm thấy bị cô lập.'),
        ("It's important to set clear boundaries.", 'Điều quan trọng là đặt ranh giới rõ ràng.'),
        ('According to a recent survey, most workers prefer a hybrid model.', 'Theo một khảo sát gần đây, phần lớn người lao động thích mô hình kết hợp.'),
        ('The main point of the episode is balance.', 'Ý chính của tập này là sự cân bằng.'),
        ('In short, there is no perfect answer.', 'Tóm lại, không có câu trả lời hoàn hảo.'),
    ],
    'vocab': [
        ('productivity', '/ˌprɒdʌkˈtɪvəti/', 'n', 'năng suất', 'Some studies show that productivity goes up at home.', 'Một số nghiên cứu cho thấy năng suất tăng khi làm ở nhà.'),
        ('distraction', '/dɪˈstrækʃn/', 'n', 'sự xao nhãng', 'My phone is my biggest distraction.', 'Điện thoại là thứ làm tôi xao nhãng nhất.'),
        ('flexible', '/ˈfleksəbl/', 'adj', 'linh hoạt', 'I like having flexible working hours.', 'Tôi thích có giờ làm linh hoạt.'),
        ('isolated', '/ˈaɪsəleɪtɪd/', 'adj', 'cô lập, cô đơn', 'Remote workers can feel isolated.', 'Người làm từ xa có thể thấy cô đơn.'),
        ('boundary', '/ˈbaʊndri/', 'n', 'ranh giới', 'Set a boundary: no work emails after 7 p.m.', 'Đặt ranh giới: không đọc email công việc sau 7 giờ tối.'),
        ('burnout', '/ˈbɜːnaʊt/', 'n', 'kiệt sức (vì công việc)', 'Working long hours can lead to burnout.', 'Làm việc nhiều giờ có thể dẫn đến kiệt sức.'),
        ('hybrid', '/ˈhaɪbrɪd/', 'adj', 'kết hợp (nhà + văn phòng)', 'Our company uses a hybrid model.', 'Công ty chúng tôi dùng mô hình kết hợp.'),
        ('face-to-face', '/ˌfeɪs tə ˈfeɪs/', 'adj / adv', 'trực tiếp, gặp mặt', 'Some problems are easier to solve face-to-face.', 'Một số vấn đề dễ giải quyết hơn khi gặp trực tiếp.'),
        ('work-life balance', '/ˌwɜːk laɪf ˈbæləns/', 'n', 'cân bằng công việc – cuộc sống', 'Remote work improved my work-life balance.', 'Làm từ xa cải thiện sự cân bằng công việc – cuộc sống của tôi.'),
        ('survey', '/ˈsɜːveɪ/', 'n', 'cuộc khảo sát', 'The survey asked 2,000 office workers.', 'Cuộc khảo sát hỏi 2.000 nhân viên văn phòng.'),
        ('according to', '/əˈkɔːdɪŋ tə/', 'phrase', 'theo (nguồn nào)', 'According to the report, sales doubled.', 'Theo báo cáo, doanh số tăng gấp đôi.'),
        ('collaborate', '/kəˈlæbəreɪt/', 'verb', 'cộng tác', 'We collaborate with a team in Japan.', 'Chúng tôi cộng tác với một team ở Nhật.'),
        ('in short', '/ɪn ʃɔːt/', 'phrase', 'tóm lại', 'In short, the project was a success.', 'Tóm lại, dự án đã thành công.'),
        ('the main point', '/ðə meɪn pɔɪnt/', 'phrase', 'ý chính', 'The main point is that we need more testing.', 'Ý chính là chúng ta cần kiểm thử nhiều hơn.'),
    ],
    'lesson': """
<h3>1. Cách nghe một tập podcast</h3>
<table class="table">
<tr><th>Lần</th><th>Mục tiêu</th></tr>
<tr><td>Lần 1 (không lời)</td><td>Chỉ cần hiểu chủ đề và cảm xúc chung. Đừng dừng lại.</td></tr>
<tr><td>Lần 2 (không lời)</td><td>Ghi nhanh 3 ý chính bằng từ khóa (tiếng Anh nếu được).</td></tr>
<tr><td>Lần 3 (có lời)</td><td>Đọc lời, đánh dấu cụm từ hay, tra từ mới.</td></tr>
<tr><td>Shadowing</td><td>Chọn 5–6 câu hay nhất, shadow mỗi câu 3–5 lần.</td></tr>
</table>

<h3>2. Khung tóm tắt 1 phút</h3>
<ol>
<li><b>Chủ đề:</b> <span class="say">The episode was about whether working from home is good for us.</span></li>
<li><b>Ý chính 1–2–3:</b> <span class="say">First, they talked about… Then, they mentioned… Finally, they said…</span></li>
<li><b>Một số liệu/ví dụ:</b> <span class="say">According to a survey, …</span></li>
<li><b>Kết luận + ý kiến của bạn:</b> <span class="say">In short, … Personally, I think…</span></li>
</ol>

<h3>3. Cụm từ dùng khi tóm tắt</h3>
<div class="ex"><span class="en">The speakers discussed…</span><span class="vi">Các diễn giả đã bàn về…</span></div>
<div class="ex"><span class="en">One interesting point was that…</span><span class="vi">Một ý thú vị là…</span></div>
<div class="ex"><span class="en">They also mentioned that…</span><span class="vi">Họ cũng nhắc đến việc…</span></div>
<div class="ex"><span class="en">The main takeaway is…</span><span class="vi">Điều rút ra chính là…</span></div>
<div class="note"><b>Mẹo:</b> Khi tóm tắt, dùng <b>quá khứ đơn</b> cho việc diễn giả đã nói (<i>they said, they talked about</i>) và <b>hiện tại đơn</b> cho sự thật/ý kiến (<i>remote work is…</i>).</div>
""",
    'phrases': [
        ('The episode was about…', 'Tập này nói về…'),
        ('One interesting point was that…', 'Một điểm thú vị là…'),
        ('According to…', 'Theo…'),
        ('The main takeaway is…', 'Điều rút ra chính là…'),
        ('Personally, I agree / disagree because…', 'Cá nhân tôi đồng ý / không đồng ý vì…'),
    ],
    'listening': {
        'title': 'Podcast: Is working from home good for us?',
        'intro': 'Một tập podcast học tiếng Anh dài khoảng 3 phút, hai người dẫn bàn về làm việc tại nhà. Nghe 2 lần trước khi hiện lời.',
        'speakers': {'A': ('Hannah', 'sonia'), 'B': ('Tom', 'ryan')},
        'lines': [
            ('A', "Hello and welcome to Everyday English. I'm Hannah.", 'Xin chào và chào mừng đến với Everyday English. Tôi là Hannah.'),
            ('B', "And I'm Tom. Today we're asking a big question: is working from home actually good for us?", 'Và tôi là Tom. Hôm nay chúng ta đặt ra một câu hỏi lớn: làm việc ở nhà có thực sự tốt cho chúng ta?'),
            ('A', 'Tom, you work from home three days a week, right?', 'Tom, anh làm ở nhà ba ngày một tuần đúng không?'),
            ('B', "That's right. And honestly, I love it. I don't have to commute, so I save about two hours every day.", 'Đúng vậy. Và thật lòng, tôi rất thích. Tôi không phải đi lại nên tiết kiệm khoảng hai tiếng mỗi ngày.'),
            ('A', 'Two hours! That is a lot of time. What do you do with it?', 'Hai tiếng! Nhiều thời gian thật. Anh làm gì với nó?'),
            ('B', 'I sleep a bit longer and I go to the gym. My work-life balance is much better.', 'Tôi ngủ thêm một chút và đi tập gym. Cân bằng công việc – cuộc sống của tôi tốt hơn nhiều.'),
            ('A', "According to a recent survey of two thousand office workers, you're not alone. Seventy percent said they were more productive at home.", 'Theo một khảo sát gần đây với hai nghìn nhân viên văn phòng, anh không phải người duy nhất. Bảy mươi phần trăm nói họ làm việc năng suất hơn ở nhà.'),
            ('B', 'But I guess there are some problems too.', 'Nhưng tôi đoán cũng có vài vấn đề.'),
            ('A', 'Yes. The biggest one is loneliness. Many people said they felt isolated, especially young workers who live alone.', 'Vâng. Vấn đề lớn nhất là sự cô đơn. Nhiều người nói họ thấy bị cô lập, đặc biệt là người trẻ sống một mình.'),
            ('B', "I can understand that. When I started, I sometimes didn't speak to anyone all day.", 'Tôi hiểu điều đó. Hồi mới bắt đầu, có hôm tôi chẳng nói chuyện với ai cả ngày.'),
            ('A', "Another problem is that the line between work and home disappears. People check emails at ten p.m. and they never really switch off.", 'Một vấn đề khác là ranh giới giữa công việc và nhà biến mất. Mọi người đọc email lúc mười giờ tối và không bao giờ thực sự nghỉ ngơi.'),
            ('B', 'Which can lead to burnout.', 'Điều có thể dẫn tới kiệt sức.'),
            ('A', 'Exactly. So experts recommend setting clear boundaries. For example, have a separate place for work, and finish at the same time every day.', 'Chính xác. Vì vậy chuyên gia khuyên nên đặt ranh giới rõ ràng. Ví dụ, có một chỗ làm việc riêng và kết thúc vào cùng một giờ mỗi ngày.'),
            ('B', "That's why I like the hybrid model. I get focus time at home, and I see my colleagues face-to-face at the office.", 'Đó là lý do tôi thích mô hình kết hợp. Tôi có thời gian tập trung ở nhà và gặp đồng nghiệp trực tiếp ở văn phòng.'),
            ('A', 'And in the survey, that was the most popular option. Only twelve percent wanted to work from home every day.', 'Và trong khảo sát, đó là lựa chọn được ưa chuộng nhất. Chỉ mười hai phần trăm muốn làm ở nhà mỗi ngày.'),
            ('B', 'So, in short, working from home is great, but not all the time.', 'Vậy tóm lại, làm ở nhà rất tốt, nhưng không phải lúc nào cũng vậy.'),
            ('A', "That's the main point. Thanks for listening, everyone. Bye for now!", 'Đó là ý chính. Cảm ơn mọi người đã lắng nghe. Tạm biệt!'),
        ],
        'questions': [
            ('How much time does Tom save by not commuting?', ['One hour a day', 'Two hours a day', 'Three days a week', 'Two hours a week'], 1, '"I save about two hours every day."'),
            ('What percentage of workers said they were more productive at home?', ['12%', '50%', '70%', '2,000'], 2, '"Seventy percent said they were more productive at home."'),
            ('What is the biggest problem with working from home, according to the survey?', ['Bad internet', 'Loneliness', 'Lower salary', 'Noisy neighbours'], 1, '"The biggest one is loneliness."'),
            ('What do experts recommend?', ['Working longer hours', 'Checking emails at night', 'Setting clear boundaries', 'Moving to the office'], 2, '"experts recommend setting clear boundaries".'),
            ('Which option was the most popular in the survey?', ['Working from home every day', 'Working at the office every day', 'The hybrid model', 'Working part-time'], 2, '"I like the hybrid model… that was the most popular option."'),
        ],
    },
    'speaking': {
        'tips': ['Nghe xong, ĐÓNG lời thoại lại rồi mới nói.', 'Dùng khung tóm tắt 4 phần. Nói đúng 1 phút.', 'Thêm 1 câu ý kiến cá nhân ở cuối.'],
        'prompts': [
            ('Summarise the podcast in one minute without looking at the transcript.', 'Chủ đề → 3 ý chính → 1 số liệu → kết luận + ý kiến.'),
            ('Do you prefer working from home or at the office? Why?', 'Trả lời 3–4 câu.'),
        ],
        'model': (
            "The episode was about whether working from home is good for us. "
            "First, Tom said he loves it because he saves two hours a day and his work-life balance is better. "
            "According to a survey, seventy percent of workers feel more productive at home. "
            "However, the speakers also mentioned two problems: many people feel isolated, and work and home life get mixed, which can lead to burnout. "
            "Experts recommend setting clear boundaries. "
            "The main takeaway is that a hybrid model is the most popular option. "
            "Personally, I agree, because I need focus time but I also need to see my team.",
            'Tập này bàn về việc làm ở nhà có tốt cho chúng ta không. '
            'Đầu tiên, Tom nói anh rất thích vì tiết kiệm hai tiếng mỗi ngày và cân bằng cuộc sống tốt hơn. '
            'Theo một khảo sát, bảy mươi phần trăm người lao động thấy năng suất hơn ở nhà. '
            'Tuy nhiên, họ cũng nhắc đến hai vấn đề: nhiều người thấy cô lập, và công việc lẫn cuộc sống bị trộn vào nhau, có thể dẫn tới kiệt sức. '
            'Chuyên gia khuyên nên đặt ranh giới rõ ràng. '
            'Điều rút ra chính là mô hình kết hợp được ưa chuộng nhất. '
            'Cá nhân tôi đồng ý, vì tôi cần thời gian tập trung nhưng cũng cần gặp team.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Five rules for working from home',
        'text': [
            'Remote work gives you freedom, but freedom without structure quickly becomes chaos. Here are five simple rules that many experienced remote workers follow.',
            'One: get dressed. You do not need a suit, but changing out of your pyjamas tells your brain that the working day has started. Two: have a fixed place for work. If you work on your bed, your bed will start to feel like an office.',
            'Three: use your calendar. Block time for deep work, and treat those blocks like meetings. Four: talk to people. Turn your camera on, join the social channel, and call a colleague instead of sending ten messages.',
            'Five: finish on time. Close your laptop and, if possible, put it somewhere you cannot see it. The work will still be there tomorrow.',
        ],
        'vi': 'Năm quy tắc làm việc ở nhà: (1) thay đồ — báo cho não biết ngày làm việc đã bắt đầu; (2) có chỗ làm việc cố định, đừng làm trên giường; (3) dùng lịch để khóa thời gian làm việc sâu như một cuộc họp; (4) trò chuyện với mọi người — bật camera, gọi điện thay vì gửi mười tin nhắn; (5) kết thúc đúng giờ, cất laptop đi.',
        'questions': [
            ('Why should you get dressed, according to the text?', ['To look good on camera', 'It tells your brain the working day has started', 'Your boss may visit', 'It is more comfortable'], 1, 'Đoạn 2.'),
            ('What happens if you work on your bed?', ['You sleep better.', 'Your bed starts to feel like an office.', 'You work faster.', 'Nothing.'], 1, 'Đoạn 2.'),
            ('What does the writer suggest instead of sending many messages?', ['Writing an email', 'Calling a colleague', 'Waiting until tomorrow', 'Using the calendar'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết bản tóm tắt podcast 5–6 câu bằng khung 4 phần, sau đó thêm 1–2 câu ý kiến cá nhân.',
        'tips': ['Dùng: The episode was about… / According to… / The main takeaway is… / Personally, …', 'Dùng quá khứ cho lời người nói, hiện tại cho sự thật.'],
        'model': "The episode was about the pros and cons of working from home. Tom explained that he saves two hours a day because he doesn't commute. According to a survey, seventy percent of office workers feel more productive at home, but many also feel isolated. The speakers also said that work and home life can get mixed, which may lead to burnout. The main takeaway is that a hybrid model works best for most people. Personally, I agree, and I would like to work from home three days a week.",
        'min_words': 70,
    },
    'quiz': [
        ('"My phone is my biggest ___." (thứ làm xao nhãng)', ['productivity', 'distraction', 'boundary', 'survey'], 1, 'distraction = sự xao nhãng.'),
        ('Working too much without rest can lead to ___.', ['burnout', 'balance', 'hybrid', 'feedback'], 0, 'burnout = kiệt sức.'),
        ('A ___ model means working partly at home and partly at the office.', ['flexible', 'hybrid', 'isolated', 'remote'], 1, 'hybrid = kết hợp.'),
        ('___ the report, sales went up by 20%.', ['According to', 'In short', 'Because', 'Although'], 0, 'According to + nguồn = theo…'),
        ('People who live alone and work from home may feel ___.', ['isolated', 'flexible', 'productive', 'face-to-face'], 0, 'isolated = cô lập.'),
        ('"___, the project was a success." (Tóm lại)', ['According to', 'In short', 'However', 'For example'], 1, 'In short = tóm lại.'),
        ('Khi tóm tắt lời diễn giả, câu nào tự nhiên nhất?', ['Tom says yesterday he loves it.', 'Tom said that he loves working from home.', 'Tom is saying he loved.', 'Tom has said yesterday.'], 1, 'Quá khứ cho lời đã nói; hiện tại cho sự thật vẫn đúng.'),
        ('We need to set clear ___ between work and family time.', ['boundaries', 'distractions', 'surveys', 'productivity'], 0, 'boundary = ranh giới.'),
        ('I like ___ working hours, so I can start late on Mondays.', ['isolated', 'flexible', 'hybrid', 'face-to-face'], 1, 'flexible = linh hoạt.'),
        ('Some problems are easier to solve ___.', ['face-to-face', 'in short', 'according to', 'burnout'], 0, 'face-to-face = trực tiếp.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 2',
    'title_en': 'Week 2 Review',
    'goal': 'Ôn câu điều kiện, mệnh đề quan hệ, bị động và âm cuối; làm lại câu sai; dùng từ nối để viết câu phức mạch lạc.',
    'tasks': [
        'Học 14 từ nối (linking words).',
        'Đọc phần tóm tắt tuần 2 và bài sửa lỗi.',
        'Nghe buổi họp tổng kết sprint.',
        'Làm 20 câu ôn tập (làm lại câu sai đến khi đúng hết).',
        'Viết lại 3 câu có lỗi từ các ngày trước + một đoạn văn có từ nối.',
    ],
    'product': 'Điểm quiz 20 câu; 3 câu đã sửa; Đoạn văn có từ nối',
    'warmup': [
        ("The tests passed. However, the build is still slow.", 'Test đã qua. Tuy nhiên, bản build vẫn chậm.'),
        ('Although it was late, we finished the release.', 'Mặc dù đã muộn, chúng tôi vẫn hoàn thành bản phát hành.'),
        ('The server was overloaded; as a result, the site went down.', 'Máy chủ bị quá tải; kết quả là trang web bị sập.'),
        ('In addition to the API, we built a small dashboard.', 'Ngoài API, chúng tôi còn làm một trang tổng quan nhỏ.'),
        ("We'll need more time unless we reduce the scope.", 'Chúng ta sẽ cần thêm thời gian trừ khi giảm phạm vi.'),
        ('Meanwhile, the design team is working on the new logo.', 'Trong khi đó, team thiết kế đang làm logo mới.'),
    ],
    'vocab': [
        ('however', '/haʊˈevə/', 'adv', 'tuy nhiên', 'The app is fast. However, it uses a lot of memory.', 'Ứng dụng chạy nhanh. Tuy nhiên, nó tốn nhiều bộ nhớ.'),
        ('therefore', '/ˈðeəfɔː/', 'adv', 'do đó, vì vậy', 'The API changed; therefore, we must update the client.', 'API đã thay đổi; do đó chúng ta phải cập nhật phía client.'),
        ('although', '/ɔːlˈðəʊ/', 'conj', 'mặc dù', 'Although the task was hard, she finished it on time.', 'Mặc dù việc khó, cô ấy vẫn làm xong đúng hạn.'),
        ('even though', '/ˈiːvn ðəʊ/', 'conj', 'mặc dù (nhấn mạnh hơn)', 'Even though I was tired, I joined the call.', 'Dù rất mệt, tôi vẫn tham gia cuộc gọi.'),
        ('despite', '/dɪˈspaɪt/', 'prep', 'bất chấp, mặc dù (+ N/V-ing)', 'Despite the bad weather, everyone came.', 'Bất chấp thời tiết xấu, mọi người vẫn đến.'),
        ('as a result', '/æz ə rɪˈzʌlt/', 'phrase', 'kết quả là', "We didn't test it. As a result, users found many bugs.", 'Chúng tôi không test. Kết quả là người dùng phát hiện nhiều lỗi.'),
        ('in addition', '/ɪn əˈdɪʃn/', 'phrase', 'ngoài ra, thêm vào đó', 'In addition, we added a dark mode.', 'Ngoài ra, chúng tôi thêm chế độ tối.'),
        ('meanwhile', '/ˈmiːnwaɪl/', 'adv', 'trong khi đó', 'Meanwhile, the QA team prepared the test cases.', 'Trong khi đó, đội QA chuẩn bị test case.'),
        ('whereas', '/weərˈæz/', 'conj', 'trong khi (đối lập)', 'Python is easy to read, whereas C++ is more complex.', 'Python dễ đọc, trong khi C++ phức tạp hơn.'),
        ('on the other hand', '/ɒn ði ˈʌðə hænd/', 'phrase', 'mặt khác', 'On the other hand, remote work can feel lonely.', 'Mặt khác, làm từ xa có thể thấy cô đơn.'),
        ('instead', '/ɪnˈsted/', 'adv', 'thay vào đó', "Don't email him. Call him instead.", 'Đừng email anh ấy. Hãy gọi điện thay vào đó.'),
        ('so that', '/səʊ ðæt/', 'conj', 'để mà', 'I wrote clear notes so that everyone could follow.', 'Tôi viết ghi chú rõ ràng để mọi người theo kịp.'),
        ('due to', '/djuː tuː/', 'prep', 'do, bởi vì (+ N)', 'The release was delayed due to a security issue.', 'Bản phát hành bị hoãn do một vấn đề bảo mật.'),
        ('for instance', '/fər ˈɪnstəns/', 'phrase', 'ví dụ', 'Some tools, for instance Jira, are hard to learn.', 'Một số công cụ, ví dụ Jira, khá khó học.'),
    ],
    'lesson': """
<h3>1. Tóm tắt tuần 2</h3>
<table class="table">
<tr><th>Chủ đề</th><th>Công thức nhanh</th><th>Ví dụ</th></tr>
<tr><td>Điều kiện loại 1</td><td>If + hiện tại, will + V</td><td><span class="say">If it fails, I'll fix it.</span></td></tr>
<tr><td>Điều kiện loại 2</td><td>If + quá khứ, would + V</td><td><span class="say">If I were you, I'd ask.</span></td></tr>
<tr><td>Mệnh đề quan hệ</td><td>who / which / that / where / whose</td><td><span class="say">The app that I built is free.</span></td></tr>
<tr><td>Bị động</td><td>be + V3</td><td><span class="say">The data is encrypted.</span></td></tr>
<tr><td>Âm cuối</td><td>-ed: /t/ /d/ /ɪd/; -s: /s/ /z/ /ɪz/</td><td><span class="say">worked, planned, needed</span></td></tr>
</table>

<h3>2. Từ nối — đặt đúng chỗ</h3>
<table class="table">
<tr><th>Nhóm</th><th>Đứng giữa hai mệnh đề</th><th>Đứng đầu câu mới (có dấu phẩy)</th></tr>
<tr><td>Đối lập</td><td>although, even though, whereas, but</td><td>However, … / On the other hand, …</td></tr>
<tr><td>Kết quả</td><td>so</td><td>Therefore, … / As a result, …</td></tr>
<tr><td>Thêm ý</td><td>and</td><td>In addition, … / Also, …</td></tr>
<tr><td>Mục đích</td><td>so that, to + V</td><td>—</td></tr>
</table>
<div class="fix"><s>Although it was raining, but we went out.</s><span class="en">Although it was raining, we went out.</span><span class="vi">Không dùng although và but trong cùng một câu.</span></div>
<div class="fix"><s>Despite it was late, we continued.</s><span class="en">Despite the late hour, we continued. / Although it was late, we continued.</span><span class="vi">despite + danh từ/V-ing; although + mệnh đề.</span></div>
<div class="fix"><s>The app is fast, however it crashes.</s><span class="en">The app is fast. However, it crashes.</span><span class="vi">"however" thường mở đầu câu mới hoặc sau dấu chấm phẩy.</span></div>

<h3>3. Sửa câu sai của tuần</h3>
<div class="fix"><s>If the server will crash, I call you.</s><span class="en">If the server crashes, I'll call you.</span></div>
<div class="fix"><s>The developer which wrote this code left.</s><span class="en">The developer who wrote this code left.</span></div>
<div class="fix"><s>The report was write by my manager.</s><span class="en">The report was written by my manager.</span></div>
<div class="fix"><s>If I have more time, I would learn Go.</s><span class="en">If I had more time, I would learn Go.</span></div>
""",
    'listening': {
        'title': 'Sprint review',
        'intro': 'Trưởng nhóm và một lập trình viên tổng kết sprint. Chú ý từ nối, câu bị động và câu điều kiện.',
        'speakers': {'A': ('Laura', 'ava'), 'B': ('Binh', 'brian')},
        'lines': [
            ('A', "Okay Binh, let's review the sprint. How did it go?", 'Được rồi Bình, cùng tổng kết sprint nhé. Mọi thứ thế nào?'),
            ('B', 'Mostly well. All the main features were finished. However, the search page was delayed.', 'Phần lớn ổn. Tất cả tính năng chính đã xong. Tuy nhiên, trang tìm kiếm bị chậm tiến độ.'),
            ('A', 'What happened?', 'Có chuyện gì vậy?'),
            ('B', 'The requirements were changed in the middle of the sprint. As a result, we had to rewrite the filters.', 'Yêu cầu bị thay đổi giữa sprint. Kết quả là tụi em phải viết lại bộ lọc.'),
            ('A', "I see. Although that's frustrating, it happens. Did it affect anything else?", 'Chị hiểu. Mặc dù khó chịu nhưng chuyện đó vẫn xảy ra. Nó có ảnh hưởng gì khác không?'),
            ('B', 'Not really. Meanwhile, Huong finished the payment integration, which was tested by QA on Friday.', 'Không hẳn. Trong khi đó, Hương làm xong phần tích hợp thanh toán, đã được QA kiểm thử hôm thứ Sáu.'),
            ('A', 'Great. If the search page is ready by Wednesday, can we include it in the next release?', 'Tuyệt. Nếu trang tìm kiếm xong trước thứ Tư, ta có đưa nó vào bản phát hành tới được không?'),
            ('B', "Yes, unless the client changes the requirements again!", 'Được ạ, trừ khi khách hàng lại đổi yêu cầu!'),
            ('A', "Ha. In that case, I'll talk to them so that the scope is clear before we start.", 'Ha. Vậy thì chị sẽ nói chuyện với họ để phạm vi rõ ràng trước khi bắt đầu.'),
            ('B', "That would help a lot. If we had clear requirements, we'd be much faster.", 'Như vậy sẽ giúp rất nhiều. Nếu có yêu cầu rõ ràng, tụi em sẽ nhanh hơn nhiều.'),
        ],
        'questions': [
            ('Which feature was delayed?', ['Payment integration', 'The search page', 'The login page', 'The filters for payment'], 1, '"However, the search page was delayed."'),
            ('Why was it delayed?', ['A developer was sick.', 'The requirements were changed mid-sprint.', 'QA found bugs.', 'The server crashed.'], 1, '"The requirements were changed in the middle of the sprint."'),
            ('Who tested the payment integration?', ['Binh', 'Laura', 'QA', 'The client'], 2, '"…which was tested by QA on Friday."'),
            ('What will Laura do?', ['Rewrite the filters', 'Talk to the client about the scope', 'Delay the release', 'Hire more developers'], 1, '"I\'ll talk to them so that the scope is clear".'),
        ],
    },
    'speaking': {
        'tips': ['Dùng ít nhất 4 từ nối khác nhau.', 'Kết hợp: một câu điều kiện, một câu bị động, một mệnh đề quan hệ.'],
        'prompts': [
            ('Review your last week at work: what went well and what didn\'t?', 'However, as a result, meanwhile…'),
            ('Compare two programming languages or tools you know.', 'whereas, on the other hand, although'),
            ('What would you change about your workplace if you could?', 'If I could…, I would…'),
        ],
        'model': (
            "Last week went quite well overall. Most of my tasks were finished on time, and the new report page, which I had worked on for two weeks, was finally released. "
            "However, one thing didn't go well. A bug was found in production on Thursday. As a result, I spent the whole afternoon fixing it instead of preparing for the demo. "
            "Meanwhile, my teammate presented the demo alone, although he didn't know the feature very well. "
            "If I had written more tests, the bug would probably have been caught earlier. So this week, I'm going to add tests so that it doesn't happen again.",
            'Nhìn chung tuần trước khá ổn. Phần lớn việc của tôi xong đúng hạn, và trang báo cáo mới, thứ tôi làm suốt hai tuần, cuối cùng đã được phát hành. '
            'Tuy nhiên, có một việc không suôn sẻ. Một lỗi bị phát hiện trên production hôm thứ Năm. Kết quả là tôi mất cả buổi chiều sửa nó thay vì chuẩn bị demo. '
            'Trong khi đó, đồng đội tôi trình bày demo một mình dù không nắm tính năng lắm. '
            'Nếu tôi viết nhiều test hơn, có lẽ lỗi đã bị phát hiện sớm hơn. Vì vậy tuần này tôi sẽ thêm test để chuyện đó không lặp lại.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Short sentences or long sentences?',
        'text': [
            'Many learners believe that long, complex sentences show a high level of English. In fact, the opposite is often true. Clear writers use a mix of short and medium sentences, and they connect their ideas with simple linking words.',
            'Compare these two versions. Version A: "The release, which was planned for Monday but was delayed because the tests, which had been written by a new developer, failed, is now scheduled for Thursday." Version B: "The release was planned for Monday. However, it was delayed because some tests failed. It is now scheduled for Thursday."',
            'Version B is easier to read, and it contains exactly the same information. When you write emails or documentation, aim for sentences of fifteen to twenty words. Use a relative clause or a linking word when it helps the reader, not to look clever.',
        ],
        'vi': 'Nhiều người nghĩ câu dài, phức tạp thể hiện trình độ cao; thực tế thường ngược lại. Người viết rõ ràng kết hợp câu ngắn và vừa, nối ý bằng từ nối đơn giản. Ví dụ bản B tách câu dài thành ba câu ngắn với "However" nên dễ đọc hơn mà vẫn đủ thông tin. Khi viết email/tài liệu, nhắm câu dài 15–20 từ, dùng mệnh đề quan hệ hay từ nối khi giúp người đọc chứ không phải để tỏ ra giỏi.',
        'questions': [
            ('What does the writer say about long, complex sentences?', ['They always show a high level.', 'They are often harder to understand.', 'They are required in emails.', 'They should be used in documentation.'], 1, 'Đoạn 1: "the opposite is often true".'),
            ('How is Version B different from Version A?', ['It has more information.', 'It has the same information in shorter sentences.', 'It uses the passive voice.', 'It is longer.'], 1, 'Đoạn 3.'),
            ('What sentence length does the writer recommend?', ['5–10 words', '15–20 words', '30–40 words', 'As long as possible'], 1, '"aim for sentences of fifteen to twenty words".'),
        ],
    },
    'writing': {
        'task': 'Phần A: Viết lại đúng 3 câu sai bạn từng mắc trong tuần 1–2. Phần B: Viết đoạn 6–8 câu so sánh làm việc ở nhà và ở văn phòng, dùng ít nhất 5 từ nối khác nhau.',
        'tips': ['Không dùng although và but trong cùng một câu.', 'However/Therefore đứng đầu câu, theo sau là dấu phẩy.'],
        'model': "Working from home and working at the office both have advantages. At home, I can focus better because there are fewer distractions. In addition, I don't have to commute, so I save almost two hours a day. On the other hand, I sometimes feel isolated, especially when I don't talk to anyone all day. The office is noisier, whereas home is quiet. However, it's much easier to solve problems face-to-face. Therefore, I think a hybrid model is the best choice, so that I can enjoy the benefits of both.",
        'min_words': 80,
    },
    'quiz': [
        ('If the client ___ the design, we will start next week.', ['approve', 'approves', 'will approve', 'approved'], 1, 'Loại 1: If + hiện tại đơn.'),
        ('If I ___ a manager, I would allow remote work.', ['am', 'were', 'will be', 'have been'], 1, 'Loại 2: If I were…'),
        ('The tool ___ we use for chat is Slack.', ['who', 'where', 'that', 'whose'], 2, 'Chỉ vật, mệnh đề xác định → that/which.'),
        ('The woman ___ laptop was stolen called the police.', ['who', 'whose', 'which', 'that'], 1, 'Sở hữu → whose.'),
        ('All the data ___ every night.', ['backs up', 'is backed up', 'is backing up', 'backed'], 1, 'Bị động hiện tại đơn.'),
        ('The new feature ___ last week.', ['launched', 'was launched', 'has launched', 'is launched'], 1, 'Sản phẩm "được ra mắt" + last week → was launched.'),
        ('___ it was raining, we went to the office.', ['Despite', 'Although', 'However', 'Because'], 1, 'Although + mệnh đề.'),
        ('___ the rain, we went to the office.', ['Although', 'Even though', 'Despite', 'However'], 2, 'Despite + danh từ.'),
        ('The tests failed. ___, we postponed the release.', ['Although', 'Whereas', 'As a result', 'Despite'], 2, 'Kết quả → As a result.'),
        ('I like coffee, ___ my wife prefers tea.', ['therefore', 'whereas', 'despite', 'in addition'], 1, 'Đối lập hai vế → whereas.'),
        ('I left early ___ I could catch the train.', ['so that', 'because of', 'despite', 'however'], 0, 'Mục đích → so that.'),
        ('The flight was cancelled ___ bad weather.', ['because', 'due to', 'although', 'so that'], 1, 'due to + danh từ.'),
        ("We won't deploy ___ the QA team approves it.", ['if', 'unless', 'in case', 'so that'], 1, 'unless = trừ khi.'),
        ('Đuôi -ed trong "decided" đọc là:', ['/t/', '/d/', '/ɪd/'], 2, 'decide kết thúc /d/ → /ɪd/.', 'decided'),
        ('Đuôi -s trong "watches" đọc là:', ['/s/', '/z/', '/ɪz/'], 2, '/tʃ/ → /ɪz/.', 'watches'),
        ('Your password ___ every three months.', ['must change', 'must be changed', 'must changed', 'must changing'], 1, 'Modal + be + V3.'),
        ('Users ___ up before Friday will get a discount.', ['signing', 'signed', 'to sign', 'sign'], 0, 'Rút gọn mệnh đề chủ động → V-ing.'),
        ('Câu nào ĐÚNG?', ['Although it was late, but we continued.', 'Although it was late, we continued.', 'Despite it was late, we continued.', 'However it was late, we continued.'], 1, 'Although + mệnh đề, không kèm but.'),
        ('What would you do if you ___ the lottery?', ['win', 'won', 'will win', 'have won'], 1, 'Loại 2: If + quá khứ đơn.'),
        ('The meeting ___ because the manager is sick.', ['has been cancelled', 'has cancelled', 'was cancelling', 'cancels'], 0, 'Bị động hiện tại hoàn thành: has been cancelled.'),
    ],
}

WEEK = {
    'title': 'Thì nâng cao và câu phức',
    'title_en': 'Advanced Tenses & Complex Sentences',
    'goal': 'Dùng được câu điều kiện, mệnh đề quan hệ và câu bị động trong ngữ cảnh công việc.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
