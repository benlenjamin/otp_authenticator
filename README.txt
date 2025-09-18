Programming Project #3: TOTP

Instructions

1. I run the program through the command lines with the format:
    Usage: python totp.py --generate-qr | --get-otp [--forever]
    --forever only works with the --get-otp option and there is basic error handling.
    use ctrl c to exit the forever option.

2. There is a requirements.txt included that has the dependencies,
    install using pip install -r requirements.txt.

Assumptions
1. The account and issuer are hardcoded because the command line implementation
    shown in the assignment description doesn't have any dynamic input.

2  The secret key is also shared globally and hardcoded, which is not the best
    solution but should be fine for this assignment.  Hardcoded secret key allows
    --get-otp to work without first running the other command and saving to a file.

3. The QR Code doesn't display in the terminal, the assignment description just specified
    that it should be saved to a file.  Filename is default: "qrcode.png".

Implementation Explanation

The file is split into three main functions,
1. generate_qrcode(fileName):
    This function generated the initial secret key (which is now hardcoded),
    then uses that (combined with time component) to generate the uri, which
    is then used to generate the QR Code that is saved to the provided filename.

    The URI is provided with the hardcoded account name, issuer name, and secret key.
    The default period is already set to 30 seconds and the default length is already
    equal to 6 so there is no need to specify.

2. get_totp()
    The shortest function in the file, that generates the TOTP using the secret key and
    returns it, used by the main function when the --get-otp option is specified in CLI.

3. main
    This function handles the command line input, exiting if an incorrect number of parameters
    or invalid parameters are inputted. Based on the input, the main function calls either
    generate_qrcode or get_totp, with the latter having the option of running forever [--forever].

    The body of the forever section is surrounded by a try-catch block to allow for escaping
    the sequence using the Keyboard Interrupt (Ctrl-C).


There is basic print statements that provide info on the progression of the program as well
    as the results of actions taken.