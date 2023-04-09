# Movie-Website-Django

## Bước 1: Tạo môi trường ảo Python

Để sử dụng code này, bạn cần tạo một môi trường ảo Python và cài đặt các package cần thiết. Bạn có thể thực hiện các bước sau để tạo môi trường ảo Python:

`python -3.9 -m venv .venv`


Lệnh này sẽ tạo một môi trường ảo Python với tên `.venv` trong thư mục hiện tại. Bạn có thể thay đổi tên môi trường ảo tùy ý.

## Bước 2: Kích hoạt môi trường ảo Python

Sau khi tạo môi trường ảo Python, bạn cần kích hoạt môi trường này trước khi sử dụng code của bạn. Bạn có thể thực hiện các bước sau để kích hoạt môi trường ảo Python:

### Trên Windows:
`.venv\Scripts\activate`

### Trên Linux hoặc macOS:
`source .venv/bin/activate`

Lệnh này sẽ kích hoạt môi trường ảo Python và thêm tiền tố `(venv)` vào trước dấu nhắc lệnh.

## Bước 3. Để thiết lập kết nối tới database, bạn cần chỉnh sửa file `settings.py` trong project của mình. Ví dụ, nếu bạn sử dụng PostgreSQL, bạn có thể sử dụng các thông tin kết nối sau:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_DB',                      
        'USER': 'postgres',
        'PASSWORD': 'thong',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Trong đó:

- `ENGINE`: Loại database backend sử dụng (trong trường hợp này là PostgreSQL).
- `NAME`: Tên của database.
- `USER`: Tên đăng nhập để truy cập database.
- `PASSWORD`: Mật khẩu để truy cập database.
- `HOST`: Địa chỉ của database server (trong trường hợp này là localhost).
- `PORT`: Cổng kết nối tới database (trong trường hợp này là 5432 cho PostgreSQL).

Bạn có thể sửa file **settings.py** trong project của mình để thêm các thông tin kết nối tới database của bạn. Lưu ý rằng, bạn cần phải cài đặt driver tương ứng cho database của mình (ví dụ: psycopg2 cho PostgreSQL) để Django có thể kết nối và thao tác với database.

## Bước 4: Cài đặt các package, thêm dữ liệu vào database và chạy server
```bash
 > pip install -r requirements.txt
 ```
```bash
> python manage.py makemigrations
> python manage.py migrate
```

`Mọi người, hãy chạy lệnh này để điền vào cơ sở dữ liệu.`
```bash
> python data_Movie.py
```

### Sử dụng file `run.bat`

Bạn có thể sử dụng file `run.bat` bằng cách chạy lệnh command prompt:
`run.bat`
Sau khi chạy xong, bạn có thể truy cập trang web của mình trên trình duyệt với địa chỉ `http://127.0.0.1:8000/`.

