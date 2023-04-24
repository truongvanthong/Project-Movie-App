# Movie-Website-Django
This is a simple movie review and rating website developed using Django with its built-in Authentication System. It also incorporates other features like 'search' and 'add to favorites, watchlist'. 
Technologies used : - Django, HTML, CSS, Javascript, Ajax, Bootstrap
## Screenshots of the application

* Home page
![image](https://user-images.githubusercontent.com/82353328/233851531-c426b516-5d67-40c8-b948-4147cfc884e6.png)

* Signup Page
![image](https://user-images.githubusercontent.com/82353328/233851613-7334f411-0fbe-4f5e-b3eb-9aaff66e1b3e.png)

* Login Page
![image](https://user-images.githubusercontent.com/82353328/233851687-d2f47f48-f062-4aee-8761-59bd1db9e339.png)

* Dashboard
![image](https://user-images.githubusercontent.com/82353328/233965281-55c7d1b7-2a57-4569-a842-2c0303a032ce.png)
![image](https://user-images.githubusercontent.com/82353328/233965386-9b6eac13-5383-4067-bd64-8ba29620ba87.png)
![image](https://user-images.githubusercontent.com/82353328/233965439-19b5f98e-9d3d-4e33-8dbc-fc5504d84016.png)



* Movie Page
![image](https://user-images.githubusercontent.com/82353328/233852073-32ac64a0-b4e4-4dda-b03d-7ffbb0b982f4.png)
![image](https://user-images.githubusercontent.com/82353328/233852091-58ec1296-5d0e-4599-9cf0-a1714edd6284.png)
![image](https://user-images.githubusercontent.com/82353328/233852101-80a680b5-91a8-4330-bd9b-b55b690b18f2.png)

* All Reviews Page
![image](https://user-images.githubusercontent.com/82353328/233852125-9cfb932e-e20b-4701-a4e6-8e441aaeedd4.png)

* Favourites
![image](https://user-images.githubusercontent.com/82353328/233852172-3b8043b7-bff4-4c1b-a0ae-a7e235c10b5e.png)


* Watchlist
![image](https://user-images.githubusercontent.com/82353328/233852139-b49d4806-bf5f-4684-9668-f219fd4285d0.png)

# Hướng dẫn sử dụng
## Bước 1: Tạo môi trường ảo Python và Cài đặt thư viện 
`windows`
Chạy file
```bash
 > run_venvXinstall_thuvien.bat
 ```
`MacOS`
```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```


## Bước 2. Để thiết lập kết nối tới database, bạn cần chỉnh sửa file `settings.py` trong project của mình. Ví dụ, nếu bạn sử dụng PostgreSQL, bạn có thể sử dụng các thông tin kết nối sau:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Movie_DB',                      
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
> python manage.py makemigrations
> python manage.py migrate
```

`Tạo admin`
```bash
> python manage.py createsuperuser
```

`Mọi người, hãy chạy lệnh này để điền vào cơ sở dữ liệu.`
```bash
> python data_Movie.py
```

### Sử dụng file `run.bat`

Bạn có thể sử dụng file `run.bat` bằng cách chạy lệnh command prompt:
`run.bat`
Sau khi chạy xong, bạn có thể truy cập trang web của mình trên trình duyệt với địa chỉ `http://127.0.0.1:8000/`.
