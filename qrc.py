import qrcode
qr=qrcode.QRCode(version=1,box_size=10,border=5)
data="Your text/data here"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_colour="white")
img.save("test.png")