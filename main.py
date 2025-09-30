import qrcode

websiteLink = "https://github.com/rawahazkhan"



qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(websiteLink)
qr.make()


img = qr.make_image(fill_color = "black", back_color = "white")
img.save("github_qr.png")