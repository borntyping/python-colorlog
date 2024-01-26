"""
Print every color code supported by colorlog in it's own color.
"""

import colorlog.escape_codes

if __name__ == "__main__":
    for key, value in colorlog.escape_codes.escape_codes.items():
        print(value, key, colorlog.escape_codes.escape_codes["reset"])
