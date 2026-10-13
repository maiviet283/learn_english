"""Tuần 7 — Viết chuyên nghiệp."""

DAY1 = {
    'title': 'Commit message và PR description',
    'title_en': 'Commit Messages & Pull Request Descriptions',
    'goal': 'Viết commit message ngắn gọn ở thể mệnh lệnh ("Add user login endpoint") và PR description đủ 3 phần: Summary – Changes – How to test.',
    'tasks': [
        'Học 14 thuật ngữ về commit và pull request.',
        'Học quy tắc commit message và khung PR description.',
        'Nghe senior dev góp ý về PR description.',
        'Viết lại 5 commit message xấu thành tốt.',
        'Viết 2 PR description mẫu cho công việc thật của bạn.',
    ],
    'product': '2 PR description mẫu; 5 commit message đã sửa',
    'warmup': [
        ('Add user login endpoint.', 'Thêm endpoint đăng nhập người dùng.'),
        ('Fix crash when the cart is empty.', 'Sửa lỗi treo khi giỏ hàng trống.'),
        ('Refactor the payment service for easier testing.', 'Tái cấu trúc dịch vụ thanh toán để dễ test hơn.'),
        ('This PR adds a CSV export to the reports page.', 'PR này thêm chức năng xuất CSV cho trang báo cáo.'),
        ('To test, open the reports page and click Export.', 'Để kiểm thử, mở trang báo cáo và bấm Export.'),
        ('Closes ticket four hundred and twelve.', 'Đóng ticket 412.'),
    ],
    'vocab': [
        ('imperative', '/ɪmˈperətɪv/', 'adj / n', 'thể mệnh lệnh', 'Write commit messages in the imperative: "Add", not "Added".', 'Viết commit ở thể mệnh lệnh: "Add" chứ không phải "Added".'),
        ('subject line', '/ˈsʌbdʒɪkt laɪn/', 'n', 'dòng tiêu đề', 'Keep the subject line under fifty characters.', 'Giữ dòng tiêu đề dưới năm mươi ký tự.'),
        ('commit body', '/kəˈmɪt ˈbɒdi/', 'n', 'phần thân của commit', 'Use the commit body to explain why, not what.', 'Dùng phần thân commit để giải thích vì sao, không phải cái gì.'),
        ('bump', '/bʌmp/', 'verb', 'nâng (phiên bản)', 'Bump the library version to 2.4.1.', 'Nâng phiên bản thư viện lên 2.4.1.'),
        ('breaking change', '/ˈbreɪkɪŋ tʃeɪndʒ/', 'n', 'thay đổi làm hỏng tương thích', 'Renaming this field is a breaking change.', 'Đổi tên trường này là một thay đổi phá vỡ tương thích.'),
        ('changelog', '/ˈtʃeɪndʒlɒɡ/', 'n', 'nhật ký thay đổi', 'Add a line to the changelog for every release.', 'Thêm một dòng vào nhật ký thay đổi cho mỗi bản phát hành.'),
        ('squash', '/skwɒʃ/', 'verb', 'gộp (nhiều commit thành một)', 'Please squash your commits before merging.', 'Hãy gộp các commit trước khi merge.'),
        ('rebase', '/ˌriːˈbeɪs/', 'verb', 'đặt lại nhánh lên gốc mới', 'Rebase your branch on the latest main.', 'Rebase nhánh của bạn lên main mới nhất.'),
        ('rationale', '/ˌræʃəˈnɑːl/', 'n', 'lý do, cơ sở', 'Explain the rationale behind this design.', 'Giải thích lý do đằng sau thiết kế này.'),
        ('screenshot', '/ˈskriːnʃɒt/', 'n', 'ảnh chụp màn hình', 'Add before and after screenshots for UI changes.', 'Thêm ảnh trước và sau cho thay đổi giao diện.'),
        ('reviewer', '/rɪˈvjuːə/', 'n', 'người review', 'I added two reviewers to the PR.', 'Tôi đã thêm hai người review vào PR.'),
        ('draft PR', '/drɑːft ˌpiː ˈɑː/', 'n', 'PR nháp (chưa sẵn sàng)', 'Open a draft PR to get early feedback.', 'Mở PR nháp để nhận góp ý sớm.'),
        ('link to', '/lɪŋk tuː/', 'verb', 'liên kết tới', 'Link the PR to the Jira ticket.', 'Liên kết PR với ticket Jira.'),
        ('closes', '/ˈkləʊzɪz/', 'keyword', 'từ khóa tự đóng issue khi merge', 'Write "Closes #128" in the description.', 'Viết "Closes #128" trong phần mô tả.'),
    ],
    'lesson': """
<h3>1. Quy tắc commit message</h3>
<ol>
<li><b>Thể mệnh lệnh</b>, như ra lệnh cho code: <i>Add, Fix, Remove, Update, Refactor</i> — không viết <i>Added, Fixes, Adding</i>.</li>
<li><b>Dòng tiêu đề ≤ 50 ký tự</b>, viết hoa chữ đầu, không chấm cuối.</li>
<li><b>Nói cái gì thay đổi</b>, cụ thể: không phải "fix bug" mà "Fix crash when cart is empty".</li>
<li>Nếu cần, để trống một dòng rồi viết <b>phần thân</b> giải thích <b>vì sao</b>.</li>
</ol>
<div class="note"><b>Mẹo kiểm tra:</b> Câu "If applied, this commit will <i>[tiêu đề của bạn]</i>" phải đọc trơn tru. <i>"If applied, this commit will <b>add user login endpoint</b>"</i> ✓</div>
<table class="table">
<tr><th>Xấu</th><th>Tốt</th></tr>
<tr><td>fix</td><td><span class="say">Fix crash when uploading empty files</span></td></tr>
<tr><td>Updated stuff</td><td><span class="say">Update Django to 5.1</span></td></tr>
<tr><td>Added new feature for users to export</td><td><span class="say">Add CSV export to reports page</span></td></tr>
<tr><td>WIP</td><td><span class="say">Add draft validation for sign-up form</span></td></tr>
</table>

<h3>2. Khung PR description</h3>
<pre>## Summary
One or two sentences: what this PR does and why.

## Changes
- Add CSV export button to the reports page
- Add `export_csv` endpoint with pagination
- Update docs

## How to test
1. Go to /reports
2. Choose a date range and click "Export"
3. Check that the file contains the correct rows

## Notes
Closes #412. No breaking changes. Screenshots below.</pre>

<h3>3. Câu thường dùng trong PR</h3>
<div class="ex"><span class="en">This PR adds / fixes / refactors …</span></div>
<div class="ex"><span class="en">The main reason for this change is …</span></div>
<div class="ex"><span class="en">I chose X over Y because …</span><span class="vi">Giải thích lựa chọn thiết kế.</span></div>
<div class="ex"><span class="en">Out of scope: … (will be done in a follow-up PR).</span></div>
<div class="ex"><span class="en">Please pay special attention to …</span><span class="vi">Nhờ người review chú ý phần nào.</span></div>
""",
    'phrases': [
        ('This PR adds…', 'PR này thêm…'),
        ('Please pay special attention to…', 'Vui lòng chú ý đặc biệt đến…'),
        ('I chose X over Y because…', 'Tôi chọn X thay vì Y vì…'),
        ('No breaking changes.', 'Không có thay đổi phá vỡ tương thích.'),
    ],
    'listening': {
        'title': 'Feedback on a pull request description',
        'intro': 'Senior developer Grace góp ý cho Bảo về cách viết commit và PR.',
        'speakers': {'A': ('Grace', 'sonia'), 'B': ('Bao', 'brian')},
        'lines': [
            ('A', "Bao, I looked at your pull request. The code is good, but I had a hard time understanding what it does.", 'Bảo, chị xem pull request của em rồi. Code tốt, nhưng chị khá vất vả để hiểu nó làm gì.'),
            ('B', "Oh, sorry. I only wrote 'update reports'.", 'Ồ, em xin lỗi. Em chỉ viết "update reports".'),
            ('A', "Exactly. A reviewer needs three things: a summary, a list of changes, and how to test it.", 'Chính xác. Người review cần ba thứ: tóm tắt, danh sách thay đổi, và cách kiểm thử.'),
            ('B', "Should the summary be long?", 'Phần tóm tắt có nên dài không ạ?'),
            ('A', "No, one or two sentences. What does the PR do, and why? For example, 'This PR adds CSV export to the reports page, because customers asked for it in the last survey.'", 'Không, một hai câu thôi. PR làm gì, và vì sao? Ví dụ: "PR này thêm xuất CSV cho trang báo cáo, vì khách hàng yêu cầu trong khảo sát gần nhất."'),
            ('B', "That makes sense. And the commits? I have twelve of them, like 'fix', 'fix again', 'WIP'.", 'Hợp lý ạ. Còn commit? Em có mười hai cái, kiểu "fix", "fix again", "WIP".'),
            ('A', "Ha, we've all done that. Please squash them into one or two meaningful commits before merging. And write them in the imperative: 'Add CSV export', not 'Added'.", 'Ha, ai cũng từng thế. Hãy gộp chúng thành một hai commit có nghĩa trước khi merge. Và viết ở thể mệnh lệnh: "Add CSV export", không phải "Added".'),
            ('B', "Got it. Should I add screenshots?", 'Em hiểu rồi. Em có nên thêm ảnh chụp màn hình không?'),
            ('A', "Yes, for any UI change. Before and after. It saves the reviewer a lot of time. And link the PR to the Jira ticket.", 'Có, với mọi thay đổi giao diện. Trước và sau. Nó tiết kiệm rất nhiều thời gian cho người review. Và liên kết PR với ticket Jira.'),
            ('B', "Thanks, Grace. I'll update it now and ping you when it's ready.", 'Cảm ơn chị Grace. Em sẽ cập nhật ngay và nhắn chị khi xong.'),
        ],
        'questions': [
            ('What was the problem with Bao\'s PR?', ['The code was bad.', 'The description was too short to understand.', 'It had no tests.', 'It was too big.'], 1, '"I had a hard time understanding what it does" — Bảo chỉ viết "update reports".'),
            ('What three things does a reviewer need?', ['Code, tests, docs', 'Summary, list of changes, how to test', 'Title, author, date', 'Screenshots, links, emojis'], 1, '"a summary, a list of changes, and how to test it".'),
            ('What should Bao do with his twelve commits?', ['Delete them', 'Squash them into one or two meaningful commits', 'Keep them all', 'Rename them "WIP"'], 1, '"squash them into one or two meaningful commits".'),
            ('When should screenshots be added?', ['Never', 'For any UI change', 'Only for bugs', 'Only if the manager asks'], 1, '"Yes, for any UI change."'),
        ],
    },
    'speaking': {
        'tips': ['Giải thích PR của bạn bằng lời như đang nói với người review (1 phút).'],
        'prompts': [
            ('Walk a reviewer through your PR: what it does, why, what changed, and how to test it.', 'This PR adds… The main reason is… To test it…'),
            ('Explain why good commit messages matter.', 'PREP.'),
        ],
        'model': (
            "This PR adds a CSV export button to the reports page. The main reason is that customers kept asking for it in support tickets. "
            "There are three main changes: a new export endpoint with pagination, a button on the reports page, and an update to the docs. "
            "To test it, go to the reports page, choose a date range, and click Export. The file should contain one row per order. "
            "Please pay special attention to the date filter, because time zones were a bit tricky. There are no breaking changes.",
            'PR này thêm nút xuất CSV cho trang báo cáo. Lý do chính là khách hàng liên tục yêu cầu trong các ticket hỗ trợ. '
            'Có ba thay đổi chính: một endpoint xuất mới có phân trang, một nút trên trang báo cáo, và cập nhật tài liệu. '
            'Để kiểm thử, vào trang báo cáo, chọn khoảng ngày và bấm Export. File phải có mỗi đơn hàng một dòng. '
            'Vui lòng chú ý đặc biệt đến bộ lọc ngày, vì múi giờ hơi phức tạp. Không có thay đổi phá vỡ tương thích.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Why commit history matters',
        'text': [
            'Six months from now, someone will look at a strange line of code and wonder why it exists. Often, that someone will be you. The commit history is the only place where the answer might be recorded.',
            'A message like "fix" tells them nothing. A message like "Fix double charge when user clicks Pay twice" tells them exactly what problem the line solves. If the commit body explains why a simpler solution did not work, it can save hours of investigation.',
            'Good commit messages are also a sign of respect for your teammates. They show that you care about the people who will maintain the code after you, not only about getting your change merged today.',
        ],
        'vi': 'Sáu tháng nữa, ai đó (thường là chính bạn) sẽ thắc mắc vì sao một dòng code kỳ lạ tồn tại — lịch sử commit là nơi duy nhất có thể lưu câu trả lời. "fix" không nói gì; "Fix double charge when user clicks Pay twice" nói rõ dòng đó giải quyết vấn đề gì; phần thân commit giải thích vì sao cách đơn giản hơn không dùng được có thể tiết kiệm hàng giờ điều tra. Commit tốt còn thể hiện sự tôn trọng đồng đội.',
        'questions': [
            ('Who will often look at the commit history in six months?', ['The client', 'You', 'The CEO', 'Nobody'], 1, '"Often, that someone will be you."'),
            ('What can the commit body save?', ['Disk space', 'Hours of investigation', 'Money', 'Meetings'], 1, 'Đoạn 2.'),
            ('According to the text, good commit messages are a sign of…', ['speed', 'respect for your teammates', 'seniority', 'perfect English'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Phần A: Sửa 5 commit message xấu: "fix", "updated css", "WIP", "changes for login", "Fixed the bug where users couldn\'t reset password because token expired too fast". Phần B: Viết 2 PR description (Summary / Changes / How to test / Notes) cho công việc thật của bạn.',
        'tips': ['Thể mệnh lệnh, ≤ 50 ký tự.', 'PR: tóm tắt 1–2 câu, gạch đầu dòng cho thay đổi, các bước kiểm thử đánh số.'],
        'model': "Part A:\n1. fix → Fix crash when profile photo is missing\n2. updated css → Align buttons on mobile checkout page\n3. WIP → Add draft layout for settings page\n4. changes for login → Add rate limit to login endpoint\n5. → Increase password reset token lifetime to 30 min\n\nPart B – PR 1:\n## Summary\nThis PR adds a rate limit to the login endpoint to stop brute-force attacks reported by the security team.\n## Changes\n- Limit login attempts to 5 per minute per IP\n- Return 429 with a clear error message\n- Add tests for the limit\n## How to test\n1. Try to log in with a wrong password 6 times\n2. Check that the 6th attempt returns 429\n## Notes\nCloses #231. No breaking changes.",
        'min_words': 80,
    },
    'quiz': [
        ('Commit message nào tốt nhất?', ['fixed bug', 'Fix crash when cart is empty', 'Fixing some stuff', 'WIP'], 1, 'Thể mệnh lệnh, cụ thể.'),
        ('Commit messages should be written in the ___ mood.', ['imperative', 'past', 'passive', 'continuous'], 0, 'imperative: Add, Fix, Remove.'),
        ('Câu kiểm tra: "If applied, this commit will ___."', ['added login', 'add login endpoint', 'adding login', 'login added'], 1, 'Tiêu đề phải ghép trơn tru.'),
        ('Combining many small commits into one = to ___.', ['squash', 'rebase', 'bump', 'revert'], 0, 'squash.'),
        ('Renaming a public API field is a ___.', ['breaking change', 'changelog', 'draft PR', 'squash'], 0, 'breaking change.'),
        ('A PR that is not ready yet but open for early feedback is a ___.', ['draft PR', 'drift PR', 'dry PR', 'hot PR'], 0, 'draft PR.'),
        ('"___ the version of React to 18.3."', ['Bump', 'Jump', 'Pump', 'Dump'], 0, 'Bump the version.'),
        ('Three parts of a good PR description:', ['Title, emoji, date', 'Summary, changes, how to test', 'Code, code, code', 'Author, reviewer, manager'], 1, 'Summary – Changes – How to test.'),
        ('The commit body should mainly explain…', ['who wrote it', 'why the change was made', 'what time it is', 'the variable names'], 1, 'Giải thích vì sao.'),
        ('"Closes #128" in a PR description will…', ['delete issue 128', 'automatically close issue 128 when merged', 'assign issue 128 to you', 'nothing'], 1, 'Từ khóa tự đóng issue.'),
    ],
}

DAY2 = {
    'title': 'Bug report và issue',
    'title_en': 'Writing Bug Reports',
    'goal': 'Viết bug report đầy đủ: tiêu đề rõ, steps to reproduce, expected result, actual result, environment — để người khác tái hiện được lỗi ngay.',
    'tasks': [
        'Học 14 từ về báo lỗi.',
        'Học khung bug report chuẩn.',
        'Nghe QA và developer trao đổi về một lỗi khó tái hiện.',
        'Viết 1 bug report mẫu cho một lỗi bạn từng gặp.',
    ],
    'product': '1 bug report mẫu',
    'warmup': [
        ("I can't reproduce the bug on my machine.", 'Tôi không tái hiện được lỗi trên máy mình.'),
        ('The expected result is a confirmation message.', 'Kết quả mong đợi là một thông báo xác nhận.'),
        ('The actual result is a blank page.', 'Kết quả thực tế là một trang trắng.'),
        ('It only happens on Safari.', 'Nó chỉ xảy ra trên Safari.'),
        ("It's intermittent: about one in ten times.", 'Lỗi lúc có lúc không: khoảng một trên mười lần.'),
        ('This looks like a regression from last week.', 'Có vẻ đây là lỗi tái phát từ tuần trước.'),
    ],
    'vocab': [
        ('reproduce', '/ˌriːprəˈdjuːs/', 'verb', 'tái hiện (lỗi)', 'Can you reproduce it on staging?', 'Bạn tái hiện được nó trên staging không?'),
        ('steps to reproduce', '/steps tə ˌriːprəˈdjuːs/', 'n', 'các bước tái hiện', 'Please add clear steps to reproduce.', 'Vui lòng thêm các bước tái hiện rõ ràng.'),
        ('expected result', '/ɪkˈspektɪd rɪˈzʌlt/', 'n', 'kết quả mong đợi', 'Expected result: the user is logged in.', 'Kết quả mong đợi: người dùng được đăng nhập.'),
        ('actual result', '/ˈæktʃuəl rɪˈzʌlt/', 'n', 'kết quả thực tế', 'Actual result: an error message appears.', 'Kết quả thực tế: hiện thông báo lỗi.'),
        ('intermittent', '/ˌɪntəˈmɪtənt/', 'adj', 'lúc có lúc không', 'Intermittent bugs are the hardest to fix.', 'Lỗi lúc có lúc không là khó sửa nhất.'),
        ('regression', '/rɪˈɡreʃn/', 'n', 'lỗi tái phát (thứ từng chạy giờ hỏng)', 'This is a regression from version 2.3.', 'Đây là lỗi tái phát từ bản 2.3.'),
        ('severity', '/sɪˈverəti/', 'n', 'mức độ nghiêm trọng', 'We marked it as high severity.', 'Chúng tôi đánh dấu mức độ nghiêm trọng cao.'),
        ('stack trace', '/ˈstæk treɪs/', 'n', 'dấu vết ngăn xếp (log lỗi)', 'Please attach the full stack trace.', 'Vui lòng đính kèm toàn bộ stack trace.'),
        ('freeze', '/friːz/', 'verb', 'đơ, đứng hình', 'The app freezes when I open the camera.', 'Ứng dụng bị đơ khi tôi mở camera.'),
        ('unexpected', '/ˌʌnɪkˈspektɪd/', 'adj', 'bất ngờ, ngoài dự kiến', 'An unexpected error occurred.', 'Đã xảy ra lỗi ngoài dự kiến.'),
        ('error message', '/ˈerə ˈmesɪdʒ/', 'n', 'thông báo lỗi', 'Copy the exact error message, please.', 'Vui lòng sao chép chính xác thông báo lỗi.'),
        ('affect', '/əˈfekt/', 'verb', 'ảnh hưởng đến', 'The bug affects all Android users.', 'Lỗi ảnh hưởng đến mọi người dùng Android.'),
        ('occur', '/əˈkɜː/', 'verb', 'xảy ra', 'The error occurs only after midnight.', 'Lỗi chỉ xảy ra sau nửa đêm.'),
        ('consistently', '/kənˈsɪstəntli/', 'adv', 'lần nào cũng (ổn định)', 'I can reproduce it consistently.', 'Lần nào tôi cũng tái hiện được.'),
    ],
    'lesson': """
<h3>1. Khung bug report chuẩn</h3>
<pre>Title: Checkout button does nothing on Safari 17 (iOS)

Steps to reproduce:
1. Open the app on an iPhone with Safari 17
2. Add any product to the cart
3. Go to the cart and tap "Checkout"

Expected result:
The payment page opens.

Actual result:
Nothing happens. No error message is shown.

Environment:
iPhone 13, iOS 17.2, Safari 17. Production, version 3.4.0.

Frequency: Consistently (5 out of 5 attempts).
Severity: High – users cannot pay.
Notes: Works fine on Chrome. Console shows "TypeError: …" (screenshot attached).</pre>

<h3>2. Tiêu đề tốt = hiện tượng + điều kiện</h3>
<table class="table">
<tr><th>Xấu</th><th>Tốt</th></tr>
<tr><td>Checkout broken!!!</td><td><span class="say">Checkout button does nothing on Safari 17</span></td></tr>
<tr><td>Bug in login</td><td><span class="say">Login fails with a 500 error when the email has a plus sign</span></td></tr>
<tr><td>App slow</td><td><span class="say">Order history takes 20 seconds to load for users with over 1,000 orders</span></td></tr>
</table>

<h3>3. Ngôn ngữ báo lỗi</h3>
<div class="ex"><span class="en">The app crashes / freezes / hangs when…</span></div>
<div class="ex"><span class="en">I get a 500 error / a blank page / a timeout.</span></div>
<div class="ex"><span class="en">It happens consistently / intermittently / only on…</span></div>
<div class="ex"><span class="en">This used to work in version 3.3, so it might be a regression.</span></div>
<div class="note"><b>Expected vs actual:</b> Luôn viết cả hai. "Nothing happens" chỉ là lỗi khi người đọc biết <i>điều gì đáng lẽ phải xảy ra</i>.</div>
""",
    'phrases': [
        ("I can't reproduce it on my side.", 'Phía tôi không tái hiện được.'),
        ('It happens about one in ten times.', 'Khoảng mười lần thì xảy ra một lần.'),
        ('This used to work in the previous version.', 'Cái này từng chạy được ở bản trước.'),
        ('Could you share the exact steps?', 'Bạn chia sẻ chính xác các bước được không?'),
    ],
    'listening': {
        'title': 'The bug that only happens sometimes',
        'intro': 'Tester Mai và developer Jake trao đổi về một lỗi khó tái hiện.',
        'speakers': {'A': ('Mai (QA)', 'ava'), 'B': ('Jake', 'ryan')},
        'lines': [
            ('B', "Hi Mai. I saw your ticket about the profile page, but I can't reproduce it on my machine.", 'Chào Mai. Mình thấy ticket của bạn về trang hồ sơ, nhưng mình không tái hiện được trên máy.'),
            ('A', "Yes, it's intermittent. It happens about one in ten times, so you might need to try a few times.", 'Đúng, lỗi lúc có lúc không. Khoảng mười lần thì xảy ra một lần, nên có thể bạn phải thử vài lần.'),
            ('B', "Okay. What exactly happens?", 'Được. Chính xác thì chuyện gì xảy ra?'),
            ('A', "The expected result is that you see your profile with your photo. The actual result is that the page freezes for a few seconds and then shows an unexpected error.", 'Kết quả mong đợi là bạn thấy hồ sơ có ảnh. Kết quả thực tế là trang bị đơ vài giây rồi hiện một lỗi ngoài dự kiến.'),
            ('B', "Does it affect all users?", 'Nó ảnh hưởng đến mọi người dùng không?'),
            ('A', "No, only users who uploaded a large photo, over five megabytes. I've added the steps to reproduce in the ticket.", 'Không, chỉ người dùng đã tải ảnh lớn, trên năm megabyte. Mình đã thêm các bước tái hiện vào ticket.'),
            ('B', "Ah, that's useful. Did you get a stack trace?", 'À, thông tin hữu ích. Bạn có lấy được stack trace không?'),
            ('A', "Yes, it's attached. It says 'timeout while resizing image'. Also, I think it's a regression. It worked fine in version 3.2.", 'Có, mình đính kèm rồi. Nó ghi "timeout while resizing image". Ngoài ra, mình nghĩ đây là lỗi tái phát. Ở bản 3.2 nó chạy tốt.'),
            ('B', "Then it's probably the new image library we added in 3.3. What severity did you give it?", 'Vậy chắc là thư viện ảnh mới bọn mình thêm vào bản 3.3. Bạn đánh mức nghiêm trọng thế nào?'),
            ('A', "Medium. Users can still use the app, but it looks bad.", 'Trung bình. Người dùng vẫn dùng được app, nhưng trông rất tệ.'),
            ('B', "Fair enough. With a large photo, I should be able to reproduce it consistently. Thanks for the detailed report!", 'Hợp lý. Với ảnh lớn, mình sẽ tái hiện được ổn định. Cảm ơn bạn đã báo cáo chi tiết!'),
        ],
        'questions': [
            ('Why couldn\'t Jake reproduce the bug at first?', ['It is intermittent.', 'He used the wrong browser.', 'The ticket was empty.', 'The server was down.'], 0, '"it\'s intermittent. It happens about one in ten times".'),
            ('What is the actual result?', ['The profile loads normally.', 'The page freezes and shows an error.', 'The photo is deleted.', 'The user is logged out.'], 1, 'Mai mô tả kết quả thực tế.'),
            ('Which users are affected?', ['All users', 'Users with photos over five megabytes', 'New users only', 'iPhone users'], 1, '"only users who uploaded a large photo, over five megabytes".'),
            ('Why does Mai think it is a regression?', ['It worked fine in version 3.2.', 'It never worked.', 'The client said so.', 'The stack trace says so.'], 0, '"It worked fine in version 3.2."'),
            ('What severity did Mai give it?', ['Low', 'Medium', 'High', 'Critical'], 1, '"Medium."'),
        ],
    },
    'speaking': {
        'tips': ['Báo lỗi bằng lời cho đồng nghiệp: hiện tượng → điều kiện → mong đợi vs thực tế → tần suất.'],
        'prompts': [
            ('Describe a bug you found recently to a developer, as if on a call.', 'When I…, the app… Expected… Actually…'),
            ('A developer says "I can\'t reproduce it." What do you say?', 'It happens only when… Let me share the exact steps.'),
        ],
        'model': (
            "Hi, I found a bug in the search page. When I search for a word with a Vietnamese accent, for example 'phở', the results page is completely blank. "
            "The expected result is a list of restaurants. The actual result is an empty page, with no error message. "
            "It happens consistently on both Chrome and Firefox, but only on production. On staging it works fine. "
            "I think it might be a regression, because it worked last week. I've added the steps and a screenshot to the ticket.",
            'Chào bạn, tôi tìm thấy một lỗi ở trang tìm kiếm. Khi tôi tìm một từ có dấu tiếng Việt, ví dụ "phở", trang kết quả trắng trơn. '
            'Kết quả mong đợi là danh sách nhà hàng. Kết quả thực tế là trang trống, không có thông báo lỗi. '
            'Lần nào cũng xảy ra trên cả Chrome và Firefox, nhưng chỉ trên production. Trên staging thì bình thường. '
            'Tôi nghĩ có thể là lỗi tái phát, vì tuần trước nó vẫn chạy. Tôi đã thêm các bước và ảnh chụp màn hình vào ticket.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'The cost of a bad bug report',
        'text': [
            'A bug report that says "the app doesn\'t work" can cost a team hours. The developer has to ask questions, wait for answers, guess which device was used and try many different actions before finding the problem.',
            'A good bug report, on the other hand, lets the developer reproduce the issue in minutes. The most important part is the steps to reproduce. They should be numbered, specific and start from a clear point, such as "log in as a new user".',
            'Two other details are often forgotten: the environment and the frequency. A bug that happens only on old Android phones, or only one time in fifty, needs a very different investigation from one that happens every time.',
        ],
        'vi': 'Bug report kiểu "app không chạy" có thể tốn của team hàng giờ: dev phải hỏi, chờ trả lời, đoán thiết bị và thử nhiều thao tác. Báo cáo tốt giúp tái hiện lỗi trong vài phút; phần quan trọng nhất là các bước tái hiện — đánh số, cụ thể, bắt đầu từ một điểm rõ ràng. Hai chi tiết hay bị quên: môi trường và tần suất xảy ra.',
        'questions': [
            ('What is the most important part of a bug report?', ['The title', 'The steps to reproduce', 'The severity', 'The screenshot'], 1, 'Đoạn 2.'),
            ('How should the steps be written?', ['As a long paragraph', 'Numbered, specific, from a clear starting point', 'In Vietnamese', 'Only one step'], 1, 'Đoạn 2.'),
            ('Which two details are often forgotten?', ['Title and author', 'Environment and frequency', 'Code and tests', 'Date and time'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết một bug report hoàn chỉnh cho một lỗi bạn từng gặp (trong công việc hoặc một app bạn dùng): Title, Steps to reproduce, Expected result, Actual result, Environment, Frequency, Severity.',
        'tips': ['Tiêu đề = hiện tượng + điều kiện.', 'Các bước đánh số, bắt đầu từ điểm rõ ràng.'],
        'model': "Title: Password reset email not sent when email contains uppercase letters\n\nSteps to reproduce:\n1. Go to the login page and click \"Forgot password\"\n2. Enter an existing email with uppercase letters, e.g. Nam.Tran@example.com\n3. Click \"Send reset link\"\n\nExpected result: A reset email arrives within one minute.\nActual result: The page says \"Email sent\", but no email arrives. Lowercase emails work fine.\n\nEnvironment: Production, web app v4.1.2, Chrome 129 on Windows 11.\nFrequency: Consistently (5/5).\nSeverity: High – affected users cannot recover their accounts.",
        'min_words': 70,
    },
    'quiz': [
        ('"I can\'t ___ the bug on my laptop." (tái hiện)', ['reproduce', 'produce', 'repeat up', 'replace'], 0, 'reproduce.'),
        ('A bug that happens only sometimes is ___.', ['intermittent', 'consistent', 'severe', 'expected'], 0, 'intermittent.'),
        ('Something that used to work but is now broken is a ___.', ['regression', 'progression', 'recession', 'feature'], 0, 'regression.'),
        ('What should happen = the ___ result.', ['expected', 'actual', 'unexpected', 'final'], 0, 'expected result.'),
        ('What really happens = the ___ result.', ['actual', 'expected', 'real-time', 'current up'], 0, 'actual result.'),
        ('Tiêu đề bug report tốt nhất:', ['HELP!!!', 'Bug', 'Login fails with 500 error when email has a plus sign', 'Something is wrong'], 2, 'Hiện tượng + điều kiện.'),
        ('The app ___ for ten seconds and then crashes. (đơ)', ['freezes', 'freeze', 'froze up', 'frozen'], 0, 'freezes.'),
        ('"The bug ___ all iOS users." (ảnh hưởng)', ['affects', 'effects', 'infects', 'afflicts up'], 0, 'affect (động từ).'),
        ('How serious a bug is = its ___.', ['severity', 'severe', 'sincerity', 'security'], 0, 'severity.'),
        ('"It happens ___: every single time."', ['consistently', 'intermittently', 'rarely', 'occasionally'], 0, 'consistently.'),
    ],
}

DAY3 = {
    'title': 'Email công việc',
    'title_en': 'Professional Emails',
    'goal': 'Viết email công việc rõ ràng, lịch sự với cấu trúc Subject – Chào – Mục đích – Yêu cầu hành động – Kết; tránh câu cộc lốc.',
    'tasks': [
        'Học 14 cụm từ dùng trong email.',
        'Học cấu trúc 5 phần của email công việc.',
        'Nghe đồng nghiệp góp ý cho một email.',
        'Viết 2 email mẫu: hỏi thông tin và cập nhật cho khách hàng.',
    ],
    'product': '2 email mẫu',
    'warmup': [
        ("I'm writing to ask about the project timeline.", 'Tôi viết thư này để hỏi về tiến độ dự án.'),
        ('Please find attached the updated report.', 'Vui lòng xem báo cáo cập nhật đính kèm.'),
        ('As discussed in our call, here are the next steps.', 'Như đã trao đổi trong cuộc gọi, đây là các bước tiếp theo.'),
        ('Could you please confirm by Friday?', 'Bạn vui lòng xác nhận trước thứ Sáu được không?'),
        ('Please let me know if you have any questions.', 'Vui lòng cho tôi biết nếu bạn có câu hỏi.'),
        ('Kind regards, Minh.', 'Trân trọng, Minh.'),
    ],
    'vocab': [
        ('regarding', '/rɪˈɡɑːdɪŋ/', 'prep', 'về việc', "I'm writing regarding your last invoice.", 'Tôi viết thư về hóa đơn gần nhất của bạn.'),
        ('please find attached', '/pliːz faɪnd əˈtætʃt/', 'phrase', 'vui lòng xem tệp đính kèm', 'Please find attached the signed contract.', 'Vui lòng xem hợp đồng đã ký đính kèm.'),
        ('at your earliest convenience', '/æt jɔːr ˈɜːliɪst kənˈviːniəns/', 'phrase', 'sớm nhất có thể (rất trang trọng)', 'Please reply at your earliest convenience.', 'Vui lòng trả lời sớm nhất khi có thể.'),
        ("I'm writing to", '/aɪm ˈraɪtɪŋ tuː/', 'phrase', 'tôi viết thư này để', "I'm writing to follow up on our meeting.", 'Tôi viết thư này để nối tiếp cuộc họp của chúng ta.'),
        ('kind regards', '/kaɪnd rɪˈɡɑːdz/', 'phrase', 'trân trọng (lời kết)', 'Kind regards, Lan', 'Trân trọng, Lan'),
        ('cc', '/ˌsiː ˈsiː/', 'verb', 'gửi kèm (đồng gửi)', "I've cc'd my manager on this email.", 'Tôi đã cc quản lý của tôi vào email này.'),
        ('as discussed', '/æz dɪˈskʌst/', 'phrase', 'như đã trao đổi', 'As discussed, the meeting is moved to Monday.', 'Như đã trao đổi, cuộc họp dời sang thứ Hai.'),
        ('in the meantime', '/ɪn ðə ˈmiːntaɪm/', 'phrase', 'trong lúc chờ đợi', 'In the meantime, you can use the old version.', 'Trong lúc chờ, bạn có thể dùng bản cũ.'),
        ('on behalf of', '/ɒn bɪˈhɑːf əv/', 'phrase', 'thay mặt cho', "I'm writing on behalf of the whole team.", 'Tôi viết thư thay mặt cả team.'),
        ('reach out', '/riːtʃ aʊt/', 'phrasal verb', 'liên hệ', "Feel free to reach out if you need help.", 'Cứ liên hệ nếu bạn cần giúp đỡ.'),
        ('apologies for', '/əˈpɒlədʒiz fɔː/', 'phrase', 'xin lỗi vì', 'Apologies for the late reply.', 'Xin lỗi vì trả lời muộn.'),
        ('recipient', '/rɪˈsɪpiənt/', 'n', 'người nhận', 'Check the recipients before you click Send.', 'Kiểm tra người nhận trước khi bấm Gửi.'),
        ('inquiry', '/ɪnˈkwaɪəri/', 'n', 'câu hỏi, yêu cầu thông tin', 'Thank you for your inquiry about our services.', 'Cảm ơn bạn đã hỏi về dịch vụ của chúng tôi.'),
        ('reminder', '/rɪˈmaɪndə/', 'n', 'lời nhắc', 'This is a friendly reminder about tomorrow\'s demo.', 'Đây là lời nhắc thân thiện về buổi demo ngày mai.'),
    ],
    'lesson': """
<h3>1. Cấu trúc 5 phần</h3>
<table class="table">
<tr><th>Phần</th><th>Mẫu</th></tr>
<tr><td>1. Subject</td><td>Cụ thể, có hành động: <span class="say">Request: staging access for new developer</span> · <span class="say">Update: release moved to Thursday</span></td></tr>
<tr><td>2. Chào</td><td><span class="say">Hi Anna,</span> (thân thiện) · <span class="say">Dear Mr. Smith,</span> (trang trọng)</td></tr>
<tr><td>3. Mục đích</td><td><span class="say">I'm writing to…</span> · <span class="say">I'm reaching out regarding…</span> · <span class="say">As discussed in our call, …</span></td></tr>
<tr><td>4. Yêu cầu hành động</td><td><span class="say">Could you please… by Friday?</span> · <span class="say">Please let me know if…</span></td></tr>
<tr><td>5. Kết</td><td><span class="say">Thanks in advance,</span> · <span class="say">Best regards,</span> · <span class="say">Kind regards,</span> + tên</td></tr>
</table>

<h3>2. Tránh câu cộc lốc</h3>
<table class="table">
<tr><th>Cộc</th><th>Chuyên nghiệp</th></tr>
<tr><td>Send me the file.</td><td><span class="say">Could you please send me the file?</span></td></tr>
<tr><td>I need it today.</td><td><span class="say">Would it be possible to have it by the end of today?</span></td></tr>
<tr><td>You didn't reply.</td><td><span class="say">I'm just following up on my email from Monday.</span></td></tr>
<tr><td>Sorry for late.</td><td><span class="say">Apologies for the late reply.</span></td></tr>
<tr><td>See attached.</td><td><span class="say">Please find the report attached.</span></td></tr>
</table>

<h3>3. Email mẫu</h3>
<pre>Subject: Request: access to the staging database

Hi David,

I hope you're doing well. I'm writing to ask for read access to the
staging database. I'm working on the new reporting feature, and I need
to test some queries with realistic data.

Could you please grant access to my account (minh.tran@company.com)
by Thursday? In the meantime, I'll continue with the frontend part.

Please let me know if you need any approval from my manager.

Thanks in advance,
Minh</pre>
<div class="note"><b>Mức độ trang trọng:</b> Đồng nghiệp: Hi + tên, Thanks/Best. Khách hàng mới, đối tác: Dear + tên, Kind regards. Dùng "at your earliest convenience" khi rất trang trọng; với đồng nghiệp chỉ cần "when you get a chance".</div>
""",
    'phrases': [
        ("I hope you're doing well.", 'Hy vọng bạn vẫn khỏe.'),
        ('Thanks in advance.', 'Cảm ơn trước.'),
        ("I'm just following up on my email from Monday.", 'Tôi chỉ muốn nhắc lại email hôm thứ Hai.'),
        ('Would it be possible to…?', 'Liệu có thể… không?'),
        ('Please let me know if anything is unclear.', 'Hãy cho tôi biết nếu có gì chưa rõ.'),
    ],
    'listening': {
        'title': 'Can you check my email?',
        'intro': 'Hiếu nhờ đồng nghiệp người Anh Laura xem giúp email gửi khách hàng trước khi gửi.',
        'speakers': {'A': ('Laura', 'sonia'), 'B': ('Hieu', 'andrew')},
        'lines': [
            ('B', "Laura, do you have a minute? I need to email the client about the delay, and I want to make sure it sounds okay.", 'Laura, bạn có một phút không? Mình cần email cho khách hàng về việc chậm trễ, và muốn chắc là nó nghe ổn.'),
            ('A', "Sure, read it to me.", 'Chắc chắn, đọc cho mình nghe đi.'),
            ('B', "Subject: Delay. Mr. Smith, the release will be late. We need one more week. Send me the new test data. Thanks.", 'Tiêu đề: Delay. Ông Smith, bản phát hành sẽ trễ. Chúng tôi cần thêm một tuần. Gửi tôi dữ liệu test mới. Cảm ơn.'),
            ('A', "Okay, the information is clear, but it sounds a bit direct. Let's improve it. First, the subject. 'Delay' alone is a bit alarming. Try 'Update on the release date'.", 'Được, thông tin rõ ràng nhưng nghe hơi thẳng. Cùng sửa nhé. Đầu tiên là tiêu đề. Chỉ "Delay" thì hơi đáng sợ. Thử "Update on the release date".'),
            ('B', "Good idea. And the greeting?", 'Ý hay. Còn lời chào?'),
            ('A', "'Dear Mr. Smith' is good for a client. Then add a friendly line, like 'I hope you're doing well', before the bad news.", '"Dear Mr. Smith" phù hợp với khách hàng. Rồi thêm một câu thân thiện như "I hope you\'re doing well" trước tin xấu.'),
            ('B', "And how should I explain the delay?", 'Còn giải thích việc chậm trễ thế nào?'),
            ('A', "Say what happened and the new date. For example: 'I'm writing to let you know that we need to move the release to the twelfth. During testing, we found an issue with the payment integration, and we want to fix it properly.'", 'Nói chuyện gì đã xảy ra và ngày mới. Ví dụ: "Tôi viết thư để báo rằng chúng tôi cần dời bản phát hành sang ngày mười hai. Trong quá trình kiểm thử, chúng tôi phát hiện vấn đề ở phần tích hợp thanh toán và muốn sửa cho đúng."'),
            ('B', "That sounds much better. And 'send me the new test data'?", 'Nghe hay hơn nhiều. Còn "send me the new test data"?'),
            ('A', "Make it a polite request: 'Could you please send us the updated test data by Wednesday?' And end with 'Apologies for the inconvenience' and 'Kind regards'.", 'Biến nó thành yêu cầu lịch sự: "Could you please send us the updated test data by Wednesday?" Và kết bằng "Apologies for the inconvenience" và "Kind regards".'),
            ('B', "Perfect. Thanks, Laura. I owe you a coffee.", 'Hoàn hảo. Cảm ơn Laura. Mình nợ bạn một ly cà phê.'),
        ],
        'questions': [
            ('What is the problem with Hieu\'s first email?', ['It has wrong information.', 'It sounds too direct.', 'It is too long.', 'It has no subject.'], 1, '"it sounds a bit direct".'),
            ('What subject line does Laura suggest?', ['Delay!!!', 'Update on the release date', 'Bad news', 'Release'], 1, '"Try \'Update on the release date\'".'),
            ('What should Hieu add before the bad news?', ['A joke', 'A friendly line like "I hope you\'re doing well"', 'The price', 'His phone number'], 1, 'Câu thân thiện trước tin xấu.'),
            ('What is the new release date?', ['The tenth', 'The twelfth', 'The twentieth', 'Next month'], 1, '"move the release to the twelfth".'),
            ('How should Hieu ask for the test data?', ['Send me the data.', 'Could you please send us the updated test data by Wednesday?', 'I need data now.', 'Data, please.'], 1, 'Yêu cầu lịch sự kèm thời hạn.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to 2 email bạn viết với giọng bình tĩnh, chuyên nghiệp.', 'Luyện chuyển câu cộc → câu lịch sự bằng lời.'],
        'prompts': [
            ('Make these polite out loud: "Send me the report." / "I need it today." / "You didn\'t reply."', 'Could you please… / Would it be possible… / Just following up…'),
            ('Read your client email aloud, slowly and clearly.', 'Phần Viết.'),
        ],
        'model': (
            "Dear Mr. Smith, I hope you're doing well. I'm writing to let you know that we need to move the release to the twelfth. "
            "During testing, we found an issue with the payment integration, and we want to fix it properly before going live. "
            "In the meantime, the current version will keep running as normal. "
            "Could you please send us the updated test data by Wednesday? Apologies for the inconvenience, and please let me know if you have any questions. "
            "Kind regards, Hieu.",
            'Kính gửi ông Smith, hy vọng ông vẫn khỏe. Tôi viết thư để báo rằng chúng tôi cần dời bản phát hành sang ngày mười hai. '
            'Trong quá trình kiểm thử, chúng tôi phát hiện vấn đề ở phần tích hợp thanh toán và muốn sửa cho đúng trước khi chạy thật. '
            'Trong thời gian đó, phiên bản hiện tại vẫn hoạt động bình thường. '
            'Ông vui lòng gửi cho chúng tôi dữ liệu test cập nhật trước thứ Tư được không? Xin lỗi vì sự bất tiện, và vui lòng cho tôi biết nếu ông có câu hỏi. '
            'Trân trọng, Hiếu.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Emails that get answered',
        'text': [
            'Busy people decide in a few seconds whether to answer an email now, later or never. The subject line and the first two sentences make that decision for them.',
            'Put your request at the top, not at the end of a long story. Instead of three paragraphs of background followed by "so could you approve the budget?", start with "Could you approve the attached budget by Friday?" and add the background below.',
            'Ask for one clear action and give a deadline. If you need several things, use a numbered list. Finally, make it easy to reply: a question that can be answered with "yes" or "no" gets a faster response than an open question.',
        ],
        'vi': 'Người bận rộn quyết định trong vài giây có trả lời email ngay, để sau hay bỏ qua — dựa trên tiêu đề và hai câu đầu. Đặt yêu cầu lên đầu, không để cuối một câu chuyện dài. Yêu cầu một hành động rõ ràng kèm thời hạn; nếu cần nhiều thứ, dùng danh sách đánh số. Câu hỏi trả lời được bằng "có/không" được phản hồi nhanh hơn câu hỏi mở.',
        'questions': [
            ('What helps busy people decide whether to answer?', ['The signature', 'The subject line and first two sentences', 'The attachments', 'The length'], 1, 'Đoạn 1.'),
            ('Where should you put your request?', ['At the end', 'At the top', 'In the attachment', 'In the subject only'], 1, 'Đoạn 2.'),
            ('Which question gets a faster response?', ['An open question', 'A yes/no question', 'A very long question', 'No question'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 2 email: (1) gửi đồng nghiệp xin quyền truy cập một hệ thống; (2) gửi khách hàng cập nhật tiến độ — một tính năng xong, một tính năng bị trễ 3 ngày.',
        'tips': ['Đủ 5 phần. Yêu cầu đặt lên đầu.', 'Email khách hàng: Dear…, Kind regards.'],
        'model': "Email 1\nSubject: Request: access to the analytics dashboard\n\nHi Sarah,\n\nCould you please give me view access to the analytics dashboard by Wednesday? I'm working on the new onboarding flow, and I need to check how many users finish each step.\n\nMy account is nam.le@company.com. Please let me know if my manager needs to approve this.\n\nThanks in advance,\nNam\n\nEmail 2\nSubject: Project update – week 12\n\nDear Ms. Johnson,\n\nI hope you're doing well. I'm writing to give you a quick update on the project. The online booking feature is finished and is now available on the test server. However, the SMS reminders will be three days late, because the SMS provider needs more time to approve our account. We now expect to deliver them on Thursday the 15th.\n\nApologies for the delay, and please let me know if you have any questions.\n\nKind regards,\nNam Le",
        'min_words': 120,
    },
    'quiz': [
        ('Best subject line:', ['Hi', 'Question', 'Request: staging access for new developer', 'URGENT!!!'], 2, 'Cụ thể, có hành động.'),
        ('"Please find ___ the report."', ['attached', 'attach', 'attaching', 'attachment'], 0, 'Please find attached…'),
        ('"I\'m writing ___ your last invoice."', ['regarding', 'regard', 'regards', 'in regard'], 0, 'regarding = về việc.'),
        ('Polite version of "Sorry for late":', ['Apologies for the late reply.', 'Sorry late.', 'I am late sorry.', 'Late, sorry.'], 0, 'Apologies for the late reply.'),
        ('"___ discussed, the meeting is on Monday."', ['As', 'Like', 'Such', 'So'], 0, 'As discussed.'),
        ('"___, you can use the old version." (trong lúc chờ)', ['In the meantime', 'In the meanwhile time', 'At meantime', 'Meantime in'], 0, 'In the meantime.'),
        ('Formal closing for a new client:', ['Cheers', 'Kind regards', 'Bye', 'See ya'], 1, 'Kind regards.'),
        ('Where should the main request go?', ['At the very end', 'At the top', 'In a P.S.', 'In the subject only'], 1, 'Đặt yêu cầu lên đầu.'),
        ('"Thank you for your ___ about our prices."', ['inquiry', 'inquire', 'inquiring', 'inquired'], 0, 'inquiry (danh từ).'),
        ('Nhắc lại email chưa được trả lời một cách lịch sự:', ['Why no reply?', "I'm just following up on my email from Monday.", 'Hello???', 'Answer please.'], 1, 'Just following up…'),
    ],
}

DAY4 = {
    'title': 'Tin nhắn trên Slack',
    'title_en': 'Slack & Chat Messages',
    'goal': 'Viết tin nhắn chat ngắn, rõ, thân thiện: hỏi thông tin, xin review, báo trễ hạn, cảm ơn đồng nghiệp — và dùng đúng các viết tắt phổ biến.',
    'tasks': [
        'Học 14 từ/viết tắt dùng trên Slack.',
        'Học quy tắc "một tin nhắn đầy đủ" (không gửi "hi" rồi chờ).',
        'Nghe hai đồng nghiệp nói về văn hóa chat của team.',
        'Viết 5 tin nhắn mẫu.',
    ],
    'product': '5 tin nhắn Slack mẫu',
    'warmup': [
        ("Hi Tom! Quick question about the API, when you get a chance.", 'Chào Tom! Một câu hỏi nhanh về API, khi bạn rảnh nhé.'),
        ('No rush, tomorrow is fine.', 'Không gấp đâu, mai cũng được.'),
        ("I'll ping you when it's ready.", 'Tôi sẽ nhắn bạn khi xong.'),
        ("Let's move this to a thread.", 'Mình chuyển sang thread nhé.'),
        ('FYI, the staging server is down.', 'Thông tin để bạn biết: server staging đang sập.'),
        ('Thanks so much, really appreciate it!', 'Cảm ơn nhiều, thật sự rất cảm kích!'),
    ],
    'vocab': [
        ('when you get a chance', '/wen juː ɡet ə tʃɑːns/', 'phrase', 'khi bạn rảnh', 'Could you review my PR when you get a chance?', 'Bạn review PR của tôi khi rảnh nhé?'),
        ('ping', '/pɪŋ/', 'verb', 'nhắn (nhanh)', "Ping me if you need anything.", 'Nhắn tôi nếu bạn cần gì.'),
        ('no rush', '/nəʊ rʌʃ/', 'phrase', 'không gấp', 'No rush, but it would be great to have it this week.', 'Không gấp, nhưng có trong tuần này thì tốt.'),
        ('appreciate', '/əˈpriːʃieɪt/', 'verb', 'cảm kích, trân trọng', 'I really appreciate your help.', 'Tôi rất cảm kích sự giúp đỡ của bạn.'),
        ('thread', '/θred/', 'n', 'luồng trả lời (thread)', 'Please reply in the thread to keep the channel clean.', 'Vui lòng trả lời trong thread cho kênh gọn gàng.'),
        ('DM', '/ˌdiː ˈem/', 'n / verb', 'tin nhắn riêng; nhắn riêng', "I'll DM you the password.", 'Tôi sẽ nhắn riêng mật khẩu cho bạn.'),
        ('loop in', '/luːp ɪn/', 'phrasal verb', 'kéo (ai) vào cuộc trao đổi', "Let me loop in Sarah, she knows the payment system.", 'Để tôi kéo Sarah vào, cô ấy rành hệ thống thanh toán.'),
        ('FYI', '/ˌef waɪ ˈaɪ/', 'abbr', 'để bạn biết (for your information)', 'FYI, the meeting moved to 3 p.m.', 'Để bạn biết, cuộc họp dời sang 3 giờ chiều.'),
        ('ASAP', '/ˌeɪ es eɪ ˈpiː/', 'abbr', 'càng sớm càng tốt', 'Please fix it ASAP, the client is waiting.', 'Vui lòng sửa càng sớm càng tốt, khách đang chờ.'),
        ('EOD', '/ˌiː əʊ ˈdiː/', 'abbr', 'cuối ngày (end of day)', "I'll send the report by EOD.", 'Tôi sẽ gửi báo cáo trước cuối ngày.'),
        ('TL;DR', '/ˌtiː el ˈdiː ɑː/', 'abbr', 'tóm tắt nhanh (too long; didn\'t read)', 'TL;DR: the release moves to Thursday.', 'Tóm tắt: bản phát hành dời sang thứ Năm.'),
        ('shout-out', '/ˈʃaʊt aʊt/', 'n', 'lời khen công khai', 'Big shout-out to Linh for fixing the outage!', 'Xin khen Linh vì đã khắc phục sự cố!'),
        ('hop on a call', '/hɒp ɒn ə kɔːl/', 'phrase', 'gọi nhanh', 'Can we hop on a call for five minutes?', 'Mình gọi nhanh năm phút được không?'),
        ('OOO', '/ˌəʊ əʊ ˈəʊ/', 'abbr', 'vắng mặt (out of office)', "I'm OOO tomorrow, back on Thursday.", 'Mai tôi nghỉ, thứ Năm quay lại.'),
    ],
    'lesson': """
<h3>1. Quy tắc vàng: đừng gửi "Hi" rồi chờ</h3>
<p>Ở team remote, một tin nhắn chỉ có "Hi" bắt người kia phải chờ bạn gõ tiếp. Hãy gửi <b>chào + câu hỏi + bối cảnh</b> trong một tin:</p>
<div class="fix"><s>Hi<br>(5 phút sau) Are you there?<br>(5 phút sau) I have a question</s><span class="en">Hi Tom! Quick question: which endpoint should I use to get a user's orders? I tried /orders but it returns everything. No rush 🙂</span></div>

<h3>2. Năm loại tin nhắn hay gặp</h3>
<table class="table">
<tr><th>Mục đích</th><th>Mẫu</th></tr>
<tr><td>Hỏi thông tin</td><td><span class="say">Hi Anna, quick question about the new API: do we need authentication for the public endpoints? No rush.</span></td></tr>
<tr><td>Xin review</td><td><span class="say">Hey team, my PR for the export feature is ready for review. It's quite small, about 150 lines. Thanks in advance!</span></td></tr>
<tr><td>Báo trễ hạn</td><td><span class="say">Heads-up: the export feature will be one day late. I found an issue with large files. New ETA: Thursday EOD.</span></td></tr>
<tr><td>Cảm ơn</td><td><span class="say">Thanks so much for your help with the migration yesterday, really appreciate it!</span></td></tr>
<tr><td>Thông báo</td><td><span class="say">FYI: staging will be down from 8 to 9 p.m. tonight for maintenance.</span></td></tr>
</table>

<h3>3. Viết tắt — dùng đúng chỗ</h3>
<table class="table">
<tr><th>Viết tắt</th><th>Nghĩa</th><th>Lưu ý</th></tr>
<tr><td>FYI</td><td>for your information</td><td>Thông tin, không cần làm gì</td></tr>
<tr><td>ASAP</td><td>as soon as possible</td><td>Dùng ít — dễ nghe như ra lệnh</td></tr>
<tr><td>EOD / EOW</td><td>end of day / week</td><td>Ghi rõ múi giờ nếu team ở nhiều nước</td></tr>
<tr><td>TL;DR</td><td>tóm tắt</td><td>Đặt đầu tin nhắn dài</td></tr>
<tr><td>OOO</td><td>out of office</td><td>Báo nghỉ</td></tr>
<tr><td>IMO</td><td>in my opinion</td><td>Thân mật</td></tr>
</table>
<div class="note"><b>Giọng điệu:</b> Chat ngắn dễ nghe lạnh lùng. Một lời cảm ơn, "no rush" hay một emoji 🙂 làm tin nhắn thân thiện hơn mà vẫn chuyên nghiệp.</div>
""",
    'phrases': [
        ('Quick question about…', 'Một câu hỏi nhanh về…'),
        ('Let me loop in…', 'Để tôi kéo … vào.'),
        ("Let's move this to a thread.", 'Mình chuyển sang thread nhé.'),
        ('Can we hop on a quick call?', 'Mình gọi nhanh được không?'),
        ('Really appreciate it!', 'Thật sự cảm kích!'),
    ],
    'listening': {
        'title': 'Our team\'s chat rules',
        'intro': 'Team lead Ben giải thích "luật chat" của team cho thành viên mới Nhi.',
        'speakers': {'A': ('Ben', 'guy'), 'B': ('Nhi', 'ava')},
        'lines': [
            ('A', "Nhi, before you start, let me explain how we use Slack. We're in four time zones, so chat is really important.", 'Nhi, trước khi bắt đầu, để anh giải thích cách team dùng Slack. Chúng ta ở bốn múi giờ nên chat rất quan trọng.'),
            ('B', "Sure, I'd love to know.", 'Vâng, em rất muốn biết.'),
            ('A', "Rule one: don't just say 'hi' and wait. Write your whole question in one message, with context. People might be asleep when you send it.", 'Quy tắc một: đừng chỉ gửi "hi" rồi chờ. Viết cả câu hỏi trong một tin, kèm bối cảnh. Người nhận có thể đang ngủ khi em gửi.'),
            ('B', "That makes sense. What else?", 'Hợp lý ạ. Còn gì nữa?'),
            ('A', "Rule two: reply in threads. If ten people answer in the main channel, it becomes impossible to follow.", 'Quy tắc hai: trả lời trong thread. Nếu mười người trả lời ở kênh chính, sẽ không thể theo dõi được.'),
            ('B', "Got it. And if something is urgent?", 'Em hiểu. Còn nếu có việc gấp?'),
            ('A', "Then mention the person directly and say why it's urgent. But please don't write ASAP on everything. If everything is urgent, nothing is.", 'Thì nhắc trực tiếp người đó và nói vì sao gấp. Nhưng đừng ghi ASAP cho mọi thứ. Nếu cái gì cũng gấp thì chẳng có gì gấp cả.'),
            ('B', "Ha, fair. What about deadlines like EOD? Whose end of day?", 'Ha, đúng ạ. Còn hạn kiểu EOD? Cuối ngày của ai ạ?'),
            ('A', "Great question. Always add the time zone, like 'Thursday 5 p.m. Vietnam time'. And if a chat takes more than five messages back and forth, just hop on a quick call.", 'Câu hỏi hay. Luôn ghi múi giờ, kiểu "5 giờ chiều thứ Năm giờ Việt Nam". Và nếu một cuộc chat qua lại hơn năm tin, cứ gọi nhanh.'),
            ('B', "Thanks, Ben. Really appreciate it.", 'Cảm ơn anh Ben. Em rất cảm kích.'),
            ('A', "No problem. Oh, and we give shout-outs in the general channel when someone helps us. It's a nice habit.", 'Không có gì. À, team mình hay khen công khai ở kênh chung khi ai đó giúp mình. Thói quen hay đấy.'),
        ],
        'questions': [
            ('Why is chat especially important for this team?', ['They don\'t like meetings.', 'They work in four time zones.', 'The office is noisy.', 'Their manager prefers it.'], 1, '"We\'re in four time zones".'),
            ('What is rule one?', ['Always use emojis', 'Don\'t just say "hi" and wait', 'Never send DMs', 'Reply within five minutes'], 1, 'Quy tắc một.'),
            ('Why should people reply in threads?', ['It is faster to type.', 'The main channel becomes impossible to follow otherwise.', 'Threads are private.', 'Managers can\'t see threads.'], 1, 'Quy tắc hai.'),
            ('What does Ben say about ASAP?', ['Use it on every message.', 'If everything is urgent, nothing is.', 'Never use it.', 'Only managers can use it.'], 1, '"If everything is urgent, nothing is."'),
            ('When should you hop on a call?', ['Every morning', 'When a chat takes more than five messages back and forth', 'Never', 'Only for urgent issues'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to 5 tin nhắn bạn viết như đang gửi voice message.', 'Luyện xin gọi nhanh khi chat quá dài.'],
        'prompts': [
            ('Leave a voice message asking a colleague a question, with context.', 'Hi…, quick question… No rush.'),
            ('Give a shout-out to a teammate who helped you this week.', 'Big shout-out to… for…'),
        ],
        'model': (
            "Hi Linh, quick question about the invoice service. When I call the create invoice endpoint, it returns a 403 error, even with an admin token. "
            "Do I need a special permission for it? No rush, any time today is fine. Thanks! "
            "And a big shout-out to Khoa for helping me set up my local environment yesterday. It took him an hour of his evening, and I really appreciate it.",
            'Chào Linh, một câu hỏi nhanh về dịch vụ hóa đơn. Khi mình gọi endpoint tạo hóa đơn, nó trả lỗi 403, kể cả với token admin. '
            'Mình có cần quyền đặc biệt không? Không gấp, trong hôm nay lúc nào cũng được. Cảm ơn! '
            'Và xin gửi lời khen tới Khoa vì đã giúp mình cài môi trường trên máy hôm qua. Bạn ấy mất một tiếng buổi tối, mình thật sự cảm kích.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'No hello',
        'text': [
            'Imagine you are focused on a difficult bug. A message arrives: "Hi". You reply "Hi!" and wait. Two minutes later: "Are you busy?" You reply "A bit, what\'s up?" Another two minutes: "I have a question about the API." Five minutes and three interruptions later, you finally know what the question is.',
            'This pattern is so common that some developers add a link to a page called "No Hello" in their chat status. The idea is simple: say hello and ask your question in the same message.',
            'It may feel less polite at first, especially in cultures where greetings are important. But in remote work, a complete message is actually the polite option, because it respects the other person\'s time and focus.',
        ],
        'vi': 'Tưởng tượng bạn đang tập trung gỡ lỗi khó, một tin "Hi" đến, bạn trả lời rồi chờ… năm phút và ba lần gián đoạn sau mới biết câu hỏi là gì. Kiểu này phổ biến đến mức nhiều dev để link trang "No Hello" ở trạng thái chat: chào và hỏi trong cùng một tin. Lúc đầu có vẻ kém lịch sự, nhất là ở văn hóa coi trọng lời chào, nhưng trong làm việc từ xa, tin nhắn đầy đủ mới là lựa chọn lịch sự vì tôn trọng thời gian và sự tập trung của người khác.',
        'questions': [
            ('What is the problem in the first paragraph?', ['The question is too hard.', 'Many small messages interrupt the person.', 'The person never replies.', 'The API is broken.'], 1, 'Đoạn 1.'),
            ('What is the "No Hello" idea?', ['Never greet people', 'Say hello and ask your question in one message', 'Only use email', 'Use voice messages'], 1, 'Đoạn 2.'),
            ('Why is a complete message the polite option in remote work?', ['It is shorter.', 'It respects the other person\'s time and focus.', 'Managers require it.', 'It uses fewer emojis.'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 5 tin nhắn Slack: (1) hỏi thông tin, (2) xin review PR, (3) báo trễ hạn kèm ETA mới, (4) cảm ơn đồng nghiệp, (5) thông báo FYI cho cả kênh.',
        'tips': ['Mỗi tin nhắn đầy đủ trong một lần gửi.', 'Có múi giờ khi nói về thời hạn.'],
        'model': "1. Hi Sarah! Quick question about the payment API: is the refund endpoint idempotent, or should we add our own key? No rush, tomorrow is fine 🙂\n2. Hey team, my PR for the CSV export is ready for review (~150 lines, mostly tests). Could someone take a look when you get a chance? Thanks!\n3. Heads-up: the CSV export will be one day late. Large files time out, so I'm adding pagination. New ETA: Thursday 5 p.m. Vietnam time.\n4. Thanks so much for pairing with me on the migration yesterday, Duc. Really appreciate it!\n5. FYI: staging will be down tonight from 8 to 9 p.m. (Vietnam time) for a database upgrade.",
        'min_words': 80,
    },
    'quiz': [
        ('Cách nhắn tốt nhất trong team remote:', ['Hi (rồi chờ)', 'Are you there?', 'Hi Tom! Quick question: which endpoint returns user orders? No rush.', '???'], 2, 'Chào + câu hỏi + bối cảnh trong một tin.'),
        ('"___: the meeting moved to 3 p.m." (để bạn biết)', ['FYI', 'ASAP', 'EOD', 'OOO'], 0, 'FYI.'),
        ('"I\'ll send it by ___." (cuối ngày)', ['EOD', 'OOO', 'TL;DR', 'DM'], 0, 'EOD.'),
        ('"I\'m ___ tomorrow, back on Thursday."', ['OOO', 'FYI', 'ASAP', 'EOD'], 0, 'OOO = out of office.'),
        ('"Let me ___ Sarah, she knows the system."', ['loop in', 'loop out', 'ping off', 'take in'], 0, 'loop in.'),
        ('"Can we ___ a quick call?"', ['hop on', 'jump at', 'go in', 'hop up'], 0, 'hop on a call.'),
        ('A short summary at the top of a long message:', ['TL;DR', 'FYI', 'EOD', 'DM'], 0, 'TL;DR.'),
        ('"No ___, tomorrow is fine."', ['rush', 'hurry up', 'fast', 'quick'], 0, 'No rush.'),
        ('Viết ASAP cho mọi tin nhắn thì:', ['Mọi người làm nhanh hơn', 'Không còn gì thực sự gấp', 'Lịch sự hơn', 'Chuyên nghiệp hơn'], 1, '"If everything is urgent, nothing is."'),
        ('Khi nói hạn chót với team nhiều nước, nên:', ['Ghi rõ múi giờ', 'Chỉ ghi EOD', 'Không ghi giờ', 'Dùng giờ của mình'], 0, 'Ghi rõ múi giờ.'),
    ],
}

DAY5 = {
    'title': 'Tự sửa bài viết',
    'title_en': 'Self-editing Your Writing',
    'goal': 'Tự soát và sửa văn bản trước khi gửi: các cặp từ hay nhầm, lỗi ngữ pháp thường gặp, câu quá dài — thay cho buổi sửa bài với gia sư.',
    'tasks': [
        'Học 12 cặp từ hay nhầm.',
        'Học checklist tự sửa 6 bước.',
        'Nghe gia sư sửa một email.',
        'Sửa 3 văn bản đã viết trong tuần, ghi lại từng lỗi và cách sửa.',
        '(Tùy chọn) Gửi 3 văn bản cho gia sư thật hoặc đồng nghiệp sửa.',
    ],
    'product': 'Danh sách lỗi và cách sửa',
    'warmup': [
        ("It's important to check its spelling.", 'Quan trọng là kiểm tra chính tả của nó.'),
        ('The new design will affect the whole app.', 'Thiết kế mới sẽ ảnh hưởng đến toàn ứng dụng.'),
        ('The effect was bigger than we expected.', 'Tác động lớn hơn chúng tôi dự kiến.'),
        ("This version is faster than the old one.", 'Phiên bản này nhanh hơn bản cũ.'),
        ("We had fewer bugs and less stress.", 'Chúng tôi có ít lỗi hơn và ít căng thẳng hơn.'),
        ("Always proofread before you hit Send.", 'Luôn soát lại trước khi bấm Gửi.'),
    ],
    'vocab': [
        ('affect / effect', '/əˈfekt/ – /ɪˈfekt/', 'verb / n', 'ảnh hưởng (động từ) / tác động (danh từ)', 'The outage affected thousands of users; the effect on sales was huge.', 'Sự cố ảnh hưởng hàng nghìn người dùng; tác động lên doanh số rất lớn.'),
        ("its / it's", "/ɪts/ – /ɪts/", 'det / contraction', "của nó / = it is, it has", "It's a great tool, but its documentation is poor.", 'Đó là công cụ tuyệt vời, nhưng tài liệu của nó kém.'),
        ('then / than', '/ðen/ – /ðæn/', 'adv / conj', 'sau đó / hơn (so sánh)', 'First test it, then deploy it. It is faster than before.', 'Đầu tiên kiểm thử, sau đó triển khai. Nó nhanh hơn trước.'),
        ('lose / loose', '/luːz/ – /luːs/', 'verb / adj', 'mất / lỏng', "Don't lose your keys. The cable is loose.", 'Đừng làm mất chìa khóa. Dây cáp bị lỏng.'),
        ('advice / advise', '/ədˈvaɪs/ – /ədˈvaɪz/', 'n / verb', 'lời khuyên / khuyên', 'Thanks for the advice. I advise you to back up first.', 'Cảm ơn lời khuyên. Tôi khuyên bạn sao lưu trước.'),
        ('fewer / less', '/ˈfjuːə/ – /les/', 'det', 'ít hơn (đếm được / không đếm được)', 'Fewer bugs, less time spent on support.', 'Ít lỗi hơn, ít thời gian hỗ trợ hơn.'),
        ("your / you're", "/jɔː/ – /jʊə/", 'det / contraction', "của bạn / = you are", "You're right, your code works.", 'Bạn đúng, code của bạn chạy được.'),
        ('there / their', '/ðeə/ – /ðeə/', 'adv / det', 'ở đó, có / của họ', 'There are three developers; their team is in Hue.', 'Có ba lập trình viên; team của họ ở Huế.'),
        ('accept / except', '/əkˈsept/ – /ɪkˈsept/', 'verb / prep', 'chấp nhận / ngoại trừ', 'We accept all cards except American Express.', 'Chúng tôi chấp nhận mọi thẻ ngoại trừ American Express.'),
        ('complement / compliment', '/ˈkɒmplɪment/', 'n / verb', 'bổ sung / lời khen', 'The two tools complement each other. Thanks for the compliment!', 'Hai công cụ bổ sung cho nhau. Cảm ơn lời khen!'),
        ('principle / principal', '/ˈprɪnsəpl/', 'n / adj', 'nguyên tắc / chính, chủ yếu', 'Keep it simple is a good principle. She is a principal engineer.', '"Giữ mọi thứ đơn giản" là nguyên tắc hay. Cô ấy là kỹ sư chính.'),
        ('who\'s / whose', '/huːz/ – /huːz/', 'contraction / det', '= who is / của ai', "Who's on call tonight? Whose laptop is this?", 'Ai trực tối nay? Laptop này của ai?'),
        ('proofread', '/ˈpruːfriːd/', 'verb', 'soát lỗi văn bản', 'Proofread your email before sending it.', 'Soát lỗi email trước khi gửi.'),
        ('typo', '/ˈtaɪpəʊ/', 'n', 'lỗi gõ máy', 'There is a typo in the subject line.', 'Có một lỗi gõ ở dòng tiêu đề.'),
    ],
    'lesson': """
<h3>1. Checklist tự sửa 6 bước</h3>
<ol>
<li><b>Mục đích có ở 2 câu đầu chưa?</b> Người đọc biết ngay bạn muốn gì?</li>
<li><b>Thì động từ:</b> since/for → hiện tại hoàn thành; mốc quá khứ → quá khứ đơn.</li>
<li><b>Chủ ngữ – động từ:</b> he/she/it + V-s; there is/are đúng số.</li>
<li><b>Mạo từ:</b> a/an/the — danh từ đếm được số ít cần mạo từ.</li>
<li><b>Cặp từ hay nhầm:</b> its/it's, then/than, affect/effect, fewer/less…</li>
<li><b>Câu dài &gt; 25 từ:</b> tách đôi. Đọc to — chỗ nào vấp thì sửa.</li>
</ol>

<h3>2. Lỗi viết người Việt hay mắc</h3>
<div class="fix"><s>I have attached file for you.</s><span class="en">I have attached the file for you.</span><span class="vi">Thiếu mạo từ.</span></div>
<div class="fix"><s>Please kindly check and feedback.</s><span class="en">Could you please check it and let me know your feedback?</span><span class="vi">"feedback" là danh từ, không dùng như động từ.</span></div>
<div class="fix"><s>I will inform to you later.</s><span class="en">I will let you know later. / I will inform you later.</span></div>
<div class="fix"><s>Please advise me the solution.</s><span class="en">Please advise on the best solution.</span></div>
<div class="fix"><s>We have discussed about this issue.</s><span class="en">We have discussed this issue.</span></div>
<div class="fix"><s>The informations are in the attachment.</s><span class="en">The information is in the attachment.</span><span class="vi">information không đếm được.</span></div>
<div class="fix"><s>It's more faster then before.</s><span class="en">It's much faster than before.</span></div>

<h3>3. Công cụ hỗ trợ (nhưng đừng phụ thuộc)</h3>
<ul>
<li>Bật kiểm tra chính tả tiếng Anh trong trình duyệt và editor.</li>
<li>Dùng Grammarly hoặc trợ lý AI để <b>tìm</b> lỗi, nhưng tự hiểu và sửa — ghi lỗi vào danh sách của bạn.</li>
<li>Dùng nút <b>"Nghe bài của tôi"</b> ở phần Viết: nghe máy đọc bài của bạn, câu nào nghe lạ thì sửa.</li>
</ul>
""",
    'phrases': [
        ('Could you proofread this for me?', 'Bạn soát lỗi giúp tôi được không?'),
        ('Does this sound natural?', 'Câu này nghe có tự nhiên không?'),
        ('Is there a better way to say this?', 'Có cách nói nào hay hơn không?'),
    ],
    'listening': {
        'title': 'A tutor corrects an email',
        'intro': 'Gia sư Rachel sửa email của học viên Tùng, giải thích từng lỗi.',
        'speakers': {'A': ('Rachel (tutor)', 'jenny'), 'B': ('Tung', 'brian')},
        'lines': [
            ('A', "Okay Tung, I've read your email. The structure is really good. Let's look at a few small things.", 'Được rồi Tùng, cô đọc email của em rồi. Cấu trúc rất tốt. Cùng xem vài điểm nhỏ nhé.'),
            ('B', "Great, thank you.", 'Tuyệt, cảm ơn cô.'),
            ('A', "In the first line, you wrote 'I have attached file for you'. What's missing?", 'Dòng đầu em viết "I have attached file for you". Thiếu gì?'),
            ('B', "Oh, 'the'. 'I have attached the file.'", 'Ồ, "the". "I have attached the file."'),
            ('A', "Exactly. Articles are the most common mistake for Vietnamese speakers, because Vietnamese doesn't have them.", 'Chính xác. Mạo từ là lỗi phổ biến nhất của người Việt, vì tiếng Việt không có mạo từ.'),
            ('A', "Next: 'Please check and feedback.' 'Feedback' is a noun, so we say 'Please check it and let me know your feedback'.", 'Tiếp theo: "Please check and feedback." "Feedback" là danh từ, nên ta nói "Please check it and let me know your feedback".'),
            ('B', "I see. I've been writing that for years!", 'Em hiểu rồi. Em viết vậy nhiều năm rồi!'),
            ('A', "You're not alone. Then here: 'The new version is more faster then the old one.' There are two mistakes.", 'Em không phải người duy nhất đâu. Rồi ở đây: "The new version is more faster then the old one." Có hai lỗi.'),
            ('B', "Hmm, 'faster' already means 'more fast', so no 'more'. And… 'than', not 'then'?", 'Hừm, "faster" đã là "more fast" nên bỏ "more". Và… "than" chứ không phải "then"?'),
            ('A', "Perfect. 'Then' is about time, 'than' is for comparisons. My advice: keep a list of these mistakes and check it before you send any important email.", 'Hoàn hảo. "Then" nói về thời gian, "than" dùng để so sánh. Lời khuyên của cô: giữ một danh sách các lỗi này và kiểm tra trước khi gửi email quan trọng.'),
        ],
        'questions': [
            ('What does Rachel say about the structure of the email?', ['It is bad.', 'It is really good.', 'It is too long.', 'It needs a subject.'], 1, '"The structure is really good."'),
            ('Why are articles difficult for Vietnamese speakers?', ['They are too long.', 'Vietnamese doesn\'t have them.', 'They are not important.', 'Teachers don\'t teach them.'], 1, '"because Vietnamese doesn\'t have them".'),
            ('What is wrong with "Please check and feedback"?', ['"feedback" is a noun, not a verb', '"check" is wrong', 'It is too polite', 'Nothing'], 0, '"\'Feedback\' is a noun".'),
            ('What is Rachel\'s final advice?', ['Use a translation app', 'Keep a list of mistakes and check it before sending', 'Write shorter emails', 'Stop writing emails'], 1, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to các cặp từ hay nhầm, chú ý cặp phát âm khác nhau: advice /s/ – advise /z/, lose /z/ – loose /s/.'],
        'prompts': [
            ('Read the confusing pairs aloud: advice/advise, lose/loose, affect/effect, accept/except.', 'Chú ý âm cuối /s/ và /z/.'),
            ('Explain to a friend the difference between "fewer" and "less".', 'fewer + danh từ đếm được; less + không đếm được.'),
        ],
        'model': (
            "Here's an easy way to remember fewer and less. Use fewer with things you can count, like bugs, meetings or users. "
            "For example, this sprint we had fewer bugs than last sprint. "
            "Use less with things you can't count, like time, money or stress. For example, we spent less time on support. "
            "So you could say: fewer meetings, less stress.",
            'Đây là cách dễ nhớ fewer và less. Dùng fewer với những thứ đếm được, như lỗi, cuộc họp hay người dùng. '
            'Ví dụ, sprint này chúng tôi có ít lỗi hơn sprint trước. '
            'Dùng less với những thứ không đếm được, như thời gian, tiền hay căng thẳng. Ví dụ, chúng tôi tốn ít thời gian hỗ trợ hơn. '
            'Vậy bạn có thể nói: ít cuộc họp hơn, ít căng thẳng hơn.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Read it aloud',
        'text': [
            'One of the simplest editing techniques is also one of the most effective: read your text aloud before you send it. Your ears notice problems that your eyes skip.',
            'When you read silently, your brain fills in missing words and corrects small mistakes automatically. When you read aloud, you have to say every word, so a missing "the" or a sentence that is far too long becomes obvious. If you run out of breath, the sentence needs to be split.',
            'If you are shy about reading aloud at work, let your computer do it. Most operating systems and browsers can read text with a natural voice. Listening to your own email in someone else\'s voice is a surprisingly good way to hear how it will sound to the reader.',
        ],
        'vi': 'Một kỹ thuật sửa bài đơn giản mà hiệu quả: đọc to văn bản trước khi gửi — tai nhận ra lỗi mà mắt bỏ qua. Khi đọc thầm, não tự điền từ thiếu và sửa lỗi nhỏ; khi đọc to, mỗi từ phải được nói ra nên thiếu "the" hay câu quá dài lộ rõ; hết hơi nghĩa là câu cần tách. Nếu ngại đọc to ở văn phòng, hãy để máy đọc — nghe email của mình bằng giọng người khác giúp bạn hình dung người đọc sẽ cảm nhận thế nào.',
        'questions': [
            ('Why does reading aloud help?', ['It is faster.', 'Your ears notice problems your eyes skip.', 'It improves your accent.', 'It makes emails shorter.'], 1, 'Đoạn 1.'),
            ('What does it mean if you run out of breath?', ['You need water.', 'The sentence should be split.', 'The email is good.', 'You read too slowly.'], 1, 'Đoạn 2.'),
            ('What can you do if you are shy about reading aloud?', ['Never edit', 'Let your computer read it', 'Ask your manager', 'Write in Vietnamese'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Dán lại 3 văn bản bạn đã viết trong tuần (commit/PR, bug report, email hoặc Slack). Dùng checklist 6 bước để sửa. Ghi danh sách lỗi theo dạng: Lỗi → Sửa → Quy tắc.',
        'tips': ['Bấm "Nghe bài của tôi" để nghe máy đọc — chỗ nào nghe lạ thì xem lại.', 'Cập nhật danh sách lỗi cá nhân của bạn (từ tuần 1).'],
        'model': "1. \"I have attached file\" → \"I have attached the file\" → singular countable nouns need an article.\n2. \"Please check and feedback\" → \"Please check it and let me know your feedback\" → feedback is a noun.\n3. \"more faster then\" → \"much faster than\" → no 'more' with -er; 'than' for comparisons.\n4. \"We discussed about the issue\" → \"We discussed the issue\" → discuss takes no preposition.\n5. \"The bug effects all users\" → \"The bug affects all users\" → affect = verb.\n6. \"Its ready for review\" → \"It's ready for review\" → it's = it is.",
        'min_words': 60,
    },
    'quiz': [
        ('The new law will ___ small businesses.', ['affect', 'effect'], 0, 'affect = động từ.'),
        ('The ___ of the change was positive.', ['affect', 'effect'], 1, 'effect = danh từ.'),
        ("___ a great tool, but ___ docs are poor.", ["It's / its", "Its / it's", "Its / its", "It's / it's"], 0, "It's = it is; its = của nó."),
        ('This is faster ___ the old version.', ['then', 'than'], 1, 'than dùng để so sánh.'),
        ('We had ___ bugs this sprint.', ['less', 'fewer'], 1, 'bugs đếm được → fewer.'),
        ('I spent ___ time on meetings.', ['less', 'fewer'], 0, 'time không đếm được → less.'),
        ('Thanks for your ___.', ['advice', 'advise'], 0, 'advice = danh từ.'),
        ('Câu nào đúng?', ['Please check and feedback.', 'Please check it and let me know your feedback.', 'Please feedback me.', 'Please give feedback me.'], 1, 'feedback là danh từ.'),
        ('Câu nào đúng?', ['We discussed about the issue.', 'We discussed the issue.', 'We discussed on the issue.', 'We discussed for the issue.'], 1, 'discuss + tân ngữ trực tiếp.'),
        ('Câu nào đúng?', ['The informations are attached.', 'The information is attached.', 'The informations is attached.', 'An information is attached.'], 1, 'information không đếm được.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 7',
    'title_en': 'Week 7 Review: The Weekly Status Update',
    'goal': 'Viết một bản status update khoảng 150 từ về công việc trong tuần: thành tựu, việc đang làm, rủi ro và bước tiếp theo — áp dụng mọi kỹ năng viết của tuần.',
    'tasks': [
        'Học 14 từ dùng trong báo cáo tiến độ.',
        'Học khung status update 4 phần.',
        'Nghe quản lý giải thích họ muốn đọc gì trong status update.',
        'Viết status update ~150 từ cho tuần làm việc thật của bạn.',
        'Tự sửa bằng checklist 6 bước, rồi nghe máy đọc lại.',
    ],
    'product': 'Bản status update khoảng 150 từ',
    'warmup': [
        ("Here's my status update for this week.", 'Đây là cập nhật tình hình tuần này của tôi.'),
        ('Highlights: we shipped the new checkout.', 'Điểm nổi bật: chúng tôi đã phát hành trang thanh toán mới.'),
        ('The SMS integration is still ongoing.', 'Phần tích hợp SMS vẫn đang tiến hành.'),
        ('The mobile release is at risk.', 'Bản phát hành mobile đang gặp rủi ro.'),
        ('Next steps: finish testing and prepare the demo.', 'Bước tiếp theo: hoàn thành kiểm thử và chuẩn bị demo.'),
        ('Two tickets are still outstanding.', 'Còn hai ticket chưa xong.'),
    ],
    'vocab': [
        ('status update', '/ˈsteɪtəs ʌpˈdeɪt/', 'n', 'bản cập nhật tình hình', 'I send a status update every Friday.', 'Tôi gửi cập nhật tình hình mỗi thứ Sáu.'),
        ('highlights', '/ˈhaɪlaɪts/', 'n (pl)', 'điểm nổi bật', 'Highlights of the week: two features shipped.', 'Điểm nổi bật trong tuần: phát hành hai tính năng.'),
        ('lowlights', '/ˈləʊlaɪts/', 'n (pl)', 'điểm chưa tốt', 'Lowlights: the pipeline was red for a day.', 'Điểm chưa tốt: pipeline báo đỏ suốt một ngày.'),
        ('accomplishment', '/əˈkʌmplɪʃmənt/', 'n', 'thành tựu, việc đã đạt', 'Finishing the migration was our biggest accomplishment.', 'Hoàn thành migration là thành tựu lớn nhất của chúng tôi.'),
        ('ongoing', '/ˈɒnɡəʊɪŋ/', 'adj', 'đang tiếp diễn', 'The performance work is ongoing.', 'Việc cải thiện hiệu năng vẫn đang tiếp diễn.'),
        ('next steps', '/nekst steps/', 'n (pl)', 'các bước tiếp theo', 'Next steps: QA testing and the client demo.', 'Bước tiếp theo: QA kiểm thử và demo cho khách.'),
        ('upcoming', '/ˈʌpkʌmɪŋ/', 'adj', 'sắp tới', 'Please prepare for the upcoming release.', 'Hãy chuẩn bị cho bản phát hành sắp tới.'),
        ('outstanding', '/aʊtˈstændɪŋ/', 'adj', 'còn tồn đọng; xuất sắc', 'There are three outstanding bugs.', 'Còn ba lỗi tồn đọng.'),
        ('at risk', '/æt rɪsk/', 'phrase', 'có nguy cơ (trễ/thất bại)', 'The Friday deadline is at risk.', 'Hạn chót thứ Sáu có nguy cơ trễ.'),
        ('key metric', '/kiː ˈmetrɪk/', 'n', 'chỉ số chính', 'Our key metric is the number of daily active users.', 'Chỉ số chính của chúng tôi là số người dùng hoạt động hằng ngày.'),
        ('overview', '/ˈəʊvəvjuː/', 'n', 'tổng quan', 'Here is a short overview of the project.', 'Đây là tổng quan ngắn về dự án.'),
        ('summary', '/ˈsʌməri/', 'n', 'bản tóm tắt', 'Start with a one-line summary.', 'Bắt đầu bằng một dòng tóm tắt.'),
        ('completed', '/kəmˈpliːtɪd/', 'adj', 'đã hoàn thành', 'Completed: login, sign-up and password reset.', 'Đã hoàn thành: đăng nhập, đăng ký và đặt lại mật khẩu.'),
        ('delivered', '/dɪˈlɪvəd/', 'adj', 'đã bàn giao', 'All features were delivered on time.', 'Mọi tính năng đều được bàn giao đúng hạn.'),
    ],
    'lesson': """
<h3>1. Khung status update 4 phần</h3>
<pre>Subject: Weekly update – Booking app – Week 48

TL;DR: Online booking is live. SMS reminders are at risk for Friday.

✅ Completed
- Online booking released to all users (Tuesday)
- Fixed 6 bugs reported by QA

🔨 Ongoing
- SMS reminders: about 70% done

⚠️ Risks / blockers
- The SMS provider hasn't approved our account yet.
  If it's not approved by Wednesday, reminders will slip to next week.

➡️ Next steps
- Finish SMS reminders and test with real phones
- Prepare the demo for the client on Thursday</pre>

<h3>2. Nguyên tắc</h3>
<ul>
<li><b>TL;DR đầu tiên</b>: người đọc bận chỉ đọc 1 dòng đó.</li>
<li><b>Kết quả, không phải hoạt động</b>: "Released online booking" thay vì "Worked on booking".</li>
<li><b>Rủi ro phải có điều kiện và hệ quả</b>: <i>If X doesn't happen by Y, then Z.</i></li>
<li><b>Con số</b>: % hoàn thành, số lỗi, số người dùng.</li>
<li><b>Ngắn</b>: 100–200 từ. Gạch đầu dòng.</li>
</ul>

<h3>3. Tổng kết tuần 7</h3>
<table class="table">
<tr><th>Loại văn bản</th><th>Điều quan trọng nhất</th></tr>
<tr><td>Commit</td><td>Thể mệnh lệnh, ≤ 50 ký tự, cụ thể</td></tr>
<tr><td>PR</td><td>Summary – Changes – How to test</td></tr>
<tr><td>Bug report</td><td>Steps – Expected – Actual – Environment</td></tr>
<tr><td>Email</td><td>Yêu cầu ở đầu, lịch sự, có hạn</td></tr>
<tr><td>Slack</td><td>Một tin đầy đủ, có bối cảnh, ghi múi giờ</td></tr>
<tr><td>Status update</td><td>TL;DR, kết quả, rủi ro, bước tiếp</td></tr>
</table>
""",
    'listening': {
        'title': 'What managers want to read',
        'intro': 'Một engineering manager chia sẻ điều họ muốn thấy trong status update hằng tuần.',
        'speakers': {'A': ('Host', 'jenny'), 'B': ('Karen (manager)', 'sonia')},
        'lines': [
            ('A', "Karen, you manage three teams. How many status updates do you read every week?", 'Karen, chị quản lý ba team. Mỗi tuần chị đọc bao nhiêu bản cập nhật tình hình?'),
            ('B', "About twenty. So honestly, I spend maybe one minute on each one.", 'Khoảng hai mươi. Nên thật lòng, chị dành có lẽ một phút cho mỗi bản.'),
            ('A', "One minute! So what makes a good update?", 'Một phút! Vậy điều gì làm nên một bản cập nhật tốt?'),
            ('B', "First, a one-line summary at the top. If I only read that line, do I know if things are okay?", 'Đầu tiên, một dòng tóm tắt ở trên cùng. Nếu chị chỉ đọc dòng đó, chị có biết mọi thứ ổn không?'),
            ('B', "Second, results, not activity. 'I worked on the API' tells me nothing. 'The payment API is finished and tested' tells me a lot.", 'Thứ hai, kết quả, không phải hoạt động. "Tôi làm API" chẳng nói gì. "API thanh toán đã xong và được kiểm thử" nói rất nhiều.'),
            ('A', "What about problems? Some people are afraid to mention them.", 'Còn vấn đề thì sao? Một số người ngại nhắc tới.'),
            ('B', "That's the most important part! I can only help if I know about a risk early. The best updates say: here's the risk, here's what happens if it isn't solved, and here's what I need.", 'Đó là phần quan trọng nhất! Chị chỉ giúp được nếu biết rủi ro sớm. Bản tốt nhất nói: đây là rủi ro, đây là hệ quả nếu không giải quyết, và đây là điều tôi cần.'),
            ('A', "And length?", 'Còn độ dài?'),
            ('B', "Short. Bullet points. Around a hundred and fifty words is perfect. If I want details, I'll ask.", 'Ngắn. Gạch đầu dòng. Khoảng một trăm năm mươi từ là hoàn hảo. Nếu muốn chi tiết, chị sẽ hỏi.'),
            ('A', "Any advice for non-native speakers?", 'Có lời khuyên nào cho người không phải bản xứ?'),
            ('B', "Don't worry about perfect grammar. Clear and simple beats fancy every time. Some of my best updates come from engineers who write very simple English.", 'Đừng lo về ngữ pháp hoàn hảo. Rõ ràng và đơn giản luôn thắng hoa mỹ. Một số bản cập nhật hay nhất chị nhận được đến từ các kỹ sư viết tiếng Anh rất đơn giản.'),
        ],
        'questions': [
            ('How long does Karen spend on each update?', ['About one minute', 'About ten minutes', 'About half an hour', 'She doesn\'t read them'], 0, '"maybe one minute on each one".'),
            ('What should be at the top of an update?', ['A greeting', 'A one-line summary', 'A list of meetings', 'The author\'s name'], 1, '"a one-line summary at the top".'),
            ('Which is a "result", according to Karen?', ['I worked on the API.', 'The payment API is finished and tested.', 'I had meetings.', 'I was busy.'], 1, 'Kết quả cụ thể.'),
            ('What does Karen say is the most important part?', ['The length', 'Mentioning risks early', 'Perfect grammar', 'Emojis'], 1, '"That\'s the most important part!" — nói về vấn đề/rủi ro.'),
            ('What is Karen\'s advice for non-native speakers?', ['Use fancy words', 'Clear and simple beats fancy', 'Write long paragraphs', 'Avoid writing updates'], 1, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to bản status update của bạn như đang báo cáo trong cuộc họp cuối tuần (1 phút).'],
        'prompts': [
            ('Give a one-minute spoken status update for your week.', 'Summary → completed → ongoing → risks → next steps.'),
            ('Describe one risk: what it is, what happens if it isn\'t solved, and what you need.', 'If… by…, then…'),
        ],
        'model': (
            "Here's my update for this week. In short, online booking is live, but SMS reminders are at risk. "
            "We released online booking to all users on Tuesday, and we fixed six bugs from QA. "
            "The SMS reminders are about seventy percent done. "
            "The main risk is that the SMS provider hasn't approved our account yet. If it isn't approved by Wednesday, the reminders will slip to next week. It would help if you could contact their account manager. "
            "Next week, I'll finish the reminders and prepare the client demo for Thursday.",
            'Đây là cập nhật tuần này của tôi. Tóm lại, đặt lịch online đã chạy, nhưng nhắc nhở SMS có nguy cơ trễ. '
            'Chúng tôi phát hành đặt lịch online cho mọi người dùng hôm thứ Ba và sửa sáu lỗi từ QA. '
            'Nhắc nhở SMS xong khoảng bảy mươi phần trăm. '
            'Rủi ro chính là bên SMS chưa duyệt tài khoản. Nếu chưa duyệt trước thứ Tư, nhắc nhở sẽ lùi sang tuần sau. Sẽ có ích nếu anh/chị liên hệ quản lý tài khoản bên đó. '
            'Tuần tới tôi sẽ hoàn thành nhắc nhở và chuẩn bị demo cho khách hàng vào thứ Năm.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'A real status update',
        'text': [
            'TL;DR: The new search is live for 20% of users. Search speed improved by 60%. The full release is on track for next Wednesday.',
            'Completed: We released the new search behind a feature flag on Monday. Average search time dropped from 1.2 seconds to 0.5 seconds. We fixed three bugs found during the first day, including a problem with Vietnamese accents.',
            'Ongoing and risks: We are monitoring error rates before turning the flag on for everyone. One risk is the database load during peak hours. If it goes above 80%, we will need to add a read replica, which would delay the release by about two days. Next steps: increase traffic to 50% on Friday and collect feedback from the support team.',
        ],
        'vi': 'Một bản status update thật: TL;DR nêu tìm kiếm mới đã chạy cho 20% người dùng, tốc độ cải thiện 60%, bản phát hành đầy đủ đúng tiến độ thứ Tư tới. Phần đã hoàn thành có số liệu cụ thể (1,2 giây → 0,5 giây; sửa ba lỗi). Phần rủi ro nêu điều kiện (tải cơ sở dữ liệu trên 80%) và hệ quả (thêm read replica, chậm khoảng hai ngày). Bước tiếp: tăng lên 50% vào thứ Sáu.',
        'questions': [
            ('How many users have the new search now?', ['20%', '50%', '60%', 'All users'], 0, 'TL;DR.'),
            ('How much faster is the search?', ['From 1.2 s to 0.5 s', 'From 2 s to 1 s', '20% faster', 'Twice as slow'], 0, 'Đoạn 2.'),
            ('What would delay the release by about two days?', ['Vietnamese accents', 'Needing a read replica if database load goes above 80%', 'Support feedback', 'The feature flag'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết bản status update khoảng 150 từ cho tuần làm việc thật của bạn theo khung 4 phần (TL;DR, Completed, Ongoing & risks, Next steps). Sau đó tự sửa bằng checklist và bấm "Nghe bài của tôi".',
        'tips': ['TL;DR một dòng. Kết quả có con số.', 'Rủi ro: If… by…, … will…'],
        'model': "Subject: Weekly update – HR system – Week 49\n\nTL;DR: Leave requests v2 is live. The payslip export is at risk for Friday.\n\nCompleted\n- Released leave requests v2 to all 2,000 employees on Tuesday\n- Approval time dropped from 2 days to 4 hours on average\n- Fixed 5 bugs from QA, including the time zone issue for the Tokyo office\n\nOngoing\n- Payslip PDF export: about 60% done\n\nRisks\n- Vietnamese fonts don't display correctly in the PDF library. If I can't fix this by Wednesday, the export will slip to next Tuesday. Pairing with Mai (who solved this before) would help.\n\nNext steps\n- Fix fonts and finish the export\n- Prepare a short demo for HR on Thursday",
        'min_words': 120,
    },
    'quiz': [
        ('The one-line summary at the top of an update is the ___.', ['TL;DR', 'FYI', 'EOD', 'P.S.'], 0, 'TL;DR.'),
        ('Work that is still in progress is ___.', ['ongoing', 'outgoing', 'upgoing', 'undergoing'], 0, 'ongoing.'),
        ('"The deadline is ___ risk."', ['at', 'in', 'on', 'under'], 0, 'at risk.'),
        ('Bugs that are not fixed yet are ___.', ['outstanding', 'outside', 'overdue up', 'standing'], 0, 'outstanding = còn tồn đọng.'),
        ('Better status update line:', ['I worked on the API.', 'The payment API is finished and tested.', 'I was busy.', 'Many things.'], 1, 'Kết quả, không phải hoạt động.'),
        ('A good risk statement includes:', ['Only the problem', 'The risk, what happens if not solved, and what you need', 'Who is to blame', 'An apology'], 1, 'Rủi ro + hệ quả + điều cần.'),
        ('Ideal length of a weekly update:', ['10 words', 'About 150 words', '1,000 words', '5 pages'], 1, '~150 từ.'),
        ('The best moments of the week are the ___.', ['highlights', 'lowlights', 'headlines', 'deadlines'], 0, 'highlights.'),
        ('"Please prepare for the ___ release." (sắp tới)', ['upcoming', 'oncoming', 'outcoming', 'incoming up'], 0, 'upcoming.'),
        ('Our most important number to track is our ___.', ['key metric', 'key word', 'main count', 'top number'], 0, 'key metric.'),
    ],
}

WEEK = {
    'title': 'Viết chuyên nghiệp',
    'title_en': 'Professional Writing',
    'goal': 'Viết commit message, PR description, email và tin nhắn công việc rõ ràng, lịch sự.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
