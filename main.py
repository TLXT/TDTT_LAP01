import os
os.environ["HF_HOME"] = r"D:\HuggingFace_Models"

from fastapi import FastAPI, File, UploadFile
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO
from deep_translator import GoogleTranslator
import uvicorn

app = FastAPI()

print("Đang khởi động và kiểm tra mô hình BLIP tại ổ D...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("Tải thành công! Server đã sẵn sàng.")

@app.get("/get")
async def root():
    return {
        "message": "API Sinh mô tả ảnh AI (Sử dụng BLIP)",
        "author": "Trần Lê Xuân Tân",
        "function": "Hỗ trợ 2 cách: Gửi URL ảnh HOẶC upload file ảnh từ máy tính."
    }

@app.get("/health")
async def health_check():
    return {"status": "hoạt động bình thường", "model": "BLIP-base"}

@app.post("/predict")
async def predict_url(image_url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(image_url, headers=headers)
        response.raise_for_status() 

        raw_image = Image.open(BytesIO(response.content)).convert('RGB')
        
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)
        caption_en = processor.decode(out[0], skip_special_tokens=True)
        caption_vi = GoogleTranslator(source='en', target='vi').translate(caption_en)

        return {
            "url": image_url,
            "description_en": caption_en,
            "description_vi": caption_vi,
            "status": "success"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/predict/upload")
async def predict_upload(file: UploadFile = File(...)):
    try:

        contents = await file.read()
        raw_image = Image.open(BytesIO(contents)).convert('RGB')

        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)
        caption_en = processor.decode(out[0], skip_special_tokens=True)

        caption_vi = GoogleTranslator(source='en', target='vi').translate(caption_en)

        return {
            "filename": file.filename,
            "description_en": caption_en,
            "description_vi": caption_vi,
            "status": "success"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
