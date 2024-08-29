import qrcode 

# Generate QR code
data = "https://www.youtube.com/"  # The data or link you want to encode in the QR code

# Create QRCode object with specific parameters
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used
    box_size=10,  # Controls how many pixels each “box” of the QR code is
    border=4,  # Controls how many boxes thick the border should be
)

# Add data to the QRCode object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')

# Save the generated QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
