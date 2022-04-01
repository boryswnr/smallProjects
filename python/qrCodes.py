import qrcode

data = "https://boryswnr.github.io/cv/"

# img = qrcode.make(data)
#
# img.save("/home/borys/Documents/qrCodeFromPython1.svg")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

qrImg = qr.make_image(fill_color = 'red', back_color = 'black')

# below commented so as to not create file by mistake
# qrImg.save("/home/borys/Documents/cvqr")