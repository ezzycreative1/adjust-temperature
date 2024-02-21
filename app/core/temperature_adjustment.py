from PIL import Image, ImageEnhance
import io

def adjust_temperature(input_file, adjustment_value: float):
    image = Image.open(input_file.file)

    # Adjust temperature by enhancing color
    enhancer = ImageEnhance.Color(image)
    adjusted_image = enhancer.enhance(1 + adjustment_value)

    output_buffer = io.BytesIO()
    adjusted_image.save(output_buffer, format="JPEG")
    return output_buffer.getvalue()
