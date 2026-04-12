# Lab 1: APPLICATION PROGRAMMING INTERFACE
# GVHD: Lê Đức Khoan

## 1. Thông tin sinh viên
* **Họ và tên:** Trần Lê Xuân Tân
* **MSSV:** 24120136

---

## 2. Thông tin Mô hình (Model)
* **Tên mô hình:** `BLIP` (Bootstrapping Language-Image Pre-training) - Phiên bản Base.
* **Liên kết Hugging Face:** [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
* **Lý do lựa chọn:** Đây là một mô hình được tối ưu cực kỳ tốt, dung lượng nhẹ. Nó cho phép suy luận mượt mà và ổn định trên phần cứng CPU cá nhân nhưng vẫn đảm bảo độ chính xác cao trong việc nhận diện và mô tả chi tiết hình ảnh.

---

## 3. Mô tả chức năng hệ thống
Hệ thống là một Web API được xây dựng bằng framework **FastAPI**, cung cấp chức năng Nhận diện và Sinh mô tả ảnh tự động (Image Captioning) dựa trên công nghệ học sâu.

* **Đa dạng đầu vào:** Hỗ trợ 2 phương thức linh hoạt: Nhận diện qua đường dẫn liên kết mạng (`URL`) HOẶC nhận diện trực tiếp qua file ảnh tải lên từ máy tính (`Upload`).
* **Phiên dịch tự động:** Kết quả mô tả gốc bằng tiếng Anh từ mô hình BLIP sẽ được hệ thống tự động dịch sang tiếng Việt thông qua thư viện `deep-translator` trước khi đóng gói trả về cho người dùng.

---

## 4. Hướng dẫn cài đặt môi trường
Yêu cầu máy tính đã cài đặt sẵn Python (khuyến nghị phiên bản `3.8` trở lên).
Mở Terminal (hoặc Command Prompt) tại thư mục chứa dự án và chạy lệnh sau để tự động cài đặt toàn bộ môi trường và các thư viện phụ thuộc:

```text
pip install -r requirements.txt
```
---

## 5. Hướng dẫn chạy chương trình
Sau khi cài đặt xong thư viện, khởi động Server bằng lệnh sau tại Terminal:
```text
uvicorn main:app --reload
```
* Server sẽ khởi chạy mặc định tại địa chỉ Localhost: http://127.0.0.1:8000.

* Trải nghiệm giao diện tương tác trực quan (Swagger UI) tại: http://127.0.0.1:8000/docs.

## 6. Hướng dẫn gọi API & Ví dụ
Dự án có đi kèm file test_api.py sử dụng thư viện requests để tự động hóa việc gọi API. Bạn mở một Terminal mới và chạy lệnh sau để kiểm thử:

```text
python test_api.py
```
Cấu trúc Request & Response mẫu (Endpoint POST /predict/upload):

* Phương thức: POST

* Dữ liệu gửi đi (Body): File ảnh (.jpg, .png) định dạng multipart/form-data.

* Kết quả trả về (JSON Format):

```JSON
{
  "filename": "anh_test.jpg",
  "description_en": "a cat sitting on a laptop computer",
  "description_vi": "một con mèo ngồi trên máy tính xách tay",
  "status": "success"
}
```
## 7. Video Demo tính năng
Thầy/Cô vui lòng truy cập liên kết bên dưới để xem video demo chi tiết toàn bộ quá trình khởi động server, lấy link public và kiểm thử hệ thống:
