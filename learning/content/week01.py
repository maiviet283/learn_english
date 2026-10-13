"""Tuần 1 — Nền tảng: ngữ pháp và phát âm."""

DAY1 = {
    'title': 'Đánh giá đầu vào',
    'title_en': 'Your Starting Point',
    'goal': 'Biết chính xác mình đang ở đâu: ghi âm 2 phút tự giới thiệu, làm bài ngữ pháp 20 câu và tự chấm theo 4 tiêu chí. Đây là mốc để so sánh ở tuần 12.',
    'tasks': [
        'Học 14 từ/cụm từ dùng để giới thiệu bản thân.',
        'Đọc phần cấu trúc bài tự giới thiệu, nghe hội thoại mẫu.',
        'Ghi âm 2 phút tự giới thiệu, KHÔNG đọc nháp. Nói sai cũng được — đây là bản đầu vào.',
        'Làm bài ngữ pháp 20 câu (quiz cuối trang), không tra cứu.',
        'Nghe lại bản ghi âm và tự chấm 4 tiêu chí: trôi chảy, từ vựng, ngữ pháp, phát âm.',
    ],
    'product': 'Bản ghi âm đầu vào 2 phút; Bảng điểm tự chấm 4 tiêu chí; Điểm bài ngữ pháp 20 câu',
    'rubric': True,
    'warmup': [
        ("Hi, I'm Minh. Nice to meet you.", 'Chào bạn, mình là Minh. Rất vui được gặp bạn.'),
        ("I'm a software developer based in Hanoi.", 'Mình là lập trình viên, sống và làm việc ở Hà Nội.'),
        ("I've been working in IT for about three years.", 'Mình làm trong ngành IT được khoảng ba năm.'),
        ('In my free time, I like reading and playing badminton.', 'Lúc rảnh, mình thích đọc sách và chơi cầu lông.'),
        ("I'm learning English because I want to work remotely.", 'Mình học tiếng Anh vì muốn làm việc từ xa.'),
        ('My goal is to speak confidently in meetings.', 'Mục tiêu của mình là nói tự tin trong các cuộc họp.'),
    ],
    'vocab': [
        ('introduce yourself', '/ˌɪntrəˈdjuːs jɔːˈself/', 'phrase', 'giới thiệu bản thân', 'Could you briefly introduce yourself?', 'Bạn có thể giới thiệu ngắn gọn về bản thân không?'),
        ('background', '/ˈbækɡraʊnd/', 'n', 'lý lịch, nền tảng (học vấn, kinh nghiệm)', 'I have a background in computer science.', 'Tôi có nền tảng về khoa học máy tính.'),
        ('be based in', '/biː beɪst ɪn/', 'phrase', 'sống/làm việc ở (thành phố nào)', "I'm based in Da Nang, but my company is in Singapore.", 'Tôi ở Đà Nẵng, nhưng công ty tôi ở Singapore.'),
        ('work as', '/wɜːk æz/', 'phrase', 'làm nghề, làm vị trí', 'I work as a backend developer at a fintech startup.', 'Tôi làm lập trình viên backend ở một startup tài chính.'),
        ('currently', '/ˈkʌrəntli/', 'adv', 'hiện tại, hiện nay', "I'm currently working on a mobile banking app.", 'Hiện tôi đang làm một ứng dụng ngân hàng di động.'),
        ('major in', '/ˈmeɪdʒər ɪn/', 'phrasal verb', 'học chuyên ngành', 'I majored in information technology at university.', 'Tôi học chuyên ngành công nghệ thông tin ở đại học.'),
        ('graduate from', '/ˈɡrædʒueɪt frɒm/', 'verb', 'tốt nghiệp (trường nào)', 'She graduated from Hanoi University of Science and Technology.', 'Cô ấy tốt nghiệp Đại học Bách khoa Hà Nội.'),
        ('hometown', '/ˈhəʊmtaʊn/', 'n', 'quê nhà', 'My hometown is a small city near the sea.', 'Quê tôi là một thành phố nhỏ gần biển.'),
        ('be passionate about', '/biː ˈpæʃənət əˈbaʊt/', 'phrase', 'đam mê, rất thích', "I'm passionate about building products that people actually use.", 'Tôi đam mê xây dựng những sản phẩm mà mọi người thực sự dùng.'),
        ('in my free time', '/ɪn maɪ friː taɪm/', 'phrase', 'lúc rảnh rỗi', 'In my free time, I watch tech videos on YouTube.', 'Lúc rảnh, tôi xem video công nghệ trên YouTube.'),
        ('goal', '/ɡəʊl/', 'n', 'mục tiêu', 'My main goal this year is to find a remote job.', 'Mục tiêu chính năm nay của tôi là tìm một công việc từ xa.'),
        ('fluent', '/ˈfluːənt/', 'adj', 'trôi chảy, lưu loát', 'I want to be fluent enough to join daily meetings.', 'Tôi muốn đủ lưu loát để tham gia họp hằng ngày.'),
        ('improve', '/ɪmˈpruːv/', 'verb', 'cải thiện, tiến bộ', 'Recording myself helps me improve my pronunciation.', 'Tự ghi âm giúp tôi cải thiện phát âm.'),
        ('confident', '/ˈkɒnfɪdənt/', 'adj', 'tự tin', "I feel more confident when I've prepared well.", 'Tôi thấy tự tin hơn khi đã chuẩn bị kỹ.'),
    ],
    'lesson': """
<h3>1. Khung bài tự giới thiệu 5 bước</h3>
<p>Một bài giới thiệu tốt không cần câu phức tạp. Nó cần <b>rõ ràng, có thứ tự</b> và nói được mà không nhìn giấy. Hãy đi theo 5 bước:</p>
<table class="table">
<tr><th>Bước</th><th>Nội dung</th><th>Mẫu câu</th></tr>
<tr><td>1. Chào &amp; tên</td><td>Bạn là ai</td><td><span class="say">Hi, I'm Minh. Nice to meet you.</span></td></tr>
<tr><td>2. Công việc</td><td>Làm gì, ở đâu</td><td><span class="say">I work as a backend developer at a startup.</span></td></tr>
<tr><td>3. Nền tảng</td><td>Học gì, bao lâu</td><td><span class="say">I majored in IT and I've been coding for three years.</span></td></tr>
<tr><td>4. Sở thích</td><td>Ngoài công việc</td><td><span class="say">In my free time, I enjoy running and reading.</span></td></tr>
<tr><td>5. Mục tiêu</td><td>Vì sao học tiếng Anh</td><td><span class="say">My goal is to work for an international team.</span></td></tr>
</table>

<h3>2. Lỗi người Việt hay gặp khi tự giới thiệu</h3>
<div class="fix"><s>I am work in a bank.</s><span class="en">I work in a bank.</span><span class="vi">Không dùng "am" cùng động từ thường. Hoặc dùng "I am working…" (đang làm).</span></div>
<div class="fix"><s>I have 28 years old.</s><span class="en">I am 28 years old.</span><span class="vi">Tuổi dùng động từ "be", không dùng "have".</span></div>
<div class="fix"><s>I very like reading books.</s><span class="en">I really like reading books.</span><span class="vi">"very" không đứng trước động từ. Dùng "really like" hoặc "like … very much".</span></div>
<div class="fix"><s>I live in Hanoi since 2018.</s><span class="en">I have lived in Hanoi since 2018.</span><span class="vi">Có "since/for" (kéo dài tới hiện tại) → dùng hiện tại hoàn thành.</span></div>
<div class="fix"><s>My major is Information Technology at university.</s><span class="en">I majored in Information Technology.</span><span class="vi">Gọn và tự nhiên hơn.</span></div>

<h3>3. Bốn tiêu chí tự chấm (1–5 điểm)</h3>
<table class="table">
<tr><th>Tiêu chí</th><th>Câu hỏi để tự chấm</th></tr>
<tr><td><b>Trôi chảy</b> (Fluency)</td><td>Có dừng lâu để tìm từ không? Có "ừm… à…" quá nhiều không? Có nói liền mạch đủ 2 phút không?</td></tr>
<tr><td><b>Từ vựng</b> (Vocabulary)</td><td>Có lặp đi lặp lại vài từ đơn giản không? Có dùng được cụm từ tự nhiên không?</td></tr>
<tr><td><b>Ngữ pháp</b> (Grammar)</td><td>Thì có đúng không? Có thiếu "s" ở ngôi thứ ba, thiếu mạo từ không?</td></tr>
<tr><td><b>Phát âm</b> (Pronunciation)</td><td>Có nuốt âm cuối không? Trọng âm từ có đúng không? Người khác có hiểu ngay không?</td></tr>
</table>
<div class="note"><b>Mẹo:</b> 1 = rất khó hiểu, 3 = hiểu được nhưng nhiều lỗi, 5 = tự nhiên, ít lỗi. Hãy chấm thật lòng — điểm thấp hôm nay chính là thứ giúp bạn thấy mình tiến bộ ở tuần 12.</div>
""",
    'phrases': [
        ('Let me briefly introduce myself.', 'Cho phép tôi giới thiệu ngắn gọn về bản thân.'),
        ("I've been working as a developer for three years.", 'Tôi làm lập trình viên được ba năm.'),
        ('I mainly work with Python and JavaScript.', 'Tôi chủ yếu làm việc với Python và JavaScript.'),
        ("Outside of work, I'm into photography.", 'Ngoài công việc, tôi mê chụp ảnh.'),
        ("That's a bit about me.", 'Đó là đôi nét về tôi.'),
    ],
    'listening': {
        'title': 'First day on a new team',
        'intro': 'Linh vừa vào một team phát triển phần mềm quốc tế. Trưởng nhóm Mark đón cô ấy trong buổi gọi video đầu tiên.',
        'speakers': {'A': ('Mark', 'andrew'), 'B': ('Linh', 'ava')},
        'lines': [
            ('A', 'Hi Linh, welcome to the team! Can you hear me okay?', 'Chào Linh, chào mừng em đến với team! Em nghe anh rõ không?'),
            ('B', 'Hi Mark, yes, I can hear you clearly. Thanks for having me.', 'Chào anh Mark, vâng, em nghe rõ ạ. Cảm ơn anh đã đón em.'),
            ('A', "Great. So, before we start, could you briefly introduce yourself to everyone?", 'Tốt quá. Trước khi bắt đầu, em giới thiệu ngắn gọn về mình với mọi người nhé?'),
            ('B', "Sure. I'm Linh, and I'm based in Ho Chi Minh City. I work as a frontend developer.", 'Vâng. Em là Linh, em ở TP. Hồ Chí Minh. Em làm lập trình viên frontend.'),
            ('B', "I've been working with React for about four years, mostly on e-commerce projects.", 'Em làm với React khoảng bốn năm, chủ yếu là các dự án thương mại điện tử.'),
            ('A', 'Nice. And what did you study at university?', 'Hay đấy. Thế ở đại học em học ngành gì?'),
            ('B', 'I majored in software engineering. I graduated in 2020.', 'Em học chuyên ngành kỹ thuật phần mềm. Em tốt nghiệp năm 2020.'),
            ('A', 'Cool. What do you like doing outside of work?', 'Hay quá. Ngoài giờ làm em thích làm gì?'),
            ('B', "In my free time, I go running and I'm learning to play the guitar.", 'Lúc rảnh em chạy bộ và đang học chơi guitar.'),
            ('A', "That's great. Is there anything you'd like to improve in your first few months?", 'Tuyệt. Có điều gì em muốn cải thiện trong mấy tháng đầu không?'),
            ('B', "Honestly, my English speaking. I can read documents easily, but I'm not very confident in meetings yet.", 'Thật lòng thì là kỹ năng nói tiếng Anh. Em đọc tài liệu dễ dàng nhưng chưa tự tin lắm khi họp.'),
            ('A', "Don't worry, you're doing fine. Just speak slowly and ask us to repeat if you need to.", 'Đừng lo, em đang làm tốt mà. Cứ nói chậm và nhờ mọi người nhắc lại nếu cần nhé.'),
            ('B', 'Thanks, Mark. That really helps.', 'Cảm ơn anh Mark. Điều đó giúp em nhiều lắm.'),
        ],
        'questions': [
            ('Where is Linh based?', ['Hanoi', 'Ho Chi Minh City', 'Singapore', 'Da Nang'], 1, 'Linh nói: "I\'m based in Ho Chi Minh City."'),
            ('How long has Linh been working with React?', ['About two years', 'About three years', 'About four years', 'Since 2018'], 2, '"I\'ve been working with React for about four years."'),
            ('What does Linh want to improve?', ['Her reading skills', 'Her React skills', 'Her English speaking', 'Her guitar playing'], 2, 'Cô ấy nói: "Honestly, my English speaking."'),
            ('What advice does Mark give?', ['Read more documents', 'Speak slowly and ask people to repeat', 'Take an English course', 'Avoid speaking in meetings'], 1, '"Just speak slowly and ask us to repeat if you need to."'),
        ],
    },
    'speaking': {
        'tips': [
            'Nói theo 5 bước ở phần kiến thức. Không cần câu dài — câu ngắn, đúng là đủ.',
            'Không đọc nháp. Quên từ thì nói vòng: "the thing you use to…".',
            'Ghi âm đủ 2 phút, kể cả khi bị ngắt quãng. Đây là bản đầu vào để so sánh với tuần 12.',
        ],
        'prompts': [
            ('Tell me about yourself.', 'Tên, công việc, ở đâu.'),
            ('What do you do, and what are you working on right now?', 'Công việc hiện tại, dự án đang làm.'),
            ('What did you study, and how did you get into IT?', 'Ngành học, lý do vào nghề.'),
            ('What do you enjoy doing in your free time?', 'Sở thích ngoài công việc.'),
            ('Why are you learning English, and what is your goal for the next three months?', 'Lý do học, mục tiêu 3 tháng.'),
        ],
        'model': (
            "Hi, I'm Minh, and I'm a backend developer based in Hanoi. I work for a small software company that builds booking systems for hotels. "
            "I've been working there for almost three years. Most of the time I write APIs in Python, and I also take care of the database. "
            "I majored in information technology, and I got into programming because I loved solving puzzles when I was a kid. "
            "In my free time, I like playing badminton with my friends and reading about new technology. "
            "I'm learning English because I want to join an international team and work remotely. "
            "Right now, I can read documentation quite easily, but speaking is still hard for me. "
            "My goal for the next three months is to speak in meetings without translating in my head.",
            'Chào bạn, mình là Minh, lập trình viên backend ở Hà Nội. Mình làm cho một công ty phần mềm nhỏ chuyên làm hệ thống đặt phòng cho khách sạn. '
            'Mình làm ở đó gần ba năm. Phần lớn thời gian mình viết API bằng Python và lo cả phần cơ sở dữ liệu. '
            'Mình học chuyên ngành công nghệ thông tin, và mình đến với lập trình vì hồi nhỏ rất thích giải đố. '
            'Lúc rảnh, mình thích chơi cầu lông với bạn bè và đọc về công nghệ mới. '
            'Mình học tiếng Anh vì muốn vào một team quốc tế và làm việc từ xa. '
            'Hiện tại mình đọc tài liệu khá dễ, nhưng nói vẫn còn khó. '
            'Mục tiêu ba tháng tới của mình là nói trong cuộc họp mà không phải dịch trong đầu.'
        ),
        'seconds': 120,
    },
    'reading': {
        'title': 'Why you should record yourself',
        'text': [
            'Most English learners never hear their own voice. They practise speaking in their head, or they talk to a teacher once a week. The problem is simple: you cannot fix a mistake that you do not notice.',
            'When you record yourself, you become your own listener. On the first day, the recording may feel uncomfortable. Many people do not like the sound of their voice. That feeling is normal, and it goes away after a week or two.',
            'A recording is also a record of your progress. Progress in speaking is slow, so it is easy to feel that you are not improving. But if you compare a recording from week one with a recording from week twelve, the difference is usually very clear.',
            'Keep your recordings short, about one or two minutes. Listen once for fluency, once for grammar, and once for pronunciation. Write down only the three most common mistakes, and focus on those the next day.',
        ],
        'vi': 'Phần lớn người học không bao giờ nghe giọng của chính mình, nên không thể sửa lỗi mà mình không nhận ra. Khi ghi âm, bạn trở thành người nghe của chính mình. Lúc đầu có thể thấy ngại, nhưng cảm giác đó hết sau một hai tuần. Bản ghi âm cũng là bằng chứng tiến bộ: so sánh tuần 1 với tuần 12 sẽ thấy khác biệt rõ. Hãy ghi âm ngắn 1–2 phút, nghe 3 lần cho 3 tiêu chí, và chỉ ghi lại 3 lỗi lặp lại nhiều nhất.',
        'questions': [
            ('According to the text, why do many learners not improve their speaking?', ['They do not have a teacher.', 'They do not notice their own mistakes.', 'They speak too fast.', 'They record too often.'], 1, 'Đoạn 1: "you cannot fix a mistake that you do not notice."'),
            ('How does the writer describe the uncomfortable feeling of hearing your own voice?', ['It never goes away.', 'It is a sign of bad pronunciation.', 'It is normal and goes away after a week or two.', 'It only happens to beginners.'], 2, 'Đoạn 2: "That feeling is normal, and it goes away after a week or two."'),
            ('How many mistakes does the writer suggest writing down?', ['One', 'Three', 'Five', 'All of them'], 1, 'Đoạn 4: "Write down only the three most common mistakes".'),
        ],
    },
    'writing': {
        'task': 'Viết 5–7 câu giới thiệu bản thân theo khung 5 bước (tên, công việc, nền tảng, sở thích, mục tiêu). Sau đó đọc to đoạn văn của bạn 2 lần.',
        'tips': ['Dùng ít nhất 3 từ trong phần từ vựng hôm nay.', 'Kiểm tra động từ ngôi thứ ba có "s" chưa (he works, she lives).', 'Dùng "I have been + V-ing … for/since" cho việc kéo dài đến hiện tại.'],
        'model': "My name is Minh, and I'm a backend developer based in Hanoi. I currently work for a company that builds booking systems for hotels. I majored in information technology and graduated in 2021. I've been working with Python for about three years. In my free time, I play badminton and read tech blogs. My goal is to become fluent enough to work in an international team.",
        'min_words': 50,
    },
    'quiz': [
        ('She ___ to work by bus every day.', ['go', 'goes', 'is going', 'going'], 1, 'Thói quen hằng ngày → hiện tại đơn; chủ ngữ "she" → goes.'),
        ('Look! The server ___ again.', ['crashes', 'crashed', 'is crashing', 'crash'], 2, '"Look!" → việc đang xảy ra ngay lúc nói → hiện tại tiếp diễn.'),
        ('I ___ in this company since 2021.', ['work', 'am working', 'have worked', 'worked'], 2, '"since 2021" → kéo dài đến hiện tại → hiện tại hoàn thành.'),
        ('We ___ the new feature last Friday.', ['release', 'released', 'have released', 'are releasing'], 1, '"last Friday" là mốc quá khứ đã kết thúc → quá khứ đơn.'),
        ('I am interested ___ learning machine learning.', ['on', 'at', 'in', 'about'], 2, 'Cấu trúc cố định: be interested in.'),
        ('He is ___ engineer with ten years of experience.', ['a', 'an', 'the', '(không cần mạo từ)'], 1, '"engineer" bắt đầu bằng nguyên âm /e/ → an.'),
        ('This laptop is ___ than my old one.', ['fast', 'more fast', 'faster', 'the fastest'], 2, 'Tính từ ngắn so sánh hơn: fast → faster.'),
        ('If it rains tomorrow, we ___ the meeting online.', ['have', 'will have', 'would have', 'had'], 1, 'Câu điều kiện loại 1: If + hiện tại đơn, will + V.'),
        ('The report ___ by the manager every Monday.', ['checks', 'is checked', 'is checking', 'checked'], 1, 'Báo cáo "được kiểm tra" → bị động hiện tại đơn: is checked.'),
        ('I enjoy ___ new things.', ['learn', 'to learn', 'learning', 'learned'], 2, 'enjoy + V-ing.'),
        ('She decided ___ a new job.', ['find', 'to find', 'finding', 'found'], 1, 'decide + to V.'),
        ('The developer ___ wrote this code has left the company.', ['which', 'who', 'where', 'whose'], 1, 'Chỉ người làm chủ ngữ → who.'),
        ('There ___ many bugs in the last release.', ['was', 'were', 'is', 'has'], 1, '"many bugs" số nhiều, "last release" quá khứ → were.'),
        ('I ___ my keys. I can’t find them anywhere.', ['lose', 'lost', 'have lost', 'am losing'], 2, 'Hành động quá khứ có kết quả ở hiện tại (bây giờ không tìm thấy) → have lost.'),
        ('How ___ does this course cost?', ['many', 'much', 'long', 'often'], 1, 'Hỏi giá tiền: How much.'),
        ('We have a meeting ___ Monday morning.', ['in', 'at', 'on', 'by'], 2, 'Ngày trong tuần dùng "on" (on Monday morning).'),
        ('He ___ like coffee. He prefers tea.', ["don't", "doesn't", "isn't", "not"], 1, 'Phủ định hiện tại đơn ngôi thứ ba: doesn\'t + V.'),
        ('If I ___ more time, I would learn Japanese.', ['have', 'had', 'will have', 'would have'], 1, 'Câu điều kiện loại 2 (giả định hiện tại): If + quá khứ đơn.'),
        ('You ___ wear a suit. The meeting is casual.', ["mustn't", "don't have to", "shouldn't to", "can't to"], 1, '"don\'t have to" = không cần thiết. "mustn\'t" = bị cấm.'),
        ('This is the ___ interesting book I have ever read.', ['more', 'most', 'much', 'very'], 1, 'So sánh nhất tính từ dài: the most + adj.'),
    ],
}

DAY2 = {
    'title': 'Thì hiện tại đơn và tiếp diễn',
    'title_en': 'Present Simple vs Present Continuous',
    'goal': 'Dùng đúng hiện tại đơn (thói quen, sự thật) và hiện tại tiếp diễn (việc đang diễn ra, tạm thời); tránh lỗi "I am living here since…".',
    'tasks': [
        'Học 14 từ về công việc hằng ngày.',
        'Ôn cách dùng 2 thì và động từ trạng thái (know, need, want…).',
        'Nghe hội thoại "A typical day", trả lời câu hỏi và chép chính tả.',
        'Làm 15 câu bài tập.',
        'Viết 10 câu về công việc hằng ngày của bạn.',
    ],
    'product': '10 câu tự viết về công việc hằng ngày; Điểm bài tập 15 câu',
    'warmup': [
        ('I usually start work at nine.', 'Tôi thường bắt đầu làm việc lúc chín giờ.'),
        ("I'm working from home this week.", 'Tuần này tôi làm việc ở nhà.'),
        ('We have a stand-up meeting every morning.', 'Sáng nào chúng tôi cũng có cuộc họp đứng.'),
        ("Right now, I'm fixing a bug in the payment page.", 'Ngay lúc này tôi đang sửa một lỗi ở trang thanh toán.'),
        ("She doesn't drink coffee after lunch.", 'Cô ấy không uống cà phê sau bữa trưa.'),
        ('What are you working on at the moment?', 'Hiện tại bạn đang làm gì vậy?'),
    ],
    'vocab': [
        ('commute', '/kəˈmjuːt/', 'verb / n', 'đi làm (quãng đường đi lại hằng ngày)', 'I commute to the office by motorbike.', 'Tôi đi làm bằng xe máy.'),
        ('routine', '/ruːˈtiːn/', 'n', 'thói quen, lịch sinh hoạt cố định', 'My morning routine starts with a cup of tea.', 'Thói quen buổi sáng của tôi bắt đầu bằng một tách trà.'),
        ('usually', '/ˈjuːʒuəli/', 'adv', 'thường thường', 'I usually check my emails before lunch.', 'Tôi thường kiểm tra email trước bữa trưa.'),
        ('at the moment', '/æt ðə ˈməʊmənt/', 'phrase', 'hiện tại, lúc này', "I'm testing the new login page at the moment.", 'Lúc này tôi đang kiểm thử trang đăng nhập mới.'),
        ('deal with', '/diːl wɪð/', 'phrasal verb', 'xử lý, giải quyết', 'I deal with customer tickets every afternoon.', 'Chiều nào tôi cũng xử lý các ticket của khách hàng.'),
        ('be in charge of', '/biː ɪn tʃɑːdʒ əv/', 'phrase', 'phụ trách', "I'm in charge of the database.", 'Tôi phụ trách phần cơ sở dữ liệu.'),
        ('task', '/tɑːsk/', 'n', 'nhiệm vụ, đầu việc', "I've got three tasks to finish today.", 'Hôm nay tôi có ba đầu việc cần xong.'),
        ('priority', '/praɪˈɒrəti/', 'n', 'sự ưu tiên, việc ưu tiên', 'Fixing this bug is our top priority.', 'Sửa lỗi này là ưu tiên hàng đầu của chúng tôi.'),
        ('take a break', '/teɪk ə breɪk/', 'phrase', 'nghỉ giải lao', 'I take a short break every hour.', 'Cứ mỗi giờ tôi nghỉ một chút.'),
        ('work from home', '/wɜːk frəm həʊm/', 'phrase', 'làm việc tại nhà', 'Most of our team works from home on Fridays.', 'Phần lớn team làm việc ở nhà vào thứ Sáu.'),
        ('schedule', '/ˈʃedjuːl/', 'n / verb', 'lịch trình; lên lịch', "Let's schedule a call for Thursday.", 'Hãy lên lịch một cuộc gọi vào thứ Năm.'),
        ('rarely', '/ˈreəli/', 'adv', 'hiếm khi', 'I rarely work at weekends.', 'Tôi hiếm khi làm việc cuối tuần.'),
        ('temporary', '/ˈtemprəri/', 'adj', 'tạm thời', "It's only a temporary solution.", 'Đó chỉ là giải pháp tạm thời.'),
        ('responsible for', '/rɪˈspɒnsəbl fɔː/', 'phrase', 'chịu trách nhiệm về', "I'm responsible for the mobile app.", 'Tôi chịu trách nhiệm về ứng dụng di động.'),
    ],
    'lesson': """
<h3>1. Hiện tại đơn — Present Simple</h3>
<p><b>Công thức:</b> I/You/We/They + V &nbsp;·&nbsp; He/She/It + V-s/es &nbsp;·&nbsp; Phủ định: don't/doesn't + V &nbsp;·&nbsp; Hỏi: Do/Does + S + V?</p>
<p><b>Dùng cho:</b></p>
<ul>
<li>Thói quen, việc lặp lại: <span class="say">I check my emails every morning.</span></li>
<li>Sự thật, điều luôn đúng: <span class="say">Python uses indentation for blocks.</span></li>
<li>Lịch cố định: <span class="say">The sprint starts on Monday.</span></li>
</ul>
<p>Dấu hiệu: always, usually, often, sometimes, rarely, never, every day/week, on Mondays.</p>

<h3>2. Hiện tại tiếp diễn — Present Continuous</h3>
<p><b>Công thức:</b> am/is/are + V-ing</p>
<ul>
<li>Việc đang diễn ra lúc nói: <span class="say">I'm reviewing your pull request now.</span></li>
<li>Việc tạm thời trong giai đoạn này: <span class="say">I'm working on a new project this month.</span></li>
<li>Kế hoạch đã sắp xếp trong tương lai gần: <span class="say">We're meeting the client tomorrow.</span></li>
<li>Xu hướng đang thay đổi: <span class="say">More companies are hiring remote developers.</span></li>
</ul>
<p>Dấu hiệu: now, right now, at the moment, currently, this week, these days, Look!, Listen!</p>

<h3>3. So sánh nhanh</h3>
<table class="table">
<tr><th>Hiện tại đơn</th><th>Hiện tại tiếp diễn</th></tr>
<tr><td><span class="say">I work in Hanoi.</span><br><small>(lâu dài, cố định)</small></td><td><span class="say">I'm working in Hanoi this month.</span><br><small>(tạm thời)</small></td></tr>
<tr><td><span class="say">He usually writes tests first.</span></td><td><span class="say">He's writing tests right now.</span></td></tr>
<tr><td><span class="say">What do you do?</span><br><small>(Bạn làm nghề gì?)</small></td><td><span class="say">What are you doing?</span><br><small>(Bạn đang làm gì?)</small></td></tr>
</table>

<h3>4. Động từ trạng thái — không dùng tiếp diễn</h3>
<p>Các động từ chỉ suy nghĩ, cảm xúc, sở hữu, giác quan thường <b>không</b> chia tiếp diễn: <i>know, understand, believe, need, want, like, love, hate, prefer, own, belong, seem, mean</i>.</p>
<div class="fix"><s>I am knowing the answer.</s><span class="en">I know the answer.</span></div>
<div class="fix"><s>We are needing more time.</s><span class="en">We need more time.</span></div>

<h3>5. Lỗi kinh điển: "since/for" với thì hiện tại</h3>
<div class="fix"><s>I am living here since 2020.</s><span class="en">I have lived here since 2020.</span><span class="vi">Việc bắt đầu trong quá khứ và kéo dài tới bây giờ → hiện tại hoàn thành (hoặc "I have been living here since 2020").</span></div>
<div class="fix"><s>I work here for two years.</s><span class="en">I have worked here for two years.</span></div>
<div class="note"><b>Ghi nhớ:</b> Tiếng Việt không chia thì, nên ta hay nói "Tôi sống ở đây từ 2020" → dịch thẳng thành hiện tại đơn. Cứ thấy <b>since/for + kéo dài đến nay</b> là nghĩ ngay tới <b>have + V3</b>.</div>
""",
    'phrases': [
        ('What does a typical day look like for you?', 'Một ngày điển hình của bạn trông thế nào?'),
        ("I'm currently working on…", 'Hiện tôi đang làm…'),
        ('Most of my day is spent on…', 'Phần lớn thời gian trong ngày tôi dành cho…'),
        ('I tend to…', 'Tôi có xu hướng / thường…'),
        ('These days, I’m focusing on…', 'Dạo này tôi đang tập trung vào…'),
    ],
    'listening': {
        'title': 'A typical day',
        'intro': 'Hai đồng nghiệp mới quen nói chuyện về một ngày làm việc của họ.',
        'speakers': {'A': ('Sarah', 'emma'), 'B': ('Tuan', 'brian')},
        'lines': [
            ('A', 'So Tuan, what does a typical day look like for you?', 'Tuấn này, một ngày điển hình của bạn thế nào?'),
            ('B', 'Well, I usually start at eight thirty. The first thing I do is check Slack and my emails.', 'À, mình thường bắt đầu lúc tám rưỡi. Việc đầu tiên là xem Slack và email.'),
            ('B', 'Then we have our daily stand-up at nine.', 'Sau đó tụi mình có buổi stand-up hằng ngày lúc chín giờ.'),
            ('A', 'Do you work from home or at the office?', 'Bạn làm ở nhà hay ở văn phòng?'),
            ('B', "Normally I go to the office, but this week I'm working from home because my son is sick.", 'Bình thường mình lên văn phòng, nhưng tuần này mình làm ở nhà vì con trai bị ốm.'),
            ('A', "Oh, I'm sorry to hear that. I hope he gets better soon.", 'Ồ, tiếc quá. Mong bé sớm khỏe lại.'),
            ('B', "Thanks. He's feeling much better today.", 'Cảm ơn bạn. Hôm nay bé đỡ nhiều rồi.'),
            ('A', 'And what are you working on at the moment?', 'Thế dạo này bạn đang làm gì?'),
            ('B', "I'm building a new search feature. It's taking longer than we expected.", 'Mình đang làm tính năng tìm kiếm mới. Nó tốn thời gian hơn tụi mình dự tính.'),
            ('A', 'What usually takes the most time?', 'Thường thì việc gì tốn thời gian nhất?'),
            ('B', 'Testing, definitely. I write tests for everything, so it takes a while.', 'Chắc chắn là kiểm thử. Mình viết test cho mọi thứ nên khá lâu.'),
            ('A', 'That sounds like a good habit. Do you ever work late?', 'Nghe là thói quen tốt đấy. Bạn có bao giờ làm muộn không?'),
            ('B', 'Rarely. I try to stop at six and spend the evening with my family.', 'Hiếm lắm. Mình cố gắng dừng lúc sáu giờ để buổi tối dành cho gia đình.'),
        ],
        'questions': [
            ('What does Tuan do first every morning?', ['He joins the stand-up.', 'He checks Slack and his emails.', 'He writes tests.', 'He takes his son to school.'], 1, '"The first thing I do is check Slack and my emails."'),
            ('Why is Tuan working from home this week?', ['His office is closed.', 'He prefers it.', 'His son is sick.', 'He is on holiday.'], 2, '"…this week I\'m working from home because my son is sick." — việc tạm thời → hiện tại tiếp diễn.'),
            ('What is Tuan working on at the moment?', ['A payment page', 'A search feature', 'A mobile app', 'A testing tool'], 1, '"I\'m building a new search feature."'),
            ('How often does Tuan work late?', ['Every day', 'Often', 'Rarely', 'Never'], 2, '"Rarely. I try to stop at six…"'),
        ],
    },
    'speaking': {
        'tips': ['Dùng hiện tại đơn cho lịch cố định, tiếp diễn cho việc đang làm tuần này.', 'Dùng từ nối: first, then, after that, in the afternoon, finally.'],
        'prompts': [
            ('What does a typical working day look like for you?', 'Kể theo thứ tự thời gian: sáng → trưa → chiều.'),
            ('What are you working on at the moment?', 'Dự án/đầu việc hiện tại.'),
            ('What do you usually do after work?', 'Thói quen buổi tối.'),
            ('Is anything different in your life these days?', 'Thay đổi tạm thời: dùng tiếp diễn.'),
        ],
        'model': (
            "On a typical day, I wake up at seven and I usually get to work at around eight thirty. "
            "First, I check my messages and plan my tasks for the day. At nine, we have a short stand-up meeting. "
            "Most of my morning is spent writing code, because that's when I can focus best. "
            "After lunch, I usually review my teammates' pull requests and deal with small bugs. "
            "These days, I'm working on a reporting feature for our admin dashboard, so I'm learning a lot about charts. "
            "I rarely stay late. I try to finish at six and then I go for a run or study English for an hour.",
            'Một ngày bình thường, tôi dậy lúc bảy giờ và thường đến chỗ làm khoảng tám rưỡi. '
            'Đầu tiên tôi xem tin nhắn và lên kế hoạch công việc trong ngày. Chín giờ có buổi stand-up ngắn. '
            'Phần lớn buổi sáng tôi viết code vì đó là lúc tôi tập trung tốt nhất. '
            'Sau bữa trưa, tôi thường review pull request của đồng đội và xử lý các lỗi nhỏ. '
            'Dạo này tôi đang làm tính năng báo cáo cho trang quản trị nên học được nhiều về biểu đồ. '
            'Tôi hiếm khi ở lại muộn. Tôi cố gắng xong lúc sáu giờ rồi đi chạy bộ hoặc học tiếng Anh một tiếng.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'How remote developers organise their day',
        'text': [
            'Working from home sounds easy, but many developers find it hard to stay focused. Without a commute or an office, the line between work and life becomes blurry. That is why most successful remote developers follow a clear routine.',
            'A common pattern is to protect the morning for "deep work". Developers turn off notifications, close their chat apps and work on the most difficult task first. Meetings and messages usually wait until the afternoon.',
            'Another habit is to write a short plan at the start of the day and a short summary at the end. The summary takes only five minutes, but it helps teammates in other time zones know what is happening.',
            'Finally, good remote workers take real breaks. They stand up, walk around or go outside. Sitting in front of a screen for ten hours does not make you more productive; it usually makes you more tired.',
        ],
        'vi': 'Làm việc ở nhà nghe có vẻ dễ nhưng nhiều lập trình viên khó tập trung vì ranh giới giữa công việc và cuộc sống bị mờ đi. Người làm remote giỏi thường có thói quen rõ ràng: dành buổi sáng cho "làm việc sâu" (tắt thông báo, làm việc khó nhất trước), viết kế hoạch đầu ngày và tóm tắt cuối ngày để đồng đội ở múi giờ khác nắm được tình hình, và nghỉ giải lao thực sự thay vì ngồi lì trước màn hình.',
        'questions': [
            ('Why do many remote developers find it hard to focus?', ['They have long commutes.', 'Work and life are not clearly separated.', 'They have too many meetings in the morning.', 'Their teammates are in other countries.'], 1, 'Đoạn 1: "the line between work and life becomes blurry".'),
            ('What do many developers do in the morning?', ['Answer messages', 'Join meetings', 'Work on the hardest task', 'Write a summary'], 2, 'Đoạn 2: "work on the most difficult task first".'),
            ('Why is the end-of-day summary useful?', ['It helps teammates in other time zones.', 'It replaces meetings.', 'Managers require it.', 'It takes a long time.'], 0, 'Đoạn 3: "it helps teammates in other time zones know what is happening".'),
        ],
    },
    'writing': {
        'task': 'Viết 10 câu về công việc hằng ngày của bạn: 6 câu dùng hiện tại đơn (thói quen), 4 câu dùng hiện tại tiếp diễn (việc đang làm dạo này).',
        'tips': ['Dùng trạng từ tần suất: always, usually, often, sometimes, rarely.', 'Thêm một câu với "since" hoặc "for" và nhớ dùng have + V3.'],
        'model': "I usually wake up at 6:30 and have breakfast with my family. I commute to the office by motorbike, which takes about twenty minutes. I always check my emails before the stand-up meeting. I'm in charge of the payment service, so I deal with a lot of bug reports. I rarely have time for a long lunch. I often review code in the afternoon. This month, I'm working on a new checkout page. I'm also learning Docker because our team is moving to containers. These days, I'm trying to go to bed earlier. I'm studying English for ninety minutes every evening, and I have worked here since 2022.",
        'min_words': 80,
    },
    'quiz': [
        ('Water ___ at 100 degrees Celsius.', ['boil', 'boils', 'is boiling', 'boiled'], 1, 'Sự thật khoa học → hiện tại đơn; "water" là ngôi thứ ba số ít → boils.'),
        ("Please be quiet. I ___ on a call.", ['am', 'have', 'do', 'was'], 0, '"I\'m on a call" = đang trong cuộc gọi; câu nói về lúc này.'),
        ('She ___ in the marketing team, but this month she ___ with us.', ['works / is working', 'is working / works', 'work / works', 'works / works'], 0, 'Cố định → works; tạm thời tháng này → is working.'),
        ('I ___ what you mean.', ['am understanding', 'understand', 'understanding', 'am understand'], 1, '"understand" là động từ trạng thái → không dùng tiếp diễn.'),
        ('How often ___ you deploy to production?', ['are', 'do', 'does', 'have'], 1, 'Hỏi tần suất, chủ ngữ "you" → do.'),
        ('Our team ___ a new member next week.', ['is welcoming', 'welcome', 'welcomed', 'has welcomed'], 0, 'Kế hoạch đã sắp xếp cho tương lai gần → hiện tại tiếp diễn.'),
        ("He ___ coffee. He's allergic to caffeine.", ["isn't drinking", "doesn't drink", "don't drink", "not drink"], 1, 'Sự thật/thói quen → hiện tại đơn phủ định ngôi ba: doesn\'t drink.'),
        ('Prices ___ every year.', ['rise', 'are rise', 'rises', 'is rising'], 0, 'Xu hướng chung lặp lại hằng năm → hiện tại đơn; "prices" số nhiều → rise.'),
        ('I ___ here since I graduated.', ['work', 'am working', 'have worked', 'working'], 2, '"since I graduated" → hiện tại hoàn thành.'),
        ('Listen! Someone ___ at the door.', ['knocks', 'is knocking', 'knock', 'knocked'], 1, '"Listen!" → đang diễn ra lúc nói.'),
        ('This box ___ to my colleague.', ['is belonging', 'belongs', 'belong', 'are belonging'], 1, '"belong" là động từ trạng thái → hiện tại đơn.'),
        ('What ___ she do? — She is a data analyst.', ['is', 'does', 'do', 'has'], 1, '"What does she do?" hỏi nghề nghiệp.'),
        ('More and more people ___ online these days.', ['shop', 'are shopping', 'shops', 'shopped'], 1, 'Xu hướng đang thay đổi ("these days") → hiện tại tiếp diễn.'),
        ('I usually ___ to work, but today I ___ a taxi.', ['walk / am taking', 'am walking / take', 'walk / take', 'walks / am taking'], 0, 'Thói quen → walk; hôm nay khác thường → am taking.'),
        ('The train to Hai Phong ___ at 6 a.m. tomorrow.', ['leave', 'leaves', 'is leave', 'leaving'], 1, 'Lịch trình cố định (tàu, xe, sự kiện) → hiện tại đơn dù nói về tương lai.'),
    ],
}

DAY3 = {
    'title': 'Phát âm: nguyên âm ngắn và dài',
    'title_en': 'Short and Long Vowels',
    'goal': 'Đọc được ký hiệu IPA cơ bản; phân biệt và phát âm rõ /ɪ/–/iː/, /æ/–/e/, /ʌ/–/ɑː/, /ʊ/–/uː/.',
    'tasks': [
        'Học bảng nguyên âm IPA và cách đặt miệng.',
        'Nghe và luyện 7 cặp từ tối thiểu (ship/sheep, bit/beat, bad/bed…).',
        'Làm bài "nghe chọn từ đúng" — bật âm thanh và chọn từ bạn nghe được.',
        'Ghi âm đọc 10 cặp từ, nghe lại và tự sửa.',
    ],
    'product': 'Bản ghi âm đọc 10 cặp từ; Điểm bài nghe chọn từ',
    'warmup': [
        ('Please sit in this seat.', 'Mời ngồi vào ghế này.'),
        ('The ship carries sheep.', 'Con tàu chở cừu.'),
        ("Don't leave. Live here with us.", 'Đừng đi. Ở lại đây với chúng tôi.'),
        ('The man and the men went to the market.', 'Người đàn ông và những người đàn ông đã đi chợ.'),
        ('I bought a cup and a cap.', 'Tôi mua một cái cốc và một cái mũ lưỡi trai.'),
        ('Look at the full moon. It looks like a pool.', 'Nhìn trăng tròn kìa. Nó trông như một cái hồ.'),
    ],
    'vocab': [
        ('ship', '/ʃɪp/', 'n', 'con tàu', 'We ship new features every two weeks.', 'Chúng tôi phát hành tính năng mới mỗi hai tuần. (ship còn có nghĩa "phát hành")'),
        ('sheep', '/ʃiːp/', 'n', 'con cừu', 'There are many sheep on the farm.', 'Có nhiều cừu ở trang trại.'),
        ('live', '/lɪv/', 'verb', 'sống', 'I live in a small apartment.', 'Tôi sống trong một căn hộ nhỏ.'),
        ('leave', '/liːv/', 'verb', 'rời đi, để lại', 'I leave the office at six.', 'Tôi rời văn phòng lúc sáu giờ.'),
        ('bit', '/bɪt/', 'n', 'một chút; bit (máy tính)', "I'm a bit tired today.", 'Hôm nay tôi hơi mệt một chút.'),
        ('beat', '/biːt/', 'verb', 'đánh bại; nhịp', 'Our app beat the competition.', 'Ứng dụng của chúng tôi đánh bại đối thủ.'),
        ('bad', '/bæd/', 'adj', 'tệ, xấu', "It wasn't a bad idea.", 'Đó không phải ý tồi.'),
        ('bed', '/bed/', 'n', 'cái giường', 'I went to bed late last night.', 'Tối qua tôi đi ngủ muộn.'),
        ('cap', '/kæp/', 'n', 'mũ lưỡi trai; giới hạn', 'There is a cap on API requests.', 'Có giới hạn số lượng request API.'),
        ('cup', '/kʌp/', 'n', 'cái cốc, tách', 'Would you like a cup of tea?', 'Bạn có muốn một tách trà không?'),
        ('full', '/fʊl/', 'adj', 'đầy', 'The disk is almost full.', 'Ổ đĩa gần đầy rồi.'),
        ('fool', '/fuːl/', 'n', 'kẻ ngốc', "Don't be fooled by simple code.", 'Đừng để code đơn giản đánh lừa.'),
        ('heart', '/hɑːt/', 'n', 'trái tim; cốt lõi', 'The database is the heart of the system.', 'Cơ sở dữ liệu là trái tim của hệ thống.'),
        ('hut', '/hʌt/', 'n', 'túp lều', 'They stayed in a small hut in the mountains.', 'Họ ở trong một túp lều nhỏ trên núi.'),
    ],
    'lesson': """
<h3>1. Vì sao nguyên âm quan trọng?</h3>
<p>Người Việt hay nói tất cả nguyên âm "dài như nhau", nên <span class="say">ship</span> nghe thành <span class="say">sheep</span>, <span class="say">live</span> thành <span class="say">leave</span>. Người nghe phải đoán nghĩa theo ngữ cảnh và rất nhanh mệt. Chỉ cần sửa 4 cặp dưới đây, bạn sẽ dễ nghe hơn rất nhiều.</p>

<h3>2. Bốn cặp nguyên âm cần nắm</h3>
<table class="table">
<tr><th>Âm ngắn</th><th>Cách phát âm</th><th>Âm dài</th><th>Cách phát âm</th></tr>
<tr><td><b>/ɪ/</b> <span class="say">ship</span>, <span class="say">bit</span>, <span class="say">live</span></td><td>Ngắn, thả lỏng, giữa "i" và "ê" của tiếng Việt.</td><td><b>/iː/</b> <span class="say">sheep</span>, <span class="say">beat</span>, <span class="say">leave</span></td><td>Kéo dài, miệng cười căng sang hai bên.</td></tr>
<tr><td><b>/e/</b> <span class="say">bed</span>, <span class="say">men</span>, <span class="say">set</span></td><td>Giống "e" tiếng Việt, miệng mở vừa.</td><td><b>/æ/</b> <span class="say">bad</span>, <span class="say">man</span>, <span class="say">sat</span></td><td>Mở miệng rộng, hạ hàm xuống, giữa "e" và "a".</td></tr>
<tr><td><b>/ʌ/</b> <span class="say">cup</span>, <span class="say">hut</span>, <span class="say">much</span></td><td>Ngắn, giống "ă" tiếng Việt.</td><td><b>/ɑː/</b> <span class="say">heart</span>, <span class="say">car</span>, <span class="say">start</span></td><td>Dài, mở miệng rộng, lưỡi thấp, giống "a" kéo dài.</td></tr>
<tr><td><b>/ʊ/</b> <span class="say">full</span>, <span class="say">look</span>, <span class="say">book</span></td><td>Ngắn, môi tròn nhẹ, giống "ư/u" ngắn.</td><td><b>/uː/</b> <span class="say">fool</span>, <span class="say">food</span>, <span class="say">pool</span></td><td>Dài, môi tròn và chu ra.</td></tr>
</table>

<h3>3. Mẹo luyện tập</h3>
<ul>
<li>Bấm vào từng từ để nghe. Nghe <b>cặp</b> liên tiếp (ship → sheep) để tai nhận ra sự khác biệt.</li>
<li>Nhìn gương: âm dài /iː/ miệng căng như cười; âm /æ/ cằm hạ xuống thấy rõ.</li>
<li>Phóng đại khi luyện (kéo /iː/ thật dài). Khi nói thật, tự nhiên sẽ vừa phải.</li>
<li>Âm dài thường được viết bằng <b>ee, ea, oo, ar</b>: s<b>ee</b>, t<b>ea</b>m, f<b>oo</b>d, c<b>ar</b>.</li>
</ul>

<h3>4. Cặp từ trong ngữ cảnh công việc</h3>
<div class="ex"><span class="en">Can you fill in this form, please? Then we can feel confident about the data.</span><span class="vi">/ɪ/ fill – /iː/ feel</span></div>
<div class="ex"><span class="en">I'll fix the bug before I leave. I live near the office.</span><span class="vi">/ɪ/ fix, live – /iː/ leave</span></div>
<div class="ex"><span class="en">The man said the men need a bigger desk.</span><span class="vi">/æ/ man – /e/ men, desk</span></div>
<div class="warn"><b>Chú ý:</b> <span class="say">sheet</span> và <span class="say">beach</span> phải là âm dài /iː/. Nói ngắn thành /ɪ/ sẽ thành một từ thô tục. Đây là lý do cần luyện kỹ cặp /ɪ/–/iː/!</div>
""",
    'phrases': [
        ('Could you say that word again, please?', 'Bạn có thể nói lại từ đó được không?'),
        ('How do you pronounce this word?', 'Từ này phát âm thế nào?'),
        ('Is it a long or a short sound?', 'Đó là âm dài hay âm ngắn?'),
        ('Did you say "ship" or "sheep"?', 'Bạn nói "ship" hay "sheep"?'),
    ],
    'listening': {
        'title': 'At the coffee machine',
        'intro': 'Một đoạn hội thoại ngắn chứa nhiều cặp âm ngắn–dài. Nghe kỹ các từ in đậm trong lời thoại.',
        'speakers': {'A': ('Jim', 'brian'), 'B': ('Lily', 'jenny')},
        'lines': [
            ('A', 'Hi Lily. Do you want a cup of tea or coffee?', 'Chào Lily. Bạn muốn một tách trà hay cà phê?'),
            ('B', "Tea, please. I've already had three cups of coffee today.", 'Trà nhé. Hôm nay mình uống ba cốc cà phê rồi.'),
            ('A', 'Wow. Are you feeling okay? You look a bit tired.', 'Chà. Bạn ổn chứ? Trông bạn hơi mệt.'),
            ('B', "I didn't sleep well. I had to fix a bug until midnight.", 'Mình ngủ không ngon. Mình phải sửa lỗi đến nửa đêm.'),
            ('A', 'That sounds bad. Was it a big bug?', 'Nghe tệ thật. Lỗi lớn à?'),
            ('B', 'Not really, but it was hard to find. It was in a file I had never seen before.', 'Không hẳn, nhưng khó tìm. Nó nằm trong một file mình chưa từng thấy.'),
            ('A', 'Are you going to leave early today?', 'Hôm nay bạn có về sớm không?'),
            ('B', "I hope so. If I can, I'll leave at four and go straight to bed.", 'Mình hy vọng thế. Nếu được thì bốn giờ mình về và đi ngủ luôn.'),
            ('A', 'Good idea. Enjoy your tea, and take it easy.', 'Ý hay đấy. Thưởng thức trà đi, và cứ thong thả nhé.'),
        ],
        'questions': [
            ('What does Lily drink?', ['Coffee', 'Tea', 'Water', 'Nothing'], 1, '"Tea, please."'),
            ('Why is Lily tired?', ['She worked until midnight fixing a bug.', 'She drank too much coffee.', 'She had a long commute.', 'She went to a party.'], 0, '"I had to fix a bug until midnight."'),
            ('What does Lily want to do after work?', ['Go to the gym', 'Have dinner with Jim', 'Go straight to bed', 'Fix another bug'], 2, '"…go straight to bed."'),
        ],
    },
    'speaking': {
        'tips': ['Đọc mỗi cặp 3 lần: chậm → bình thường → trong câu.', 'Ghi âm, nghe lại: người khác có phân biệt được hai từ trong cặp không?'],
        'prompts': [
            ('Read the 10 pairs: ship–sheep, bit–beat, live–leave, fill–feel, bad–bed, man–men, cup–cap, hut–heart, full–fool, look–Luke.', 'Đọc chậm từng cặp, phóng đại âm dài.'),
            ('Say: "I live near the office, so I leave at six."', 'Phân biệt live /ɪ/ – leave /iː/.'),
            ('Say: "The man said the men had a bad bed."', 'Phân biệt /æ/ – /e/.'),
            ('Say: "Look at the pool. It is full of fools."', 'Phân biệt /ʊ/ – /uː/.'),
        ],
        'model': (
            "I live in a small flat, and I leave for work at eight. "
            "I sit in the same seat on the bus every day. "
            "At the office, I fix bugs and feel happy when the tests pass. "
            "My manager is a kind man, and the men in my team are friendly. "
            "At lunch, I have a cup of soup and a piece of fruit. "
            "In the evening, I look at my notes and choose good food for dinner.",
            'Tôi sống trong một căn hộ nhỏ và đi làm lúc tám giờ. '
            'Ngày nào tôi cũng ngồi cùng một ghế trên xe buýt. '
            'Ở văn phòng, tôi sửa lỗi và thấy vui khi test chạy qua. '
            'Quản lý của tôi là một người tốt bụng, và các anh trong team đều thân thiện. '
            'Bữa trưa tôi ăn một bát súp và một miếng trái cây. '
            'Buổi tối tôi xem lại ghi chú và chọn đồ ăn ngon cho bữa tối.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Reading IPA in a dictionary',
        'text': [
            'Every good dictionary shows how a word is pronounced using the International Phonetic Alphabet, or IPA. At first, the symbols look strange, but you only need to learn about forty of them, and many look like normal letters.',
            'The colon-like symbol ː after a vowel means the sound is long. So /iː/ in "sheep" is longer than /ɪ/ in "ship". The small mark ˈ shows which syllable is stressed. In /ˈkʌmpəni/, the stress is on the first syllable: COM-pa-ny.',
            'When you learn a new word, check its IPA and listen to the audio at the same time. After a few weeks, you will be able to guess the pronunciation of new words just by looking at the symbols, even without audio.',
        ],
        'vi': 'Từ điển dùng bảng ký hiệu IPA để ghi cách phát âm. Chỉ cần học khoảng 40 ký hiệu. Dấu ː sau nguyên âm nghĩa là âm dài (/iː/ dài hơn /ɪ/). Dấu ˈ đánh dấu âm tiết mang trọng âm. Khi học từ mới, hãy xem IPA và nghe audio cùng lúc; vài tuần sau bạn có thể đoán cách đọc chỉ bằng ký hiệu.',
        'questions': [
            ('What does the symbol ː mean?', ['The word is stressed.', 'The vowel is long.', 'The word is a noun.', 'The sound is silent.'], 1, '"The colon-like symbol ː after a vowel means the sound is long."'),
            ('In /ˈkʌmpəni/, which syllable is stressed?', ['The first', 'The second', 'The third', 'None'], 0, 'Dấu ˈ đứng trước âm tiết đầu: COM-pa-ny.'),
            ('What does the writer suggest when you learn a new word?', ['Only read the IPA', 'Only listen to the audio', 'Check the IPA and listen to the audio together', 'Ask a teacher'], 2, '"check its IPA and listen to the audio at the same time".'),
        ],
    },
    'writing': {
        'task': 'Viết 5 câu, mỗi câu chứa một cặp từ tối thiểu (ví dụ: "I live near the office, so I can leave late."). Đọc to từng câu và ghi âm.',
        'tips': ['Gạch chân hai từ trong cặp.', 'Câu càng gần công việc thực tế càng dễ nhớ.'],
        'model': "I live near the office, so I usually leave at six.\nI fixed a bit of the code to beat the deadline.\nThe man and the other men in my team work hard.\nI drank a cup of coffee and put on my cap.\nThe disk is full, so don't be a fool — delete old logs.",
        'min_words': 30,
    },
    'quiz': [
        ('Nghe và chọn từ bạn nghe được.', ['ship', 'sheep'], 1, 'Âm dài /iː/ → sheep.', 'sheep'),
        ('Nghe và chọn từ bạn nghe được.', ['live', 'leave'], 0, 'Âm ngắn /ɪ/ → live.', 'live'),
        ('Nghe và chọn từ bạn nghe được.', ['bad', 'bed'], 1, '/e/ → bed.', 'bed'),
        ('Nghe và chọn từ bạn nghe được.', ['bit', 'beat'], 1, '/iː/ → beat.', 'beat'),
        ('Nghe và chọn từ bạn nghe được.', ['cup', 'cap'], 0, '/ʌ/ → cup.', 'cup'),
        ('Nghe và chọn từ bạn nghe được.', ['full', 'fool'], 1, '/uː/ → fool.', 'fool'),
        ('Nghe và chọn từ bạn nghe được.', ['man', 'men'], 0, '/æ/ → man.', 'man'),
        ('Nghe và chọn từ bạn nghe được.', ['fill', 'feel'], 0, '/ɪ/ → fill.', 'fill'),
        ('Nghe và chọn từ bạn nghe được.', ['hut', 'heart'], 1, '/ɑː/ → heart.', 'heart'),
        ('Nghe và chọn từ bạn nghe được.', ['sit', 'seat'], 1, '/iː/ → seat.', 'seat'),
        ('Từ nào có nguyên âm dài /iː/?', ['big', 'team', 'list', 'fix'], 1, 'team /tiːm/ — "ea" thường đọc /iː/.'),
        ('Từ nào có nguyên âm /æ/?', ['said', 'cat', 'cut', 'cart'], 1, 'cat /kæt/.'),
        ('Từ nào có nguyên âm ngắn /ʊ/?', ['food', 'pool', 'book', 'blue'], 2, 'book /bʊk/; food, pool, blue đều là /uː/.'),
        ('Trong IPA /ˈprɒdʌkt/, trọng âm rơi vào âm tiết nào?', ['pro', 'duct', 'Cả hai', 'Không có'], 0, 'Dấu ˈ đứng trước "pro" → PRO-duct.'),
    ],
}

DAY4 = {
    'title': 'Quá khứ đơn và hiện tại hoàn thành',
    'title_en': 'Past Simple vs Present Perfect',
    'goal': 'Phân biệt quá khứ đơn (việc đã xong, có thời điểm cụ thể) và hiện tại hoàn thành (kinh nghiệm, kết quả, kéo dài đến nay); dùng đúng for, since, already, yet, ever, never, just.',
    'tasks': [
        'Học 14 từ về kinh nghiệm và thành tựu.',
        'Ôn cách dùng 2 thì và các trạng từ đi kèm.',
        'Nghe đoạn phỏng vấn ngắn về kinh nghiệm làm việc.',
        'Làm quiz 15 câu.',
        'Viết 8 câu về kinh nghiệm cá nhân.',
    ],
    'product': '8 câu về kinh nghiệm cá nhân; Điểm quiz',
    'warmup': [
        ("I've worked with Python for five years.", 'Tôi đã làm việc với Python được năm năm.'),
        ('I started my first job in 2019.', 'Tôi bắt đầu công việc đầu tiên năm 2019.'),
        ('Have you ever worked with a foreign team?', 'Bạn đã bao giờ làm việc với team nước ngoài chưa?'),
        ("I haven't finished the report yet.", 'Tôi chưa làm xong báo cáo.'),
        ('We launched the app last month.', 'Chúng tôi ra mắt ứng dụng tháng trước.'),
        ("She's just pushed a fix.", 'Cô ấy vừa đẩy bản sửa lỗi lên.'),
    ],
    'vocab': [
        ('experience', '/ɪkˈspɪəriəns/', 'n', 'kinh nghiệm; trải nghiệm', 'I have some experience with cloud services.', 'Tôi có chút kinh nghiệm với dịch vụ đám mây.'),
        ('achieve', '/əˈtʃiːv/', 'verb', 'đạt được', 'We achieved our goal two weeks early.', 'Chúng tôi đạt mục tiêu sớm hai tuần.'),
        ('achievement', '/əˈtʃiːvmənt/', 'n', 'thành tựu', 'Passing the exam was a big achievement for me.', 'Thi đỗ là một thành tựu lớn với tôi.'),
        ('launch', '/lɔːntʃ/', 'verb / n', 'ra mắt, khởi chạy', 'They launched the new version yesterday.', 'Họ ra mắt phiên bản mới hôm qua.'),
        ('complete', '/kəmˈpliːt/', 'verb', 'hoàn thành', "I've completed three online courses this year.", 'Năm nay tôi đã hoàn thành ba khóa học online.'),
        ('so far', '/səʊ fɑː/', 'phrase', 'cho đến nay', "So far, we haven't had any complaints.", 'Đến giờ chúng tôi chưa nhận lời phàn nàn nào.'),
        ('recently', '/ˈriːsntli/', 'adv', 'gần đây', "I've recently moved to a new team.", 'Gần đây tôi chuyển sang một team mới.'),
        ('manage to', '/ˈmænɪdʒ tə/', 'phrase', 'xoay xở được, làm được (việc khó)', 'We managed to fix the issue before the demo.', 'Chúng tôi xoay xở sửa được lỗi trước buổi demo.'),
        ('lead', '/liːd/', 'verb', 'dẫn dắt, lãnh đạo (quá khứ: led)', 'I led a team of four developers last year.', 'Năm ngoái tôi dẫn dắt một team bốn lập trình viên.'),
        ('join', '/dʒɔɪn/', 'verb', 'gia nhập, tham gia', 'I joined the company in 2022.', 'Tôi vào công ty năm 2022.'),
        ('career', '/kəˈrɪə/', 'n', 'sự nghiệp', "I've changed my career path twice.", 'Tôi đã đổi hướng sự nghiệp hai lần.'),
        ('milestone', '/ˈmaɪlstəʊn/', 'n', 'cột mốc', 'Reaching 10,000 users was an important milestone.', 'Đạt 10.000 người dùng là một cột mốc quan trọng.'),
        ('used to', '/ˈjuːst tə/', 'phrase', 'đã từng (nay không còn)', 'I used to work as a tester.', 'Tôi từng làm tester.'),
        ('since then', '/sɪns ðen/', 'phrase', 'kể từ đó', "I moved to Hanoi in 2018, and I've lived here since then.", 'Tôi chuyển đến Hà Nội năm 2018 và sống ở đây từ đó.'),
    ],
    'lesson': """
<h3>1. Quá khứ đơn — việc đã xong, có (hoặc ngầm hiểu) thời điểm</h3>
<p><b>Công thức:</b> S + V2/V-ed &nbsp;·&nbsp; Phủ định: didn't + V &nbsp;·&nbsp; Hỏi: Did + S + V?</p>
<div class="ex"><span class="en">I joined the company in 2022.</span><span class="vi">Có mốc thời gian cụ thể: in 2022.</span></div>
<div class="ex"><span class="en">We fixed the bug yesterday.</span><span class="vi">yesterday, last week, ago, in 2020, when I was…</span></div>

<h3>2. Hiện tại hoàn thành — nối quá khứ với hiện tại</h3>
<p><b>Công thức:</b> S + have/has + V3 &nbsp;·&nbsp; Phủ định: haven't/hasn't + V3 &nbsp;·&nbsp; Hỏi: Have/Has + S + V3?</p>
<table class="table">
<tr><th>Cách dùng</th><th>Ví dụ</th></tr>
<tr><td>Kinh nghiệm (không nói khi nào)</td><td><span class="say">I've worked with AWS.</span> <span class="say">Have you ever been to Japan?</span></td></tr>
<tr><td>Kéo dài đến nay (for/since)</td><td><span class="say">I've lived here for six years.</span> <span class="say">She's been here since March.</span></td></tr>
<tr><td>Kết quả ở hiện tại</td><td><span class="say">I've lost my password.</span> (giờ không đăng nhập được)</td></tr>
<tr><td>Vừa mới xảy ra (just)</td><td><span class="say">I've just merged your pull request.</span></td></tr>
</table>

<h3>3. Các từ đi kèm</h3>
<table class="table">
<tr><th>Từ</th><th>Vị trí &amp; nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>for</b></td><td>+ khoảng thời gian</td><td><span class="say">for three years, for a long time</span></td></tr>
<tr><td><b>since</b></td><td>+ mốc thời gian</td><td><span class="say">since 2020, since Monday, since I was a student</span></td></tr>
<tr><td><b>already</b></td><td>câu khẳng định — đã … rồi</td><td><span class="say">I've already sent the email.</span></td></tr>
<tr><td><b>yet</b></td><td>cuối câu phủ định/hỏi — chưa / … chưa?</td><td><span class="say">Have you deployed it yet?</span> <span class="say">Not yet.</span></td></tr>
<tr><td><b>ever / never</b></td><td>đã từng / chưa bao giờ</td><td><span class="say">Have you ever used Rust? — No, never.</span></td></tr>
<tr><td><b>just</b></td><td>vừa mới</td><td><span class="say">The build has just finished.</span></td></tr>
</table>

<h3>4. Lỗi hay gặp</h3>
<div class="fix"><s>I have finished the project last week.</s><span class="en">I finished the project last week.</span><span class="vi">Có "last week" (mốc quá khứ) → không dùng hiện tại hoàn thành.</span></div>
<div class="fix"><s>I didn't finish it yet.</s><span class="en">I haven't finished it yet.</span><span class="vi">"yet" đi với hiện tại hoàn thành (tiếng Anh-Anh).</span></div>
<div class="fix"><s>I work here since 2021.</s><span class="en">I've worked here since 2021.</span></div>
<div class="note"><b>Kể chuyện kinh nghiệm:</b> mở đầu bằng hiện tại hoàn thành, rồi chuyển sang quá khứ đơn để kể chi tiết.<br><span class="say">I've worked on a few e-commerce projects. The biggest one was in 2023. We built a marketplace for local farmers.</span></div>
""",
    'phrases': [
        ('I have X years of experience in…', 'Tôi có X năm kinh nghiệm về…'),
        ("I've had the chance to work on…", 'Tôi đã có cơ hội làm việc với…'),
        ('One of my biggest achievements was…', 'Một trong những thành tựu lớn nhất của tôi là…'),
        ("I've never… before, but I'm keen to try.", 'Tôi chưa từng… nhưng rất muốn thử.'),
    ],
    'listening': {
        'title': 'Talking about experience',
        'intro': 'Một nhà tuyển dụng hỏi ứng viên về kinh nghiệm làm việc. Chú ý thì của động từ.',
        'speakers': {'A': ('Rachel', 'jenny'), 'B': ('Duc', 'andrew')},
        'lines': [
            ('A', 'So Duc, how long have you been a developer?', 'Đức này, bạn làm lập trình viên bao lâu rồi?'),
            ('B', "I've been a developer for about five years. I started in 2021, right after I graduated.", 'Mình làm lập trình viên khoảng năm năm. Mình bắt đầu năm 2021, ngay sau khi tốt nghiệp.'),
            ('A', 'And have you ever worked with an international team?', 'Bạn đã bao giờ làm với team quốc tế chưa?'),
            ('B', 'Yes, I have. In my last job, I worked with a team in Australia for two years.', 'Có rồi. Ở công việc trước, mình làm với một team ở Úc trong hai năm.'),
            ('A', 'What was the biggest challenge?', 'Thử thách lớn nhất là gì?'),
            ('B', 'The time difference, at first. But we managed to find a good meeting time, and it worked well.', 'Ban đầu là chênh lệch múi giờ. Nhưng tụi mình tìm được giờ họp phù hợp và mọi thứ ổn.'),
            ('A', "What's something you've achieved that you're proud of?", 'Có thành tựu nào bạn tự hào không?'),
            ('B', 'Last year, I led the migration of our main database. We moved twenty million records without any downtime.', 'Năm ngoái mình dẫn dắt việc chuyển đổi cơ sở dữ liệu chính. Tụi mình chuyển hai mươi triệu bản ghi mà không gián đoạn hệ thống.'),
            ('A', "That's impressive. Have you used Kubernetes?", 'Ấn tượng đấy. Bạn đã dùng Kubernetes chưa?'),
            ('B', "Not in production yet, but I've completed a course and I've built a few small projects with it.", 'Chưa dùng trên production, nhưng mình đã học xong một khóa và làm vài dự án nhỏ với nó.'),
        ],
        'questions': [
            ('When did Duc start working as a developer?', ['In 2019', 'In 2020', 'In 2021', 'Last year'], 2, '"I started in 2021, right after I graduated."'),
            ('Where was the international team located?', ['Singapore', 'Australia', 'Japan', 'The US'], 1, '"I worked with a team in Australia for two years."'),
            ('What is Duc proud of?', ['Learning Kubernetes', 'Leading a database migration', 'Moving to Australia', 'Finding a good meeting time'], 1, '"I led the migration of our main database."'),
            ("What is true about Duc's Kubernetes experience?", ['He uses it every day in production.', 'He has never heard of it.', 'He has taken a course and built small projects.', 'He taught a course about it.'], 2, '"I\'ve completed a course and I\'ve built a few small projects with it."'),
        ],
    },
    'speaking': {
        'tips': ['Mở đầu bằng "I\'ve…" (hiện tại hoàn thành), kể chi tiết bằng quá khứ đơn.', 'Mỗi câu trả lời 30–45 giây.'],
        'prompts': [
            ('How long have you worked in your current job?', 'for/since'),
            ('Have you ever worked on a project that failed? What happened?', 'Have/ever → kể bằng quá khứ đơn'),
            ("What's the most useful thing you've learned this year?", 'Hiện tại hoàn thành + ví dụ'),
            ("What haven't you done yet that you want to do?", 'yet / never'),
        ],
        'model': (
            "I've worked as a developer for almost four years. I joined my current company in 2023, and since then I've worked on three big projects. "
            "One of them didn't go very well. In 2024, we built a chat feature, but we didn't talk to users first, and nobody used it. "
            "We removed it after six months. I learned a lot from that experience. "
            "Now I always ask what problem we're solving before I start coding. "
            "I've never worked abroad, but I've collaborated with clients from Japan and the US. "
            "I haven't joined a fully remote team yet, and that's my goal for next year.",
            'Tôi làm lập trình viên gần bốn năm. Tôi vào công ty hiện tại năm 2023 và từ đó đã làm ba dự án lớn. '
            'Một dự án không suôn sẻ lắm. Năm 2024, chúng tôi làm tính năng chat nhưng không hỏi người dùng trước, và chẳng ai dùng. '
            'Chúng tôi gỡ nó sau sáu tháng. Tôi học được rất nhiều từ trải nghiệm đó. '
            'Giờ tôi luôn hỏi mình đang giải quyết vấn đề gì trước khi bắt đầu code. '
            'Tôi chưa từng làm việc ở nước ngoài, nhưng đã cộng tác với khách hàng từ Nhật và Mỹ. '
            'Tôi chưa vào một team remote hoàn toàn, và đó là mục tiêu năm sau của tôi.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'A short career story',
        'text': [
            'Hoa has worked in tech for seven years, but she did not start as a programmer. After university, she worked as an English teacher for two years. She enjoyed teaching, but she wanted a new challenge.',
            'In 2020, she joined an online coding bootcamp. It was the hardest year of her life. She studied every evening after work and built small projects at weekends. In 2021, she got her first job as a junior developer.',
            'Since then, she has worked for three companies and has become a senior engineer. She has also given talks at two conferences. "I have never regretted the change," she says. "My teaching experience still helps me every day, especially when I explain technical ideas to clients."',
        ],
        'vi': 'Hoa làm trong ngành công nghệ bảy năm nhưng không bắt đầu là lập trình viên. Sau đại học, cô dạy tiếng Anh hai năm. Năm 2020 cô học bootcamp lập trình online — năm vất vả nhất đời cô. Năm 2021 cô có việc junior developer đầu tiên. Từ đó cô làm cho ba công ty, trở thành kỹ sư senior và đã nói ở hai hội thảo. Cô chưa bao giờ hối hận và thấy kinh nghiệm dạy học giúp ích khi giải thích kỹ thuật cho khách hàng.',
        'questions': [
            ('What was Hoa\'s first job after university?', ['Junior developer', 'English teacher', 'Bootcamp instructor', 'Project manager'], 1, '"she worked as an English teacher for two years."'),
            ('When did Hoa get her first developer job?', ['2019', '2020', '2021', '2022'], 2, '"In 2021, she got her first job as a junior developer."'),
            ('Why does the text use "has worked" and "has become" in the last paragraph?', ['The actions are finished and dated.', 'The actions connect the past to now.', 'The actions will happen in the future.', 'The writer made a mistake.'], 1, '"Since then…" → kéo dài từ quá khứ đến hiện tại → hiện tại hoàn thành.'),
        ],
    },
    'writing': {
        'task': 'Viết 8 câu về kinh nghiệm cá nhân: ít nhất 3 câu hiện tại hoàn thành (ever/never/since/for/already/yet) và 3 câu quá khứ đơn có mốc thời gian.',
        'tips': ['Câu mở đầu: "I\'ve been a … for … years."', 'Kể một thành tựu bằng quá khứ đơn: "In 2024, I led…"'],
        'model': "I've been a software developer for four years. I graduated from Da Nang University in 2021. I joined my first company the same year and worked there for two years. In 2023, I moved to a startup that builds education apps. I've built three mobile apps since then. Last year, I led a small team for the first time. I've never worked abroad, but I've worked with clients from Korea. I haven't tried Rust yet, but I'm planning to learn it soon.",
        'min_words': 70,
    },
    'quiz': [
        ('I ___ my first job in 2019.', ['have started', 'started', 'start', 'have been starting'], 1, '"in 2019" → quá khứ đơn.'),
        ('She ___ here for three years.', ['works', 'worked', 'has worked', 'is working'], 2, '"for three years" kéo dài đến nay → has worked.'),
        ('___ you ever ___ a conference talk?', ['Did / give', 'Have / given', 'Have / gave', 'Do / give'], 1, '"ever" hỏi kinh nghiệm → Have you ever given…?'),
        ("I haven't received your email ___.", ['already', 'yet', 'just', 'ever'], 1, '"yet" ở cuối câu phủ định.'),
        ("We've ___ released the update. You can download it now.", ['yet', 'ever', 'just', 'since'], 2, '"just" = vừa mới.'),
        ('They moved to Da Lat two years ___.', ['for', 'since', 'ago', 'before'], 2, '"two years ago" → mốc quá khứ, đi với quá khứ đơn.'),
        ('I have known him ___ we were at school.', ['for', 'since', 'ago', 'from'], 1, '"since" + mốc (một mệnh đề quá khứ).'),
        ('When ___ you ___ the bug?', ['have / found', 'did / find', 'did / found', 'do / find'], 1, 'Câu hỏi "When" hỏi thời điểm → quá khứ đơn.'),
        ("I've ___ seen such a fast laptop. It's amazing!", ['ever', 'never', 'yet', 'already'], 1, '"I\'ve never seen…" = chưa từng thấy.'),
        ('He ___ the company last year and ___ there ever since.', ['joined / has worked', 'has joined / worked', 'joined / worked', 'has joined / has worked'], 0, '"last year" → joined; "ever since" → has worked.'),
        ("I ___ my password, so I can't log in.", ['forgot', 'have forgotten', 'forget', 'was forgetting'], 1, 'Kết quả ở hiện tại (không đăng nhập được) → have forgotten.'),
        ('She has already ___ the documentation.', ['write', 'wrote', 'written', 'writing'], 2, 'have/has + V3: write → wrote → written.'),
        ('How long ___ you known your manager?', ['did', 'do', 'have', 'are'], 2, '"How long have you known…?" → kéo dài đến nay.'),
        ('I ___ to work by bus, but now I drive.', ['use', 'used', 'used to go', 'am used to go'], 2, '"used to + V" = đã từng (nay không còn).'),
        ('We ___ the meeting because the client was sick.', ['have cancelled', 'cancelled', 'cancel', 'were cancel'], 1, 'Việc đã xong, có lý do trong quá khứ (was sick) → quá khứ đơn.'),
    ],
}

DAY5 = {
    'title': 'Shadowing 1: hội thoại ngắn',
    'title_en': 'Shadowing 1: Everyday Small Talk',
    'goal': 'Nắm kỹ thuật shadowing (nghe – nói đuổi theo ngay), bắt chước ngữ điệu và nối âm qua một hội thoại small talk khoảng 1 phút.',
    'tasks': [
        'Đọc hướng dẫn kỹ thuật shadowing 4 bước.',
        'Nghe hội thoại 2–3 lần, đọc lời thoại và nghĩa.',
        'Shadow toàn bộ hội thoại 5 lần (dùng trình phát lặp lại).',
        'Ghi âm lần 1 và lần 5 để so sánh.',
        'Đóng vai: nói phần của Nam, máy đóng vai Emily.',
    ],
    'product': 'Bản ghi âm shadowing lần 1; Bản ghi âm shadowing lần 5',
    'warmup': [
        ("How's it going?", 'Dạo này thế nào?'),
        ('Not bad, thanks. How about you?', 'Cũng ổn, cảm ơn. Còn bạn?'),
        ('What have you been up to?', 'Dạo này bạn làm gì?'),
        ('Did you do anything fun at the weekend?', 'Cuối tuần bạn có làm gì vui không?'),
        ('It was nice catching up with you.', 'Rất vui được hàn huyên với bạn.'),
        ('Talk to you later!', 'Nói chuyện sau nhé!'),
    ],
    'vocab': [
        ('small talk', '/ˈsmɔːl tɔːk/', 'n', 'nói chuyện xã giao', 'We usually make small talk before the meeting starts.', 'Chúng tôi thường nói chuyện xã giao trước khi họp.'),
        ("How's it going?", '/haʊz ɪt ˈɡəʊɪŋ/', 'phrase', 'Dạo này thế nào? (thân mật)', "Hey Tom, how's it going?", 'Chào Tom, dạo này thế nào?'),
        ('be up to', '/biː ʌp tuː/', 'phrase', 'đang làm gì, bận gì', 'What have you been up to lately?', 'Dạo này bạn bận gì thế?'),
        ('catch up', '/kætʃ ʌp/', 'phrasal verb', 'hàn huyên, cập nhật tình hình', "Let's grab a coffee and catch up.", 'Đi cà phê hàn huyên chút đi.'),
        ('lately', '/ˈleɪtli/', 'adv', 'dạo gần đây', "I've been really busy lately.", 'Dạo này tôi rất bận.'),
        ('pretty', '/ˈprɪti/', 'adv', 'khá (thân mật)', 'The weekend was pretty relaxing.', 'Cuối tuần khá thư giãn.'),
        ('hang out', '/hæŋ aʊt/', 'phrasal verb', 'đi chơi, tụ tập', 'We hung out at a café near the lake.', 'Tụi mình đi chơi ở quán cà phê gần hồ.'),
        ('sounds fun', '/saʊndz fʌn/', 'phrase', 'nghe vui đấy', '"We went camping." — "Sounds fun!"', '"Tụi mình đi cắm trại." — "Nghe vui đấy!"'),
        ('no way', '/nəʊ weɪ/', 'phrase', 'không thể nào! (ngạc nhiên)', 'No way! You ran twenty kilometres?', 'Không thể nào! Bạn chạy hai mươi cây số á?'),
        ('take it easy', '/teɪk ɪt ˈiːzi/', 'phrase', 'thư giãn, cứ thong thả', 'I just took it easy and stayed at home.', 'Tôi chỉ thư giãn và ở nhà.'),
        ('looking forward to', '/ˈlʊkɪŋ ˈfɔːwəd tə/', 'phrase', 'mong chờ (+ V-ing/N)', "I'm looking forward to the holiday.", 'Tôi đang mong kỳ nghỉ.'),
        ('anyway', '/ˈeniweɪ/', 'adv', 'dù sao thì (chuyển ý/kết thúc chuyện)', 'Anyway, I should get back to work.', 'Dù sao thì mình nên quay lại làm việc.'),
        ('see you around', '/siː juː əˈraʊnd/', 'phrase', 'hẹn gặp lại (thân mật)', 'Nice talking to you. See you around!', 'Rất vui nói chuyện với bạn. Gặp lại sau nhé!'),
        ('intonation', '/ˌɪntəˈneɪʃn/', 'n', 'ngữ điệu (lên xuống giọng)', 'Questions often have rising intonation.', 'Câu hỏi thường có ngữ điệu lên giọng.'),
    ],
    'lesson': """
<h3>1. Shadowing là gì?</h3>
<p>Shadowing = nghe một câu tiếng Anh rồi <b>nói theo ngay</b>, cố bắt chước y hệt tốc độ, ngữ điệu, chỗ nhấn và chỗ ngắt. Bạn không chỉ học phát âm từng từ mà học cả "giai điệu" của câu — đây là thứ làm người Việt nghe "rất Việt" khi nói tiếng Anh.</p>

<h3>2. Bốn bước shadowing</h3>
<table class="table">
<tr><th>Bước</th><th>Làm gì</th></tr>
<tr><td>1. Nghe hiểu</td><td>Nghe 1–2 lần không nhìn chữ. Sau đó đọc lời thoại và nghĩa cho hiểu hết.</td></tr>
<tr><td>2. Nói nhẩm</td><td>Bật chế độ <b>chậm</b>, nghe từng câu rồi nhắc lại trong khoảng lặng. Chú ý chỗ lên/xuống giọng.</td></tr>
<tr><td>3. Đuổi theo</td><td>Tốc độ bình thường, nói gần như cùng lúc (trễ 0,5 giây) với giọng mẫu.</td></tr>
<tr><td>4. Ghi âm &amp; so sánh</td><td>Ghi âm lần 1 và lần 5. Nghe giọng mẫu ngay sau giọng mình để thấy khác biệt.</td></tr>
</table>

<h3>3. Ba điểm cần bắt chước</h3>
<h4>a) Ngữ điệu (intonation)</h4>
<div class="ex"><span class="en">Did you have a good weekend?</span><span class="vi">Câu hỏi Yes/No → lên giọng ở cuối ↗</span></div>
<div class="ex"><span class="en">What did you do at the weekend?</span><span class="vi">Câu hỏi Wh- → xuống giọng ở cuối ↘</span></div>
<h4>b) Nhấn từ quan trọng (sentence stress)</h4>
<p>Người bản xứ nhấn <b>từ mang nghĩa</b> (danh từ, động từ chính, tính từ) và đọc lướt từ chức năng (a, the, to, of, and…): <span class="say">I WENT to the BEACH with my FRIENDS.</span></p>
<h4>c) Nối âm (linking)</h4>
<p>Phụ âm cuối nối với nguyên âm đầu từ sau: <span class="say">What have you been up to?</span> → "wha-dəv-yə-bi-nʌp-tə". <span class="say">Not at all</span> → "no-tə-tall".</p>

<div class="note"><b>Mẹo:</b> Đừng cố nói hoàn hảo ở lần 1. Mục tiêu của lần 1 → lần 5 là thấy mình bớt "đều đều" và nối câu mượt hơn.</div>
""",
    'phrases': [
        ('How was your weekend?', 'Cuối tuần của bạn thế nào?'),
        ('Anything exciting happening this week?', 'Tuần này có gì thú vị không?'),
        ("Oh really? Tell me more.", 'Thật à? Kể thêm đi.'),
        ("That's awesome! / That's a shame.", 'Tuyệt quá! / Tiếc thật.'),
        ('Anyway, I should let you go.', 'Thôi, mình không làm phiền bạn nữa.'),
    ],
    'listening': {
        'title': 'Monday morning small talk',
        'intro': 'Nam và Emily gặp nhau đầu buổi họp online sáng thứ Hai. Đây là đoạn để shadow cả tuần.',
        'speakers': {'A': ('Emily', 'emma'), 'B': ('Nam', 'brian')},
        'lines': [
            ('A', "Morning, Nam! How's it going?", 'Chào buổi sáng, Nam! Dạo này thế nào?'),
            ('B', 'Hey Emily! Pretty good, thanks. How about you?', 'Chào Emily! Khá ổn, cảm ơn. Còn bạn?'),
            ('A', "Not bad. A bit tired, but it's Monday, right?", 'Cũng được. Hơi mệt, nhưng thứ Hai mà, đúng không?'),
            ('B', 'Ha, exactly. Did you do anything fun at the weekend?', 'Ha, chuẩn luôn. Cuối tuần bạn có làm gì vui không?'),
            ('A', 'Yeah, I went hiking with some friends. The weather was perfect.', 'Có, mình đi leo núi với vài người bạn. Thời tiết đẹp tuyệt.'),
            ('B', 'Oh, nice! Where did you go?', 'Ồ, hay quá! Bạn đi đâu?'),
            ('A', 'Just a small mountain outside the city. It took about three hours. What about you?', 'Chỉ là một ngọn núi nhỏ ngoài thành phố. Mất khoảng ba tiếng. Còn bạn?'),
            ('B', 'I mostly took it easy. I watched a couple of movies and cooked dinner for my parents.', 'Mình chủ yếu nghỉ ngơi. Xem vài bộ phim và nấu bữa tối cho bố mẹ.'),
            ('A', 'That sounds lovely. What did you cook?', 'Nghe dễ thương ghê. Bạn nấu món gì?'),
            ('B', 'Pho! It took me all afternoon, but it was worth it.', 'Phở! Mất cả buổi chiều nhưng rất đáng.'),
            ('A', 'No way! You have to teach me one day.', 'Không thể nào! Hôm nào bạn phải dạy mình đấy.'),
            ('B', 'Sure, anytime. Oh, looks like everyone has joined. Shall we start?', 'Chắc chắn rồi. Ồ, có vẻ mọi người vào đủ rồi. Mình bắt đầu nhé?'),
        ],
        'questions': [
            ('What did Emily do at the weekend?', ['She cooked pho.', 'She went hiking.', 'She watched movies.', 'She worked.'], 1, '"I went hiking with some friends."'),
            ('How long did the hike take?', ['One hour', 'Two hours', 'Three hours', 'All afternoon'], 2, '"It took about three hours."'),
            ('Who did Nam cook dinner for?', ['Emily', 'His friends', 'His parents', 'His team'], 2, '"cooked dinner for my parents".'),
            ('What does "No way!" show in this conversation?', ['Emily refuses to eat pho.', 'Emily is surprised and impressed.', 'Emily is angry.', 'Emily wants to leave.'], 1, '"No way!" ở đây thể hiện sự ngạc nhiên, thán phục.'),
        ],
    },
    'speaking': {
        'tips': ['Dùng trình phát shadowing ở phần Khởi động với các câu của hội thoại: chậm → bình thường.', 'Ghi âm lần 1 ngay bây giờ, lần 5 sau khi luyện xong. So sánh.', 'Sau đó dùng chế độ đóng vai ở phần Nghe: chọn "Bạn là Nam".'],
        'prompts': [
            ('Shadow the whole conversation 5 times. Record attempt 1 and attempt 5.', 'Dùng nút "Phát cả bài" ở phần Nghe, nói theo.'),
            ('Role-play: you are Nam. Answer Emily naturally.', 'Chế độ đóng vai ở phần Nghe.'),
            ('Answer: "Did you do anything fun at the weekend?"', 'Trả lời bằng 3–4 câu thật về cuối tuần của bạn.'),
        ],
        'model': (
            "Yeah, it was pretty relaxing, actually. On Saturday morning, I went to a café with my old classmates and we caught up for hours. "
            "In the afternoon, I took it easy and read a book. "
            "On Sunday, I cooked a big lunch for my family. "
            "How about you? Did you get up to anything interesting?",
            'Ừ, thực ra khá thư giãn. Sáng thứ Bảy mình đi cà phê với bạn học cũ và tụi mình hàn huyên hàng giờ. '
            'Buổi chiều mình nghỉ ngơi và đọc sách. '
            'Chủ nhật mình nấu một bữa trưa thịnh soạn cho gia đình. '
            'Còn bạn? Bạn có làm gì thú vị không?'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Why small talk matters in remote teams',
        'text': [
            'Many developers think small talk is a waste of time. Why talk about the weather when there is work to do? But in remote teams, those few minutes at the start of a meeting are often the only chance people have to get to know each other.',
            'Small talk builds trust. When you know that a teammate has a new baby or loves hiking, it is easier to ask for help, give feedback or forgive a mistake. Teams with good relationships also solve problems faster because people are not afraid to speak up.',
            'You do not need to be funny or clever. Ask simple, open questions such as "How was your weekend?" and listen to the answer. Then ask one follow-up question. That is enough to make a good impression.',
        ],
        'vi': 'Nhiều dev nghĩ nói chuyện xã giao là lãng phí, nhưng với team remote, vài phút đầu cuộc họp thường là cơ hội duy nhất để hiểu nhau. Small talk xây dựng lòng tin: biết đồng đội vừa có em bé hay thích leo núi giúp việc nhờ vả, góp ý và bỏ qua lỗi dễ hơn. Không cần hài hước — chỉ cần hỏi câu mở đơn giản, lắng nghe và hỏi thêm một câu.',
        'questions': [
            ('Why is small talk especially important in remote teams?', ['Meetings are very long.', 'It may be the only chance to get to know each other.', 'Managers require it.', 'It replaces documentation.'], 1, 'Đoạn 1: "the only chance people have to get to know each other".'),
            ('According to the text, what does small talk build?', ['Trust', 'Code quality', 'Speed', 'Documentation'], 0, 'Đoạn 2: "Small talk builds trust."'),
            ('What is the writer\'s advice?', ['Tell jokes.', 'Talk about yourself a lot.', 'Ask a simple question and one follow-up.', 'Avoid personal topics completely.'], 2, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết một đoạn hội thoại small talk 8–10 lượt lời giữa bạn và một đồng nghiệp nước ngoài vào sáng thứ Hai. Dùng ít nhất 5 cụm từ hôm nay.',
        'tips': ['Mỗi lượt lời 1–2 câu, ngắn và tự nhiên.', 'Có một câu hỏi follow-up (Where did you go? / What did you cook?).'],
        'model': "A: Morning! How's it going?\nB: Pretty good, thanks. How about you?\nA: Not bad. What have you been up to lately?\nB: I've been busy with the new release, but I took it easy at the weekend.\nA: Nice. Did you do anything fun?\nB: I hung out with some old friends at a café. How about you?\nA: I went cycling around West Lake.\nB: Sounds fun! How long did it take?\nA: About two hours. Anyway, shall we start the meeting?\nB: Sure, let's go.",
        'min_words': 60,
    },
    'quiz': [
        ('"How\'s it going?" — Câu trả lời tự nhiên nhất là:', ["I'm going to the office.", 'Pretty good, thanks. You?', 'It is going.', 'Yes, it goes.'], 1, '"How\'s it going?" = "Dạo này thế nào?" → trả lời "Pretty good, thanks."'),
        ('"What have you been up to?" nghĩa là:', ['Bạn đã lên đâu?', 'Dạo này bạn làm gì?', 'Bạn định làm gì?', 'Bạn cao bao nhiêu?'], 1, '"be up to" = đang bận làm gì.'),
        ('Câu hỏi Yes/No như "Did you have a good weekend?" thường có ngữ điệu:', ['Xuống giọng ở cuối', 'Lên giọng ở cuối', 'Đều đều', 'Lên giọng ở đầu'], 1, 'Yes/No question → lên giọng ở cuối.'),
        ('Câu hỏi "Where did you go?" thường có ngữ điệu:', ['Lên giọng ở cuối', 'Xuống giọng ở cuối', 'Không có ngữ điệu', 'Lên rồi xuống ở giữa'], 1, 'Wh-question → thường xuống giọng ở cuối.'),
        ('"We went camping." — Phản hồi tự nhiên:', ['Sounds fun!', 'You are camping.', 'I am fun.', 'Good camping.'], 0, '"Sounds fun!" = Nghe vui đấy!'),
        ('Từ nào thường được NHẤN trong câu "I went to the beach with my friends"?', ['to, the, with', 'went, beach, friends', 'I, my', 'the, my'], 1, 'Nhấn từ mang nghĩa: went, beach, friends.'),
        ('"Let\'s grab a coffee and ___ up."', ['catch', 'take', 'make', 'hang'], 0, '"catch up" = hàn huyên, cập nhật tình hình.'),
        ("I'm looking forward to ___ you next week.", ['see', 'seeing', 'saw', 'be seen'], 1, '"look forward to" + V-ing ("to" ở đây là giới từ).'),
        ('"Anyway, I should let you go." dùng để:', ['Đuổi ai đó đi', 'Kết thúc cuộc trò chuyện lịch sự', 'Mời ai đó đi chơi', 'Xin nghỉ việc'], 1, 'Cách kết thúc cuộc nói chuyện lịch sự.'),
        ('Chọn câu tự nhiên nhất để hỏi về cuối tuần:', ['What did you do in the weekend holiday?', 'How was your weekend?', 'Your weekend is how?', 'Did you have weekend?'], 1, '"How was your weekend?" là cách hỏi phổ biến nhất.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 1',
    'title_en': 'Week 1 Review',
    'goal': 'Tổng kết các điểm ngữ pháp và phát âm của tuần, nhận diện 5 lỗi lặp lại nhiều nhất của bản thân và viết đoạn 5 câu về một dự án.',
    'tasks': [
        'Học 14 từ để nói về dự án.',
        'Đọc danh sách "10 lỗi kinh điển" và đánh dấu những lỗi bạn mắc.',
        'Làm 15 câu trắc nghiệm ngữ pháp tổng hợp.',
        'Nghe lại các bản ghi âm trong tuần, liệt kê 5 lỗi lặp lại nhiều nhất.',
        'Viết đoạn 5 câu về một dự án đang làm.',
    ],
    'product': 'Đoạn văn 5 câu về dự án; Điểm quiz; Danh sách 5 lỗi của bạn',
    'warmup': [
        ("I'm working on an app that helps people book doctors.", 'Tôi đang làm một ứng dụng giúp mọi người đặt lịch bác sĩ.'),
        ('We started the project three months ago.', 'Chúng tôi bắt đầu dự án ba tháng trước.'),
        ("So far, we've built the login and the booking pages.", 'Đến giờ chúng tôi đã làm xong trang đăng nhập và đặt lịch.'),
        ("I'm responsible for the backend.", 'Tôi phụ trách phần backend.'),
        ('The hardest part is handling payments.', 'Phần khó nhất là xử lý thanh toán.'),
        ('We plan to launch it next month.', 'Chúng tôi dự định ra mắt vào tháng sau.'),
    ],
    'vocab': [
        ('project', '/ˈprɒdʒekt/', 'n', 'dự án', "It's a side project I work on at weekends.", 'Đó là dự án phụ tôi làm vào cuối tuần.'),
        ('feature', '/ˈfiːtʃə/', 'n', 'tính năng', 'The most popular feature is the dark mode.', 'Tính năng được yêu thích nhất là chế độ tối.'),
        ('user', '/ˈjuːzə/', 'n', 'người dùng', 'We have about two thousand active users.', 'Chúng tôi có khoảng hai nghìn người dùng hoạt động.'),
        ('purpose', '/ˈpɜːpəs/', 'n', 'mục đích', 'The purpose of the app is to save time for teachers.', 'Mục đích của ứng dụng là tiết kiệm thời gian cho giáo viên.'),
        ('build', '/bɪld/', 'verb', 'xây dựng, làm ra (built – built)', 'We built the first version in two weeks.', 'Chúng tôi làm phiên bản đầu trong hai tuần.'),
        ('tool', '/tuːl/', 'n', 'công cụ', 'We use Jira as our main planning tool.', 'Chúng tôi dùng Jira làm công cụ lập kế hoạch chính.'),
        ('client', '/ˈklaɪənt/', 'n', 'khách hàng (dịch vụ)', 'The client wants a simple design.', 'Khách hàng muốn thiết kế đơn giản.'),
        ('requirement', '/rɪˈkwaɪəmənt/', 'n', 'yêu cầu', 'The requirements changed twice last month.', 'Yêu cầu đã thay đổi hai lần trong tháng trước.'),
        ('challenge', '/ˈtʃælɪndʒ/', 'n', 'thử thách, khó khăn', 'Our biggest challenge is performance.', 'Thử thách lớn nhất của chúng tôi là hiệu năng.'),
        ('solve', '/sɒlv/', 'verb', 'giải quyết', 'This feature solves a real problem.', 'Tính năng này giải quyết một vấn đề thực tế.'),
        ('release', '/rɪˈliːs/', 'verb / n', 'phát hành; bản phát hành', 'The next release is planned for June.', 'Bản phát hành tiếp theo dự kiến vào tháng Sáu.'),
        ('team member', '/tiːm ˈmembə/', 'n', 'thành viên nhóm', 'There are five team members in total.', 'Tổng cộng có năm thành viên trong nhóm.'),
        ('progress', '/ˈprəʊɡres/', 'n', 'tiến độ, sự tiến bộ', "We're making good progress.", 'Chúng tôi đang tiến triển tốt.'),
        ('mistake', '/mɪˈsteɪk/', 'n', 'lỗi sai', "Everyone makes mistakes. That's how we learn.", 'Ai cũng mắc lỗi. Đó là cách chúng ta học.'),
    ],
    'lesson': """
<h3>1. Tóm tắt tuần 1</h3>
<table class="table">
<tr><th>Chủ đề</th><th>Điều cần nhớ</th></tr>
<tr><td>Hiện tại đơn</td><td>Thói quen, sự thật, lịch cố định. Nhớ <b>-s</b> với he/she/it.</td></tr>
<tr><td>Hiện tại tiếp diễn</td><td>Đang xảy ra, tạm thời, kế hoạch gần. Không dùng với know, need, want…</td></tr>
<tr><td>Quá khứ đơn</td><td>Việc đã xong, có mốc: yesterday, last…, …ago, in 2020.</td></tr>
<tr><td>Hiện tại hoàn thành</td><td>Kinh nghiệm, kết quả, kéo dài đến nay: for, since, ever, never, already, yet, just.</td></tr>
<tr><td>Nguyên âm</td><td>/ɪ/–/iː/, /e/–/æ/, /ʌ/–/ɑː/, /ʊ/–/uː/. Âm dài thì kéo dài thật sự.</td></tr>
<tr><td>Shadowing</td><td>Nghe → nói đuổi theo, bắt chước ngữ điệu, nhấn từ quan trọng, nối âm.</td></tr>
</table>

<h3>2. 10 lỗi kinh điển của người Việt — bạn mắc lỗi nào?</h3>
<div class="fix"><s>He work in a bank.</s><span class="en">He works in a bank.</span><span class="vi">Quên -s ngôi thứ ba.</span></div>
<div class="fix"><s>I am agree with you.</s><span class="en">I agree with you.</span><span class="vi">"agree" là động từ, không cần "am".</span></div>
<div class="fix"><s>I have been to Da Lat last year.</s><span class="en">I went to Da Lat last year.</span><span class="vi">Có mốc thời gian → quá khứ đơn.</span></div>
<div class="fix"><s>She is very like coffee.</s><span class="en">She really likes coffee.</span></div>
<div class="fix"><s>I want to discuss about the bug.</s><span class="en">I want to discuss the bug.</span><span class="vi">"discuss" không đi với "about".</span></div>
<div class="fix"><s>Can you explain me this function?</s><span class="en">Can you explain this function to me?</span></div>
<div class="fix"><s>I have many experiences in Java.</s><span class="en">I have a lot of experience with Java.</span><span class="vi">"experience" (kinh nghiệm) là danh từ không đếm được.</span></div>
<div class="fix"><s>Yesterday I go to the office.</s><span class="en">Yesterday I went to the office.</span></div>
<div class="fix"><s>There have many users.</s><span class="en">There are many users.</span><span class="vi">"Có" = there is/are, không dùng "have".</span></div>
<div class="fix"><s>I'm boring with this task.</s><span class="en">I'm bored with this task.</span><span class="vi">-ed: cảm xúc của người; -ing: tính chất của vật (This task is boring).</span></div>

<h3>3. Nói về dự án: khung 5 câu</h3>
<ol>
<li><b>Là gì:</b> <span class="say">I'm working on an app that helps small shops manage orders.</span></li>
<li><b>Vai trò:</b> <span class="say">I'm responsible for the backend and the database.</span></li>
<li><b>Tiến độ:</b> <span class="say">So far, we've built the order and payment features.</span></li>
<li><b>Khó khăn:</b> <span class="say">The biggest challenge is syncing data when the internet is slow.</span></li>
<li><b>Tiếp theo:</b> <span class="say">We're planning to release the first version next month.</span></li>
</ol>
""",
    'listening': {
        'title': 'Tell me about your project',
        'intro': 'Hai lập trình viên giới thiệu dự án của mình trong một buổi meetup online.',
        'speakers': {'A': ('Chris', 'guy'), 'B': ('Mai', 'jenny')},
        'lines': [
            ('A', 'So Mai, what are you working on these days?', 'Mai này, dạo này bạn đang làm gì?'),
            ('B', "I'm working on a small app for language teachers. It helps them create quizzes and track their students' progress.", 'Mình đang làm một ứng dụng nhỏ cho giáo viên ngoại ngữ. Nó giúp họ tạo bài kiểm tra và theo dõi tiến độ học sinh.'),
            ('A', 'Interesting. Is it a side project or a client project?', 'Hay đấy. Đó là dự án phụ hay dự án cho khách hàng?'),
            ('B', 'It started as a side project, but a language school has just agreed to pay for it.', 'Ban đầu là dự án phụ, nhưng một trung tâm ngoại ngữ vừa đồng ý trả tiền cho nó.'),
            ('A', 'Wow, congratulations! How long have you been working on it?', 'Chà, chúc mừng nhé! Bạn làm nó bao lâu rồi?'),
            ('B', 'About six months. I built the first version alone, and then two friends joined me in March.', 'Khoảng sáu tháng. Mình làm phiên bản đầu một mình, rồi hai người bạn tham gia vào tháng Ba.'),
            ('A', "What's been the biggest challenge so far?", 'Thử thách lớn nhất đến giờ là gì?'),
            ('B', "Honestly, the requirements. The school keeps changing its mind, so we've rewritten the reports page three times.", 'Thật lòng là yêu cầu. Trung tâm cứ đổi ý nên tụi mình đã viết lại trang báo cáo ba lần.'),
            ('A', "That's frustrating. What's next?", 'Bực thật. Bước tiếp theo là gì?'),
            ('B', "We're planning to release it to all their teachers next month. Fingers crossed!", 'Tụi mình định phát hành cho tất cả giáo viên của họ vào tháng sau. Cầu mong suôn sẻ!'),
        ],
        'questions': [
            ('Who is Mai\'s app for?', ['Students', 'Language teachers', 'Parents', 'Developers'], 1, '"a small app for language teachers".'),
            ('How long has Mai been working on the app?', ['Three months', 'Six months', 'One year', 'Since March'], 1, '"About six months."'),
            ('What has been the biggest challenge?', ['Money', 'Finding users', 'Changing requirements', 'Slow servers'], 2, '"Honestly, the requirements. The school keeps changing its mind…"'),
            ('What is the plan for next month?', ['Rewrite the reports page', 'Hire more developers', 'Release the app to all teachers', 'Start a new project'], 2, '"We\'re planning to release it to all their teachers next month."'),
        ],
    },
    'speaking': {
        'tips': ['Dùng khung 5 câu. Nói 1 phút, không nhìn giấy.', 'Kết hợp đủ 4 thì đã học trong tuần.'],
        'prompts': [
            ('Tell me about a project you are working on (or worked on).', 'Là gì – vai trò – tiến độ – khó khăn – tiếp theo.'),
            ('What mistakes do you often make when you speak English?', 'Dùng danh sách 10 lỗi.'),
            ('What did you learn this week?', 'Tóm tắt tuần 1.'),
        ],
        'model': (
            "Right now, I'm working on an internal tool for our sales team. It helps them track customers and send follow-up emails automatically. "
            "I'm responsible for the API and the email service. We started three months ago, and so far we've finished the customer list and the email templates. "
            "The biggest challenge has been data quality, because the old system had a lot of duplicate records. "
            "We're planning to release the first version to ten users next week and collect feedback.",
            'Hiện tôi đang làm một công cụ nội bộ cho đội kinh doanh. Nó giúp họ theo dõi khách hàng và tự động gửi email chăm sóc. '
            'Tôi phụ trách API và dịch vụ email. Chúng tôi bắt đầu ba tháng trước, và đến giờ đã xong danh sách khách hàng và mẫu email. '
            'Thử thách lớn nhất là chất lượng dữ liệu, vì hệ thống cũ có rất nhiều bản ghi trùng. '
            'Chúng tôi dự định phát hành phiên bản đầu cho mười người dùng vào tuần sau để thu thập phản hồi.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Learning from your mistakes',
        'text': [
            'Language learners often feel bad about their mistakes, but mistakes are useful data. They show you exactly what your brain has not learned yet. The trick is to stop looking at every mistake and start looking for patterns.',
            'Most learners make the same five or six mistakes again and again. For Vietnamese speakers, common ones are missing the "-s" on verbs, using the wrong tense with "since" and "for", and dropping final consonants. If you fix only these, people will understand you much more easily.',
            'Keep a "mistake list" in a notebook or on your phone. Each week, write down the mistakes you hear in your recordings. Next to each one, write the correct version and read it aloud five times. After a month, look back at your list. You will be surprised how many of them have disappeared.',
        ],
        'vi': 'Lỗi sai là dữ liệu hữu ích, cho thấy chính xác não bạn chưa học được gì. Bí quyết là tìm "mẫu lỗi" thay vì nhìn từng lỗi. Người Việt hay quên -s, dùng sai thì với since/for và nuốt phụ âm cuối. Hãy giữ một "danh sách lỗi": mỗi tuần ghi lỗi từ bản ghi âm, viết câu đúng bên cạnh và đọc to 5 lần. Sau một tháng, nhiều lỗi sẽ biến mất.',
        'questions': [
            ('How does the writer describe mistakes?', ['As something to be ashamed of', 'As useful data', 'As random', 'As impossible to fix'], 1, '"mistakes are useful data".'),
            ('What should you look for in your mistakes?', ['Patterns', 'Excuses', 'New grammar rules', 'A teacher'], 0, '"start looking for patterns".'),
            ('What should you do next to each mistake on your list?', ['Delete it after a day', 'Write the correct version and read it aloud', 'Translate it into Vietnamese', 'Show it to your manager'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Phần A: Viết đoạn 5 câu về một dự án bạn đang làm (theo khung 5 câu). Phần B: Liệt kê 5 lỗi bạn mắc nhiều nhất trong tuần, mỗi lỗi kèm câu đúng.',
        'tips': ['Dùng ít nhất 3 thì khác nhau.', 'Đọc to đoạn văn sau khi viết.'],
        'model': "I'm working on a booking app for small spas and beauty salons. I'm responsible for the backend API and the payment integration. We started in January, and so far we've built online booking and SMS reminders. The biggest challenge has been handling double bookings when two customers book at the same time. We're planning to launch in three cities next month.\n\nMy 5 mistakes:\n1. He work → He works\n2. I work here since 2022 → I've worked here since 2022\n3. discuss about → discuss\n4. many experiences → a lot of experience\n5. dropping /t/ at the end of \"next\", \"last\"",
        'min_words': 60,
    },
    'quiz': [
        ('My manager ___ to the office on Fridays.', ["don't come", "doesn't come", "isn't come", "not comes"], 1, 'Ngôi ba số ít, phủ định → doesn\'t + V.'),
        ('I ___ with you. That is a good idea.', ['am agree', 'agree', 'agreeing', 'am agreed'], 1, '"agree" là động từ thường.'),
        ('We ___ the client last Tuesday.', ['have met', 'met', 'meet', 'are meeting'], 1, '"last Tuesday" → quá khứ đơn.'),
        ('She ___ for this company since 2020.', ['works', 'worked', 'has worked', 'is working'], 2, '"since 2020" → hiện tại hoàn thành.'),
        ('Let\'s discuss ___ the new design tomorrow.', ['about', 'on', '(không cần giới từ)', 'for'], 2, '"discuss something" — không có "about".'),
        ('Could you explain ___ how this works?', ['me', 'to me', 'for me', 'with me'], 1, '"explain something to somebody" / "explain to me how…"'),
        ('I have a lot of ___ with React.', ['experiences', 'experience', 'experienced', 'an experience'], 1, 'Kinh nghiệm (chuyên môn) là danh từ không đếm được.'),
        ('There ___ three bugs in this file.', ['have', 'has', 'are', 'is'], 2, '"Có" = there are (số nhiều).'),
        ('The meeting was so long. I was really ___.', ['boring', 'bored', 'bore', 'bores'], 1, 'Cảm xúc của người → bored.'),
        ('Right now I ___ the release notes.', ['write', 'am writing', 'have written', 'wrote'], 1, '"Right now" → hiện tại tiếp diễn.'),
        ('___ you finished the report yet?', ['Did', 'Have', 'Are', 'Do'], 1, '"yet" → Have you finished…?'),
        ('He ___ the bug two hours ago.', ['has fixed', 'fixed', 'fixes', 'is fixing'], 1, '"two hours ago" → quá khứ đơn.'),
        ('I ___ you need more time. Take it.', ['am knowing', 'know', 'known', 'knowing'], 1, '"know" là động từ trạng thái.'),
        ('Từ nào có âm /æ/?', ['bed', 'bad', 'bud', 'bird'], 1, 'bad /bæd/.'),
        ('Từ nào có âm dài /iː/?', ['fill', 'fit', 'feet', 'fix'], 2, 'feet /fiːt/.'),
    ],
}

WEEK = {
    'title': 'Nền tảng: ngữ pháp và phát âm',
    'title_en': 'Foundations: Grammar & Pronunciation',
    'goal': 'Sửa các lỗi ngữ pháp B1 hay gặp và nắm quy tắc phát âm cơ bản để nói rõ hơn.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
