# Spam-SMS

# Hướng dẫn chạy chương trình FastAPI và ReactJS

## Giới thiệu
Đây là một dự án tích hợp giữa FastAPI (backend) và ReactJS (frontend). Chương trình này cho phép bạn thu thập và phân tích các bình luận từ một bài đăng trên Facebook.

## Yêu cầu hệ thống
- Python 3.7+
- Node.js và npm
- MongoDB

## Cài đặt Backend (FastAPI)

1. **Clone repository**:
    ```bash
    git clone https://github.com/NT1610/Spam-SMS.git
    cd Spam-SMS
    ```

2. **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Cấu hình thông tin kết nối database** trong file `acc_pass.py`:
    ```python
    HOST_DB = "localhost"
    NAME_DB = "your_db_name"
    PORT_DB = "port_db"
    COLLECTION_NAME = "name_db"
    ```

4. **Chạy ứng dụng FastAPI**:
    ```bash
    cd Code
    python main.py
    ```

    Ứng dụng sẽ chạy tại `http://127.0.0.1:8000`.

## Cài đặt Frontend (ReactJS)

1. **Di chuyển vào thư mục frontend**:
    ```bash
    cd frontend
    ```

2. **Cài đặt các gói cần thiết**:
    ```bash
    npm install
    ```

3. **Chạy ứng dụng React**:
    ```bash
    npm start
    ```

    Ứng dụng sẽ chạy tại `http://localhost:3000`.

## Cấu trúc dự án
![image](https://github.com/NT1610/Spam-SMS/assets/101975549/4bd2ac1c-3429-4057-b4bb-a09c67fdc4c9)
## Giao diện 
Nhập comment
![image](https://github.com/NT1610/Spam-SMS/assets/101975549/f4e9319a-d380-4002-803b-4d7c48175141)
Nhập Link
![image](https://github.com/NT1610/Spam-SMS/assets/101975549/1c743e22-afe1-4ab0-ae24-15acf9799a4a)
