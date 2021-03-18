import base64
from PIL import Image
import io

 
with open("5.jpg", "rb") as imageFile:
    string1 = base64.b64encode(imageFile.read())
    print(string1)

f = io.BytesIO(base64.b64decode(string1))
pilimage = Image.open(f)