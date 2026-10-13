"""Tuần 8 — Đọc tài liệu và nghe podcast kỹ thuật."""

DAY1 = {
    'title': 'Đọc tài liệu Django',
    'title_en': 'Reading the Django Docs: Views and URLs',
    'goal': 'Đọc hiểu một mục hướng dẫn kiểu tài liệu Django chính thức và tóm tắt lại bằng tiếng Anh trong 5 câu.',
    'tasks': [
        'Học 14 thuật ngữ trong tài liệu Django.',
        'Đọc bài "Writing your first view" 2 lần: lần 1 lướt tìm ý chính, lần 2 đọc kỹ.',
        'Trả lời câu hỏi đọc hiểu.',
        'Nghe hai dev bàn về ORM và queryset.',
        'Viết tóm tắt 5 câu bằng tiếng Anh.',
    ],
    'product': 'Bản tóm tắt 5 câu',
    'warmup': [
        ('A view is a Python function that takes a request and returns a response.', 'View là một hàm Python nhận request và trả về response.'),
        ('Each URL pattern maps a path to a view.', 'Mỗi URL pattern ánh xạ một đường dẫn tới một view.'),
        ('Querysets are lazy.', 'Queryset có tính "lười" (chỉ chạy khi cần).'),
        ('The template receives a context dictionary.', 'Template nhận một dictionary ngữ cảnh.'),
        ('Middleware runs before and after every view.', 'Middleware chạy trước và sau mỗi view.'),
        ('Use the shortcut to keep your code short.', 'Dùng hàm tắt để code ngắn gọn.'),
    ],
    'vocab': [
        ('view', '/vjuː/', 'n', 'hàm xử lý request (trong Django)', 'This view returns a list of articles.', 'View này trả về danh sách bài viết.'),
        ('URLconf', '/ˌjuː ɑːr el ˈkɒnf/', 'n', 'cấu hình URL (urls.py)', 'Add the new path to your URLconf.', 'Thêm đường dẫn mới vào URLconf.'),
        ('route', '/ruːt/', 'n / verb', 'tuyến đường; định tuyến', 'The router sends each request to the right route.', 'Bộ định tuyến gửi mỗi request đến đúng tuyến.'),
        ('template', '/ˈtemplət/', 'n', 'khuôn mẫu (HTML)', 'The template uses double curly braces for variables.', 'Template dùng hai dấu ngoặc nhọn cho biến.'),
        ('context', '/ˈkɒntekst/', 'n', 'ngữ cảnh (dữ liệu truyền vào template)', 'Pass the user list to the template in the context.', 'Truyền danh sách người dùng vào template qua context.'),
        ('shortcut', '/ˈʃɔːtkʌt/', 'n', 'hàm tắt, lối tắt', 'The render shortcut saves several lines of code.', 'Hàm tắt render tiết kiệm vài dòng code.'),
        ('middleware', '/ˈmɪdlweə/', 'n', 'phần mềm trung gian', 'The security middleware adds headers to every response.', 'Middleware bảo mật thêm header vào mọi response.'),
        ('ORM', '/ˌəʊ ɑːr ˈem/', 'n', 'ánh xạ đối tượng – quan hệ', 'The ORM turns Python code into SQL.', 'ORM chuyển code Python thành SQL.'),
        ('queryset', '/ˈkwɪərɪset/', 'n', 'tập kết quả truy vấn (Django)', 'This queryset returns all published posts.', 'Queryset này trả về mọi bài đã đăng.'),
        ('lazy', '/ˈleɪzi/', 'adj', '(tính toán) trì hoãn đến khi cần', 'Querysets are lazy; the database is not hit until you use them.', 'Queryset là lười; cơ sở dữ liệu không bị truy vấn cho đến khi bạn dùng chúng.'),
        ('filter', '/ˈfɪltə/', 'verb', 'lọc', 'Filter the orders by status.', 'Lọc đơn hàng theo trạng thái.'),
        ('primary key', '/ˈpraɪməri kiː/', 'n', 'khóa chính', 'Every model has a primary key called id.', 'Mỗi model có một khóa chính tên id.'),
        ('foreign key', '/ˈfɒrən kiː/', 'n', 'khóa ngoại', 'An order has a foreign key to a customer.', 'Một đơn hàng có khóa ngoại tới khách hàng.'),
        ('decorator', '/ˈdekəreɪtə/', 'n', 'decorator (hàm bọc)', 'Use the login_required decorator to protect a view.', 'Dùng decorator login_required để bảo vệ view.'),
    ],
    'lesson': """
<h3>1. Đọc tài liệu kỹ thuật: 2 lượt</h3>
<table class="table">
<tr><th>Lượt</th><th>Cách đọc</th><th>Mục tiêu</th></tr>
<tr><td>1. Lướt (skim)</td><td>Chỉ đọc tiêu đề, câu đầu mỗi đoạn, code mẫu</td><td>Bài này dạy gì? Có những bước nào?</td></tr>
<tr><td>2. Đọc kỹ (scan + read)</td><td>Đọc từng đoạn, chạy thử code nếu được</td><td>Hiểu vì sao, lưu ý gì</td></tr>
</table>
<div class="note"><b>Mẹo:</b> Câu đầu mỗi đoạn trong tài liệu tốt thường là "câu chủ đề". Chỉ cần đọc các câu đầu, bạn đã nắm 70% bài.</div>

<h3>2. Tín hiệu quan trọng trong tài liệu</h3>
<table class="table">
<tr><th>Tín hiệu</th><th>Ý nghĩa</th></tr>
<tr><td><b>Note</b> / <b>Warning</b> / <b>Important</b></td><td>Đọc kỹ — thường là lỗi hay gặp</td></tr>
<tr><td><span class="say">In other words, …</span></td><td>Giải thích lại đơn giản hơn</td></tr>
<tr><td><span class="say">Under the hood, …</span></td><td>Cơ chế bên trong (có thể đọc lướt lần đầu)</td></tr>
<tr><td><span class="say">For example, …</span></td><td>Code mẫu — đọc kỹ</td></tr>
<tr><td><span class="say">See also / Refer to …</span></td><td>Tài liệu liên quan</td></tr>
</table>

<h3>3. Viết tóm tắt 5 câu</h3>
<ol>
<li><b>Chủ đề:</b> <span class="say">This section explains how to write views and connect them to URLs.</span></li>
<li><b>Khái niệm 1:</b> <span class="say">A view is a function that takes a request and returns a response.</span></li>
<li><b>Khái niệm 2:</b> <span class="say">URL patterns in the URLconf map paths to views.</span></li>
<li><b>Lưu ý:</b> <span class="say">The docs recommend using the render shortcut and templates instead of writing HTML in Python.</span></li>
<li><b>Kết:</b> <span class="say">In short, views connect the request, the data and the template.</span></li>
</ol>
""",
    'listening': {
        'title': 'Lazy querysets',
        'intro': 'Một dev senior giải thích cho dev mới vì sao trang của cô ấy chạy chậm.',
        'speakers': {'A': ('Victor', 'andrew'), 'B': ('Lan', 'emma')},
        'lines': [
            ('B', "Victor, my article page is really slow, and I don't understand why. It only shows twenty articles.", 'Victor, trang bài viết của em chậm lắm, mà em không hiểu vì sao. Nó chỉ hiển thị hai mươi bài.'),
            ('A', "Let's look. In the template, you show the author's name for each article, right?", 'Cùng xem. Trong template, em hiển thị tên tác giả cho mỗi bài phải không?'),
            ('B', "Yes. Article dot author dot name.", 'Vâng. article.author.name.'),
            ('A', "That's the problem. Author is a foreign key. Every time you access it, the ORM runs a new query. So you have one query for the articles, and then twenty more for the authors.", 'Đó là vấn đề. Author là khóa ngoại. Mỗi lần em truy cập nó, ORM chạy một truy vấn mới. Nên em có một truy vấn cho bài viết, rồi thêm hai mươi cái cho tác giả.'),
            ('B', "Twenty-one queries for one page? I had no idea.", 'Hai mươi mốt truy vấn cho một trang? Em không hề biết.'),
            ('A', "It's very common. The fix is easy: add select related to your queryset. Then Django gets the articles and the authors in one query with a join.", 'Rất phổ biến. Cách sửa dễ thôi: thêm select_related vào queryset. Khi đó Django lấy bài viết và tác giả trong một truy vấn có join.'),
            ('B', "And why didn't I see any queries when I created the queryset in the view?", 'Thế sao em không thấy truy vấn nào khi tạo queryset trong view?'),
            ('A', "Because querysets are lazy. Creating one doesn't touch the database. The query only runs when you actually use the data, for example when the template loops over it.", 'Vì queryset là lười. Tạo nó không chạm đến cơ sở dữ liệu. Truy vấn chỉ chạy khi em thực sự dùng dữ liệu, ví dụ khi template lặp qua nó.'),
            ('B', "That makes sense. Is there a way to see how many queries a page runs?", 'Hợp lý ạ. Có cách nào xem một trang chạy bao nhiêu truy vấn không?'),
            ('A', "Yes, install the debug toolbar. It shows every query. I'll send you the link to the docs.", 'Có, cài debug toolbar. Nó hiển thị mọi truy vấn. Anh sẽ gửi em link tài liệu.'),
        ],
        'questions': [
            ('Why is Lan\'s page slow?', ['The server is old.', 'It runs a new query for each author.', 'The template is too big.', 'There are too many articles.'], 1, '"Every time you access it, the ORM runs a new query."'),
            ('How many queries does the page run?', ['One', 'Two', 'Twenty', 'Twenty-one'], 3, '"Twenty-one queries for one page?"'),
            ('What is the fix?', ['Add more servers', 'Add select_related to the queryset', 'Remove the authors', 'Use raw SQL'], 1, '"add select related to your queryset".'),
            ('Why are querysets called "lazy"?', ['They are slow.', 'The query only runs when the data is used.', 'They are not finished.', 'They use less memory.'], 1, '"The query only runs when you actually use the data".'),
        ],
    },
    'speaking': {
        'tips': ['Tóm tắt bài đọc bằng lời trong 1 phút, không nhìn bài.', 'Giải thích "lazy queryset" cho một người mới học.'],
        'prompts': [
            ('Summarise the reading "Writing your first view" in one minute.', 'This section explains… A view is… URL patterns…'),
            ('Explain what "lazy" means for querysets and why it matters.', 'Dùng ví dụ trang bài viết.'),
        ],
        'model': (
            "The section explains how to write your first view and connect it to a URL. "
            "A view is just a Python function that takes a request and returns a response. "
            "To make the view reachable, you add a URL pattern to the URLconf, which maps a path to the view. "
            "Instead of writing HTML in Python, you use a template and pass data to it in a context dictionary. The render shortcut does all of this in one line. "
            "One important thing is that querysets are lazy, so the database is only queried when the template actually uses the data.",
            'Phần này giải thích cách viết view đầu tiên và kết nối nó với một URL. '
            'View chỉ là một hàm Python nhận request và trả về response. '
            'Để truy cập được view, bạn thêm một URL pattern vào URLconf, ánh xạ đường dẫn tới view. '
            'Thay vì viết HTML trong Python, bạn dùng template và truyền dữ liệu qua dictionary context. Hàm tắt render làm tất cả trong một dòng. '
            'Một điều quan trọng là queryset có tính lười, nên cơ sở dữ liệu chỉ bị truy vấn khi template thực sự dùng dữ liệu.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Docs: Writing your first view',
        'text': [
            'A view is the part of your application that decides what happens when someone visits a page. In Django, a view is simply a Python function that takes a web request and returns a web response. The response can be the HTML of a page, a redirect, a 404 error, a JSON document or anything else.',
            'Let\'s write the simplest possible view. Open the file views.py and add a function called index that returns an HttpResponse with the text "Hello, world." This view is complete, but nobody can reach it yet. To call the view, we need to map it to a URL.',
            'To do this, create a file called urls.py in your app directory. This file is called a URLconf. Each entry is a URL pattern that connects a path, such as "articles/", to a view. When a request arrives, Django checks the patterns in order and calls the first view that matches. Note that the order matters: if two patterns could match the same path, the first one wins.',
            'In a real application, you rarely write HTML inside a view. Instead, you create a template and pass data to it. The data is sent as a dictionary called the context. Because this pattern is so common, Django provides a shortcut called render, which loads the template, fills it with the context and returns the response in a single line.',
            'Finally, remember that most views read data from the database through the ORM. Querysets are lazy: creating a queryset does not run any SQL. The query runs only when the data is needed, for example when the template loops over the results. For more details, refer to the section on making queries.',
        ],
        'vi': 'View quyết định điều gì xảy ra khi ai đó truy cập một trang; trong Django, view là hàm Python nhận request và trả về response (HTML, chuyển hướng, lỗi 404, JSON…). Viết view đơn giản nhất trong views.py; để truy cập được cần ánh xạ nó tới URL trong urls.py (URLconf). Django kiểm tra các pattern theo thứ tự và gọi view khớp đầu tiên — thứ tự quan trọng. Thực tế hiếm khi viết HTML trong view; dùng template và truyền dữ liệu qua context; hàm tắt render làm việc này trong một dòng. Cuối cùng, queryset có tính lười: chỉ chạy SQL khi dữ liệu được dùng.',
        'questions': [
            ('What is a view in Django?', ['An HTML file', 'A Python function that takes a request and returns a response', 'A database table', 'A URL'], 1, 'Đoạn 1.'),
            ('What is a URLconf?', ['A template', 'A file that maps URL patterns to views', 'A database setting', 'A type of response'], 1, 'Đoạn 3.'),
            ('If two patterns match the same path, which one is used?', ['The last one', 'The first one', 'Both', 'Neither'], 1, '"the first one wins".'),
            ('What does the render shortcut do?', ['Runs SQL', 'Loads the template, fills it with context and returns the response', 'Creates URLs', 'Deletes old views'], 1, 'Đoạn 4.'),
            ('When does a queryset run its SQL query?', ['When it is created', 'When the data is needed', 'Every minute', 'Never'], 1, 'Đoạn 5.'),
        ],
    },
    'writing': {
        'task': 'Viết bản tóm tắt bài đọc trong đúng 5 câu bằng tiếng Anh (chủ đề – khái niệm 1 – khái niệm 2 – lưu ý – kết).',
        'tips': ['Không chép nguyên câu của bài; diễn đạt bằng lời của bạn.', 'Mỗi câu ≤ 25 từ.'],
        'model': "This section explains how to create a view in Django and connect it to a URL. A view is a Python function that receives a request and returns a response, such as an HTML page or JSON. To make a view reachable, you add a URL pattern to the URLconf, and Django uses the first pattern that matches. Instead of writing HTML in Python, you should use a template and the render shortcut, which passes data through a context dictionary. Finally, querysets are lazy, so the database is only queried when the data is actually used.",
        'min_words': 70,
    },
    'quiz': [
        ('In Django, a function that takes a request and returns a response is a ___.', ['view', 'model', 'template', 'route'], 0, 'view.'),
        ('The file that maps URLs to views is the ___.', ['URLconf', 'settings', 'template', 'queryset'], 0, 'URLconf.'),
        ('Data passed to a template is called the ___.', ['context', 'content', 'contact', 'contract'], 0, 'context.'),
        ('Querysets are ___: no SQL runs until you need the data.', ['lazy', 'busy', 'eager', 'slow'], 0, 'lazy.'),
        ('A field that links an order to a customer is a ___.', ['foreign key', 'primary key', 'route', 'decorator'], 0, 'foreign key.'),
        ('Code that runs before and after every view is ___.', ['middleware', 'template', 'queryset', 'shortcut'], 0, 'middleware.'),
        ('Khi lướt tài liệu (skim), bạn nên đọc:', ['Mọi từ', 'Tiêu đề, câu đầu mỗi đoạn và code mẫu', 'Chỉ phần cuối', 'Chỉ phần Note'], 1, 'Skim = đọc tiêu đề, câu chủ đề, code.'),
        ('One query for articles plus one query per author is called the ___ problem.', ['N+1', 'one-to-one', 'double', 'lazy'], 0, 'N+1 query problem.'),
        ('"___ the orders by status."', ['Filter', 'Filler', 'Fill', 'Field'], 0, 'filter.'),
        ('A Django ___ like login_required wraps a view.', ['decorator', 'director', 'decoder', 'designer'], 0, 'decorator.'),
    ],
}

DAY2 = {
    'title': 'Đọc tài liệu FastAPI',
    'title_en': 'Reading the FastAPI Docs: Dependency Injection',
    'goal': 'Đọc hiểu phần dependency injection kiểu tài liệu FastAPI, nắm ý chính và thêm 10+ thuật ngữ mới vào bộ thẻ.',
    'tasks': [
        'Học 14 thuật ngữ về dependency injection và async.',
        'Đọc bài "Dependencies" 2 lượt.',
        'Nghe hai dev tranh luận vì sao dependency injection hữu ích.',
        'Luyện thẻ từ (ít nhất 10 thẻ mới).',
        'Viết giải thích dependency injection bằng ví dụ đời thường.',
    ],
    'product': '10+ thẻ từ mới đã luyện; Đoạn giải thích dependency injection',
    'warmup': [
        ('A dependency is something your function needs to work.', 'Phụ thuộc là thứ hàm của bạn cần để hoạt động.'),
        ('FastAPI injects the database session for you.', 'FastAPI tự cung cấp phiên làm việc cơ sở dữ liệu cho bạn.'),
        ('Declare the dependency in the function signature.', 'Khai báo phụ thuộc trong chữ ký hàm.'),
        ('Type hints make validation automatic.', 'Type hint giúp kiểm tra hợp lệ tự động.'),
        ('In tests, you can replace it with a mock.', 'Trong test, bạn có thể thay nó bằng một bản giả.'),
        ('The code after yield runs when the request is finished.', 'Code sau yield chạy khi request kết thúc.'),
    ],
    'vocab': [
        ('dependency injection', '/dɪˈpendənsi ɪnˈdʒekʃn/', 'n', 'tiêm phụ thuộc', 'Dependency injection makes code easier to test.', 'Tiêm phụ thuộc giúp code dễ test hơn.'),
        ('inject', '/ɪnˈdʒekt/', 'verb', 'tiêm, cung cấp từ bên ngoài', 'The framework injects the current user into the endpoint.', 'Framework cung cấp người dùng hiện tại cho endpoint.'),
        ('declare', '/dɪˈkleə/', 'verb', 'khai báo', 'Declare the parameter as an integer.', 'Khai báo tham số là số nguyên.'),
        ('type hint', '/taɪp hɪnt/', 'n', 'gợi ý kiểu dữ liệu', 'Type hints help your editor catch mistakes.', 'Type hint giúp editor bắt lỗi.'),
        ('validation', '/ˌvælɪˈdeɪʃn/', 'n', 'sự kiểm tra hợp lệ', 'Validation errors return a 422 status code.', 'Lỗi kiểm tra hợp lệ trả về mã 422.'),
        ('async', '/ˈeɪsɪŋk/', 'adj', 'bất đồng bộ', 'Use async functions for slow network calls.', 'Dùng hàm bất đồng bộ cho các lời gọi mạng chậm.'),
        ('await', '/əˈweɪt/', 'verb', 'chờ (kết quả bất đồng bộ)', 'You must await the database call.', 'Bạn phải await lời gọi cơ sở dữ liệu.'),
        ('signature', '/ˈsɪɡnətʃə/', 'n', 'chữ ký hàm (tên + tham số)', 'Add the dependency to the function signature.', 'Thêm phụ thuộc vào chữ ký hàm.'),
        ('yield', '/jiːld/', 'verb', 'trả ra (tạm dừng hàm)', 'The dependency yields a session and closes it afterwards.', 'Phụ thuộc trả ra một phiên rồi đóng nó sau đó.'),
        ('resolve', '/rɪˈzɒlv/', 'verb', 'giải quyết, tính ra (giá trị)', 'FastAPI resolves all dependencies before calling your function.', 'FastAPI tính ra mọi phụ thuộc trước khi gọi hàm của bạn.'),
        ('reusable', '/ˌriːˈjuːzəbl/', 'adj', 'dùng lại được', 'Write the check once and make it reusable.', 'Viết kiểm tra một lần và làm cho nó dùng lại được.'),
        ('mock', '/mɒk/', 'n / verb', 'bản giả (dùng để test); giả lập', 'In tests, we mock the payment service.', 'Trong test, chúng tôi giả lập dịch vụ thanh toán.'),
        ('session', '/ˈseʃn/', 'n', 'phiên (kết nối cơ sở dữ liệu)', 'Each request gets its own database session.', 'Mỗi request có phiên cơ sở dữ liệu riêng.'),
        ('decouple', '/diːˈkʌpl/', 'verb', 'tách rời (giảm phụ thuộc)', 'Dependency injection decouples your logic from the database.', 'Tiêm phụ thuộc tách logic khỏi cơ sở dữ liệu.'),
    ],
    'lesson': """
<h3>1. Dependency injection — giải thích đời thường</h3>
<div class="ex"><span class="en">Imagine a chef in a restaurant. The chef doesn't go to the market every morning. Ingredients are delivered to the kitchen. The chef just says what they need.</span><span class="vi">Đầu bếp không tự đi chợ — nguyên liệu được giao tới. Đầu bếp chỉ cần nói mình cần gì. Hàm của bạn cũng vậy: nó chỉ khai báo cần gì (database, user), framework sẽ "giao" tới.</span></div>
<p>Lợi ích: khi test, bạn giao <b>nguyên liệu giả</b> (mock) thay vì nguyên liệu thật — không cần cơ sở dữ liệu thật hay tiền thật.</p>

<h3>2. Đọc câu dài trong tài liệu</h3>
<p>Tài liệu hay có câu dài với nhiều mệnh đề. Cách đọc: tìm <b>chủ ngữ + động từ chính</b> trước, bỏ qua phần phụ:</p>
<div class="ex"><span class="en">FastAPI, <i>which is built on top of Starlette and Pydantic,</i> <b>resolves</b> all the dependencies <i>that you declare in the function signature</i> before it calls your path operation.</span><span class="vi">Lõi câu: FastAPI resolves all the dependencies before it calls your path operation.</span></div>

<h3>3. Cụm từ đặc trưng của tài liệu FastAPI</h3>
<table class="table">
<tr><th>Cụm</th><th>Nghĩa</th></tr>
<tr><td><span class="say">path operation</span></td><td>hàm xử lý một đường dẫn + phương thức (GET /items)</td></tr>
<tr><td><span class="say">out of the box</span></td><td>có sẵn, không cần cấu hình</td></tr>
<tr><td><span class="say">under the hood</span></td><td>cơ chế bên trong</td></tr>
<tr><td><span class="say">behind the scenes</span></td><td>tự động phía sau</td></tr>
<tr><td><span class="say">you might be wondering…</span></td><td>tài liệu đoán trước câu hỏi của bạn</td></tr>
</table>
""",
    'listening': {
        'title': 'Why bother with dependency injection?',
        'intro': 'Một dev hoài nghi hỏi đồng nghiệp: dependency injection có thật sự cần không?',
        'speakers': {'A': ('Omar', 'guy'), 'B': ('Trang', 'ava')},
        'lines': [
            ('A', "Trang, honestly, why do we need all these dependencies in FastAPI? I could just open a database connection inside the function.", 'Trang, thật lòng, sao mình cần mấy cái dependency này trong FastAPI? Mình có thể mở kết nối cơ sở dữ liệu ngay trong hàm.'),
            ('B', "You could, but think about testing. If the connection is created inside the function, every test needs a real database.", 'Được chứ, nhưng nghĩ về việc test đi. Nếu kết nối được tạo trong hàm, mọi test đều cần cơ sở dữ liệu thật.'),
            ('A', "Okay, that's annoying, but we have a test database.", 'Ừ, phiền thật, nhưng mình có cơ sở dữ liệu test mà.'),
            ('B', "Sure. But what about the payment service? You don't want to charge a real credit card every time you run the tests.", 'Đúng. Nhưng còn dịch vụ thanh toán? Cậu không muốn trừ tiền thẻ thật mỗi lần chạy test chứ.'),
            ('A', "Ha, no. Definitely not.", 'Ha, không. Chắc chắn không.'),
            ('B', "With dependency injection, the endpoint just declares that it needs a payment client. In production, FastAPI injects the real one. In tests, we override it with a mock.", 'Với tiêm phụ thuộc, endpoint chỉ khai báo là nó cần một client thanh toán. Trên production, FastAPI cung cấp cái thật. Trong test, mình thay nó bằng bản giả.'),
            ('A', "So the code doesn't know or care where the client comes from.", 'Vậy code không biết và cũng không quan tâm client đến từ đâu.'),
            ('B', "Exactly. It's decoupled. And there's another benefit: reuse. We check the current user in thirty endpoints. We wrote that logic once, as a dependency.", 'Chính xác. Nó được tách rời. Và còn lợi ích khác: dùng lại. Mình kiểm tra người dùng hiện tại ở ba mươi endpoint. Mình viết logic đó đúng một lần, dưới dạng một dependency.'),
            ('A', "Fair point. And the database session? Who closes it?", 'Có lý. Còn phiên cơ sở dữ liệu? Ai đóng nó?'),
            ('B', "The dependency yields the session, and the code after yield closes it when the request is done, even if there's an error.", 'Dependency yield phiên, và code sau yield đóng nó khi request xong, kể cả khi có lỗi.'),
            ('A', "Okay, I'm convinced. I'll read the docs tonight.", 'Được rồi, mình bị thuyết phục rồi. Tối nay mình sẽ đọc tài liệu.'),
        ],
        'questions': [
            ('What is Trang\'s first argument for dependency injection?', ['It is faster.', 'Testing is easier.', 'It uses less memory.', 'It is required by Python.'], 1, '"think about testing".'),
            ('Why don\'t they want the real payment service in tests?', ['It is slow.', 'It would charge real credit cards.', 'It is broken.', 'It has no API.'], 1, '"You don\'t want to charge a real credit card".'),
            ('What does "decoupled" mean in this conversation?', ['The code doesn\'t care where the client comes from.', 'The code is deleted.', 'The code runs twice.', 'The code is in two files.'], 0, '"the code doesn\'t know or care where the client comes from".'),
            ('How many endpoints check the current user?', ['Three', 'Thirteen', 'Thirty', 'Three hundred'], 2, '"in thirty endpoints".'),
            ('When is the database session closed?', ['Never', 'After yield, when the request is done', 'Before the request', 'Every hour'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Giải thích dependency injection bằng ví dụ đời thường (đầu bếp, ổ cắm điện…).'],
        'prompts': [
            ('Explain dependency injection to a junior developer using an everyday example.', 'Imagine… / It\'s like…'),
            ('What are two benefits of dependency injection?', 'testing, reuse, decoupling'),
        ],
        'model': (
            "Think of dependency injection like a power socket. Your laptop doesn't build its own power plant. It just says, 'I need electricity', and you plug it into the wall. "
            "In code, a function says what it needs, like a database session or the current user, and the framework provides it. "
            "There are two big benefits. First, testing: you can plug in a fake version, a mock, instead of the real database or payment service. "
            "Second, reuse: you write the logic once, for example checking the user, and use it in many endpoints.",
            'Hãy nghĩ tiêm phụ thuộc như ổ cắm điện. Laptop của bạn không tự xây nhà máy điện. Nó chỉ nói "tôi cần điện" và bạn cắm nó vào tường. '
            'Trong code, một hàm nói nó cần gì, như phiên cơ sở dữ liệu hay người dùng hiện tại, và framework cung cấp. '
            'Có hai lợi ích lớn. Thứ nhất, test: bạn có thể cắm một phiên bản giả (mock) thay vì cơ sở dữ liệu hay dịch vụ thanh toán thật. '
            'Thứ hai, dùng lại: bạn viết logic một lần, ví dụ kiểm tra người dùng, và dùng ở nhiều endpoint.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Docs: Dependencies',
        'text': [
            'FastAPI has a very powerful but intuitive dependency injection system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with FastAPI.',
            '"Dependency injection" means, in programming, that there is a way for your code (in this case, your path operation functions) to declare the things that it requires to work and use: its "dependencies". Then, the system takes care of doing whatever is needed to provide your code with those dependencies.',
            'This is very useful when you need to have shared logic (the same code logic again and again), share database connections, enforce security, authentication and role requirements, and many other things. All of this while minimising code repetition.',
            'A dependency is just a function that can take the same parameters that a path operation function can take. You declare it in the parameters of your path operation using Depends. FastAPI will call the dependency with the correct parameters, get the result and assign it to the parameter in your function.',
            'You might be wondering how to clean up resources, such as closing a database session. For this, write a dependency that uses yield instead of return. The code before yield runs before your response is created, and the code after yield runs after the response has been sent.',
        ],
        'vi': 'FastAPI có hệ thống tiêm phụ thuộc mạnh mà trực quan. "Tiêm phụ thuộc" nghĩa là code của bạn khai báo những thứ nó cần ("dependencies"), và hệ thống lo việc cung cấp chúng. Rất hữu ích cho logic dùng chung, chia sẻ kết nối cơ sở dữ liệu, bảo mật, xác thực… mà giảm lặp code. Một dependency chỉ là một hàm nhận cùng loại tham số như path operation; khai báo bằng Depends. Muốn dọn dẹp tài nguyên (đóng phiên cơ sở dữ liệu), dùng yield thay vì return: code trước yield chạy trước khi tạo response, code sau yield chạy sau khi response đã gửi.',
        'questions': [
            ('What does "dependency injection" mean, according to the docs?', ['Copying code into every function', 'Code declares what it needs and the system provides it', 'Installing packages', 'Running code in parallel'], 1, 'Đoạn 2.'),
            ('Which use is NOT mentioned?', ['Shared logic', 'Sharing database connections', 'Enforcing security', 'Designing the user interface'], 3, 'Đoạn 3.'),
            ('How do you declare a dependency in a path operation?', ['With import', 'With Depends in the parameters', 'With a decorator only', 'In the URLconf'], 1, 'Đoạn 4.'),
            ('When does the code after yield run?', ['Before the request', 'After the response has been sent', 'Never', 'At server start'], 1, 'Đoạn 5.'),
        ],
    },
    'writing': {
        'task': 'Viết đoạn 5–7 câu giải thích dependency injection cho người mới, dùng một ví dụ đời thường và ít nhất 5 thuật ngữ hôm nay.',
        'tips': ['Câu 1: định nghĩa đơn giản. Câu 2–3: ví dụ. Câu 4–5: lợi ích. Câu cuối: tóm lại.'],
        'model': "Dependency injection is a way to give a function the things it needs, instead of letting the function create them itself. It's like a chef who receives ingredients from a supplier instead of going to the market every morning. In FastAPI, you declare a dependency in the function signature, and the framework resolves and injects it for you. This decouples your business logic from the database and other services. In tests, you can replace the real payment client with a mock, so no real money is involved. You can also write common logic, like checking the current user, once and reuse it in many endpoints. In short, dependency injection makes code cleaner, safer and easier to test.",
        'min_words': 80,
    },
    'quiz': [
        ('Giving a function what it needs from outside = dependency ___.', ['injection', 'infection', 'inspection', 'invention'], 0, 'dependency injection.'),
        ('In tests, we replace the real service with a ___.', ['mock', 'mark', 'mug', 'monk'], 0, 'mock.'),
        ('The function name plus its parameters is its ___.', ['signature', 'signal', 'sign-off', 'design'], 0, 'signature.'),
        ('"You must ___ the async database call."', ['await', 'awake', 'wait on', 'aware'], 0, 'await.'),
        ('Code that runs after ___ in a dependency is used to clean up.', ['yield', 'return', 'break', 'pass'], 0, 'yield.'),
        ('"Write the check once and make it ___."', ['reusable', 'refusable', 'reversible', 'removable'], 0, 'reusable.'),
        ('Separating logic from the database = to ___ them.', ['decouple', 'double', 'deploy', 'decode'], 0, 'decouple.'),
        ('A Python annotation like "item_id: int" is a ___.', ['type hint', 'type tip', 'type note', 'hint type'], 0, 'type hint.'),
        ('Lõi của câu "FastAPI, which is built on Starlette, resolves all dependencies before it calls your function" là:', ['FastAPI is built on Starlette', 'FastAPI resolves all dependencies', 'it calls your function', 'which is built'], 1, 'Chủ ngữ + động từ chính: FastAPI resolves…'),
        ('"Out of the box" nghĩa là:', ['Có sẵn, không cần cài thêm', 'Bị hỏng', 'Ngoài phạm vi', 'Mới mua'], 0, 'Có sẵn ngay.'),
    ],
}

DAY3 = {
    'title': 'Đọc tài liệu React',
    'title_en': 'Reading the React Docs: Hooks',
    'goal': 'Đọc hiểu phần hooks kiểu tài liệu React; tóm tắt cách useState và useEffect hoạt động trong 5 câu.',
    'tasks': [
        'Học 14 thuật ngữ về React hooks.',
        'Đọc bài "State and Effects" 2 lượt.',
        'Nghe một buổi pair programming sửa lỗi vòng lặp vô hạn.',
        'Viết tóm tắt 5 câu về useState và useEffect.',
    ],
    'product': 'Tóm tắt 5 câu về useState và useEffect',
    'warmup': [
        ('A hook lets a component use React features.', 'Hook cho phép component dùng các tính năng của React.'),
        ('useState returns the current value and a setter function.', 'useState trả về giá trị hiện tại và một hàm setter.'),
        ('Effects run after the component renders.', 'Effect chạy sau khi component hiển thị.'),
        ('The dependency array controls when the effect runs.', 'Mảng phụ thuộc điều khiển khi nào effect chạy.'),
        ('Return a cleanup function to unsubscribe.', 'Trả về một hàm dọn dẹp để hủy đăng ký.'),
        ("Don't update state on every render, or you'll get an infinite loop.", 'Đừng cập nhật state mỗi lần render, kẻo bị vòng lặp vô hạn.'),
    ],
    'vocab': [
        ('hook', '/hʊk/', 'n', 'hook (hàm đặc biệt của React)', 'Hooks must be called at the top level of a component.', 'Hook phải được gọi ở cấp cao nhất của component.'),
        ('side effect', '/saɪd ɪˈfekt/', 'n', 'tác dụng phụ (việc ngoài việc hiển thị)', 'Fetching data is a side effect.', 'Lấy dữ liệu là một tác dụng phụ.'),
        ('dependency array', '/dɪˈpendənsi əˈreɪ/', 'n', 'mảng phụ thuộc', 'Add userId to the dependency array.', 'Thêm userId vào mảng phụ thuộc.'),
        ('mount', '/maʊnt/', 'verb', 'gắn (component xuất hiện trên trang)', 'The effect runs when the component mounts.', 'Effect chạy khi component được gắn vào.'),
        ('unmount', '/ʌnˈmaʊnt/', 'verb', 'gỡ (component biến mất)', 'Stop the timer when the component unmounts.', 'Dừng bộ đếm khi component bị gỡ.'),
        ('cleanup function', '/ˈkliːnʌp ˈfʌŋkʃn/', 'n', 'hàm dọn dẹp', 'The cleanup function closes the connection.', 'Hàm dọn dẹp đóng kết nối.'),
        ('stale', '/steɪl/', 'adj', 'cũ, lỗi thời (giá trị)', 'The callback uses a stale value of count.', 'Callback dùng giá trị cũ của count.'),
        ('memoize', '/ˈmeməʊaɪz/', 'verb', 'ghi nhớ kết quả (tránh tính lại)', 'Memoize the expensive calculation.', 'Ghi nhớ phép tính tốn kém.'),
        ('custom hook', '/ˈkʌstəm hʊk/', 'n', 'hook tự viết', 'We wrote a custom hook for fetching user data.', 'Chúng tôi viết một hook riêng để lấy dữ liệu người dùng.'),
        ('subscribe', '/səbˈskraɪb/', 'verb', 'đăng ký (nhận sự kiện)', 'Subscribe to the chat messages when the page opens.', 'Đăng ký nhận tin nhắn chat khi trang mở.'),
        ('closure', '/ˈkləʊʒə/', 'n', 'bao đóng (hàm nhớ biến bên ngoài)', 'Stale values are usually caused by closures.', 'Giá trị cũ thường do bao đóng gây ra.'),
        ('initial value', '/ɪˈnɪʃl ˈvæljuː/', 'n', 'giá trị ban đầu', 'The initial value of count is zero.', 'Giá trị ban đầu của count là không.'),
        ('setter function', '/ˈsetə ˈfʌŋkʃn/', 'n', 'hàm cập nhật giá trị', 'Call the setter function to update the state.', 'Gọi hàm setter để cập nhật state.'),
        ('infinite loop', '/ˈɪnfɪnət luːp/', 'n', 'vòng lặp vô hạn', 'Missing dependencies can cause an infinite loop.', 'Thiếu phụ thuộc có thể gây vòng lặp vô hạn.'),
    ],
    'lesson': """
<h3>1. Đọc code mẫu trong tài liệu bằng tiếng Anh</h3>
<p>Khi giải thích code, người ta thường đọc theo cách sau:</p>
<pre>const [count, setCount] = useState(0);</pre>
<div class="ex"><span class="en">We declare a state variable called count, with an initial value of zero. setCount is the setter function.</span></div>
<pre>useEffect(() =&gt; {
  const id = setInterval(tick, 1000);
  return () =&gt; clearInterval(id);
}, []);</pre>
<div class="ex"><span class="en">This effect starts a timer when the component mounts. The cleanup function clears the timer when the component unmounts. The empty dependency array means the effect runs only once.</span></div>

<h3>2. Ba trường hợp của dependency array</h3>
<table class="table">
<tr><th>Viết</th><th>Effect chạy khi…</th></tr>
<tr><td>Không có mảng</td><td><span class="say">after every render</span></td></tr>
<tr><td><code>[]</code></td><td><span class="say">only once, when the component mounts</span></td></tr>
<tr><td><code>[userId]</code></td><td><span class="say">on mount and whenever userId changes</span></td></tr>
</table>

<h3>3. Từ ngữ mô tả lỗi React thường gặp</h3>
<div class="ex"><span class="en">The component re-renders in an infinite loop.</span></div>
<div class="ex"><span class="en">The callback reads a stale value because of a closure.</span></div>
<div class="ex"><span class="en">We forgot to clean up the subscription, so there's a memory leak.</span></div>
<div class="ex"><span class="en">React warns that a dependency is missing from the array.</span></div>
""",
    'listening': {
        'title': 'Pair programming: the infinite loop',
        'intro': 'Hai dev pair programming để tìm vì sao một component gọi API liên tục.',
        'speakers': {'A': ('Felix', 'ryan'), 'B': ('Ngoc', 'jenny')},
        'lines': [
            ('B', "Felix, can you look at this? The profile page keeps calling the API. The network tab is full of requests.", 'Felix, xem giúp mình cái này? Trang hồ sơ cứ gọi API liên tục. Tab network đầy request.'),
            ('A', "Let me see. Okay, you fetch the user inside useEffect, and then you call setUser with the result.", 'Để mình xem. Được, cậu lấy user trong useEffect, rồi gọi setUser với kết quả.'),
            ('B', "Right. Is that wrong?", 'Đúng. Vậy sai à?'),
            ('A', "Not by itself. But look: there's no dependency array. So the effect runs after every render.", 'Bản thân thì không. Nhưng nhìn này: không có mảng phụ thuộc. Nên effect chạy sau mỗi lần render.'),
            ('B', "Oh. And setUser causes a re-render, which runs the effect again…", 'Ồ. Và setUser gây render lại, làm effect chạy lại…'),
            ('A', "Exactly. It's an infinite loop. The fix is to add the dependency array with user ID, so it only runs when the ID changes.", 'Chính xác. Vòng lặp vô hạn. Cách sửa là thêm mảng phụ thuộc có user ID, để nó chỉ chạy khi ID thay đổi.'),
            ('B', "Done. Only one request now. Nice!", 'Xong. Giờ chỉ còn một request. Tuyệt!'),
            ('A', "One more thing. If the user leaves the page before the request finishes, you'll try to update a component that no longer exists.", 'Thêm một việc. Nếu người dùng rời trang trước khi request xong, cậu sẽ cố cập nhật một component không còn tồn tại.'),
            ('B', "So I need a cleanup function?", 'Vậy mình cần hàm dọn dẹp?'),
            ('A', "Yes. Use an abort controller and cancel the request in the cleanup. Actually, since we fetch data in a lot of places, maybe we should write a custom hook for it.", 'Đúng. Dùng abort controller và hủy request trong hàm dọn dẹp. Thực ra, vì mình lấy dữ liệu ở nhiều chỗ, có lẽ nên viết một custom hook cho việc này.'),
        ],
        'questions': [
            ('What is the problem with the profile page?', ['It shows the wrong user.', 'It keeps calling the API.', 'It is too slow to render.', 'It crashes immediately.'], 1, '"The profile page keeps calling the API."'),
            ('Why does the effect run after every render?', ['There is no dependency array.', 'The API is slow.', 'setUser is missing.', 'The component unmounts.'], 0, '"there\'s no dependency array".'),
            ('What is the fix?', ['Remove useEffect', 'Add a dependency array with the user ID', 'Call the API twice', 'Use a class component'], 1, 'Thêm mảng phụ thuộc có user ID.'),
            ('Why do they need a cleanup function?', ['To clear the cache', 'To cancel the request if the user leaves the page', 'To log errors', 'To reset the state'], 1, 'Người dùng có thể rời trang trước khi request xong.'),
            ('What does Felix suggest at the end?', ['Rewrite the app', 'Write a custom hook for fetching data', 'Stop using React', 'Ask the backend team'], 1, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Đọc to code mẫu ở phần kiến thức theo cách người bản xứ giải thích.', 'Giải thích lỗi vòng lặp vô hạn trong 1 phút.'],
        'prompts': [
            ('Explain how useState works, as if you were teaching a junior developer.', 'declare, initial value, setter function, re-render'),
            ('Explain why an effect without a dependency array can cause an infinite loop.', 'runs after every render → setState → re-render…'),
        ],
        'model': (
            "useState lets a component remember a value between renders. You call it with an initial value, and it gives you two things: the current value and a setter function. "
            "When you call the setter, React updates the value and re-renders the component. "
            "useEffect is for side effects, like fetching data or starting a timer. It runs after the component renders. "
            "If you don't pass a dependency array, the effect runs after every render. So if the effect calls a setter, you get a re-render, the effect runs again, and you have an infinite loop. "
            "The fix is to list the values the effect depends on, so it only runs when they change.",
            'useState cho phép component nhớ một giá trị giữa các lần render. Bạn gọi nó với giá trị ban đầu, và nó trả về hai thứ: giá trị hiện tại và hàm setter. '
            'Khi gọi setter, React cập nhật giá trị và render lại component. '
            'useEffect dùng cho tác dụng phụ như lấy dữ liệu hay chạy bộ đếm. Nó chạy sau khi component render. '
            'Nếu bạn không truyền mảng phụ thuộc, effect chạy sau mỗi lần render. Vậy nếu effect gọi setter, component render lại, effect chạy lại, và bạn có vòng lặp vô hạn. '
            'Cách sửa là liệt kê các giá trị effect phụ thuộc vào, để nó chỉ chạy khi chúng thay đổi.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Docs: State and Effects',
        'text': [
            'Components often need to change what is on the screen as a result of an interaction. Typing into a form should update the input field, and clicking "next" on an image carousel should change which image is displayed. Components need to "remember" things: the current input value, the current image. In React, this kind of component-specific memory is called state.',
            'To add state, call the useState hook at the top level of your component. It returns an array with exactly two values: the current state, and a setter function that lets you update it. When you call the setter, React stores the new value and re-renders the component with it. Note that the state variable does not change immediately; it changes in the next render.',
            'Some components also need to synchronise with systems outside React, such as a network request, a timer or a browser API. Code that does this is called an effect. Effects run after rendering, so they do not slow down what the user sees.',
            'You can control when an effect runs with the dependency array. If you pass an empty array, the effect runs only after the first render. If you include values, the effect runs again whenever one of them changes. If you omit the array completely, the effect runs after every render, which is rarely what you want.',
            'Finally, many effects need to clean up after themselves. If your effect subscribes to something or starts a timer, return a cleanup function. React will call it before the effect runs again and when the component is removed from the screen.',
        ],
        'vi': 'Component cần "ghi nhớ" những thứ như giá trị đang nhập hay ảnh đang hiển thị — gọi là state. Gọi useState ở cấp cao nhất của component; nó trả về giá trị hiện tại và hàm setter; khi gọi setter, React lưu giá trị mới và render lại (biến state không đổi ngay mà ở lần render sau). Effect dùng để đồng bộ với hệ thống bên ngoài React (request mạng, bộ đếm, API trình duyệt) và chạy sau khi render. Mảng phụ thuộc điều khiển khi nào effect chạy: mảng rỗng = chỉ lần đầu; có giá trị = chạy lại khi giá trị đổi; bỏ hẳn = sau mỗi lần render. Effect đăng ký hay chạy bộ đếm nên trả về hàm dọn dẹp.',
        'questions': [
            ('What is "state" in React?', ['A CSS file', 'Component-specific memory', 'A type of effect', 'A server'], 1, 'Đoạn 1.'),
            ('What does useState return?', ['One value', 'The current state and a setter function', 'A promise', 'A cleanup function'], 1, 'Đoạn 2.'),
            ('When does the state variable actually change?', ['Immediately', 'In the next render', 'After an effect', 'Never'], 1, '"it changes in the next render".'),
            ('When does an effect with an empty dependency array run?', ['After every render', 'Only after the first render', 'Never', 'When the user clicks'], 1, 'Đoạn 4.'),
            ('When does React call the cleanup function?', ['Before the effect runs again and when the component is removed', 'Only at the start', 'Every second', 'When state changes'], 0, 'Đoạn 5.'),
        ],
    },
    'writing': {
        'task': 'Viết tóm tắt 5 câu: useState là gì, trả về gì, useEffect dùng để làm gì, mảng phụ thuộc hoạt động thế nào, và khi nào cần hàm dọn dẹp.',
        'tips': ['Mỗi câu một ý.', 'Dùng từ mới hôm nay.'],
        'model': "useState is a hook that gives a component its own memory, called state. It returns the current value and a setter function, and calling the setter re-renders the component. useEffect is used for side effects, such as fetching data or starting a timer, and it runs after rendering. The dependency array controls when the effect runs: an empty array means only on mount, and listed values make it run again when they change. If an effect subscribes to something or starts a timer, it should return a cleanup function that React calls on unmount.",
        'min_words': 70,
    },
    'quiz': [
        ('Fetching data in a component is a ___.', ['side effect', 'side job', 'state', 'hook'], 0, 'side effect.'),
        ('useState returns the current value and a ___.', ['setter function', 'cleanup function', 'dependency array', 'closure'], 0, 'setter function.'),
        ('An effect with an empty dependency array runs ___.', ['after every render', 'only once on mount', 'never', 'every second'], 1, 'Chỉ một lần khi mount.'),
        ('An effect with NO dependency array runs ___.', ['after every render', 'only once', 'never', 'on unmount only'], 0, 'Sau mỗi lần render.'),
        ('When a component is removed from the screen, it ___.', ['unmounts', 'mounts', 'renders', 'subscribes'], 0, 'unmount.'),
        ('A function returned from an effect to stop a timer is a ___.', ['cleanup function', 'setter function', 'custom hook', 'closure'], 0, 'cleanup function.'),
        ('A callback that reads an old value has a ___ value.', ['stale', 'steel', 'stable', 'still'], 0, 'stale.'),
        ('A hook you write yourself is a ___.', ['custom hook', 'custom effect', 'own hook', 'private hook'], 0, 'custom hook.'),
        ('Calling setState inside an effect with no dependency array can cause an ___.', ['infinite loop', 'empty loop', 'endless array', 'open loop'], 0, 'infinite loop.'),
        ('Cách đọc "const [count, setCount] = useState(0)":', ['We declare a state variable count with an initial value of zero.', 'We delete count.', 'We count to zero.', 'We set the state to count.'], 0, 'Declare a state variable with an initial value of zero.'),
    ],
}

DAY4 = {
    'title': 'Đọc blog kỹ thuật',
    'title_en': 'Reading a Tech Blog Post',
    'goal': 'Đọc một bài blog kỹ thuật dài (~600 từ), ghi 3 ý chính và 5 từ mới; luyện kỹ năng đọc lướt để tìm ý.',
    'tasks': [
        'Học 14 từ về hiệu năng và mở rộng hệ thống.',
        'Đọc lướt bài blog trong 3 phút: chỉ đọc câu đầu mỗi đoạn.',
        'Đọc kỹ, trả lời câu hỏi.',
        'Nghe phỏng vấn ngắn với tác giả bài blog.',
        'Ghi 3 ý chính và 5 từ mới.',
    ],
    'product': 'Ghi chú 3 ý chính và 5 từ mới',
    'warmup': [
        ('Our side project suddenly went viral.', 'Dự án phụ của chúng tôi bất ngờ nổi tiếng.'),
        ('Traffic spiked from one hundred to fifty thousand users.', 'Lưu lượng tăng vọt từ một trăm lên năm mươi nghìn người dùng.'),
        ("Don't overengineer it on day one.", 'Đừng thiết kế quá mức ngay từ ngày đầu.'),
        ('We moved the slow tasks to a background job queue.', 'Chúng tôi chuyển việc chậm sang hàng đợi tác vụ nền.'),
        ('A CDN serves images from servers close to the user.', 'CDN phục vụ ảnh từ máy chủ gần người dùng.'),
        ('Run a load test before the big launch.', 'Chạy kiểm thử tải trước buổi ra mắt lớn.'),
    ],
    'vocab': [
        ('traffic', '/ˈtræfɪk/', 'n', 'lưu lượng truy cập', 'Most of our traffic comes from mobile phones.', 'Phần lớn lưu lượng của chúng tôi đến từ điện thoại.'),
        ('spike', '/spaɪk/', 'n / verb', 'sự tăng vọt; tăng vọt', 'There was a spike in errors at 9 a.m.', 'Lỗi tăng vọt lúc 9 giờ sáng.'),
        ('go viral', '/ɡəʊ ˈvaɪrəl/', 'phrase', 'lan truyền mạnh, nổi tiếng nhanh', 'Her post went viral overnight.', 'Bài đăng của cô ấy lan truyền chỉ sau một đêm.'),
        ('overengineer', '/ˌəʊvərendʒɪˈnɪə/', 'verb', 'thiết kế phức tạp quá mức', "Don't overengineer a prototype.", 'Đừng thiết kế quá mức cho một bản thử nghiệm.'),
        ('premature optimization', '/ˌpreməˈtʃʊə ˌɒptɪmaɪˈzeɪʃn/', 'n', 'tối ưu quá sớm', 'Premature optimization wastes time.', 'Tối ưu quá sớm lãng phí thời gian.'),
        ('vertical scaling', '/ˈvɜːtɪkl ˈskeɪlɪŋ/', 'n', 'mở rộng theo chiều dọc (máy mạnh hơn)', 'Vertical scaling means buying a bigger server.', 'Mở rộng theo chiều dọc nghĩa là mua máy chủ mạnh hơn.'),
        ('horizontal scaling', '/ˌhɒrɪˈzɒntl ˈskeɪlɪŋ/', 'n', 'mở rộng theo chiều ngang (thêm máy)', 'Horizontal scaling means adding more servers.', 'Mở rộng theo chiều ngang nghĩa là thêm máy chủ.'),
        ('CDN', '/ˌsiː diː ˈen/', 'n', 'mạng phân phối nội dung', 'We serve all images through a CDN.', 'Chúng tôi phục vụ mọi ảnh qua CDN.'),
        ('read replica', '/riːd ˈreplɪkə/', 'n', 'bản sao chỉ đọc của cơ sở dữ liệu', 'Reports run on a read replica.', 'Báo cáo chạy trên bản sao chỉ đọc.'),
        ('queue', '/kjuː/', 'n', 'hàng đợi', 'Emails are added to a queue and sent later.', 'Email được đưa vào hàng đợi và gửi sau.'),
        ('background job', '/ˈbækɡraʊnd dʒɒb/', 'n', 'tác vụ nền', 'Generating the PDF is a background job.', 'Tạo PDF là một tác vụ nền.'),
        ('load test', '/ləʊd test/', 'n', 'kiểm thử tải', 'The load test showed problems at 2,000 users.', 'Kiểm thử tải cho thấy vấn đề ở mức 2.000 người dùng.'),
        ('observability', '/əbˌzɜːvəˈbɪləti/', 'n', 'khả năng quan sát hệ thống', 'Good observability helps you find problems fast.', 'Khả năng quan sát tốt giúp tìm sự cố nhanh.'),
        ('cost-effective', '/ˌkɒst ɪˈfektɪv/', 'adj', 'tiết kiệm chi phí, hiệu quả', 'A small server was the most cost-effective option.', 'Một máy chủ nhỏ là lựa chọn tiết kiệm nhất.'),
    ],
    'lesson': """
<h3>1. Đọc lướt bài dài: chiến lược 3 phút</h3>
<ol>
<li>Đọc <b>tiêu đề và đoạn mở đầu</b>: tác giả hứa sẽ nói gì?</li>
<li>Đọc <b>câu đầu</b> của mỗi đoạn (câu chủ đề).</li>
<li>Đọc <b>đoạn kết</b>: thường tóm tắt các bài học.</li>
<li>Bây giờ đoán 3 ý chính → rồi mới đọc kỹ để kiểm tra.</li>
</ol>

<h3>2. Từ báo hiệu cấu trúc bài blog</h3>
<table class="table">
<tr><th>Tín hiệu</th><th>Nghĩa</th></tr>
<tr><td><span class="say">Lesson one / The first thing we learned…</span></td><td>Ý chính bắt đầu</td></tr>
<tr><td><span class="say">It turned out that…</span></td><td>Kết quả bất ngờ</td></tr>
<tr><td><span class="say">In hindsight…</span> / <span class="say">Looking back…</span></td><td>Nhìn lại, bài học</td></tr>
<tr><td><span class="say">The takeaway is…</span></td><td>Điều rút ra</td></tr>
<tr><td><span class="say">That said, …</span></td><td>Tuy vậy (đối lập nhẹ)</td></tr>
</table>

<h3>3. Ghi chú: ý chính khác chi tiết</h3>
<p>Ý chính trả lời câu hỏi "vậy thì sao?". Chi tiết (số liệu, tên công cụ) là bằng chứng:</p>
<div class="ex"><span class="en">Main idea: Measure before you optimise.</span><span class="vi">Chi tiết: "We spent two weeks on caching, but the real problem was one missing index."</span></div>
""",
    'listening': {
        'title': 'Interview with the blog author',
        'intro': 'Host podcast phỏng vấn tác giả bài blog bạn sắp đọc.',
        'speakers': {'A': ('Host', 'brian'), 'B': ('Elena', 'ava')},
        'lines': [
            ('A', "Elena, your blog post about scaling your side project got a lot of attention. What happened?", 'Elena, bài blog của chị về việc mở rộng dự án phụ được rất nhiều chú ý. Chuyện gì đã xảy ra?'),
            ('B', "We built a small app for sharing recipes. For a year, we had about a hundred users. Then a famous chef mentioned us on TikTok, and the app went viral.", 'Chúng tôi làm một ứng dụng nhỏ chia sẻ công thức nấu ăn. Suốt một năm có khoảng một trăm người dùng. Rồi một đầu bếp nổi tiếng nhắc đến chúng tôi trên TikTok, và ứng dụng lan truyền chóng mặt.'),
            ('A', "How big was the spike?", 'Lượng truy cập tăng vọt bao nhiêu?'),
            ('B', "From a hundred to fifty thousand users in two days. Our single server was not happy.", 'Từ một trăm lên năm mươi nghìn người dùng trong hai ngày. Máy chủ duy nhất của chúng tôi không vui chút nào.'),
            ('A', "What did you do first?", 'Việc đầu tiên chị làm là gì?'),
            ('B', "Honestly, we panicked and started adding servers. But it didn't help, because the real bottleneck was the database. One query had no index.", 'Thật lòng thì chúng tôi hoảng và bắt đầu thêm máy chủ. Nhưng không ăn thua, vì điểm nghẽn thật là cơ sở dữ liệu. Một truy vấn không có index.'),
            ('A', "So lesson one: measure before you fix?", 'Vậy bài học một: đo trước khi sửa?'),
            ('B', "Exactly. If we'd had better observability, we would have found it in ten minutes instead of a day.", 'Chính xác. Nếu có khả năng quan sát tốt hơn, chúng tôi đã tìm ra nó trong mười phút thay vì một ngày.'),
            ('A', "Do you regret not building a bigger system from the start?", 'Chị có hối tiếc vì không xây hệ thống lớn hơn ngay từ đầu không?'),
            ('B', "Not at all. If we had overengineered it, we would have wasted months on a system for users we didn't have. Starting simple was the right choice.", 'Không hề. Nếu thiết kế quá mức, chúng tôi đã lãng phí hàng tháng cho một hệ thống phục vụ người dùng không hề có. Bắt đầu đơn giản là lựa chọn đúng.'),
        ],
        'questions': [
            ('What kind of app did Elena build?', ['A fitness app', 'A recipe-sharing app', 'A music app', 'A shopping app'], 1, '"a small app for sharing recipes".'),
            ('Why did the app go viral?', ['It was on TV.', 'A famous chef mentioned it on TikTok.', 'They paid for ads.', 'It won a prize.'], 1, '"a famous chef mentioned us on TikTok".'),
            ('Why didn\'t adding servers help?', ['The servers were broken.', 'The real bottleneck was a database query without an index.', 'They added too few.', 'The CDN was down.'], 1, '"the real bottleneck was the database. One query had no index."'),
            ('Does Elena regret starting simple?', ['Yes, very much', 'Not at all', 'A little', 'She doesn\'t say'], 1, '"Not at all."'),
        ],
    },
    'speaking': {
        'tips': ['Tóm tắt bài blog: 3 ý chính, mỗi ý kèm một chi tiết.', 'Nêu ý kiến: bạn đồng ý với bài học nào nhất?'],
        'prompts': [
            ('Summarise the blog post in one minute: the story and the three lessons.', 'The post is about… Lesson one… Lesson two… Lesson three…'),
            ('Which lesson do you agree with most? Why?', 'PREP.'),
        ],
        'model': (
            "The post is about a small recipe app that suddenly went viral and grew from a hundred to fifty thousand users in two days. "
            "The author shares three lessons. First, measure before you optimise: they added servers, but the real problem was one slow database query. "
            "Second, start simple and don't overengineer, because a complex system for users you don't have is a waste of time. "
            "Third, move slow work, like sending emails and resizing images, to background jobs, and use a CDN for images. "
            "I agree most with the first lesson. I've seen teams spend weeks optimising the wrong thing.",
            'Bài viết kể về một ứng dụng công thức nấu ăn nhỏ bất ngờ nổi tiếng và tăng từ một trăm lên năm mươi nghìn người dùng trong hai ngày. '
            'Tác giả chia sẻ ba bài học. Thứ nhất, đo trước khi tối ưu: họ thêm máy chủ nhưng vấn đề thật là một truy vấn chậm. '
            'Thứ hai, bắt đầu đơn giản và đừng thiết kế quá mức, vì hệ thống phức tạp cho người dùng chưa có là lãng phí thời gian. '
            'Thứ ba, chuyển việc chậm như gửi email, đổi kích thước ảnh sang tác vụ nền, và dùng CDN cho ảnh. '
            'Tôi đồng ý nhất với bài học đầu tiên. Tôi từng thấy các team mất hàng tuần tối ưu sai chỗ.'
        ),
        'seconds': 90,
    },
    'reading': {
        'title': 'Blog: What 50,000 surprise users taught us',
        'text': [
            'Last spring, our tiny recipe app had about a hundred users, most of them friends and family. We ran everything on one small server that cost us twelve dollars a month. Then, on a Saturday morning, a well-known chef mentioned the app in a video. By Monday evening, we had fifty thousand users, and our server was on fire. This post describes what we learned in those 48 hours, and in the weeks after.',
            'Lesson one: measure before you optimise. Our first reaction was to add more servers. It felt like the obvious thing to do, and it did nothing. It turned out that the problem was a single database query on the home page, which scanned the entire recipes table on every visit. Adding an index took five minutes and reduced the page load time from eight seconds to 300 milliseconds. If we had had basic observability, such as slow query logs and a simple dashboard, we would have found it immediately.',
            'Lesson two: starting simple was the right decision. Many people asked us why we had not built a "scalable" architecture from day one. In hindsight, we are glad we did not. For a whole year, we had no idea whether anyone would use the app. Building microservices, queues and multiple databases for a hundred users would have been a classic case of overengineering. One server and one database were enough to get us through the spike after a few small fixes.',
            'Lesson three: move slow work out of the request. When a user uploaded a photo, our server resized it into three sizes before responding. With a few users, nobody noticed. With thousands, uploads took twenty seconds and blocked other requests. We moved image resizing and email sending to a background job queue, and we started serving all images through a CDN. These two changes reduced the load on our server by about seventy percent.',
            'That said, we did eventually change some things. We moved to a slightly bigger server, a simple case of vertical scaling that was far more cost-effective than adding many small machines, and we added a read replica for the reports page. We also now run a load test before every big marketing campaign.',
            'The takeaway is simple: you do not need a perfect system; you need a system you understand. If you can see what is happening and fix the real bottleneck, a surprisingly simple setup can handle a surprisingly large amount of traffic.',
        ],
        'vi': 'Ứng dụng công thức nấu ăn nhỏ (~100 người dùng, máy chủ 12 đô/tháng) bỗng có 50.000 người dùng sau khi một đầu bếp nổi tiếng nhắc đến. Bài học 1: đo trước khi tối ưu — thêm máy chủ không giúp gì; vấn đề thật là một truy vấn quét toàn bảng, thêm index mất 5 phút, tải trang từ 8 giây xuống 300 ms. Bài học 2: bắt đầu đơn giản là đúng — xây kiến trúc phức tạp cho 100 người dùng là thiết kế quá mức. Bài học 3: chuyển việc chậm ra khỏi request — đổi kích thước ảnh và gửi email sang hàng đợi nền, phục vụ ảnh qua CDN, giảm tải khoảng 70%. Sau đó họ nâng cấp máy chủ (mở rộng chiều dọc, tiết kiệm hơn), thêm read replica và chạy kiểm thử tải trước mỗi chiến dịch. Kết luận: bạn không cần hệ thống hoàn hảo, bạn cần hệ thống mình hiểu.',
        'questions': [
            ('How much did the original server cost?', ['$5 a month', '$12 a month', '$50 a month', '$120 a month'], 1, 'Đoạn 1.'),
            ('What was the real cause of the slow home page?', ['Too few servers', 'A query that scanned the whole table', 'Large images', 'Slow internet'], 1, 'Đoạn 2.'),
            ('How long did adding the index take?', ['Five minutes', 'One day', 'Two weeks', '48 hours'], 0, 'Đoạn 2.'),
            ('Why are they glad they didn\'t build a complex architecture from day one?', ['It was too expensive to learn.', 'They didn\'t know if anyone would use the app.', 'Their team was too small.', 'Microservices are bad.'], 1, 'Đoạn 3.'),
            ('By how much did the background jobs and CDN reduce server load?', ['About 20%', 'About 50%', 'About 70%', 'About 90%'], 2, 'Đoạn 4.'),
            ('What is the main takeaway?', ['Always use microservices', 'You need a system you understand', 'Never use a CDN', 'Buy the biggest server'], 1, 'Đoạn 6.'),
        ],
    },
    'writing': {
        'task': 'Ghi chú bài blog: 3 ý chính (mỗi ý 1 câu + 1 chi tiết chứng minh) và 5 từ mới kèm câu ví dụ của bạn.',
        'tips': ['Ý chính trả lời "vậy thì sao?", chi tiết là con số/ví dụ.'],
        'model': "Main ideas:\n1. Measure before you optimise. – Adding servers didn't help; one missing index was the real problem (8 s → 300 ms).\n2. Start simple; don't overengineer. – One server and one database survived 50,000 users after small fixes.\n3. Move slow work out of the request. – Background jobs + CDN cut server load by ~70%.\n\nNew words:\n1. spike – We saw a spike in sign-ups after the newsletter.\n2. overengineer – Let's not overengineer the admin page; only three people use it.\n3. in hindsight – In hindsight, we should have added logging earlier.\n4. cost-effective – A managed database was more cost-effective than hiring a DBA.\n5. load test – We ran a load test with 5,000 virtual users.",
        'min_words': 80,
    },
    'quiz': [
        ('A sudden, sharp increase is a ___.', ['spike', 'spark', 'spoke', 'speck'], 0, 'spike.'),
        ('Buying a bigger server = ___ scaling.', ['vertical', 'horizontal', 'diagonal', 'parallel'], 0, 'vertical scaling.'),
        ('Adding more servers = ___ scaling.', ['horizontal', 'vertical', 'upward', 'deep'], 0, 'horizontal scaling.'),
        ('Making a system more complex than needed = to ___.', ['overengineer', 'overload', 'overwork', 'overdo it up'], 0, 'overengineer.'),
        ('Slow tasks like sending emails should be ___.', ['background jobs', 'front jobs', 'side jobs', 'foreground tasks'], 0, 'background jobs.'),
        ('A network of servers that delivers images close to users is a ___.', ['CDN', 'API', 'ORM', 'SDK'], 0, 'CDN.'),
        ('Testing how a system behaves with thousands of users = a ___.', ['load test', 'unit test', 'smoke test up', 'type test'], 0, 'load test.'),
        ('"___, we should have added logs earlier." (nhìn lại)', ['In hindsight', 'In sight', 'On hind', 'At hindsight'], 0, 'In hindsight.'),
        ('Khi đọc lướt, câu đầu mỗi đoạn thường là:', ['Câu chủ đề', 'Câu ví dụ', 'Câu đùa', 'Câu không quan trọng'], 0, 'Topic sentence.'),
        ('"___ said, we did change a few things." (tuy vậy)', ['That', 'This', 'What', 'It'], 0, 'That said, … = tuy vậy.'),
    ],
}

DAY5 = {
    'title': 'Nghe podcast công nghệ',
    'title_en': 'Tech Podcast: Should You Use an ORM?',
    'goal': 'Nghe trọn một tập podcast kỹ thuật dài (~4 phút) và ghi 5 ý chính bằng tiếng Anh.',
    'tasks': [
        'Học 14 thuật ngữ về cơ sở dữ liệu và ORM.',
        'Nghe cả tập một lần không dừng, không hiện lời.',
        'Nghe lần 2, ghi 5 ý chính bằng tiếng Anh (từ khóa).',
        'Trả lời câu hỏi, hiện lời để kiểm tra.',
        'Nói 1 phút: bạn đứng về phía host nào?',
    ],
    'product': 'Ghi chú 5 ý chính của tập podcast',
    'warmup': [
        ('An ORM lets you work with objects instead of raw SQL.', 'ORM cho phép làm việc với đối tượng thay vì SQL thuần.'),
        ("It's a leaky abstraction.", 'Đó là một lớp trừu tượng "rò rỉ".'),
        ('Watch out for the N plus one problem.', 'Cẩn thận vấn đề N cộng một.'),
        ('Every good ORM has an escape hatch.', 'ORM tốt nào cũng có "lối thoát".'),
        ('My rule of thumb is to start with the ORM.', 'Nguyên tắc kinh nghiệm của tôi là bắt đầu với ORM.'),
        ("It's a bit of a footgun.", 'Nó hơi dễ khiến bạn tự gây hại.'),
    ],
    'vocab': [
        ('raw SQL', '/rɔː ˌes kjuː ˈel/', 'n', 'SQL viết tay (thuần)', 'For complex reports, we write raw SQL.', 'Với báo cáo phức tạp, chúng tôi viết SQL thuần.'),
        ('abstraction', '/æbˈstrækʃn/', 'n', 'lớp trừu tượng', 'An ORM is an abstraction over the database.', 'ORM là một lớp trừu tượng trên cơ sở dữ liệu.'),
        ('leaky abstraction', '/ˈliːki æbˈstrækʃn/', 'n', 'trừu tượng "rò rỉ" (vẫn phải hiểu tầng dưới)', 'ORMs are leaky abstractions; you still need to know SQL.', 'ORM là trừu tượng rò rỉ; bạn vẫn cần biết SQL.'),
        ('N+1 problem', '/en plʌs wʌn ˈprɒbləm/', 'n', 'vấn đề N+1 truy vấn', 'The N+1 problem made the page very slow.', 'Vấn đề N+1 làm trang rất chậm.'),
        ('query builder', '/ˈkwɪəri ˈbɪldə/', 'n', 'công cụ dựng truy vấn', 'A query builder is a middle ground between SQL and an ORM.', 'Query builder là giải pháp ở giữa SQL và ORM.'),
        ('escape hatch', '/ɪˈskeɪp hætʃ/', 'n', 'lối thoát (cách vượt khỏi giới hạn công cụ)', 'Raw SQL is the escape hatch when the ORM is not enough.', 'SQL thuần là lối thoát khi ORM không đủ.'),
        ('type safety', '/taɪp ˈseɪfti/', 'n', 'an toàn kiểu dữ liệu', 'The ORM gives us type safety in our queries.', 'ORM cho chúng tôi an toàn kiểu trong truy vấn.'),
        ('portability', '/ˌpɔːtəˈbɪləti/', 'n', 'tính khả chuyển (đổi hệ thống dễ)', 'Portability matters if you might change databases.', 'Tính khả chuyển quan trọng nếu bạn có thể đổi cơ sở dữ liệu.'),
        ('vendor lock-in', '/ˈvendə ˈlɒk ɪn/', 'n', 'bị trói buộc vào nhà cung cấp', 'Using special cloud features can cause vendor lock-in.', 'Dùng tính năng đặc biệt của nhà cung cấp cloud có thể khiến bạn bị trói buộc.'),
        ('opinionated', '/əˈpɪnjəneɪtɪd/', 'adj', '(framework) áp đặt cách làm riêng', 'Rails is an opinionated framework.', 'Rails là một framework áp đặt cách làm.'),
        ('footgun', '/ˈfʊtɡʌn/', 'n', 'tính năng dễ khiến tự gây lỗi', 'Lazy loading can be a footgun.', 'Tải lười có thể là "cái bẫy tự bắn vào chân".'),
        ('ergonomics', '/ˌɜːɡəˈnɒmɪks/', 'n', 'sự tiện dụng (khi dùng công cụ)', 'The ergonomics of this library are great.', 'Thư viện này dùng rất tiện.'),
        ('prototype', '/ˈprəʊtətaɪp/', 'n / verb', 'bản mẫu; làm bản mẫu', 'We built a prototype in one week.', 'Chúng tôi làm bản mẫu trong một tuần.'),
        ('rule of thumb', '/ruːl əv θʌm/', 'n', 'nguyên tắc kinh nghiệm', 'As a rule of thumb, keep functions under forty lines.', 'Theo kinh nghiệm, giữ hàm dưới bốn mươi dòng.'),
    ],
    'lesson': """
<h3>1. Ghi chú khi nghe podcast dài</h3>
<p>Một tập podcast dài có nhiều đoạn lan man, đùa giỡn. Bạn chỉ cần bắt các <b>luận điểm</b>. Dấu hiệu:</p>
<table class="table">
<tr><th>Tín hiệu</th><th>Ý nghĩa</th></tr>
<tr><td><span class="say">My main argument is…</span> · <span class="say">The big advantage is…</span></td><td>Luận điểm chính</td></tr>
<tr><td><span class="say">The problem with that is…</span> · <span class="say">The catch is…</span></td><td>Phản biện</td></tr>
<tr><td><span class="say">My rule of thumb is…</span></td><td>Lời khuyên thực tế (thường là ý đáng ghi nhất)</td></tr>
<tr><td><span class="say">So where do we land?</span> · <span class="say">To wrap up…</span></td><td>Kết luận sắp đến</td></tr>
</table>

<h3>2. Mẫu ghi chú 5 ý</h3>
<pre>Topic: ORM vs raw SQL
1. ORM + : fast to build, type safety, less boilerplate
2. ORM − : leaky abstraction → still need SQL; N+1 problem
3. Raw SQL + : full control, complex reports
4. Middle: query builders; ORMs have escape hatches
5. Rule of thumb: start with ORM, measure, drop to SQL for hot paths</pre>

<h3>3. Ngôn ngữ tranh luận lịch sự trong podcast</h3>
<div class="ex"><span class="en">I'll push back on that a little.</span></div>
<div class="ex"><span class="en">That's fair, but in my experience…</span></div>
<div class="ex"><span class="en">I think we actually agree more than we disagree.</span></div>
""",
    'listening': {
        'title': 'Podcast: Should you use an ORM?',
        'intro': 'Một tập podcast dài khoảng 4 phút. Hai host tranh luận về ORM và SQL thuần. Nghe cả tập một lần không dừng trước khi trả lời.',
        'speakers': {'A': ('Wes', 'guy'), 'B': ('Maya', 'emma')},
        'lines': [
            ('A', "Welcome back to Dev Talk. Today's topic is a classic argument: should you use an ORM, or should you just write SQL? Maya, where do you stand?", 'Chào mừng trở lại Dev Talk. Chủ đề hôm nay là một tranh luận kinh điển: nên dùng ORM hay chỉ viết SQL? Maya, bạn đứng ở đâu?'),
            ('B', "I'm firmly on the ORM side, at least for most projects. My main argument is speed. With an ORM, I can build a prototype in a day. I define my models, and I get queries, migrations and type safety for free.", 'Mình kiên định ở phía ORM, ít nhất là với phần lớn dự án. Luận điểm chính của mình là tốc độ. Với ORM, mình làm được bản mẫu trong một ngày. Mình định nghĩa model và có ngay truy vấn, migration và an toàn kiểu miễn phí.'),
            ('A', "I'll push back on that a little. The problem with ORMs is that they're a leaky abstraction. They promise you won't need to think about SQL, but sooner or later, you do.", 'Mình phản đối nhẹ chỗ đó. Vấn đề của ORM là nó là một lớp trừu tượng rò rỉ. Nó hứa rằng bạn không cần nghĩ về SQL, nhưng sớm muộn gì bạn cũng phải nghĩ.'),
            ('B', "That's fair. When?", 'Công bằng. Khi nào?'),
            ('A', "Performance, mostly. The classic example is the N plus one problem. You load a list of fifty orders, then you access the customer for each one, and suddenly you've run fifty-one queries without noticing. It's a real footgun.", 'Chủ yếu là hiệu năng. Ví dụ kinh điển là vấn đề N cộng một. Bạn tải danh sách năm mươi đơn hàng, rồi truy cập khách hàng của từng đơn, và bỗng nhiên bạn đã chạy năm mươi mốt truy vấn mà không hay biết. Đó thực sự là cái bẫy.'),
            ('B', "Sure, but every good ORM has a solution for that, like select related or eager loading. You just need to know about it.", 'Đúng, nhưng ORM tốt nào cũng có giải pháp, như select related hay eager loading. Bạn chỉ cần biết nó.'),
            ('A', "Which proves my point: you still need to understand what SQL is being generated.", 'Điều đó chứng minh ý mình: bạn vẫn cần hiểu SQL nào đang được sinh ra.'),
            ('B', "Okay, I agree with that. Developers who use an ORM should still learn SQL. But that doesn't mean we should write everything by hand.", 'Được, mình đồng ý điều đó. Dev dùng ORM vẫn nên học SQL. Nhưng không có nghĩa là mình nên viết mọi thứ bằng tay.'),
            ('A', "What about portability? People say an ORM lets you switch databases easily.", 'Còn tính khả chuyển? Người ta nói ORM giúp đổi cơ sở dữ liệu dễ dàng.'),
            ('B', "Honestly, I've never seen a team switch databases. That argument is a bit overrated. The real benefits are productivity and ergonomics.", 'Thật lòng, mình chưa từng thấy team nào đổi cơ sở dữ liệu. Lập luận đó hơi bị đánh giá quá cao. Lợi ích thật là năng suất và sự tiện dụng.'),
            ('A', "Ha, agreed. So when would you write raw SQL?", 'Ha, đồng ý. Vậy khi nào bạn viết SQL thuần?'),
            ('B', "Complex reports, analytics, anything with heavy joins or window functions. Most ORMs have an escape hatch that lets you run raw SQL when you need it.", 'Báo cáo phức tạp, phân tích, bất cứ thứ gì có nhiều join hay window function. Phần lớn ORM có lối thoát cho phép chạy SQL thuần khi cần.'),
            ('A', "And there's a middle ground too: query builders. You write something close to SQL, but in your programming language, with less boilerplate.", 'Và còn có giải pháp ở giữa: query builder. Bạn viết thứ gần giống SQL, nhưng bằng ngôn ngữ lập trình của bạn, ít code lặp hơn.'),
            ('B', "So, where do we land? I think we actually agree more than we disagree.", 'Vậy, chúng ta kết luận thế nào? Mình nghĩ thực ra chúng ta đồng ý nhiều hơn là bất đồng.'),
            ('A', "We do. My rule of thumb: start with the ORM, measure, and drop down to raw SQL for the hot paths, the queries that run thousands of times a minute.", 'Đúng vậy. Nguyên tắc của mình: bắt đầu với ORM, đo lường, và chuyển xuống SQL thuần cho các đường nóng, những truy vấn chạy hàng nghìn lần mỗi phút.'),
            ('B', "And learn SQL either way. That's it for today. Thanks for listening!", 'Và dù sao cũng hãy học SQL. Hôm nay vậy thôi. Cảm ơn đã lắng nghe!'),
        ],
        'questions': [
            ('What is Maya\'s main argument for ORMs?', ['Better performance', 'Speed of development', 'Portability', 'Security'], 1, '"My main argument is speed."'),
            ('Why does Wes call ORMs a "leaky abstraction"?', ['They lose data.', 'Sooner or later you still need to think about SQL.', 'They are insecure.', 'They are slow to install.'], 1, '"sooner or later, you do".'),
            ('In Wes\'s example, how many queries run for fifty orders?', ['One', 'Two', 'Fifty', 'Fifty-one'], 3, '"you\'ve run fifty-one queries".'),
            ('What does Maya think about the portability argument?', ['It is the most important.', 'It is a bit overrated.', 'It is false.', 'She doesn\'t mention it.'], 1, '"That argument is a bit overrated."'),
            ('When would Maya write raw SQL?', ['For everything', 'For complex reports and analytics', 'Never', 'Only for migrations'], 1, '"Complex reports, analytics…"'),
            ('What is Wes\'s rule of thumb?', ['Always write raw SQL', 'Start with the ORM, measure, use raw SQL for hot paths', 'Never use an ORM', 'Use query builders only'], 1, 'Câu áp chót.'),
        ],
    },
    'speaking': {
        'tips': ['Nói 1 phút: tóm tắt tranh luận + quan điểm của bạn.', 'Dùng ngôn ngữ tranh luận lịch sự.'],
        'prompts': [
            ('Summarise the podcast: what did each host argue, and where did they land?', 'Maya argued… Wes pushed back… In the end…'),
            ('Do you prefer ORMs or raw SQL? Why?', 'My rule of thumb is…'),
        ],
        'model': (
            "The episode was about whether to use an ORM or raw SQL. Maya argued that ORMs make development much faster and give you type safety and migrations for free. "
            "Wes pushed back and said ORMs are leaky abstractions, because you still need to understand SQL, especially to avoid the N+1 problem. "
            "In the end, they agreed more than they disagreed. Their rule of thumb is to start with an ORM, measure performance, and use raw SQL only for the hot paths. "
            "I agree with them. In my projects, the ORM handles ninety percent of queries, and I write raw SQL for the big reports.",
            'Tập này bàn về việc dùng ORM hay SQL thuần. Maya cho rằng ORM giúp phát triển nhanh hơn nhiều và cho bạn an toàn kiểu cùng migration miễn phí. '
            'Wes phản đối, nói ORM là trừu tượng rò rỉ vì bạn vẫn cần hiểu SQL, nhất là để tránh vấn đề N+1. '
            'Cuối cùng, họ đồng ý nhiều hơn bất đồng. Nguyên tắc của họ là bắt đầu với ORM, đo hiệu năng và chỉ dùng SQL thuần cho các đường nóng. '
            'Tôi đồng ý. Trong dự án của tôi, ORM xử lý chín mươi phần trăm truy vấn, còn tôi viết SQL thuần cho các báo cáo lớn.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'How to take notes from a podcast',
        'text': [
            'Listening to a 45-minute podcast and remembering nothing a week later is very common. The problem is not your memory; it is that listening is passive. To learn from a podcast, you need to do something with it.',
            'The simplest technique is the "five ideas" note. During or right after the episode, write down five main ideas in your own words, using English keywords rather than full sentences. If you cannot find five, listen to the section where you lost focus again.',
            'Then, the next day, try to explain those five ideas out loud in two minutes, without looking at your notes. This combines listening, writing and speaking, and it is much more effective than listening to three episodes without any notes.',
        ],
        'vi': 'Nghe podcast 45 phút rồi tuần sau quên sạch là chuyện thường vì nghe là hoạt động thụ động. Kỹ thuật đơn giản nhất: ghi "năm ý chính" bằng từ khóa tiếng Anh, theo lời của bạn; nếu không tìm đủ năm ý, nghe lại đoạn bạn mất tập trung. Hôm sau, thử giải thích năm ý đó thành tiếng trong hai phút không nhìn ghi chú — kết hợp nghe, viết, nói, hiệu quả hơn nghe ba tập mà không ghi chép.',
        'questions': [
            ('Why do people forget podcasts, according to the text?', ['Bad memory', 'Listening is passive', 'Podcasts are too long', 'The audio is poor'], 1, 'Đoạn 1.'),
            ('How should you write the five ideas?', ['Full sentences in Vietnamese', 'English keywords in your own words', 'Copy the transcript', 'Draw pictures'], 1, 'Đoạn 2.'),
            ('What should you do the next day?', ['Listen to three more episodes', 'Explain the five ideas out loud without notes', 'Read the transcript', 'Nothing'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Ghi 5 ý chính của tập podcast bằng tiếng Anh (từ khóa, theo mẫu ở phần kiến thức). Sau đó viết 2–3 câu nêu quan điểm của bạn.',
        'tips': ['Dùng ký hiệu + / − / → cho gọn.'],
        'model': "Topic: ORM vs raw SQL\n1. ORM + : fast prototypes, models → queries, migrations, type safety\n2. ORM − : leaky abstraction; N+1 problem (50 orders → 51 queries)\n3. Fix: select_related / eager loading → still need to know SQL\n4. Portability argument = overrated; real benefit = productivity\n5. Rule of thumb: start with ORM → measure → raw SQL for hot paths; query builders = middle ground\n\nMy opinion: I agree with the rule of thumb. ORMs save a lot of time, but every developer should be able to read the SQL they generate.",
        'min_words': 60,
    },
    'quiz': [
        ('SQL written by hand is called ___ SQL.', ['raw', 'pure up', 'hard', 'native up'], 0, 'raw SQL.'),
        ('An abstraction where you still need to understand the layer below is ___.', ['leaky', 'lazy', 'loose', 'light'], 0, 'leaky abstraction.'),
        ('Loading 50 orders and then 50 customers one by one = the ___ problem.', ['N+1', '50+1', 'double', 'lazy'], 0, 'N+1 problem.'),
        ('A way to bypass a tool\'s limits is an ___.', ['escape hatch', 'exit door', 'back gate', 'emergency key'], 0, 'escape hatch.'),
        ('Being stuck with one cloud provider = vendor ___.', ['lock-in', 'lock-up', 'lock-out', 'lockdown'], 0, 'vendor lock-in.'),
        ('A framework that forces its own way of doing things is ___.', ['opinionated', 'optional', 'open-minded', 'operational'], 0, 'opinionated.'),
        ('"As a ___ of thumb, start with the ORM."', ['rule', 'law', 'tip', 'role'], 0, 'rule of thumb.'),
        ('A feature that makes it easy to hurt yourself is a ___.', ['footgun', 'handgun', 'shortcut', 'footnote'], 0, 'footgun.'),
        ('Tín hiệu kết luận trong podcast:', ['So, where do we land?', 'Let me start…', 'First of all…', 'Welcome back…'], 0, '"Where do we land?" = kết luận thế nào?'),
        ('Maya and Wes finally…', ['agreed more than they disagreed', 'stopped talking', 'chose raw SQL only', 'chose ORM only'], 0, 'Họ đồng ý nhiều hơn bất đồng.'),
    ],
}

DAY6 = {
    'title': 'Tổng kết tuần 8',
    'title_en': 'Week 8 Review: Technical Reading',
    'goal': 'Ôn lại nội dung đọc và nghe trong tuần qua bài quiz 10 câu; học các từ nối học thuật hay gặp trong tài liệu kỹ thuật.',
    'tasks': [
        'Học 14 từ học thuật hay gặp trong tài liệu.',
        'Đọc bài về cách đọc tài liệu hiệu quả.',
        'Nghe hai dev chia sẻ thói quen đọc tài liệu.',
        'Làm quiz 10 câu về nội dung đã đọc và nghe trong tuần.',
    ],
    'product': 'Điểm quiz',
    'warmup': [
        ('Essentially, a view connects a URL to a response.', 'Về bản chất, view kết nối URL với response.'),
        ('This approach is robust, but it adds some overhead.', 'Cách này chắc chắn, nhưng thêm một chút chi phí.'),
        ('In contrast, raw SQL gives you full control.', 'Ngược lại, SQL thuần cho bạn toàn quyền kiểm soát.'),
        ('Consequently, the page loads much faster.', 'Do đó, trang tải nhanh hơn nhiều.'),
        ('The two tests take approximately five and ten minutes, respectively.', 'Hai bài test lần lượt mất khoảng năm và mười phút.'),
        ('Notably, the docs recommend using a CDN.', 'Đáng chú ý, tài liệu khuyên dùng CDN.'),
    ],
    'vocab': [
        ('essentially', '/ɪˈsenʃəli/', 'adv', 'về bản chất', 'Essentially, a hook is just a function.', 'Về bản chất, hook chỉ là một hàm.'),
        ('thereby', '/ˌðeəˈbaɪ/', 'adv', 'nhờ đó, qua đó', 'The cache reduces database calls, thereby improving speed.', 'Cache giảm lời gọi cơ sở dữ liệu, nhờ đó tăng tốc độ.'),
        ('leverage', '/ˈliːvərɪdʒ/', 'verb', 'tận dụng', 'We leverage the browser cache to load pages faster.', 'Chúng tôi tận dụng cache trình duyệt để tải trang nhanh hơn.'),
        ('robust', '/rəʊˈbʌst/', 'adj', 'chắc chắn, bền vững', 'We need a robust solution, not a quick hack.', 'Chúng ta cần giải pháp chắc chắn, không phải mẹo tạm.'),
        ('overhead', '/ˈəʊvəhed/', 'n', 'chi phí phát sinh (thời gian/tài nguyên)', 'Logging adds a small performance overhead.', 'Ghi log thêm một chút chi phí hiệu năng.'),
        ('in contrast', '/ɪn ˈkɒntrɑːst/', 'phrase', 'ngược lại', 'In contrast, the old system needed manual steps.', 'Ngược lại, hệ thống cũ cần các bước thủ công.'),
        ('consequently', '/ˈkɒnsɪkwəntli/', 'adv', 'do đó, hậu quả là', 'The index was missing; consequently, queries were slow.', 'Thiếu index; do đó truy vấn bị chậm.'),
        ('approximately', '/əˈprɒksɪmətli/', 'adv', 'xấp xỉ, khoảng', 'The migration takes approximately ten minutes.', 'Migration mất khoảng mười phút.'),
        ('respectively', '/rɪˈspektɪvli/', 'adv', 'lần lượt (theo thứ tự đã nêu)', 'Lan and Minh lead the web and mobile teams, respectively.', 'Lan và Minh lần lượt dẫn dắt team web và team mobile.'),
        ('namely', '/ˈneɪmli/', 'adv', 'cụ thể là', 'Two tools are required, namely Docker and Git.', 'Cần hai công cụ, cụ thể là Docker và Git.'),
        ('subsequently', '/ˈsʌbsɪkwəntli/', 'adv', 'sau đó', 'The bug was reported and subsequently fixed.', 'Lỗi được báo cáo và sau đó được sửa.'),
        ('inherently', '/ɪnˈhɪərəntli/', 'adv', 'vốn dĩ, bản chất', 'Distributed systems are inherently complex.', 'Hệ thống phân tán vốn dĩ phức tạp.'),
        ('arguably', '/ˈɑːɡjuəbli/', 'adv', 'có thể nói là', 'This is arguably the best book on the topic.', 'Có thể nói đây là cuốn sách hay nhất về chủ đề này.'),
        ('notably', '/ˈnəʊtəbli/', 'adv', 'đáng chú ý là', 'Several companies, notably Netflix, use this approach.', 'Một số công ty, đáng chú ý là Netflix, dùng cách này.'),
    ],
    'lesson': """
<h3>1. Từ nối học thuật trong tài liệu</h3>
<table class="table">
<tr><th>Chức năng</th><th>Văn nói</th><th>Văn tài liệu</th></tr>
<tr><td>Bản chất</td><td>basically</td><td><span class="say">essentially, in essence</span></td></tr>
<tr><td>Kết quả</td><td>so</td><td><span class="say">consequently, therefore, thereby</span></td></tr>
<tr><td>Đối lập</td><td>but</td><td><span class="say">in contrast, however, whereas</span></td></tr>
<tr><td>Ví dụ / cụ thể</td><td>like</td><td><span class="say">namely, notably, for instance</span></td></tr>
<tr><td>Thời gian</td><td>then, later</td><td><span class="say">subsequently</span></td></tr>
<tr><td>Ước lượng</td><td>about</td><td><span class="say">approximately, roughly</span></td></tr>
</table>
<div class="note"><b>respectively:</b> "A and B take 5 and 10 minutes, <i>respectively</i>" = A mất 5 phút, B mất 10 phút. Rất hay gặp trong tài liệu và bài báo kỹ thuật.</div>

<h3>2. Ôn tuần 8</h3>
<table class="table">
<tr><th>Ngày</th><th>Ý chính</th></tr>
<tr><td>Django</td><td>View = request → response; URLconf ánh xạ path → view; querysets lazy</td></tr>
<tr><td>FastAPI</td><td>Dependency injection: khai báo thứ cần, framework cung cấp; yield để dọn dẹp</td></tr>
<tr><td>React</td><td>useState = bộ nhớ; useEffect = tác dụng phụ; dependency array; cleanup</td></tr>
<tr><td>Blog</td><td>Đo trước khi tối ưu; bắt đầu đơn giản; việc chậm → tác vụ nền</td></tr>
<tr><td>Podcast</td><td>ORM vs SQL: bắt đầu với ORM, đo, SQL thuần cho đường nóng</td></tr>
</table>
""",
    'listening': {
        'title': 'How do you read documentation?',
        'intro': 'Hai lập trình viên chia sẻ thói quen đọc tài liệu tiếng Anh.',
        'speakers': {'A': ('Anh', 'andrew'), 'B': ('Grace', 'sonia')},
        'lines': [
            ('A', "Grace, when you learn a new library, do you read the docs from start to finish?", 'Grace, khi học thư viện mới, chị có đọc tài liệu từ đầu đến cuối không?'),
            ('B', "Almost never. I start with the tutorial or the quick start, because it shows the main ideas in about twenty minutes.", 'Hầu như không. Chị bắt đầu với phần hướng dẫn hoặc quick start, vì nó cho thấy các ý chính trong khoảng hai mươi phút.'),
            ('A', "And then?", 'Rồi sao nữa?'),
            ('B', "Then I build something small. When I get stuck, I search the reference docs for that specific problem. Essentially, I read the docs on demand.", 'Rồi chị làm thứ gì đó nhỏ. Khi bị bí, chị tìm trong tài liệu tra cứu cho đúng vấn đề đó. Về bản chất, chị đọc tài liệu khi cần.'),
            ('A', "I do something similar, but English is my second language, so long explanations are tiring. Sometimes I paste paragraphs into a translator.", 'Em cũng làm tương tự, nhưng tiếng Anh là ngôn ngữ thứ hai của em, nên phần giải thích dài khá mệt. Đôi khi em dán cả đoạn vào công cụ dịch.'),
            ('B', "That's understandable. But try reading the code examples first. Code is a universal language. Then read only the sentences around the example.", 'Dễ hiểu thôi. Nhưng thử đọc ví dụ code trước. Code là ngôn ngữ chung. Rồi chỉ đọc các câu xung quanh ví dụ.'),
            ('A', "That's a good tip. What about warnings and notes?", 'Mẹo hay. Còn phần cảnh báo và ghi chú?'),
            ('B', "Always read them carefully. They're usually there because many people made the same mistake. Notably, the security notes.", 'Luôn đọc kỹ. Chúng thường có mặt vì nhiều người đã mắc cùng lỗi. Đáng chú ý là các ghi chú bảo mật.'),
            ('A', "Makes sense. I've been reading docs every day this week, and I already feel faster.", 'Hợp lý. Tuần này ngày nào em cũng đọc tài liệu, và em đã thấy mình nhanh hơn.'),
            ('B', "That's the best way. The vocabulary in technical docs is quite limited, so it gets easier very quickly.", 'Đó là cách tốt nhất. Từ vựng trong tài liệu kỹ thuật khá hạn chế, nên sẽ dễ lên rất nhanh.'),
        ],
        'questions': [
            ('How does Grace start learning a new library?', ['Reading all the docs', 'With the tutorial or quick start', 'Watching videos', 'Asking colleagues'], 1, '"I start with the tutorial or the quick start".'),
            ('What does "read the docs on demand" mean?', ['Read everything first', 'Read only when she needs a specific answer', 'Pay for the docs', 'Never read them'], 1, 'Đọc khi cần.'),
            ('What does Grace suggest reading first?', ['The warnings', 'The code examples', 'The introduction', 'The changelog'], 1, '"try reading the code examples first".'),
            ('Why should you read warnings carefully?', ['They are long.', 'Many people made the same mistake.', 'They are funny.', 'They are new.'], 1, 'Grace giải thích.'),
            ('Why does reading technical docs get easier quickly?', ['The vocabulary is quite limited.', 'They are short.', 'They have pictures.', 'They are in Vietnamese.'], 0, 'Câu cuối.'),
        ],
    },
    'speaking': {
        'tips': ['Kể lại 3 điều bạn học được từ tài liệu tuần này.', 'Dùng ít nhất 4 từ học thuật hôm nay.'],
        'prompts': [
            ('What are the three most useful things you learned from the docs this week?', 'Essentially… Consequently… Notably…'),
            ('How will you read documentation from now on?', 'Kế hoạch đọc của bạn.'),
        ],
        'model': (
            "This week I learned three useful things from the docs. First, Django querysets are lazy; consequently, the database is only queried when the data is actually used. "
            "Second, dependency injection in FastAPI is essentially a way for a function to declare what it needs, which makes testing much easier. "
            "Third, in React, an effect without a dependency array runs after every render, which can lead to an infinite loop. "
            "From now on, I'll start with the quick start, read the code examples first, and always read the warnings carefully.",
            'Tuần này tôi học được ba điều hữu ích từ tài liệu. Thứ nhất, queryset của Django có tính lười; do đó cơ sở dữ liệu chỉ bị truy vấn khi dữ liệu thực sự được dùng. '
            'Thứ hai, tiêm phụ thuộc trong FastAPI về bản chất là cách để hàm khai báo thứ nó cần, giúp test dễ hơn nhiều. '
            'Thứ ba, trong React, effect không có mảng phụ thuộc chạy sau mỗi lần render, có thể dẫn đến vòng lặp vô hạn. '
            'Từ giờ, tôi sẽ bắt đầu với quick start, đọc ví dụ code trước và luôn đọc kỹ phần cảnh báo.'
        ),
        'seconds': 60,
    },
    'reading': {
        'title': 'Reading documentation like a senior engineer',
        'text': [
            'Junior developers often believe that senior engineers have memorised the documentation. In reality, senior engineers are simply very good at finding the right page quickly and reading only what they need.',
            'Most documentation sites are organised in four parts: tutorials, how-to guides, reference and explanation. Tutorials teach you the basics step by step. How-to guides solve specific problems. Reference pages list every function and parameter. Explanation pages discuss the ideas and design decisions behind the tool. Knowing which part you need saves a lot of time.',
            'Senior engineers also read the changelog before upgrading a library, notably the sections on breaking changes and deprecations. Consequently, they avoid many of the problems that surprise other developers after an upgrade.',
        ],
        'vi': 'Dev junior thường nghĩ senior thuộc lòng tài liệu; thực ra senior chỉ giỏi tìm đúng trang và đọc đúng phần cần. Phần lớn trang tài liệu chia 4 phần: tutorial (học cơ bản từng bước), how-to guide (giải quyết vấn đề cụ thể), reference (liệt kê mọi hàm, tham số), explanation (ý tưởng và quyết định thiết kế). Senior còn đọc changelog trước khi nâng cấp thư viện, đặc biệt phần thay đổi phá vỡ tương thích và tính năng lỗi thời, nhờ đó tránh nhiều vấn đề bất ngờ.',
        'questions': [
            ('What are senior engineers really good at, according to the text?', ['Memorising docs', 'Finding the right page quickly and reading only what they need', 'Writing docs', 'Avoiding docs'], 1, 'Đoạn 1.'),
            ('Which part of the docs lists every function and parameter?', ['Tutorials', 'How-to guides', 'Reference', 'Explanation'], 2, 'Đoạn 2.'),
            ('What do senior engineers read before upgrading a library?', ['The tutorial', 'The changelog', 'The source code', 'Blog posts'], 1, 'Đoạn 3.'),
        ],
    },
    'writing': {
        'task': 'Viết 6 câu về những gì bạn đọc và nghe tuần này, mỗi câu dùng một từ học thuật hôm nay (essentially, consequently, in contrast, notably, approximately, respectively…).',
        'tips': ['Câu ngắn, rõ, đúng ngữ cảnh kỹ thuật.'],
        'model': "1. Essentially, a Django view takes a request and returns a response.\n2. The article page ran 21 queries; consequently, it was very slow.\n3. In contrast, the fixed version needs only one query.\n4. Several features, notably type hints and dependency injection, make FastAPI easy to test.\n5. Adding the index took approximately five minutes.\n6. useState and useEffect handle memory and side effects, respectively.",
        'min_words': 60,
    },
    'quiz': [
        ('In Django, querysets are ___: SQL runs only when data is needed.', ['lazy', 'eager', 'robust', 'stale'], 0, 'Ngày 43.'),
        ('What does a URLconf do?', ['Maps URL patterns to views', 'Stores user data', 'Renders templates', 'Runs migrations'], 0, 'Ngày 43.'),
        ('In FastAPI, code after ___ in a dependency runs after the response is sent.', ['yield', 'return', 'await', 'Depends'], 0, 'Ngày 44.'),
        ('The main benefit of dependency injection discussed this week:', ['Easier testing with mocks', 'Faster CSS', 'Smaller images', 'Fewer users'], 0, 'Ngày 44.'),
        ('An effect with no dependency array runs…', ['after every render', 'only once', 'never', 'on unmount'], 0, 'Ngày 45.'),
        ('In the blog post, what really fixed the slow home page?', ['Adding servers', 'Adding a database index', 'A new framework', 'Removing images'], 1, 'Ngày 46.'),
        ('In the podcast, what was the hosts\' rule of thumb?', ['Always raw SQL', 'Start with the ORM, measure, raw SQL for hot paths', 'Never use ORMs', 'Switch databases often'], 1, 'Ngày 47.'),
        ('"A and B take 5 and 10 minutes, ___." (lần lượt)', ['respectively', 'respectfully', 'respective', 'in respect'], 0, 'respectively.'),
        ('"The index was missing; ___, queries were slow."', ['consequently', 'in contrast', 'namely', 'arguably'], 0, 'consequently = do đó.'),
        ('Documentation part that lists every function and parameter:', ['Reference', 'Tutorial', 'How-to guide', 'Blog'], 0, 'Reference.'),
    ],
}

WEEK = {
    'title': 'Đọc tài liệu và nghe podcast kỹ thuật',
    'title_en': 'Technical Reading & Podcasts',
    'goal': 'Đọc hiểu tài liệu kỹ thuật và tóm tắt được nội dung podcast công nghệ.',
    'days': [DAY1, DAY2, DAY3, DAY4, DAY5, DAY6],
}
