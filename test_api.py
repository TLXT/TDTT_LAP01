import requests

api_url = "http://127.0.0.1:8000/predict/upload"
image_path = "anh_test.jpg" 

print(f"Đang tải ảnh '{image_path}' lên server...")

try:
    with open(image_path, "rb") as image_file:
        files = {"file": (image_path, image_file, "image/jpeg")}
        response = requests.post(api_url, files=files)
        
    response.raise_for_status() 
    result = response.json()
    
    print("================ KẾT QUẢ ================")
    if result.get("status") == "success":
        print(f"Tên file: {result['filename']}")
        print(f"Bản tiếng Anh: {result['description_en']}")
        print(f"Bản tiếng Việt: {result['description_vi']}")
    else:
        print(f"Lỗi từ hệ thống: {result.get('message')}")
    print("=========================================")

except FileNotFoundError:
    print(f"[ LỖI ] Không tìm thấy file '{image_path}'. Vui lòng kiểm tra lại.")
except requests.exceptions.ConnectionError:
    print("[ LỖI ] Không thể kết nối tới Server. Hãy kiểm tra xem uvicorn đã chạy chưa.")
except Exception as e:
    print(f"Lỗi không xác định: {e}")