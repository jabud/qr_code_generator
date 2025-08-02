import qrcode

img = qrcode.make('jabud.github.io')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")

print("QR code generated and saved as example_qrcode.png")