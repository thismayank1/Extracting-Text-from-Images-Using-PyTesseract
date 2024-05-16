import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\91620\tesseract.exe'
from PIL import Image

img = Image.open('text5.jpg')
text = tess.image_to_string(img)
print(text)