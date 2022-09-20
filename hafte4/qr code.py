#Qr Code
import qrcode
text = input('enter your adress:\n')
Qr = qrcode.make(text)
Qr.save('text_qrcode.jpg')