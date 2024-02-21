from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.core.temperature_adjustment import adjust_temperature
from PIL import Image
import imghdr, io

router = APIRouter()

def is_valid_image(file):
    allowed_formats = {"jpeg"}
    file.seek(0)
    format_info = imghdr.what(file)
    return format_info in allowed_formats

@router.post("/adjust-temperature")
async def adjust_temperature_endpoint(input_file: UploadFile = File(...), adjustment_value: float = 0.0):
    try:
        if not is_valid_image(input_file.file):
            raise HTTPException(status_code=400, detail="Invalid image format. Only JPEG is allowed.")
        
        adjusted_image = adjust_temperature(input_file, adjustment_value)
        return StreamingResponse(io.BytesIO(adjusted_image), media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename=output.jpg"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
