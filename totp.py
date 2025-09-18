# choosing python because of libraries available
# and so I don't have to manually manage memory
import os

import pyotp
import qrcode
from PIL import Image
import sys
import time

# using a global variable to share secret key
SECRET_KEY = "DNZBRP5CL6QA3MO7VZVMPTXRSLONUOM6"

# hardcoding account details
ACCOUNT_NAME = "leonarbe@oregonstate.edu"
ISSUER_NAME = "PP#3: OTP"

def generate_qrcode(fileName = "qrcode.png"):
    # generate a secret key, then use it to generate the URL
    global SECRET_KEY
    # SECRET_KEY = pyotp.random_base32()
    SECRET_KEY = "DNZBRP5CL6QA3MO7VZVMPTXRSLONUOM6"

    totp = pyotp.TOTP(SECRET_KEY)

    # default period is already 30 seconds, default length is = 6
    uri = totp.provisioning_uri(name=ACCOUNT_NAME, issuer_name=ISSUER_NAME)

    # will use the printed key to hardcode for the future
    print(f"Secret Key: {SECRET_KEY}")
    print(f"URI: {uri}")

    qrcodePNG = qrcode.make(uri)
    qrcodePNG.save(fileName)
    print(f"QR Code saved to {fileName}")

####################################################

def get_totp():
    my_totp = pyotp.TOTP(SECRET_KEY)
    return my_totp.now()

####################################################

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python totp.py --generate-qr | --get-otp [--forever]")
        sys.exit(1)

    choice = sys.argv[1]

    if choice == "--generate-qr":
        generate_qrcode()
    elif choice == "--get-otp":
        forever = False
        if (len(sys.argv) > 2):
            if sys.argv[2] == "--forever":
                forever = True
            else:
                print(f"Should never see this, bad arg[2]")

        print(f"Getting TOTP for issuer: {ISSUER_NAME}, account: {ACCOUNT_NAME}")

        try:
            if forever == True:
                print(f"Getting TOTPs every 30 seconds.")

                while True:
                    totp = get_totp()
                    print(f"TOTP: {totp}")
                    time.sleep(30 - (int(time.time()) % 30))
            else:
                totp = get_totp()
                print(f"TOTP: {totp}")
        except KeyboardInterrupt:
            print("TOTP Generation Stopped.")
    else:
        print("Invalid choice. Try again.")
        sys.exit(1)
    sys.exit(0)

