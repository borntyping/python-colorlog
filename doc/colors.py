"""
Print every color code supported by colorlog in it's own color.
"""

from colorlog import escape_codes

if __name__ == "__main__":
    for key, value in escape_codes.items():
        print(value, key, escape_codes["reset"])
