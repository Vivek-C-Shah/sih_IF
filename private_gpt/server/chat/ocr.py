from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use pytesseract to convert image into text
    text = pytesseract.image_to_string(img)
    return text