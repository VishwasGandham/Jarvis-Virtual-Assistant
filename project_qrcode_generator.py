import qrcode
from PIL import Image

of=input("Where shall the QR Code redirect to: ")
name=input("Name of your QR Code: ")
img=qrcode.make(of)
img.save(name+".png")
op=Image.open(r"D:/Educational/Python/"+name+".png")
print("Please wait, opening your QR Code")
op.show()
print()