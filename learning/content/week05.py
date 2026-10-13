"""Tuần 5 — Từ vựng công nghệ và shadowing."""

DAY1 = {
    'title': 'Từ vựng backend',
    'title_en': 'Backend Vocabulary',
    'goal': 'Nắm và phát âm đúng 14 thuật ngữ backend (API, endpoint, latency, idempotent, migration, rollback…); dùng được chúng trong câu khi thảo luận thiết kế.',
    'tasks': [
        'Học 14 thuật ngữ backend, chú ý cách phát âm.',
        'Đọc phần giải thích từng khái niệm bằng tiếng Anh đơn giản.',
        'Nghe buổi thảo luận thiết kế một endpoint mới.',
        'Luyện thẻ từ (Thẻ từ → Nghe & gõ).',
        'Viết mỗi thuật ngữ một câu ví dụ về dự án của bạn.',
    ],
    'product': '14 thẻ từ đã luyện; Câu ví dụ cho từng thuật ngữ',
    'warmup': [
        ('The endpoint returns a list of orders.', 'Endpoint trả về danh sách đơn hàng.'),
        ('Latency went up after the last release.', 'Độ trễ tăng lên sau bản phát hành gần nhất.'),
        ('This request must be idempotent.', 'Request này phải có tính idempotent.'),
        ('We need a migration to add the new column.', 'Chúng ta cần một migration để thêm cột mới.'),
        ("If something goes wrong, we'll roll back.", 'Nếu có sự cố, chúng ta sẽ quay lui phiên bản.'),
        ('The response is cached for sixty seconds.', 'Phản hồi được cache trong sáu mươi giây.'),
    ],
    'vocab': [
        ('API', '/ˌeɪ piː ˈaɪ/', 'n', 'giao diện lập trình ứng dụng', 'Our mobile app talks to the server through a REST API.', 'Ứng dụng di động giao tiếp với server qua REST API.'),
        ('endpoint', '/ˈendpɔɪnt/', 'n', 'điểm cuối API (một URL cụ thể)', 'The orders endpoint is very slow.', 'Endpoint đơn hàng rất chậm.'),
        ('request', '/rɪˈkwest/', 'n', 'yêu cầu gửi đến server', 'Each request must include an API key.', 'Mỗi request phải kèm API key.'),
        ('latency', '/ˈleɪtənsi/', 'n', 'độ trễ', 'We reduced latency from 800 to 120 milliseconds.', 'Chúng tôi giảm độ trễ từ 800 xuống 120 mili giây.'),
        ('throughput', '/ˈθruːpʊt/', 'n', 'thông lượng (lượng xử lý trên đơn vị thời gian)', 'The new server doubled our throughput.', 'Server mới tăng gấp đôi thông lượng.'),
        ('idempotent', '/ˌaɪdemˈpəʊtənt/', 'adj', 'gọi nhiều lần cho kết quả như một lần', 'Payment requests should be idempotent.', 'Request thanh toán nên có tính idempotent.'),
        ('migration', '/maɪˈɡreɪʃn/', 'n', 'bản chuyển đổi cấu trúc cơ sở dữ liệu', 'Run the migration before you start the server.', 'Chạy migration trước khi khởi động server.'),
        ('rollback', '/ˈrəʊlbæk/', 'n', 'sự quay lui về phiên bản trước', 'The rollback took less than two minutes.', 'Việc quay lui mất chưa đến hai phút.'),
        ('schema', '/ˈskiːmə/', 'n', 'lược đồ (cấu trúc dữ liệu)', 'We changed the database schema twice this month.', 'Tháng này chúng tôi đổi lược đồ cơ sở dữ liệu hai lần.'),
        ('query', '/ˈkwɪəri/', 'n / verb', 'truy vấn', 'This query scans the whole table.', 'Truy vấn này quét toàn bộ bảng.'),
        ('cache', '/kæʃ/', 'n / verb', 'bộ nhớ đệm; lưu đệm', 'We cache the product list for five minutes.', 'Chúng tôi lưu đệm danh sách sản phẩm năm phút.'),
        ('payload', '/ˈpeɪləʊd/', 'n', 'dữ liệu gửi kèm (thân request/response)', 'The payload is too large; please paginate.', 'Dữ liệu gửi kèm quá lớn; hãy phân trang.'),
        ('rate limit', '/reɪt ˈlɪmɪt/', 'n', 'giới hạn số request', 'The rate limit is 100 requests per minute.', 'Giới hạn là 100 request mỗi phút.'),
        ('authentication', '/ɔːˌθentɪˈkeɪʃn/', 'n', 'xác thực (bạn là ai)', 'Authentication is handled by a separate service.', 'Việc xác thực do một dịch vụ riêng đảm nhiệm.'),
    ],
    'lesson': """
<h3>1. Giải thích bằng tiếng Anh đơn giản</h3>
<p>Một kỹ sư giỏi giải thích được thuật ngữ bằng câu ngắn. Đọc to từng định nghĩa:</p>
<table class="table">
<tr><th>Thuật ngữ</th><th>Simple English</th></tr>
<tr><td><b>endpoint</b></td><td><span class="say">An endpoint is a specific URL where the API accepts requests.</span></td></tr>
<tr><td><b>latency</b></td><td><span class="say">Latency is how long one request takes.</span></td></tr>
<tr><td><b>throughput</b></td><td><span class="say">Throughput is how many requests the system can handle per second.</span></td></tr>
<tr><td><b>idempotent</b></td><td><span class="say">An idempotent request gives the same result whether you send it once or ten times.</span></td></tr>
<tr><td><b>migration</b></td><td><span class="say">A migration is a script that changes the structure of the database.</span></td></tr>
<tr><td><b>rollback</b></td><td><span class="say">A rollback means going back to the previous working version.</span></td></tr>
<tr><td><b>rate limit</b></td><td><span class="say">A rate limit stops one client from sending too many requests.</span></td></tr>
</table>
<div class="note"><b>Latency vs throughput:</b> latency giống thời gian một chiếc xe đi hết con đường; throughput giống số xe đi qua mỗi phút. Đường rộng hơn tăng throughput nhưng không làm từng xe nhanh hơn.</div>

<h3>2. Phát âm dễ sai</h3>
<table class="table">
<tr><th>Từ</th><th>Đúng</th><th>Hay đọc sai</th></tr>
<tr><td><span class="say">cache</span></td><td>/kæʃ/ — giống "cash"</td><td>"ca-sê", "cát-chê"</td></tr>
<tr><td><span class="say">query</span></td><td>/ˈkwɪəri/</td><td>"quơ-ri"</td></tr>
<tr><td><span class="say">schema</span></td><td>/ˈskiːmə/</td><td>"sê-ma"</td></tr>
<tr><td><span class="say">API</span></td><td>/ˌeɪ piː ˈaɪ/ — nhấn chữ cuối</td><td>"a-pi"</td></tr>
<tr><td><span class="say">SQL</span></td><td>/ˌes kjuː ˈel/ hoặc /ˈsiːkwəl/</td><td>—</td></tr>
<tr><td><span class="say">data</span></td><td>/ˈdeɪtə/ hoặc /ˈdɑːtə/</td><td>—</td></tr>
</table>

<h3>3. Động từ đi với thuật ngữ</h3>
<div class="ex"><span class="en">call an API · hit an endpoint · send a request · return a response</span></div>
<div class="ex"><span class="en">run a migration · roll back a release · write a query · clear the cache · hit the rate limit</span></div>
<div class="ex"><span class="en">We hit the rate limit, so the API started returning 429 errors.</span><span class="vi">Chúng tôi chạm giới hạn request nên API bắt đầu trả lỗi 429.</span></div>
""",
    'phrases': [
        ('What does this endpoint return?', 'Endpoint này trả về gì?'),
        ("What's the expected latency?", 'Độ trễ mong đợi là bao nhiêu?'),
        ('Do we need a migration for this?', 'Việc này có cần migration không?'),
        ("What's our rollback plan?", 'Kế hoạch quay lui của chúng ta là gì?'),
    ],
    'listening': {
        'title': 'Designing a new endpoint',
        'intro': 'Hai kỹ sư backend thiết kế endpoint tạo đơn hàng mới.',
        'speakers': {'A': ('Priya', 'ava'), 'B': ('Nam', 'brian')},
        'lines': [
            ('A', "Okay Nam, let's design the new endpoint for creating orders. What do you have in mind?", 'Được rồi Nam, cùng thiết kế endpoint tạo đơn hàng mới nhé. Cậu có ý tưởng gì?'),
            ('B', "I'm thinking of a POST request to slash orders. The payload includes the customer ID, the items and the delivery address.", 'Mình nghĩ là một POST request tới /orders. Dữ liệu gửi kèm gồm ID khách hàng, các món hàng và địa chỉ giao.'),
            ('A', "Sounds good. One important thing: mobile networks are unreliable. If the app sends the same request twice, we can't create two orders.", 'Nghe ổn. Một điều quan trọng: mạng di động không ổn định. Nếu app gửi cùng một request hai lần, mình không được tạo hai đơn.'),
            ('B', "Right, so it needs to be idempotent. The app can send a unique key with each order, and we ignore duplicates.", 'Đúng, vậy nó cần idempotent. App có thể gửi một khóa duy nhất kèm mỗi đơn, và mình bỏ qua bản trùng.'),
            ('A', 'Perfect. Do we need to change the database schema?', 'Hoàn hảo. Có cần đổi lược đồ cơ sở dữ liệu không?'),
            ('B', "Yes, we need a migration to add a column for that key. It's a small one, it should run in seconds.", 'Có, cần một migration để thêm cột cho khóa đó. Nhỏ thôi, chạy vài giây là xong.'),
            ('A', "What about latency? The product team wants the response in under three hundred milliseconds.", 'Còn độ trễ? Team sản phẩm muốn phản hồi dưới ba trăm mili giây.'),
            ('B', "That's fine for the order itself. But sending the confirmation email is slow, so we'll do that in the background.", 'Phần tạo đơn thì ổn. Nhưng gửi email xác nhận chậm, nên mình sẽ làm việc đó ở chế độ nền.'),
            ('A', "Good idea. And let's add a rate limit, maybe ten orders per minute per user, to stop abuse.", 'Ý hay. Và thêm giới hạn request, chắc mười đơn mỗi phút mỗi người, để chặn lạm dụng.'),
            ('B', "Agreed. If anything goes wrong after the release, we can roll back, because the migration only adds a column.", 'Đồng ý. Nếu có gì sai sau khi phát hành, mình có thể quay lui, vì migration chỉ thêm một cột.'),
        ],
        'questions': [
            ('What type of request will create an order?', ['GET', 'POST', 'DELETE', 'PATCH'], 1, '"a POST request to slash orders".'),
            ('Why must the endpoint be idempotent?', ['To make it faster', 'Because the app might send the same request twice', 'Because of the rate limit', 'To save database space'], 1, '"If the app sends the same request twice, we can\'t create two orders."'),
            ('What will the migration do?', ['Delete old orders', 'Add a column for the unique key', 'Change the email service', 'Create a new database'], 1, '"a migration to add a column for that key".'),
            ('How will they keep latency low?', ['By adding more servers', 'By sending the email in the background', 'By removing the payload', 'By caching orders'], 1, '"we\'ll do that in the background".'),
            ('Why is a rollback easy?', ['The migration only adds a column.', 'They have no users.', 'The rate limit protects them.', 'They use a cache.'], 0, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Giải thích từng khái niệm bằng 1–2 câu đơn giản, như đang nói với PM.', 'Phát âm đúng cache /kæʃ/, query, schema.'],
        'prompts': [
            ('Explain the difference between latency and throughput.', 'Dùng ví dụ con đường và xe.'),
            ('What does "idempotent" mean, and why does it matter for payments?', 'Ví dụ bấm "Thanh toán" hai lần.'),
            ('Describe one API you have built or used: endpoints, payload, authentication.', 'Thực tế của bạn.'),
        ],
        'model': (
            "Latency and throughput are related, but they're not the same. Latency is how long one request takes, for example two hundred milliseconds. "
            "Throughput is how many requests the system can handle per second. "
            "Imagine a road. Latency is how long it takes one car to drive from one end to the other. Throughput is how many cars pass every minute. "
            "If you add more lanes, more cars can pass, so throughput goes up, but each car doesn't get faster. "
            "To reduce latency, you usually need to make each step quicker, for example by adding a cache or optimising a slow query.",
            'Độ trễ và thông lượng liên quan nhưng không giống nhau. Độ trễ là thời gian một request mất, ví dụ hai trăm mili giây. '
            'Thông lượng là số request hệ thống xử lý mỗi giây. '
            'Hãy tưởng tượng một con đường. Độ trễ là thời gian một chiếc xe đi hết đường. Thông lượng là số xe đi qua mỗi phút. '
            'Nếu thêm làn, nhiều xe đi qua hơn nên thông lượng tăng, nhưng từng xe không nhanh hơn. '
            'Để giảm độ trễ, thường phải làm từng bước nhanh hơn, ví dụ thêm cache hoặc tối ưu truy vấn chậm.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'API docs: Rate limits',
        'text': [
            'To keep the service fast and fair for everyone, all API requests are subject to rate limits. By default, each API key can make up to 100 requests per minute.',
            'Every response includes three headers: the limit, the number of requests remaining and the time when the limit resets. If you exceed the limit, the API returns the status code 429, "Too Many Requests". Your application should wait until the reset time and then retry.',
            'For write requests, such as creating payments, we strongly recommend sending an idempotency key. If the same key is sent twice within 24 hours, the second request returns the original response instead of creating a duplicate payment.',
        ],
        'vi': 'Để dịch vụ nhanh và công bằng, mọi request API đều bị giới hạn: mặc định mỗi API key tối đa 100 request/phút. Mỗi phản hồi có ba header: giới hạn, số request còn lại và thời điểm đặt lại. Vượt giới hạn sẽ nhận mã 429 "Too Many Requests"; ứng dụng nên chờ đến thời điểm đặt lại rồi thử lại. Với request ghi (như tạo thanh toán), nên gửi khóa idempotency: nếu cùng khóa gửi hai lần trong 24 giờ, request thứ hai trả về phản hồi ban đầu thay vì tạo thanh toán trùng.',
        'questions': [
            ('What is the default rate limit?', ['10 requests per minute', '100 requests per minute', '100 requests per hour', '429 requests per minute'], 1, 'Đoạn 1.'),
            ('What does status code 429 mean?', ['Not Found', 'Too Many Requests', 'Server Error', 'Unauthorized'], 1, 'Đoạn 2.'),
            ('What happens if the same idempotency key is sent twice within 24 hours?', ['A second payment is created.', 'The original response is returned.', 'The key is blocked.', 'The rate limit resets.'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 7 câu, mỗi câu dùng một thuật ngữ hôm nay, mô tả hệ thống bạn đang làm (hoặc một hệ thống bạn biết). Sau đó luyện thẻ từ ở trang Luyện từ.',
        'tips': ['Dùng đúng động từ đi kèm: run a migration, hit the rate limit, clear the cache…'],
        'model': "Our booking API has about thirty endpoints.\nThe slowest endpoint is the search, with an average latency of 600 milliseconds.\nLast week we ran a migration to add a 'status' column to the bookings table.\nWe cache the list of hotels for ten minutes because it rarely changes.\nThe cancel request is idempotent, so users can safely tap the button twice.\nIf a release breaks something, our rollback takes about three minutes.\nPartners who hit the rate limit receive a 429 error.",
        'min_words': 70,
    },
    'quiz': [
        ('How long one request takes is called ___.', ['throughput', 'latency', 'payload', 'schema'], 1, 'latency = độ trễ.'),
        ('How many requests a system can handle per second is ___.', ['latency', 'throughput', 'rollback', 'cache'], 1, 'throughput = thông lượng.'),
        ('A request that has the same effect whether you send it once or many times is ___.', ['authenticated', 'idempotent', 'cached', 'limited'], 1, 'idempotent.'),
        ('A script that changes the database structure is a ___.', ['migration', 'query', 'payload', 'endpoint'], 0, 'migration.'),
        ('Something broke after the release. Let\'s ___.', ['roll back', 'rate limit', 'cache', 'query'], 0, 'roll back = quay lui (động từ); rollback là danh từ.'),
        ('"cache" phát âm giống từ nào?', ['catch', 'cash', 'case', 'cast'], 1, 'cache /kæʃ/ = cash.', 'cache'),
        ('The data sent in the body of a request is the ___.', ['payload', 'header', 'schema', 'endpoint'], 0, 'payload.'),
        ('Status 429 means you hit the ___.', ['rate limit', 'cache', 'migration', 'schema'], 0, '429 Too Many Requests.'),
        ('Checking who the user is = ___.', ['authentication', 'migration', 'throughput', 'rollback'], 0, 'authentication = xác thực.'),
        ('Collocation đúng:', ['do a migration run', 'run a migration', 'make a migration go', 'play a migration'], 1, 'run a migration.'),
        ('"Our search ___ is slow." (truy vấn)', ['query', 'payload', 'rollback', 'schema'], 0, 'query.'),
        ('A specific URL of an API, like /orders, is an ___.', ['endpoint', 'environment', 'engine', 'entry'], 0, 'endpoint.'),
    ],
}

DAY2 = {
    'title': 'Từ vựng frontend và DevOps',
    'title_en': 'Frontend & DevOps Vocabulary',
    'goal': 'Nắm 14 thuật ngữ frontend và DevOps (component, state, render, pipeline, container, uptime, hotfix…) và dùng chúng để kể về một sự cố triển khai.',
    'tasks': [
        'Học 14 thuật ngữ frontend & DevOps.',
        'Nghe hội thoại về một sự cố trên production và hotfix.',
        'Luyện thẻ từ ở trang Luyện từ.',
        'Kể lại (nói) quy trình từ commit đến production ở công ty bạn.',
        'Viết câu ví dụ cho từng từ.',
    ],
    'product': '14 thẻ từ đã luyện; Câu ví dụ cho từng từ',
    'warmup': [
        ('This component renders the user profile.', 'Component này hiển thị hồ sơ người dùng.'),
        ('The page re-renders every time the state changes.', 'Trang vẽ lại mỗi khi state thay đổi.'),
        ('The pipeline failed at the test stage.', 'Pipeline bị lỗi ở bước test.'),
        ('Everything runs in containers.', 'Mọi thứ chạy trong container.'),
        ('Our uptime last month was 99.9 percent.', 'Thời gian hoạt động tháng trước là 99,9%.'),
        ("We're pushing a hotfix to production now.", 'Chúng tôi đang đẩy bản vá nóng lên production.'),
    ],
    'vocab': [
        ('component', '/kəmˈpəʊnənt/', 'n', 'thành phần giao diện', 'We built a reusable button component.', 'Chúng tôi làm một component nút bấm dùng lại được.'),
        ('state', '/steɪt/', 'n', 'trạng thái (dữ liệu thay đổi của giao diện)', 'Keep the form data in the component state.', 'Giữ dữ liệu form trong state của component.'),
        ('props', '/prɒps/', 'n (pl)', 'tham số truyền vào component', 'The card component receives the title as props.', 'Component thẻ nhận tiêu đề qua props.'),
        ('render', '/ˈrendə/', 'verb', 'hiển thị, vẽ ra giao diện', 'The list renders slowly when there are 5,000 items.', 'Danh sách hiển thị chậm khi có 5.000 mục.'),
        ('responsive', '/rɪˈspɒnsɪv/', 'adj', 'tương thích nhiều kích thước màn hình', 'The new design is fully responsive.', 'Thiết kế mới tương thích hoàn toàn với mọi màn hình.'),
        ('pipeline', '/ˈpaɪplaɪn/', 'n', 'chuỗi bước tự động (build, test, deploy)', 'The CI pipeline takes twelve minutes.', 'Pipeline CI mất mười hai phút.'),
        ('container', '/kənˈteɪnə/', 'n', 'container (môi trường đóng gói ứng dụng)', 'Each service runs in its own container.', 'Mỗi dịch vụ chạy trong container riêng.'),
        ('uptime', '/ˈʌptaɪm/', 'n', 'thời gian hệ thống hoạt động', 'We promise 99.9 percent uptime.', 'Chúng tôi cam kết 99,9% thời gian hoạt động.'),
        ('downtime', '/ˈdaʊntaɪm/', 'n', 'thời gian hệ thống ngừng hoạt động', 'The migration caused ten minutes of downtime.', 'Migration gây ra mười phút ngừng hoạt động.'),
        ('hotfix', '/ˈhɒtfɪks/', 'n', 'bản vá khẩn cấp', 'We released a hotfix at midnight.', 'Chúng tôi phát hành bản vá khẩn lúc nửa đêm.'),
        ('monitoring', '/ˈmɒnɪtərɪŋ/', 'n', 'giám sát (hệ thống)', 'Good monitoring tells you about problems before users do.', 'Giám sát tốt báo cho bạn biết sự cố trước người dùng.'),
        ('staging', '/ˈsteɪdʒɪŋ/', 'n', 'môi trường thử nghiệm (giống production)', 'Always test on staging first.', 'Luôn thử trên staging trước.'),
        ('production', '/prəˈdʌkʃn/', 'n', 'môi trường chạy thật (prod)', 'Never test new code directly in production.', 'Đừng bao giờ thử code mới trực tiếp trên production.'),
        ('CI/CD', '/ˌsiː aɪ ˌsiː ˈdiː/', 'n', 'tích hợp & triển khai liên tục', 'With CI/CD, every merge goes live automatically.', 'Với CI/CD, mỗi lần merge đều tự động lên production.'),
    ],
    'lesson': """
<h3>1. Frontend trong một câu</h3>
<div class="ex"><span class="en">A page is made of components. Each component receives props from its parent and keeps its own state. When the state changes, the component re-renders.</span><span class="vi">Trang được tạo từ các component. Mỗi component nhận props từ component cha và giữ state riêng. Khi state đổi, component vẽ lại.</span></div>

<h3>2. DevOps: hành trình của một dòng code</h3>
<table class="table">
<tr><th>Bước</th><th>Câu mô tả</th></tr>
<tr><td>1. Merge</td><td><span class="say">The pull request is merged into main.</span></td></tr>
<tr><td>2. Pipeline</td><td><span class="say">The CI pipeline builds the code and runs the tests.</span></td></tr>
<tr><td>3. Container</td><td><span class="say">The app is packaged into a container image.</span></td></tr>
<tr><td>4. Staging</td><td><span class="say">It's deployed to staging for a final check.</span></td></tr>
<tr><td>5. Production</td><td><span class="say">It goes live in production.</span></td></tr>
<tr><td>6. Monitoring</td><td><span class="say">Monitoring alerts us if errors go up.</span></td></tr>
</table>

<h3>3. Nói về sự cố</h3>
<table class="table">
<tr><th>Cụm từ</th><th>Nghĩa</th></tr>
<tr><td><span class="say">The site is down.</span></td><td>Trang web sập</td></tr>
<tr><td><span class="say">The build is broken.</span> / <span class="say">The pipeline is red.</span></td><td>Bản build hỏng</td></tr>
<tr><td><span class="say">We got an alert at 2 a.m.</span></td><td>Nhận cảnh báo lúc 2 giờ sáng</td></tr>
<tr><td><span class="say">We pushed a hotfix.</span></td><td>Đẩy bản vá khẩn</td></tr>
<tr><td><span class="say">It's back up now.</span></td><td>Hệ thống chạy lại rồi</td></tr>
</table>
<div class="note"><b>"Up" và "down":</b> <i>The server is up</i> = đang chạy; <i>is down</i> = sập; <i>back up</i> = chạy lại; <i>uptime/downtime</i> = thời gian chạy/sập. "99.9% uptime" ≈ 43 phút downtime mỗi tháng.</div>
""",
    'phrases': [
        ('The site is down.', 'Trang web sập rồi.'),
        ("It's back up now.", 'Hệ thống chạy lại rồi.'),
        ('The pipeline is red again.', 'Pipeline lại báo đỏ.'),
        ('Did you test it on staging?', 'Bạn đã thử trên staging chưa?'),
    ],
    'listening': {
        'title': 'Incident at midnight',
        'intro': 'Sáng hôm sau, kỹ sư DevOps kể cho lập trình viên frontend về sự cố tối qua.',
        'speakers': {'A': ('Chloe', 'jenny'), 'B': ('Tri', 'andrew')},
        'lines': [
            ('B', "Morning Chloe. You look tired. Long night?", 'Chào Chloe. Trông chị mệt thế. Tối qua thức khuya à?'),
            ('A', "Very long. Monitoring sent me an alert at midnight. The checkout page was down for about fifteen minutes.", 'Rất khuya. Hệ thống giám sát gửi cảnh báo cho chị lúc nửa đêm. Trang thanh toán sập khoảng mười lăm phút.'),
            ('B', "Oh no. Was it my component? I changed the payment form yesterday.", 'Ôi không. Có phải do component của em không? Hôm qua em sửa form thanh toán.'),
            ('A', "Not exactly. Your code worked fine on staging. But in production, the form re-rendered hundreds of times and crashed the browser on older phones.", 'Không hẳn. Code của em chạy tốt trên staging. Nhưng trên production, form vẽ lại hàng trăm lần và làm treo trình duyệt trên điện thoại đời cũ.'),
            ('B', "Hundreds of times? Why?", 'Hàng trăm lần? Sao vậy?'),
            ('A', "A small bug in the state logic. Every time the price updated, it changed the state again, so it never stopped.", 'Một lỗi nhỏ trong logic state. Mỗi lần giá cập nhật, nó lại đổi state, nên không bao giờ dừng.'),
            ('B', "I'm so sorry. How did you fix it?", 'Em xin lỗi. Chị sửa thế nào?'),
            ('A', "First, I rolled back to the previous version, so the site was back up quickly. Then I pushed a small hotfix this morning. The pipeline is green now.", 'Đầu tiên chị quay lui về phiên bản trước để trang chạy lại nhanh. Rồi sáng nay chị đẩy một bản vá nhỏ. Pipeline giờ xanh rồi.'),
            ('B', "Thank you. What can I do to make sure it doesn't happen again?", 'Cảm ơn chị. Em có thể làm gì để chuyện này không lặp lại?'),
            ('A', "Let's add a test for that component, and we should test on a slow phone before big releases. Don't worry, it happens to everyone.", 'Thêm test cho component đó, và mình nên thử trên điện thoại chậm trước các bản phát hành lớn. Đừng lo, ai cũng gặp mà.'),
        ],
        'questions': [
            ('How did Chloe find out about the problem?', ['A customer called.', 'Monitoring sent an alert.', 'Tri told her.', 'She saw it on social media.'], 1, '"Monitoring sent me an alert at midnight."'),
            ('How long was the checkout page down?', ['Five minutes', 'About fifteen minutes', 'All night', 'Two hours'], 1, '"down for about fifteen minutes".'),
            ('What was the cause?', ['A server crash', 'A state bug that caused endless re-rendering', 'A database migration', 'A slow network'], 1, '"A small bug in the state logic… it never stopped."'),
            ('What did Chloe do first?', ['Pushed a hotfix', 'Rolled back to the previous version', 'Called Tri', 'Turned off the server'], 1, '"First, I rolled back to the previous version".'),
        ],
    },
    'speaking': {
        'tips': ['Mô tả quy trình bằng câu bị động và từ chỉ trình tự.', 'Dùng ít nhất 6 thuật ngữ hôm nay.'],
        'prompts': [
            ('Describe how code gets from a developer\'s laptop to production at your company.', 'merge → pipeline → staging → production → monitoring'),
            ('Tell the story of a production incident you know about (real or imagined).', 'alert → cause → rollback/hotfix → lesson'),
        ],
        'model': (
            "At my company, when a pull request is merged into main, our CI/CD pipeline starts automatically. "
            "It builds the app, runs about two thousand tests, and packages everything into a container. "
            "Then the new version is deployed to staging, where our QA team checks the main flows. "
            "If everything looks good, we deploy to production twice a week. "
            "After each release, we watch our monitoring dashboards for about thirty minutes. "
            "If the error rate goes up, we roll back first and investigate later. Our uptime last year was 99.95 percent.",
            'Ở công ty tôi, khi một pull request được merge vào main, pipeline CI/CD tự chạy. '
            'Nó build ứng dụng, chạy khoảng hai nghìn test và đóng gói mọi thứ vào container. '
            'Sau đó phiên bản mới được triển khai lên staging, nơi đội QA kiểm tra các luồng chính. '
            'Nếu ổn, chúng tôi triển khai lên production hai lần một tuần. '
            'Sau mỗi lần phát hành, chúng tôi theo dõi bảng giám sát khoảng ba mươi phút. '
            'Nếu tỉ lệ lỗi tăng, chúng tôi quay lui trước rồi điều tra sau. Thời gian hoạt động năm ngoái là 99,95%.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Blameless post-mortems',
        'text': [
            'After a serious incident, many teams write a "post-mortem": a short document that explains what happened, why it happened and what will change. The best teams make these documents blameless.',
            'Blameless does not mean that nobody is responsible. It means the document focuses on systems, not people. Instead of writing "Tri broke the checkout page", it says "A state bug was not caught because the component had no tests and we did not test on slow devices."',
            'This matters because people who are afraid of blame hide problems. When engineers feel safe, they report mistakes early, and the whole system becomes more reliable. A typical post-mortem includes a timeline, the impact on users, the root cause and a list of action items.',
        ],
        'vi': 'Sau sự cố nghiêm trọng, nhiều team viết "post-mortem" giải thích chuyện gì xảy ra, vì sao và sẽ thay đổi gì. Team giỏi viết theo kiểu "không đổ lỗi": tập trung vào hệ thống chứ không vào con người ("lỗi state không bị phát hiện vì component không có test" thay vì "Trí làm hỏng trang"). Người sợ bị đổ lỗi sẽ giấu vấn đề; khi kỹ sư thấy an toàn, họ báo lỗi sớm và hệ thống đáng tin hơn. Post-mortem thường có dòng thời gian, tác động lên người dùng, nguyên nhân gốc và danh sách việc cần làm.',
        'questions': [
            ('What is a post-mortem?', ['A meeting to find who is guilty', 'A document explaining an incident and what will change', 'A type of test', 'A monitoring tool'], 1, 'Đoạn 1.'),
            ('What does "blameless" mean here?', ['Nobody is responsible.', 'The focus is on systems, not people.', 'Managers write it.', 'It is secret.'], 1, 'Đoạn 2.'),
            ('Which is NOT listed as part of a typical post-mortem?', ['A timeline', 'The impact on users', 'The name of the person to punish', 'Action items'], 2, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết một post-mortem ngắn (6–8 câu) cho sự cố ở bài nghe: tóm tắt, tác động, nguyên nhân gốc, cách xử lý, việc cần làm. Viết theo kiểu không đổ lỗi.',
        'tips': ['Dùng câu bị động để tập trung vào hệ thống.', 'Có ít nhất một con số (thời gian, số người dùng bị ảnh hưởng).'],
        'model': "Summary: On Tuesday night, the checkout page was down for about fifteen minutes.\nImpact: Around 300 users could not complete their orders, mostly on older Android phones.\nRoot cause: A bug in the payment form's state logic caused the component to re-render in an endless loop.\nWhy it was not caught: The component had no automated tests, and the release was only tested on fast devices.\nResolution: The previous version was restored with a rollback, and a hotfix was deployed the next morning.\nAction items: Add tests for the payment form; test major releases on a low-end phone; add an alert for client-side errors.",
        'min_words': 70,
    },
    'quiz': [
        ('A reusable piece of UI is a ___.', ['component', 'container', 'pipeline', 'payload'], 0, 'component.'),
        ('Data passed from a parent component to a child is called ___.', ['state', 'props', 'render', 'staging'], 1, 'props.'),
        ('When state changes, the component ___.', ['re-renders', 'rolls back', 'migrates', 'deploys'], 0, 're-renders = vẽ lại.'),
        ('A design that works on phones and desktops is ___.', ['responsive', 'idempotent', 'containerised', 'blameless'], 0, 'responsive.'),
        ('An urgent fix released outside the normal schedule is a ___.', ['hotfix', 'pipeline', 'backlog', 'staging'], 0, 'hotfix.'),
        ('The environment that real users use is ___.', ['staging', 'production', 'local', 'testing'], 1, 'production.'),
        ('99.9% ___ means the system is available almost all the time.', ['downtime', 'uptime', 'latency', 'payload'], 1, 'uptime.'),
        ('"The site is ___." (sập)', ['up', 'down', 'off', 'out'], 1, 'down = sập.'),
        ('"It\'s ___ now." (chạy lại rồi)', ['back up', 'back down', 'up back', 'on back'], 0, 'back up.'),
        ('The automated steps that build, test and deploy code form a ___.', ['pipeline', 'component', 'schema', 'container'], 0, 'pipeline.'),
        ('Alerts and dashboards are part of ___.', ['monitoring', 'rendering', 'staging', 'props'], 0, 'monitoring.'),
        ('Post-mortem "blameless" tập trung vào:', ['Người gây lỗi', 'Hệ thống và quy trình', 'Khách hàng', 'Chi phí'], 1, 'Hệ thống, không phải con người.'),
    ],
}

DAY3 = {
    'title': 'Từ vựng quản lý dự án',
    'title_en': 'Project Management Vocabulary',
    'goal': 'Nắm 14 thuật ngữ quản lý dự án Agile (sprint, backlog, scope creep, blocker, stakeholder, roadmap…) và tham gia được buổi lập kế hoạch sprint.',
    'tasks': [
        'Học 14 thuật ngữ quản lý dự án.',
        'Nghe buổi sprint planning, trả lời câu hỏi.',
        'Luyện thẻ từ.',
        'Nói: mô tả cách team bạn làm việc trong một sprint.',
        'Viết câu ví dụ cho từng từ.',
    ],
    'product': '14 thẻ từ đã luyện; Câu ví dụ cho từng từ',
    'warmup': [
        ("Let's look at the backlog.", 'Hãy xem backlog.'),
        ("This is out of scope for this sprint.", 'Việc này nằm ngoài phạm vi sprint này.'),
        ("I'm blocked by the API team.", 'Tôi đang bị team API chặn tiến độ.'),
        ('Our main stakeholder is the marketing director.', 'Bên liên quan chính của chúng tôi là giám đốc marketing.'),
        ('Can you give me an estimate?', 'Bạn có thể ước lượng giúp tôi không?'),
        ("We're at risk of missing the deadline.", 'Chúng ta có nguy cơ trễ hạn.'),
    ],
    'vocab': [
        ('sprint', '/sprɪnt/', 'n', 'chu kỳ làm việc ngắn (thường 2 tuần)', 'Our sprints are two weeks long.', 'Mỗi sprint của chúng tôi dài hai tuần.'),
        ('backlog', '/ˈbæklɒɡ/', 'n', 'danh sách việc chờ làm', 'The backlog has over two hundred tickets.', 'Backlog có hơn hai trăm ticket.'),
        ('scope creep', '/ˈskəʊp kriːp/', 'n', 'phạm vi công việc phình dần', 'Scope creep is why we missed the launch date.', 'Phạm vi phình dần là lý do chúng tôi lỡ ngày ra mắt.'),
        ('deadline', '/ˈdedlaɪn/', 'n', 'hạn chót', 'The deadline for the report is Friday noon.', 'Hạn chót nộp báo cáo là trưa thứ Sáu.'),
        ('blocker', '/ˈblɒkə/', 'n', 'vấn đề cản trở tiến độ', 'Do you have any blockers today?', 'Hôm nay bạn có bị vướng gì không?'),
        ('stakeholder', '/ˈsteɪkhəʊldə/', 'n', 'bên liên quan', 'We present the demo to stakeholders every month.', 'Chúng tôi demo cho các bên liên quan hằng tháng.'),
        ('roadmap', '/ˈrəʊdmæp/', 'n', 'lộ trình sản phẩm', 'Dark mode is on the roadmap for next quarter.', 'Chế độ tối nằm trong lộ trình quý tới.'),
        ('estimate', '/ˈestɪmət/ (n), /ˈestɪmeɪt/ (v)', 'n / verb', 'ước lượng', 'My estimate is three days, but it could be more.', 'Tôi ước lượng ba ngày, nhưng có thể hơn.'),
        ('deliverable', '/dɪˈlɪvərəbl/', 'n', 'sản phẩm bàn giao', 'The main deliverable is a working prototype.', 'Sản phẩm bàn giao chính là một bản mẫu chạy được.'),
        ('retrospective', '/ˌretrəˈspektɪv/', 'n', 'buổi họp nhìn lại sprint (retro)', 'In the retrospective, we discussed what went wrong.', 'Trong buổi retro, chúng tôi bàn về những gì chưa ổn.'),
        ('MVP', '/ˌem viː ˈpiː/', 'n', 'sản phẩm khả dụng tối thiểu', "Let's launch an MVP and learn from real users.", 'Hãy ra mắt một MVP và học từ người dùng thật.'),
        ('user story', '/ˈjuːzə ˈstɔːri/', 'n', 'câu chuyện người dùng (mô tả yêu cầu)', 'Each user story should fit in one sprint.', 'Mỗi user story nên vừa trong một sprint.'),
        ('ticket', '/ˈtɪkɪt/', 'n', 'phiếu công việc (Jira…)', "I've created a ticket for the bug.", 'Tôi đã tạo ticket cho lỗi đó.'),
        ('kickoff', '/ˈkɪkɒf/', 'n', 'buổi khởi động dự án', 'The project kickoff is on Monday at ten.', 'Buổi khởi động dự án vào thứ Hai lúc mười giờ.'),
    ],
    'lesson': """
<h3>1. Vòng đời một sprint</h3>
<table class="table">
<tr><th>Sự kiện</th><th>Câu thường nghe</th></tr>
<tr><td>Sprint planning</td><td><span class="say">Let's pick the top tickets from the backlog.</span> · <span class="say">How many story points is this?</span></td></tr>
<tr><td>Daily stand-up</td><td><span class="say">Any blockers?</span></td></tr>
<tr><td>Sprint review / demo</td><td><span class="say">Let's demo what we shipped to the stakeholders.</span></td></tr>
<tr><td>Retrospective</td><td><span class="say">What went well? What could we improve?</span></td></tr>
</table>

<h3>2. User story — viết yêu cầu theo góc nhìn người dùng</h3>
<div class="ex"><span class="en">As a customer, I want to save my address, so that I don't have to type it every time.</span><span class="vi">Là khách hàng, tôi muốn lưu địa chỉ, để không phải gõ lại mỗi lần.</span></div>
<p>Khung: <b>As a</b> [người dùng], <b>I want</b> [tính năng], <b>so that</b> [lợi ích].</p>

<h3>3. Nói về phạm vi và thời hạn</h3>
<table class="table">
<tr><th>Cụm từ</th><th>Nghĩa</th></tr>
<tr><td><span class="say">That's out of scope.</span></td><td>Nằm ngoài phạm vi</td></tr>
<tr><td><span class="say">Let's add it to the backlog.</span></td><td>Đưa vào danh sách chờ (lịch sự từ chối làm ngay)</td></tr>
<tr><td><span class="say">We're on track.</span></td><td>Đúng tiến độ</td></tr>
<tr><td><span class="say">We're at risk of missing the deadline.</span></td><td>Có nguy cơ trễ hạn</td></tr>
<tr><td><span class="say">That's a rough estimate.</span></td><td>Đó là ước lượng sơ bộ</td></tr>
</table>
<div class="note"><b>estimate:</b> danh từ đọc /ˈestɪmət/, động từ đọc /ˈestɪmeɪt/. <span class="say">Can you estimate it? — My estimate is two days.</span></div>
""",
    'phrases': [
        ("That's out of scope for this sprint.", 'Việc đó ngoài phạm vi sprint này.'),
        ("Let's add it to the backlog.", 'Hãy đưa nó vào backlog.'),
        ("We're on track.", 'Chúng ta đang đúng tiến độ.'),
        ("It's just a rough estimate.", 'Đó chỉ là ước lượng sơ bộ.'),
    ],
    'listening': {
        'title': 'Sprint planning',
        'intro': 'Product manager Sophie và team lead Duy lập kế hoạch sprint mới.',
        'speakers': {'A': ('Sophie', 'emma'), 'B': ('Duy', 'guy')},
        'lines': [
            ('A', "Okay, welcome to sprint planning. Our goal for this sprint is the MVP of the loyalty program.", 'Được rồi, chào mừng đến buổi sprint planning. Mục tiêu sprint này là MVP của chương trình khách hàng thân thiết.'),
            ('B', "Sounds good. What are the must-have user stories?", 'Nghe ổn. Những user story bắt buộc là gì?'),
            ('A', "Three. Customers can see their points, they can earn points when they buy, and they can use points at checkout.", 'Ba cái. Khách hàng xem được điểm, tích điểm khi mua hàng, và dùng điểm khi thanh toán.'),
            ('B', "The first two are straightforward. My estimate is about five days for both. The checkout one is trickier.", 'Hai cái đầu đơn giản. Tôi ước lượng khoảng năm ngày cho cả hai. Cái thanh toán khó hơn.'),
            ('A', "Why is that?", 'Sao vậy?'),
            ('B', "We depend on the payment team. They need to change their API, and that's currently a blocker.", 'Chúng ta phụ thuộc vào team thanh toán. Họ cần đổi API, và hiện đó là vướng mắc.'),
            ('A', "I'll talk to their manager today. The stakeholders really want to launch before the holiday season.", 'Hôm nay tôi sẽ nói với quản lý của họ. Các bên liên quan rất muốn ra mắt trước mùa lễ.'),
            ('B', "Also, marketing asked for a points history page and email notifications. That's a lot.", 'Ngoài ra, marketing yêu cầu trang lịch sử điểm và thông báo email. Nhiều quá.'),
            ('A', "That's scope creep. Let's add those to the backlog and keep this sprint focused on the MVP.", 'Đó là phạm vi phình dần. Đưa chúng vào backlog và giữ sprint này tập trung vào MVP.'),
            ('B', "Agreed. If the payment API is ready by Wednesday, we're on track. If not, we're at risk of missing the deadline.", 'Đồng ý. Nếu API thanh toán xong trước thứ Tư, chúng ta đúng tiến độ. Nếu không, có nguy cơ trễ hạn.'),
            ('A', "Understood. I'll create the tickets and update the roadmap after this meeting.", 'Đã hiểu. Tôi sẽ tạo ticket và cập nhật lộ trình sau cuộc họp này.'),
        ],
        'questions': [
            ('What is the goal of the sprint?', ['A new checkout page', 'The MVP of a loyalty program', 'Email notifications', 'A payment API'], 1, '"the MVP of the loyalty program".'),
            ('Why is the checkout story trickier?', ['It needs a new design.', 'It depends on the payment team changing their API.', 'Nobody knows how to do it.', 'Marketing doesn\'t want it.'], 1, '"We depend on the payment team…"'),
            ('What does Sophie call the extra requests from marketing?', ['A blocker', 'Scope creep', 'A deliverable', 'A retrospective'], 1, '"That\'s scope creep."'),
            ('What will happen to the extra requests?', ['They will be done this sprint.', 'They will be added to the backlog.', 'They will be cancelled forever.', 'Duy will do them at the weekend.'], 1, '"Let\'s add those to the backlog".'),
            ('When will the team be on track?', ['If marketing agrees', 'If the payment API is ready by Wednesday', 'If they work overtime', 'If they skip testing'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Mô tả quy trình Agile của team bạn (hoặc team bạn muốn).', 'Dùng ít nhất 6 thuật ngữ hôm nay.'],
        'prompts': [
            ('How does your team plan and track work?', 'sprint, backlog, tickets, stand-up, retro'),
            ('A stakeholder asks for a new feature in the middle of the sprint. What do you say?', 'out of scope / add it to the backlog'),
            ('Write a user story for a feature you want, then read it aloud.', 'As a…, I want…, so that…'),
        ],
        'model': (
            "Our team works in two-week sprints. At the start of each sprint, we have a planning meeting where we pick the most important tickets from the backlog and estimate them. "
            "Every morning there's a short stand-up where we share our progress and any blockers. "
            "At the end of the sprint, we demo the work to our stakeholders, and then we have a retrospective to discuss what went well and what to improve. "
            "Our biggest problem is scope creep: people often ask for new things in the middle of the sprint. "
            "When that happens, I politely say it's out of scope for now and suggest adding it to the backlog.",
            'Team chúng tôi làm việc theo sprint hai tuần. Đầu mỗi sprint có buổi lập kế hoạch, chúng tôi chọn các ticket quan trọng nhất trong backlog và ước lượng chúng. '
            'Mỗi sáng có buổi stand-up ngắn để chia sẻ tiến độ và vướng mắc. '
            'Cuối sprint, chúng tôi demo cho các bên liên quan, rồi họp retro để bàn điều gì tốt và cần cải thiện gì. '
            'Vấn đề lớn nhất là phạm vi phình dần: mọi người hay yêu cầu thêm việc giữa sprint. '
            'Khi đó tôi lịch sự nói việc này ngoài phạm vi hiện tại và đề nghị đưa vào backlog.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Why estimates are always wrong',
        'text': [
            'Every developer has said "it will take two days" and then spent a week on the task. Estimates are hard because software work is full of unknowns: unclear requirements, hidden bugs and dependencies on other teams.',
            'Good teams accept this. Instead of single numbers, they give ranges ("three to five days") and explain the risks ("if the payment API is ready"). They also break large tickets into smaller ones, because small tasks are much easier to estimate.',
            'Most importantly, they update their estimates early. Telling a manager on Tuesday that a task will take longer is uncomfortable. Telling them on Friday, the day of the deadline, is much worse.',
        ],
        'vi': 'Ước lượng khó vì phần mềm đầy ẩn số: yêu cầu chưa rõ, lỗi ẩn, phụ thuộc team khác. Team giỏi chấp nhận điều đó: đưa ra khoảng ("3–5 ngày") kèm rủi ro, và chia ticket lớn thành nhỏ để dễ ước lượng. Quan trọng nhất là cập nhật ước lượng sớm — báo trễ vào thứ Ba khó chịu, nhưng báo vào thứ Sáu (ngày hạn chót) còn tệ hơn nhiều.',
        'questions': [
            ('Why are estimates hard, according to the text?', ['Developers are lazy.', 'Software work has many unknowns.', 'Managers change the deadline.', 'Tools are slow.'], 1, 'Đoạn 1.'),
            ('What do good teams give instead of single numbers?', ['Ranges and risks', 'No estimates', 'Longer deadlines', 'Story points only'], 0, 'Đoạn 2.'),
            ('When should you tell a manager a task will take longer?', ['On the deadline day', 'As early as possible', 'After the deadline', 'Never'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 3 user story cho một sản phẩm bạn biết (theo khung As a… I want… so that…), sau đó viết 5 câu dùng các từ: backlog, blocker, scope creep, estimate, stakeholder.',
        'tips': ['User story tập trung vào lợi ích người dùng, không phải giải pháp kỹ thuật.'],
        'model': "User stories:\n1. As a customer, I want to save my favourite restaurants, so that I can order from them quickly.\n2. As a driver, I want to see the customer's phone number, so that I can call them if I can't find the address.\n3. As a restaurant owner, I want a daily sales report, so that I know which dishes are popular.\n\nSentences:\nOur backlog is full of small UI improvements.\nMy only blocker today is access to the staging database.\nAdding a chat feature in the middle of the sprint would be scope creep.\nMy estimate for the report page is three to five days.\nWe will show the MVP to the main stakeholders next Thursday.",
        'min_words': 80,
    },
    'quiz': [
        ('A two-week period of work is a ___.', ['sprint', 'roadmap', 'kickoff', 'ticket'], 0, 'sprint.'),
        ('The list of all work waiting to be done is the ___.', ['backlog', 'blocker', 'deliverable', 'roadmap'], 0, 'backlog.'),
        ('When a project keeps growing with new requests, that is ___.', ['scope creep', 'a blocker', 'a kickoff', 'a sprint'], 0, 'scope creep.'),
        ('"Any ___?" — "Yes, I\'m waiting for access to the server."', ['blockers', 'stakeholders', 'estimates', 'roadmaps'], 0, 'blocker.'),
        ('People who are affected by or interested in the project are ___.', ['stakeholders', 'users stories', 'tickets', 'sprints'], 0, 'stakeholders.'),
        ('The smallest version of a product you can launch is the ___.', ['MVP', 'API', 'SQL', 'CI/CD'], 0, 'MVP.'),
        ('A meeting at the end of a sprint to discuss what to improve is a ___.', ['retrospective', 'kickoff', 'roadmap', 'deliverable'], 0, 'retrospective.'),
        ('Danh từ "estimate" phát âm /ˈestɪmət/. Động từ phát âm:', ['/ˈestɪmət/', '/ˈestɪmeɪt/', '/ɪsˈtɪmeɪt/', '/ˈestmeɪt/'], 1, 'Động từ: /ˈestɪmeɪt/.'),
        ('Lịch sự từ chối yêu cầu thêm giữa sprint:', ["No, I won't.", "That's out of scope for now. Let's add it to the backlog.", 'Impossible.', 'Ask someone else.'], 1, 'out of scope + backlog.'),
        ('"We\'re on ___." (đúng tiến độ)', ['track', 'time line', 'road', 'way'], 0, 'on track.'),
        ('User story khung chuẩn:', ['As a…, I want…, so that…', 'If…, then…', 'Given…, when…', 'Because…, therefore…'], 0, 'As a…, I want…, so that…'),
        ('The first meeting that starts a project is the ___.', ['kickoff', 'retro', 'demo', 'review'], 0, 'kickoff.'),
    ],
}

DAY4 = {
    'title': 'Collocations hay gặp',
    'title_en': 'Common Workplace Collocations',
    'goal': 'Dùng đúng các cụm từ cố định trong công việc (make a decision, fix a bug, raise a concern, meet a deadline…) để nói tự nhiên như người bản xứ.',
    'tasks': [
        'Học 14 collocations, chú ý động từ đi kèm.',
        'Làm bài chọn động từ đúng.',
        'Nghe buổi retrospective, ghi lại các collocation nghe được.',
        'Viết 10 câu dùng collocations.',
    ],
    'product': '10 câu dùng collocations',
    'warmup': [
        ("We need to make a decision today.", 'Hôm nay chúng ta cần đưa ra quyết định.'),
        ("I'd like to raise a concern about the timeline.", 'Tôi muốn nêu một mối lo về tiến độ.'),
        ('Could you open a pull request when you\'re ready?', 'Bạn mở pull request khi sẵn sàng nhé?'),
        ("Let's run the tests again.", 'Hãy chạy lại test.'),
        ('We managed to meet the deadline.', 'Chúng tôi đã kịp hạn chót.'),
        ('Who will take ownership of this task?', 'Ai sẽ nhận trách nhiệm việc này?'),
    ],
    'vocab': [
        ('make a decision', '/meɪk ə dɪˈsɪʒn/', 'collocation', 'đưa ra quyết định', "We can't make a decision without more data.", 'Chúng ta không thể quyết định khi chưa có thêm dữ liệu.'),
        ('run a test', '/rʌn ə test/', 'collocation', 'chạy kiểm thử', 'Run the tests before you push.', 'Hãy chạy test trước khi push.'),
        ('fix a bug', '/fɪks ə bʌɡ/', 'collocation', 'sửa lỗi', 'It took me all morning to fix that bug.', 'Tôi mất cả buổi sáng để sửa lỗi đó.'),
        ('push a commit', '/pʊʃ ə kəˈmɪt/', 'collocation', 'đẩy commit lên', 'I pushed a commit with the new tests.', 'Tôi đã đẩy một commit kèm test mới.'),
        ('raise a concern', '/reɪz ə kənˈsɜːn/', 'collocation', 'nêu mối lo ngại', 'Lan raised a concern about security.', 'Lan nêu mối lo ngại về bảo mật.'),
        ('meet a deadline', '/miːt ə ˈdedlaɪn/', 'collocation', 'kịp hạn chót', "We worked late to meet the deadline.", 'Chúng tôi làm muộn để kịp hạn chót.'),
        ('open a pull request', '/ˈəʊpən ə pʊl rɪˈkwest/', 'collocation', 'mở pull request', 'Open a pull request and tag me as a reviewer.', 'Mở pull request và gắn tôi làm người review.'),
        ('file a ticket', '/faɪl ə ˈtɪkɪt/', 'collocation', 'tạo/gửi ticket', 'Please file a ticket so we can track it.', 'Hãy tạo ticket để chúng ta theo dõi.'),
        ('set up an environment', '/set ʌp ən ɪnˈvaɪrənmənt/', 'collocation', 'dựng môi trường', 'It took a day to set up my local environment.', 'Mất một ngày để dựng môi trường trên máy.'),
        ('take ownership', '/teɪk ˈəʊnəʃɪp/', 'collocation', 'nhận trách nhiệm (làm chủ)', 'She took ownership of the migration project.', 'Cô ấy nhận trách nhiệm dự án migration.'),
        ('reach an agreement', '/riːtʃ ən əˈɡriːmənt/', 'collocation', 'đạt được thỏa thuận', 'After an hour, we reached an agreement.', 'Sau một giờ, chúng tôi đạt được thỏa thuận.'),
        ('address an issue', '/əˈdres ən ˈɪʃuː/', 'collocation', 'giải quyết một vấn đề', 'The new release addresses several performance issues.', 'Bản phát hành mới giải quyết một số vấn đề hiệu năng.'),
        ('ship a feature', '/ʃɪp ə ˈfiːtʃə/', 'collocation', 'phát hành tính năng', 'We shipped three features last month.', 'Tháng trước chúng tôi phát hành ba tính năng.'),
        ('gather requirements', '/ˈɡæðə rɪˈkwaɪəmənts/', 'collocation', 'thu thập yêu cầu', 'We spent a week gathering requirements from users.', 'Chúng tôi mất một tuần thu thập yêu cầu từ người dùng.'),
    ],
    'lesson': """
<h3>1. Collocation là gì?</h3>
<p>Collocation là những từ <b>thường đi với nhau</b>. Dịch từng từ từ tiếng Việt sẽ cho ra câu "đúng ngữ pháp nhưng nghe lạ":</p>
<div class="fix"><s>do a decision</s><span class="en">make a decision</span></div>
<div class="fix"><s>repair a bug</s><span class="en">fix a bug</span></div>
<div class="fix"><s>catch the deadline</s><span class="en">meet the deadline</span></div>
<div class="fix"><s>say a concern</s><span class="en">raise a concern</span></div>
<div class="fix"><s>make a test</s><span class="en">run a test</span></div>

<h3>2. Make hay Do?</h3>
<table class="table">
<tr><th>MAKE (tạo ra, quyết định)</th><th>DO (làm việc, nhiệm vụ)</th></tr>
<tr><td>make a decision, make a mistake, make progress, make a change, make a suggestion, make an effort</td><td>do a task, do research, do a code review, do your best, do the dishes, do business</td></tr>
</table>

<h3>3. Collocations theo nhóm</h3>
<table class="table">
<tr><th>Nhóm</th><th>Collocations</th></tr>
<tr><td>Code</td><td><span class="say">write code</span> · <span class="say">fix a bug</span> · <span class="say">push a commit</span> · <span class="say">open a pull request</span> · <span class="say">run the tests</span> · <span class="say">ship a feature</span></td></tr>
<tr><td>Họp</td><td><span class="say">raise a concern</span> · <span class="say">make a decision</span> · <span class="say">reach an agreement</span> · <span class="say">take notes</span> · <span class="say">set an agenda</span></td></tr>
<tr><td>Dự án</td><td><span class="say">meet a deadline</span> · <span class="say">miss a deadline</span> · <span class="say">gather requirements</span> · <span class="say">take ownership</span> · <span class="say">address an issue</span></td></tr>
</table>
<div class="note"><b>Mẹo học:</b> Luôn học danh từ <b>cùng động từ</b> của nó. Khi ghi vào thẻ từ, ghi "meet / miss a deadline" thay vì chỉ "deadline".</div>
""",
    'phrases': [
        ("I'd like to raise a concern.", 'Tôi muốn nêu một mối lo ngại.'),
        ("Let's make a decision by Friday.", 'Hãy ra quyết định trước thứ Sáu.'),
        ("I'll take ownership of this.", 'Tôi sẽ nhận trách nhiệm việc này.'),
        ("Could you file a ticket for that?", 'Bạn tạo ticket cho việc đó được không?'),
    ],
    'listening': {
        'title': 'Sprint retrospective',
        'intro': 'Team họp retro cuối sprint. Ghi lại các collocation bạn nghe được.',
        'speakers': {'A': ('Anna', 'ava'), 'B': ('Kien', 'brian')},
        'lines': [
            ('A', "Okay team, let's start the retro. What went well this sprint?", 'Được rồi cả team, bắt đầu retro nào. Sprint này điều gì tốt?'),
            ('B', "We shipped the loyalty feature and we met the deadline, even with the payment API delay.", 'Chúng ta phát hành tính năng tích điểm và kịp hạn chót, dù API thanh toán bị chậm.'),
            ('A', "Great. I think it worked because Lan took ownership of the integration and talked to the payment team every day.", 'Tuyệt. Tôi nghĩ nó thành công vì Lan nhận trách nhiệm phần tích hợp và trao đổi với team thanh toán mỗi ngày.'),
            ('B', "Agreed. What didn't go so well?", 'Đồng ý. Còn điều gì chưa ổn?'),
            ('A', "I'd like to raise a concern about testing. We fixed a lot of bugs in the last two days. That's stressful.", 'Tôi muốn nêu một mối lo về kiểm thử. Hai ngày cuối chúng ta sửa rất nhiều lỗi. Căng thẳng quá.'),
            ('B', "True. Some people pushed commits without running the tests locally.", 'Đúng. Một số người đẩy commit mà không chạy test trên máy.'),
            ('A', "So how can we address this issue?", 'Vậy làm sao giải quyết vấn đề này?'),
            ('B', "Let's make it a rule: nobody opens a pull request until all tests pass. And the pipeline should block the merge if they fail.", 'Hãy đặt thành quy tắc: không ai mở pull request khi test chưa qua hết. Và pipeline nên chặn merge nếu test lỗi.'),
            ('A', "Good. Also, we need to gather requirements earlier. We started coding before the designs were final.", 'Tốt. Ngoài ra, chúng ta cần thu thập yêu cầu sớm hơn. Chúng ta bắt đầu code trước khi thiết kế được chốt.'),
            ('B', "Okay. So we've reached an agreement on two action items. I'll file a ticket for the pipeline change.", 'Được. Vậy chúng ta đã thống nhất hai việc cần làm. Tôi sẽ tạo ticket cho thay đổi pipeline.'),
        ],
        'questions': [
            ('What went well this sprint?', ['They shipped the feature and met the deadline.', 'They had no bugs.', 'The payment API was early.', 'They finished early.'], 0, '"We shipped the loyalty feature and we met the deadline".'),
            ('Who took ownership of the integration?', ['Anna', 'Kien', 'Lan', 'The payment team'], 2, '"Lan took ownership of the integration".'),
            ('What concern did Anna raise?', ['Security', 'Testing', 'Salaries', 'Design'], 1, '"I\'d like to raise a concern about testing."'),
            ('What new rule did they agree on?', ['No meetings on Friday', 'No pull requests until all tests pass', 'Only Lan can merge', 'No coding before noon'], 1, '"nobody opens a pull request until all tests pass".'),
            ('What will Kien do?', ['Fix all the bugs', 'File a ticket for the pipeline change', 'Talk to the designers', 'Cancel the next sprint'], 1, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Dùng ít nhất 6 collocations.', 'Nói như đang ở buổi retro thật: went well → didn\'t go well → action items.'],
        'prompts': [
            ('Run a mini retrospective of your last week: what went well, what didn\'t, and what will you change?', 'Collocations: meet a deadline, fix a bug, raise a concern…'),
            ('Describe a time you made a difficult decision at work.', 'make a decision, reach an agreement'),
        ],
        'model': (
            "Looking at my last week, one thing went well: I shipped the new export feature and met the deadline. "
            "I also fixed two old bugs that customers had reported. "
            "What didn't go so well was communication. I made a decision about the file format on my own, and later the product manager raised a concern about it. "
            "We had to change it on Thursday, which cost me half a day. "
            "Next week, I'll gather requirements more carefully before I start coding, and I'll take ownership of updating the documentation.",
            'Nhìn lại tuần trước, có một điều tốt: tôi phát hành tính năng xuất file mới và kịp hạn chót. '
            'Tôi cũng sửa hai lỗi cũ khách hàng đã báo. '
            'Điều chưa ổn là giao tiếp. Tôi tự quyết định định dạng file, rồi sau đó product manager nêu lo ngại về nó. '
            'Chúng tôi phải đổi vào thứ Năm, mất của tôi nửa ngày. '
            'Tuần tới, tôi sẽ thu thập yêu cầu kỹ hơn trước khi code, và tôi sẽ nhận trách nhiệm cập nhật tài liệu.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Sounding natural: the power of collocations',
        'text': [
            'Two learners can know exactly the same number of words but sound very different. The difference is often collocations. A learner who says "I did a mistake and repaired the bug" is understood, but the listener immediately notices that something is not quite right.',
            'Collocations are rarely taught as rules, because there are no clear rules. Why do we "make" a decision but "take" a break? Why do we "run" a test but "do" a review? The only way is to notice them in real texts and learn them as chunks.',
            'A practical method is to keep a collocation list organised by noun. Next to "deadline", write "meet / miss / extend / set a deadline". Next to "concern", write "raise / share / address a concern". After a few weeks, the right verb will come to you automatically.',
        ],
        'vi': 'Hai người học biết cùng số từ nhưng nghe rất khác nhau — khác biệt thường nằm ở collocation. "I did a mistake and repaired the bug" vẫn hiểu được nhưng người nghe nhận ra ngay có gì đó không ổn. Collocation hiếm khi có quy tắc rõ ràng (sao lại make a decision nhưng take a break?), nên cách duy nhất là để ý trong văn bản thật và học theo cụm. Cách thực tế: lập danh sách theo danh từ, ví dụ "deadline: meet / miss / extend / set".',
        'questions': [
            ('What often makes learners with the same vocabulary sound different?', ['Their accent', 'Collocations', 'Their speed', 'Their grammar books'], 1, 'Đoạn 1.'),
            ('Why are collocations rarely taught as rules?', ['They are not important.', 'There are no clear rules.', 'Teachers don\'t know them.', 'They change every year.'], 1, 'Đoạn 2.'),
            ('How does the writer suggest organising a collocation list?', ['By verb', 'By noun', 'Alphabetically by verb', 'By topic only'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 10 câu về công việc của bạn, mỗi câu dùng một collocation khác nhau (gạch chân collocation).',
        'tips': ['Ít nhất 2 câu dùng make, 2 câu dùng do.'],
        'model': "1. Last week we made a decision to move to PostgreSQL.\n2. I always run the tests before I push a commit.\n3. It took me two hours to fix a bug in the date picker.\n4. In the planning meeting, I raised a concern about the timeline.\n5. We worked hard and met the deadline for the demo.\n6. I opened a pull request for the new search page this morning.\n7. If you find a problem, please file a ticket.\n8. Setting up the environment for new developers takes too long.\n9. Minh took ownership of the monitoring dashboard.\n10. This release addresses the slow login issue.",
        'min_words': 80,
    },
    'quiz': [
        ('We need to ___ a decision before Friday.', ['do', 'make', 'take', 'have'], 1, 'make a decision.'),
        ("I'd like to ___ a concern about the budget.", ['raise', 'say', 'tell', 'put'], 0, 'raise a concern.'),
        ('We worked overtime to ___ the deadline.', ['catch', 'hit up', 'meet', 'reach on'], 2, 'meet a deadline.'),
        ('Please ___ the tests before you merge.', ['make', 'run', 'do up', 'play'], 1, 'run the tests.'),
        ('It took me an hour to ___ the bug.', ['repair', 'fix', 'correct up', 'solve up'], 1, 'fix a bug.'),
        ('Who will ___ ownership of the release?', ['make', 'take', 'do', 'get'], 1, 'take ownership.'),
        ('After a long meeting, they ___ an agreement.', ['reached', 'made up', 'did', 'got on'], 0, 'reach an agreement.'),
        ('I ___ a mistake in the report.', ['did', 'made', 'took', 'had'], 1, 'make a mistake.'),
        ('Could you ___ a code review for me?', ['make', 'do', 'take', 'run'], 1, 'do a code review.'),
        ('Let\'s ___ a short break.', ['make', 'do', 'take', 'have to'], 2, 'take a break.'),
        ('The new release ___ several security issues.', ['addresses', 'speaks', 'talks', 'tells'], 0, 'address an issue.'),
        ('We ___ three new features last quarter.', ['shipped', 'sent', 'posted', 'carried'], 0, 'ship a feature.'),
    ],
}

DAY5 = {
    'title': 'Shadowing 4: tài liệu kỹ thuật',
    'title_en': 'Shadowing 4: Reading Technical Docs Aloud',
    'goal': 'Đọc to một đoạn tài liệu kỹ thuật kiểu Django/FastAPI chậm, đều, rõ ràng; nắm ngôn ngữ đặc trưng của tài liệu (by default, ensure, optional, deprecated…).',
    'tasks': [
        'Học 14 từ hay gặp trong tài liệu kỹ thuật.',
        'Nghe đoạn tài liệu được đọc mẫu.',
        'Shadow từng câu ở tốc độ chậm, chú ý ngắt nghỉ và nhấn từ khóa.',
        'Tự đọc to cả đoạn và ghi âm 2 phút.',
    ],
    'product': 'Bản ghi âm đọc tài liệu 2 phút',
    'warmup': [
        ('By default, the server runs on port eight thousand.', 'Mặc định, server chạy ở cổng 8000.'),
        ('Make sure that the database is running before you start.', 'Đảm bảo cơ sở dữ liệu đang chạy trước khi bắt đầu.'),
        ('This parameter is optional.', 'Tham số này là tùy chọn.'),
        ('The function returns a list of users.', 'Hàm trả về danh sách người dùng.'),
        ('This method is deprecated and will be removed in version five.', 'Phương thức này đã lỗi thời và sẽ bị gỡ ở phiên bản 5.'),
        ('For more details, refer to the configuration guide.', 'Để biết thêm chi tiết, hãy tham khảo hướng dẫn cấu hình.'),
    ],
    'vocab': [
        ('prerequisite', '/ˌpriːˈrekwəzɪt/', 'n', 'điều kiện tiên quyết', 'The only prerequisite is Python 3.10 or later.', 'Điều kiện tiên quyết duy nhất là Python 3.10 trở lên.'),
        ('ensure', '/ɪnˈʃʊə/', 'verb', 'đảm bảo', 'Ensure that your API key is kept secret.', 'Đảm bảo API key của bạn được giữ bí mật.'),
        ('optional', '/ˈɒpʃənl/', 'adj', 'tùy chọn, không bắt buộc', 'The description field is optional.', 'Trường mô tả là tùy chọn.'),
        ('by default', '/baɪ dɪˈfɔːlt/', 'phrase', 'theo mặc định', 'By default, all fields are required.', 'Mặc định, mọi trường đều bắt buộc.'),
        ('deprecated', '/ˈdeprəkeɪtɪd/', 'adj', 'lỗi thời (sắp bị loại bỏ)', 'This setting is deprecated since version 4.', 'Thiết lập này đã lỗi thời từ phiên bản 4.'),
        ('parameter', '/pəˈræmɪtə/', 'n', 'tham số', 'The function takes two parameters.', 'Hàm nhận hai tham số.'),
        ('return', '/rɪˈtɜːn/', 'verb', 'trả về (giá trị)', 'The view returns an HTTP response.', 'View trả về một HTTP response.'),
        ('instance', '/ˈɪnstəns/', 'n', 'thể hiện, đối tượng (của lớp)', 'Each instance of the model is one row in the table.', 'Mỗi đối tượng của model là một hàng trong bảng.'),
        ('refer to', '/rɪˈfɜː tuː/', 'phrasal verb', 'tham khảo; đề cập đến', 'Refer to the FAQ for common errors.', 'Tham khảo phần FAQ cho các lỗi thường gặp.'),
        ('note that', '/nəʊt ðæt/', 'phrase', 'lưu ý rằng', 'Note that this command deletes all data.', 'Lưu ý rằng lệnh này xóa toàn bộ dữ liệu.'),
        ('argument', '/ˈɑːɡjumənt/', 'n', 'đối số (giá trị truyền vào)', 'Pass the user ID as the first argument.', 'Truyền ID người dùng làm đối số đầu tiên.'),
        ('attribute', '/ˈætrɪbjuːt/', 'n', 'thuộc tính', 'The name attribute stores the full name.', 'Thuộc tính name lưu họ tên đầy đủ.'),
        ('override', '/ˌəʊvəˈraɪd/', 'verb', 'ghi đè', 'You can override the save method.', 'Bạn có thể ghi đè phương thức save.'),
        ('straightforward', '/ˌstreɪtˈfɔːwəd/', 'adj', 'đơn giản, dễ hiểu', 'The installation is straightforward.', 'Việc cài đặt rất đơn giản.'),
    ],
    'lesson': """
<h3>1. Đọc to tài liệu: chậm, đều, rõ</h3>
<ul>
<li><b>Ngắt ở dấu câu</b> và trước mệnh đề mới. Đánh dấu chỗ ngắt bằng "/" khi luyện: <i>By default, / the server runs on port 8000.</i></li>
<li><b>Nhấn từ khóa</b> kỹ thuật và con số: <i>the server runs on port <b>EIGHT THOUSAND</b></i>.</li>
<li><b>Hạ giọng</b> ở cuối câu khẳng định — đừng lên giọng như câu hỏi.</li>
<li>Tốc độ mục tiêu: khoảng <b>130 từ/phút</b>, chậm hơn hội thoại một chút.</li>
</ul>

<h3>2. Đọc ký hiệu và code</h3>
<table class="table">
<tr><th>Viết</th><th>Đọc</th></tr>
<tr><td><code>python manage.py migrate</code></td><td>python, manage dot py, migrate</td></tr>
<tr><td><code>user.save()</code></td><td>user dot save, open/close parentheses (hoặc chỉ "user dot save")</td></tr>
<tr><td><code>models.CharField(max_length=100)</code></td><td>models dot CharField, max length equals one hundred</td></tr>
<tr><td><code>v4.2</code></td><td>version four point two</td></tr>
<tr><td><code>/api/v1/users/</code></td><td>slash API slash V one slash users</td></tr>
</table>

<h3>3. Ngôn ngữ đặc trưng của tài liệu</h3>
<table class="table">
<tr><th>Mẫu</th><th>Nghĩa</th></tr>
<tr><td><span class="say">By default, …</span></td><td>Theo mặc định…</td></tr>
<tr><td><span class="say">Make sure that… / Ensure that…</span></td><td>Đảm bảo rằng…</td></tr>
<tr><td><span class="say">Note that…</span></td><td>Lưu ý rằng…</td></tr>
<tr><td><span class="say">This is optional / required.</span></td><td>Tùy chọn / bắt buộc</td></tr>
<tr><td><span class="say">X is deprecated in favour of Y.</span></td><td>X lỗi thời, nên dùng Y</td></tr>
<tr><td><span class="say">For more details, refer to…</span></td><td>Xem thêm tại…</td></tr>
</table>
""",
    'listening': {
        'title': 'Docs: Defining your first model',
        'intro': 'Một đoạn tài liệu kiểu Django được đọc to, chậm và rõ. Đây là mẫu để bạn bắt chước khi đọc tài liệu.',
        'speakers': {'A': ('Narrator', 'sonia')},
        'lines': [
            ('A', "In this section, you will define your first model. A model is the single source of truth about your data.", 'Trong phần này, bạn sẽ định nghĩa model đầu tiên. Model là nguồn sự thật duy nhất về dữ liệu của bạn.'),
            ('A', "Each model is a Python class, and each attribute of the class represents a database field.", 'Mỗi model là một lớp Python, và mỗi thuộc tính của lớp đại diện cho một trường trong cơ sở dữ liệu.'),
            ('A', "Before you begin, make sure that you have completed the installation steps. The only prerequisite is a working project.", 'Trước khi bắt đầu, hãy đảm bảo bạn đã hoàn thành các bước cài đặt. Điều kiện tiên quyết duy nhất là một dự án chạy được.'),
            ('A', "Open the file called models dot py, and add a class named Question with two fields: the question text and the publication date.", 'Mở file models.py và thêm một lớp tên Question với hai trường: nội dung câu hỏi và ngày đăng.'),
            ('A', "The text field takes one required argument, max length, which limits the number of characters.", 'Trường văn bản nhận một đối số bắt buộc là max length, giới hạn số ký tự.'),
            ('A', "By default, every field is required. If a field is optional, set blank equals true.", 'Mặc định, mọi trường đều bắt buộc. Nếu một trường là tùy chọn, đặt blank bằng true.'),
            ('A', "Next, create a migration by running python manage dot py makemigrations. Then apply it with the migrate command.", 'Tiếp theo, tạo migration bằng cách chạy python manage.py makemigrations. Sau đó áp dụng nó bằng lệnh migrate.'),
            ('A', "Note that the migration only describes the changes. Your database is not updated until you run migrate.", 'Lưu ý rằng migration chỉ mô tả thay đổi. Cơ sở dữ liệu của bạn chưa được cập nhật cho đến khi bạn chạy migrate.'),
            ('A', "Each instance of the Question class is one row in the table. When you call the save method, the instance is written to the database.", 'Mỗi đối tượng của lớp Question là một hàng trong bảng. Khi bạn gọi phương thức save, đối tượng được ghi vào cơ sở dữ liệu.'),
            ('A', "For more details about field types, refer to the model field reference.", 'Để biết thêm về các loại trường, hãy tham khảo tài liệu tra cứu trường của model.'),
        ],
        'questions': [
            ('What does each attribute of a model class represent?', ['A database table', 'A database field', 'A migration', 'A URL'], 1, '"each attribute of the class represents a database field".'),
            ('What does "max length" do?', ['Sets the publication date', 'Limits the number of characters', 'Makes the field optional', 'Creates a migration'], 1, '"which limits the number of characters".'),
            ('How do you make a field optional?', ['Remove it', 'Set blank equals true', 'Set max length to zero', 'Run migrate'], 1, '"If a field is optional, set blank equals true."'),
            ('When is the database actually updated?', ['When you create the class', 'When you run makemigrations', 'When you run migrate', 'When you open models.py'], 2, '"Your database is not updated until you run migrate."'),
        ],
    },
    'speaking': {
        'tips': ['Shadow từng câu bài nghe ở tốc độ Chậm, rồi Bình thường.', 'Sau đó tự đọc to bài đọc bên dưới (phần Đọc) và ghi âm 2 phút.', 'Kiểm tra: có ngắt đúng chỗ không? Có lên giọng sai ở cuối câu không?'],
        'prompts': [
            ('Shadow the documentation excerpt sentence by sentence.', 'Dùng trình phát ở phần Nghe với chế độ chậm.'),
            ('Read the "Path parameters" text in the Reading section aloud and record it.', 'Mục tiêu khoảng 130 từ/phút.'),
            ('Explain in your own words what a model and a migration are.', '2–3 câu đơn giản.'),
        ],
        'model': (
            "A model is a Python class that describes your data. Each attribute is a column in a database table. "
            "When you change a model, you create a migration, which is a file that describes the change. "
            "Then you run the migrate command, and the database is updated. "
            "By default, every field is required, but you can make a field optional.",
            'Model là một lớp Python mô tả dữ liệu của bạn. Mỗi thuộc tính là một cột trong bảng cơ sở dữ liệu. '
            'Khi bạn thay đổi model, bạn tạo một migration, là file mô tả thay đổi đó. '
            'Sau đó bạn chạy lệnh migrate và cơ sở dữ liệu được cập nhật. '
            'Mặc định mọi trường đều bắt buộc, nhưng bạn có thể đặt một trường là tùy chọn.'
        ),
        'seconds': 120,
    },
    'reading': {
        'title': 'Docs: Path parameters',
        'text': [
            'You can declare path parameters with the same syntax used by Python format strings. For example, in the path slash items slash item ID, the value of item ID will be passed to your function as the argument item ID.',
            'You can also declare the type of a path parameter using standard Python type hints. If you declare item ID as an integer, the framework will automatically convert the value and validate it. Note that if the value is not a valid number, the client receives a clear error message instead of a server error.',
            'By default, all path parameters are required, because they are part of the URL. If you need an optional value, use a query parameter instead. For more details, refer to the section on query parameters.',
        ],
        'vi': 'Bạn khai báo tham số đường dẫn bằng cú pháp giống chuỗi định dạng Python; ví dụ trong /items/{item_id}, giá trị item_id được truyền vào hàm làm đối số. Bạn có thể khai báo kiểu bằng type hint; nếu khai báo là số nguyên, framework tự chuyển đổi và kiểm tra hợp lệ; giá trị sai sẽ trả lỗi rõ ràng thay vì lỗi server. Mặc định mọi tham số đường dẫn đều bắt buộc vì nằm trong URL; muốn giá trị tùy chọn thì dùng query parameter.',
        'questions': [
            ('How is the path parameter value passed to your function?', ['As a global variable', 'As an argument', 'In the request body', 'As a header'], 1, 'Đoạn 1.'),
            ('What happens if the value is not a valid number?', ['The server crashes.', 'The client gets a clear error message.', 'The value becomes zero.', 'Nothing happens.'], 1, 'Đoạn 2.'),
            ('What should you use for an optional value?', ['A path parameter', 'A query parameter', 'A type hint', 'A migration'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết một đoạn hướng dẫn ngắn (6–8 câu) kiểu tài liệu cho một tính năng/hàm trong dự án của bạn, dùng ít nhất 5 cụm: by default, make sure that, note that, optional, refer to, returns.',
        'tips': ['Giọng văn tài liệu: rõ ràng, câu mệnh lệnh, hiện tại đơn.'],
        'model': "The export command creates a CSV file of all orders in a given period. Before you run it, make sure that you have read access to the orders database. The command takes two parameters: the start date and the end date. The end date is optional; by default, it is today. The command returns the path of the new file. Note that large exports can take several minutes and may slow down the database, so avoid running them during peak hours. For more details about the file format, refer to the reporting guide.",
        'min_words': 70,
    },
    'quiz': [
        ('"___, the port is 8000." (theo mặc định)', ['By default', 'By the way', 'In default', 'For default'], 0, 'By default.'),
        ('A field that is not required is ___.', ['optional', 'deprecated', 'straightforward', 'prerequisite'], 0, 'optional.'),
        ('An old method that will be removed in the future is ___.', ['deprecated', 'overridden', 'optional', 'returned'], 0, 'deprecated.'),
        ('Something you need before you start is a ___.', ['prerequisite', 'parameter', 'attribute', 'instance'], 0, 'prerequisite.'),
        ('"___ that the API key is kept secret."', ['Ensure', 'Insure', 'Assure to', 'Sure'], 0, 'Ensure that…'),
        ('"For more details, ___ the user guide."', ['refer to', 'refer', 'reference at', 'look for to'], 0, 'refer to.'),
        ('Cách đọc "v4.2":', ['version four two', 'version four point two', 'v four dot two', 'version forty-two'], 1, 'four point two.'),
        ('Cách đọc "models.py":', ['models point py', 'models dot py', 'models period py', 'models full stop py'], 1, 'dot.'),
        ('One object created from a class is an ___.', ['instance', 'argument', 'attribute', 'override'], 0, 'instance.'),
        ('Khi đọc to tài liệu, câu khẳng định nên kết thúc bằng:', ['Lên giọng', 'Xuống giọng', 'Đọc nhanh hơn', 'Ngừng lâu'], 1, 'Xuống giọng ở cuối câu khẳng định.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 5',
    'title_en': 'Week 5 Review: Tech Vocabulary',
    'goal': 'Ôn toàn bộ từ vựng kỹ thuật của tuần qua 30 câu điền từ; học thêm các động từ mô tả công việc lập trình.',
    'tasks': [
        'Học 14 động từ dùng trong lập trình.',
        'Làm 30 câu điền từ (quiz cuối trang).',
        'Ôn lại toàn bộ thẻ từ của tuần (luyện từ của ngày và trang Ôn từ).',
        'Nghe đoạn mô tả công việc của một kỹ sư và ghi lại các động từ.',
    ],
    'product': 'Điểm quiz 30 câu',
    'warmup': [
        ('I implemented the search feature last week.', 'Tuần trước tôi đã triển khai tính năng tìm kiếm.'),
        ("Let's refactor this function before we add more code.", 'Hãy tái cấu trúc hàm này trước khi thêm code.'),
        ('We need to validate the user input.', 'Chúng ta cần kiểm tra dữ liệu người dùng nhập.'),
        ('The app fetches data from the API every minute.', 'Ứng dụng lấy dữ liệu từ API mỗi phút.'),
        ('I spent the morning debugging a weird issue.', 'Tôi mất cả buổi sáng gỡ một lỗi kỳ lạ.'),
        ('We optimized the query and it is ten times faster.', 'Chúng tôi tối ưu truy vấn và nó nhanh gấp mười lần.'),
    ],
    'vocab': [
        ('implement', '/ˈɪmplɪment/', 'verb', 'triển khai, hiện thực hóa', 'We implemented single sign-on last sprint.', 'Sprint trước chúng tôi triển khai đăng nhập một lần.'),
        ('refactor', '/ˌriːˈfæktə/', 'verb', 'tái cấu trúc code', 'I refactored the module to make it easier to test.', 'Tôi tái cấu trúc module để dễ test hơn.'),
        ('optimize', '/ˈɒptɪmaɪz/', 'verb', 'tối ưu', 'We optimized the images to load faster.', 'Chúng tôi tối ưu ảnh để tải nhanh hơn.'),
        ('validate', '/ˈvælɪdeɪt/', 'verb', 'kiểm tra tính hợp lệ', 'Always validate data on the server.', 'Luôn kiểm tra dữ liệu hợp lệ ở phía server.'),
        ('fetch', '/fetʃ/', 'verb', 'lấy (dữ liệu)', 'The page fetches the latest prices on load.', 'Trang lấy giá mới nhất khi tải.'),
        ('parse', '/pɑːz/', 'verb', 'phân tích cú pháp, đọc dữ liệu', 'The script parses the CSV file line by line.', 'Script đọc file CSV từng dòng.'),
        ('expose', '/ɪkˈspəʊz/', 'verb', 'cung cấp ra ngoài (qua API)', 'The service exposes three endpoints.', 'Dịch vụ cung cấp ba endpoint.'),
        ('configure', '/kənˈfɪɡə/', 'verb', 'cấu hình', 'You can configure the timeout in the settings file.', 'Bạn có thể cấu hình thời gian chờ trong file settings.'),
        ('debug', '/diːˈbʌɡ/', 'verb', 'gỡ lỗi', 'It took two days to debug the memory leak.', 'Mất hai ngày để gỡ lỗi rò rỉ bộ nhớ.'),
        ('benchmark', '/ˈbentʃmɑːk/', 'verb / n', 'đo hiệu năng; bài đo', 'We benchmarked both libraries before choosing.', 'Chúng tôi đo hiệu năng cả hai thư viện trước khi chọn.'),
        ('enforce', '/ɪnˈfɔːs/', 'verb', 'bắt buộc áp dụng', 'The linter enforces our coding style.', 'Linter bắt buộc áp dụng quy tắc code của chúng tôi.'),
        ('sanitize', '/ˈsænɪtaɪz/', 'verb', 'làm sạch (dữ liệu đầu vào)', 'Sanitize user input to prevent attacks.', 'Làm sạch dữ liệu người dùng để ngăn tấn công.'),
        ('throttle', '/ˈθrɒtl/', 'verb', 'giới hạn tốc độ', 'The API throttles clients that send too many requests.', 'API giới hạn tốc độ các client gửi quá nhiều request.'),
        ('provision', '/prəˈvɪʒn/', 'verb', 'cấp phát (tài nguyên máy chủ)', 'The script provisions a new server in two minutes.', 'Script cấp phát một server mới trong hai phút.'),
    ],
    'lesson': """
<h3>1. Động từ mô tả việc lập trình</h3>
<table class="table">
<tr><th>Động từ</th><th>Collocation hay gặp</th></tr>
<tr><td>implement</td><td><span class="say">implement a feature / a solution / an algorithm</span></td></tr>
<tr><td>refactor</td><td><span class="say">refactor the code / a module / legacy code</span></td></tr>
<tr><td>optimize</td><td><span class="say">optimize a query / performance / images</span></td></tr>
<tr><td>validate</td><td><span class="say">validate input / a form / a token</span></td></tr>
<tr><td>fetch</td><td><span class="say">fetch data / results / the latest version</span></td></tr>
<tr><td>configure</td><td><span class="say">configure a server / the settings / a timeout</span></td></tr>
<tr><td>debug</td><td><span class="say">debug an issue / a crash / a memory leak</span></td></tr>
</table>

<h3>2. Ôn nhanh từ vựng tuần 5</h3>
<table class="table">
<tr><th>Ngày</th><th>Từ trọng tâm</th></tr>
<tr><td>Backend</td><td>endpoint, latency, throughput, idempotent, migration, rollback, schema, cache, rate limit</td></tr>
<tr><td>Frontend &amp; DevOps</td><td>component, state, props, render, pipeline, container, uptime, hotfix, staging, production</td></tr>
<tr><td>Quản lý dự án</td><td>sprint, backlog, scope creep, blocker, stakeholder, roadmap, estimate, MVP</td></tr>
<tr><td>Collocations</td><td>make a decision, fix a bug, raise a concern, meet a deadline, take ownership</td></tr>
<tr><td>Tài liệu</td><td>by default, ensure, optional, deprecated, parameter, refer to</td></tr>
</table>
<div class="note"><b>Ôn thẻ:</b> Mở <a href="/on-tap/">Ôn từ</a> để lật lại các thẻ đến hạn. Ngày mai (Chủ nhật) dùng trang ôn tập tuần 5 để luyện thêm.</div>

<h3>3. Mô tả công việc bằng động từ mạnh</h3>
<div class="fix"><s>I did the search function.</s><span class="en">I implemented the search feature.</span></div>
<div class="fix"><s>I made the code better.</s><span class="en">I refactored the code to make it easier to test.</span></div>
<div class="fix"><s>I made the page faster.</s><span class="en">I optimized the page and reduced load time by 40%.</span></div>
""",
    'listening': {
        'title': 'What does a backend engineer do all day?',
        'intro': 'Một kỹ sư kể về một ngày làm việc. Ghi lại các động từ kỹ thuật bạn nghe được.',
        'speakers': {'A': ('Interviewer', 'jenny'), 'B': ('Quang', 'andrew')},
        'lines': [
            ('A', "Quang, what did you actually do yesterday at work?", 'Quang, hôm qua anh thực sự làm gì ở chỗ làm?'),
            ('B', "In the morning, I debugged a strange issue. Some users were logged out every few minutes.", 'Buổi sáng tôi gỡ một lỗi lạ. Một số người dùng bị đăng xuất mỗi vài phút.'),
            ('A', 'What was the cause?', 'Nguyên nhân là gì?'),
            ('B', "We had configured the session timeout incorrectly on one of the servers. A one-line fix, but it took three hours to find.", 'Chúng tôi cấu hình sai thời gian hết phiên trên một server. Sửa một dòng thôi, nhưng mất ba tiếng để tìm.'),
            ('A', "Classic. And after that?", 'Kinh điển. Sau đó thì sao?'),
            ('B', "I worked on a new feature. Our service exposes an endpoint for partners, and I implemented validation for their requests.", 'Tôi làm tính năng mới. Dịch vụ của chúng tôi cung cấp một endpoint cho đối tác, và tôi triển khai phần kiểm tra hợp lệ cho request của họ.'),
            ('B', "We also sanitize everything they send, because we can't trust external data.", 'Chúng tôi còn làm sạch mọi thứ họ gửi, vì không thể tin dữ liệu bên ngoài.'),
            ('A', "Makes sense. Anything else?", 'Hợp lý. Còn gì nữa không?'),
            ('B', "In the afternoon, I refactored an old module that parses CSV files. Then I benchmarked it: it's now four times faster.", 'Buổi chiều tôi tái cấu trúc một module cũ đọc file CSV. Sau đó tôi đo hiệu năng: giờ nó nhanh gấp bốn lần.'),
            ('A', "Impressive. Do you ever write code that isn't about fixing or improving things?", 'Ấn tượng. Anh có bao giờ viết code không phải để sửa hay cải thiện không?'),
            ('B', "Ha, not often! Most of the job is reading, debugging and optimizing. Writing brand-new code is maybe twenty percent.", 'Ha, không thường xuyên! Phần lớn công việc là đọc, gỡ lỗi và tối ưu. Viết code mới toanh có lẽ chỉ hai mươi phần trăm.'),
        ],
        'questions': [
            ('What problem did Quang debug in the morning?', ['Slow pages', 'Users being logged out every few minutes', 'A broken pipeline', 'Missing emails'], 1, '"Some users were logged out every few minutes."'),
            ('What was the cause?', ['A wrongly configured session timeout', 'A database crash', 'A partner attack', 'A frontend bug'], 0, '"We had configured the session timeout incorrectly".'),
            ('Why do they sanitize partner data?', ['It is too large.', 'They can\'t trust external data.', 'Partners asked them to.', 'To make it faster.'], 1, '"we can\'t trust external data".'),
            ('How much faster is the refactored CSV module?', ['Twice as fast', 'Three times', 'Four times', 'Ten times'], 2, '"it\'s now four times faster".'),
            ('How much of Quang\'s job is writing brand-new code?', ['About 20%', 'About 50%', 'About 80%', 'All of it'], 0, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Kể lại ngày làm việc gần nhất của bạn bằng ít nhất 6 động từ hôm nay.', 'Thêm một con số kết quả.'],
        'prompts': [
            ('Describe what you did yesterday at work, using technical verbs.', 'debug, implement, refactor, optimize, configure…'),
            ('Explain the most important new words of this week to a junior developer.', 'Chọn 5 từ, giải thích đơn giản.'),
        ],
        'model': (
            "Yesterday was a typical day. In the morning, I implemented a small feature that lets users export their invoices as PDF files. "
            "Before lunch, a colleague asked me to help debug a crash in the mobile app. It turned out we weren't validating an empty field. "
            "In the afternoon, I refactored the invoice service, because the code was very hard to test. "
            "I also optimized one slow query, and the invoice page now loads in under a second. "
            "Finally, I configured a new alert in our monitoring tool so we'll know if the PDF service fails.",
            'Hôm qua là một ngày điển hình. Buổi sáng tôi triển khai một tính năng nhỏ cho phép người dùng xuất hóa đơn thành PDF. '
            'Trước bữa trưa, một đồng nghiệp nhờ tôi gỡ lỗi treo ứng dụng di động. Hóa ra chúng tôi không kiểm tra một trường rỗng. '
            'Buổi chiều tôi tái cấu trúc dịch vụ hóa đơn vì code rất khó test. '
            'Tôi cũng tối ưu một truy vấn chậm, và trang hóa đơn giờ tải dưới một giây. '
            'Cuối cùng, tôi cấu hình một cảnh báo mới trong công cụ giám sát để biết nếu dịch vụ PDF lỗi.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Strong verbs for your CV',
        'text': [
            'Recruiters read CVs quickly, and weak verbs make your experience sound smaller than it is. Phrases like "worked on", "did" or "was responsible for" tell the reader very little.',
            'Strong verbs describe exactly what you did: designed, implemented, migrated, optimized, automated, led. Compare "worked on the payment system" with "migrated the payment system to a new provider with zero downtime". The second version is longer, but every word adds information.',
            'Add numbers whenever you can. "Optimized database queries" is good. "Optimized database queries, reducing average page load time from 3 seconds to 0.8 seconds" is much better, because it shows the impact of your work.',
        ],
        'vi': 'Nhà tuyển dụng đọc CV nhanh, và động từ yếu (worked on, did, was responsible for) khiến kinh nghiệm của bạn có vẻ nhỏ hơn thực tế. Động từ mạnh mô tả chính xác việc bạn làm: designed, implemented, migrated, optimized, automated, led. Hãy thêm con số bất cứ khi nào có thể để thể hiện tác động.',
        'questions': [
            ('Why are weak verbs a problem on a CV?', ['They are grammatically wrong.', 'They tell the reader very little.', 'They are too long.', 'Recruiters don\'t read verbs.'], 1, 'Đoạn 1.'),
            ('Which is a strong verb?', ['did', 'worked on', 'migrated', 'was responsible for'], 2, 'Đoạn 2.'),
            ('What makes a CV sentence "much better", according to the text?', ['Using more adjectives', 'Adding numbers that show impact', 'Making it shorter', 'Using passive voice'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết lại 5 dòng kinh nghiệm cho CV của bạn bằng động từ mạnh + con số. Ví dụ: "Optimized… reducing… from… to…".',
        'tips': ['Bắt đầu mỗi dòng bằng động từ quá khứ.', 'Mỗi dòng có một con số.'],
        'model': "• Implemented a booking API used by 40 partner hotels.\n• Refactored the legacy reporting module, cutting test time from 20 to 5 minutes.\n• Optimized product search queries, reducing average latency from 900 ms to 150 ms.\n• Configured CI/CD pipelines for 6 services, enabling daily releases.\n• Debugged and fixed a memory leak that caused weekly server restarts.",
        'min_words': 50,
    },
    'quiz': [
        ('A specific API URL such as /orders is an ___.', ['endpoint', 'environment', 'element', 'event'], 0, 'endpoint.'),
        ('Our ___ is 200 ms per request. (độ trễ)', ['latency', 'throughput', 'uptime', 'backlog'], 0, 'latency.'),
        ('A payment request that is safe to send twice is ___.', ['idempotent', 'deprecated', 'optional', 'responsive'], 0, 'idempotent.'),
        ('We need a ___ to add a new column.', ['migration', 'rollback', 'hotfix', 'kickoff'], 0, 'migration.'),
        ('The release failed, so we did a ___.', ['rollback', 'roadmap', 'retrospective', 'payload'], 0, 'rollback.'),
        ('Status 429 means you hit the ___.', ['rate limit', 'deadline', 'cache', 'schema'], 0, 'rate limit.'),
        ('A reusable piece of UI is a ___.', ['component', 'container', 'constraint', 'commit'], 0, 'component.'),
        ('The site was down. It was a lot of ___.', ['downtime', 'uptime', 'overtime', 'runtime'], 0, 'downtime.'),
        ('We released an urgent ___ at midnight.', ['hotfix', 'roadmap', 'sprint', 'schema'], 0, 'hotfix.'),
        ('Always test on ___ before production.', ['staging', 'stage', 'stating', 'storage'], 0, 'staging.'),
        ('The CI ___ runs build, test and deploy.', ['pipeline', 'pipe', 'line', 'process'], 0, 'pipeline.'),
        ('Our sprint ___ has 200 tickets waiting.', ['backlog', 'blocker', 'stakeholder', 'kickoff'], 0, 'backlog.'),
        ('New requests keep coming in. That is ___.', ['scope creep', 'blocker', 'payload', 'roadmap'], 0, 'scope creep.'),
        ('"Any ___?" — "Yes, I need access to the server."', ['blockers', 'estimates', 'roadmaps', 'components'], 0, 'blockers.'),
        ('The marketing director is an important ___.', ['stakeholder', 'deliverable', 'endpoint', 'sprint'], 0, 'stakeholder.'),
        ('We need to ___ a decision today.', ['make', 'do', 'take', 'run'], 0, 'make a decision.'),
        ("I'd like to ___ a concern about security.", ['raise', 'rise', 'arise', 'say'], 0, 'raise a concern.'),
        ('We worked late to ___ the deadline.', ['meet', 'catch', 'hit up', 'touch'], 0, 'meet a deadline.'),
        ('Lan will ___ ownership of the project.', ['take', 'make', 'do', 'run'], 0, 'take ownership.'),
        ('Please ___ a ticket for that bug.', ['file', 'fill', 'fall', 'feel'], 0, 'file a ticket.'),
        ('"___, all fields are required." (mặc định)', ['By default', 'In default', 'At default', 'On default'], 0, 'By default.'),
        ('This parameter is ___; you can leave it empty.', ['optional', 'required', 'deprecated', 'mandatory'], 0, 'optional.'),
        ('This method is ___ and will be removed soon.', ['deprecated', 'depreciated', 'decorated', 'dedicated'], 0, 'deprecated.'),
        ('I ___ the old code to make it easier to read.', ['refactored', 'reacted', 'refused', 'reflected'], 0, 'refactored.'),
        ('Always ___ user input on the server.', ['validate', 'vacate', 'value', 'vary'], 0, 'validate.'),
        ('The app ___ new data from the API every minute.', ['fetches', 'catches', 'matches', 'fits'], 0, 'fetches.'),
        ('I spent hours trying to ___ the crash.', ['debug', 'debut', 'decode up', 'delay'], 0, 'debug.'),
        ('We ___ the query and it is now 10x faster.', ['optimized', 'optioned', 'opted', 'operated'], 0, 'optimized.'),
        ('The service ___ three endpoints for partners.', ['exposes', 'explodes', 'exports up', 'expands'], 0, 'exposes.'),
        ('The script ___ the JSON file and saves the data.', ['parses', 'passes', 'pauses', 'paces'], 0, 'parses.'),
    ],
}

WEEK = {
    'title': 'Từ vựng công nghệ và shadowing',
    'title_en': 'Tech Vocabulary & Shadowing',
    'goal': 'Nắm vốn từ chuyên ngành IT, dùng đúng collocations và đọc tài liệu kỹ thuật tự nhiên.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
