try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import requests

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename), lang='eng+equ')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

url = "" #url to image
r = requests.get(url)
open('test.png', 'wb').write(r.content)
print(ocr_core("test.png"))
