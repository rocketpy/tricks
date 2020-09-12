#  docs:  https://github.com/lincolnloop/python-qrcode
#  pip:  https://pypi.org/project/qrcode/

#  pip install qrcode


# base examples 
import qrcode

img = qrcode.make('Some data here')

#  or

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
