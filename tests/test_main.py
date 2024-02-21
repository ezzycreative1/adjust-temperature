from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_adjust_temperature():
    with open("path/to/input.jpg", "rb") as image_file:
        files = {"input_file": ("input.jpg", image_file, "image/jpeg")}
        response = client.post("/adjust-temperature", files=files, data={"adjustment_value": 0.1})
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
    assert response.headers["content-disposition"] == 'attachment; filename="output.jpg"'
