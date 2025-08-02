# from pyodide import create_proxy
from js import document, console, Uint8Array, window, File
import asyncio

import io
from PIL import Image
import segno
from pyscript import when


@when('click', '#generate-btn')
def generate_qr():
    # Create a 5-H QR code
    content = document.querySelector("#qr_content")
    qrcode = segno.make(content.value, error='h')

    # Save the QR code into a memory buffer as PNG
    out = io.BytesIO()
    qrcode.save(out, scale=5, kind='png')
    out.seek(0)  # Important to let PIL / Pillow load the image
    my_image = Image.open(out)  # Done, do what ever you want with the PIL/Pillow image
    
    my_stream = io.BytesIO()
    my_image.save(my_stream, format="PNG")

    #Create a JS File object with our data and the proper mime type
    image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"})

    #Create new tag and insert into page
    img = document.querySelector("#A")
    img.src = window.URL.createObjectURL(image_file)
