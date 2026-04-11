# Bài Thực Hành Lab 1: Xây Dựng API Trí Tuệ Nhân Tạo (Image Captioning)

## 1. Thông tin sinh viên
* **Họ và tên:** Trần Lê Xuân Tân
* **MSSV:** 24120136

## 2. Thông tin Mô hình (Model)
* **Tên mô hình:** BLIP (Bootstrapping Language-Image Pre-training) - Phiên bản Base.
* **Liên kết Hugging Face:** [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
* **Lý do lựa chọn:** Mô hình nhẹ, chạy mượt mà trên CPU cá nhân nhưng vẫn đảm bảo độ chính xác cao trong việc nhận diện và mô tả chi tiết hình ảnh.

## 3. Mô tả ngắn về chức năng hệ thống
Hệ thống là một Web API được xây dựng bằng **FastAPI**, cung cấp chức năng Nhận diện và Sinh mô tả ảnh (Image Captioning). 
* Hệ thống hỗ trợ 2 phương thức đầu vào: Gửi liên kết ảnh (URL) hoặc Tải trực tiếp file ảnh từ máy tính (Upload).
* Kết quả mô tả bằng tiếng Anh từ mô hình BLIP sẽ được hệ thống tự động dịch sang tiếng Việt thông qua thư viện `deep-translator` trước khi trả về cho người dùng.

## 4. Hướng dẫn cài đặt thư viện
Yêu cầu máy tính đã cài đặt sẵn Python (phiên bản 3.8 trở lên).
Mở Terminal/Command Prompt tại thư mục chứa dự án và chạy lệnh sau để cài đặt toàn bộ môi trường:
```bash
pip install -r requirements.txt
