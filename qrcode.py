import pyqrcode                 # pip install pyqrcode
import os                       # built-in module
import png                      # pip install pypng
from pyqrcode import QRCode     # pip install pyqrcode
  

# takes the string as input of what user exactly wants qr code of  
user_inp = input("Please type of what QR Code your want : ")  
print(os.getcwd())
# Generate QR code
url = pyqrcode.create(user_inp)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)