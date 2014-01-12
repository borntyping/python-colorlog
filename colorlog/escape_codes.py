"""
Generates a dictionary of ANSI escape codes

http://en.wikipedia.org/wiki/ANSI_escape_code
"""

__all__ = ['escape_codes']

# Returns escape codes from format codes
esc = lambda *x: '\033[' + ';'.join(x) + 'm'
esc_alt = lambda *x: '\033[1;' + ';'.join(x) + 'm'

# The initial list of escape codes
escape_codes = {
    'reset': esc('39', '49', '0'),
    'bold': esc('01'),
}

# The color names
colors = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'purple',
    'cyan',
    'light_gray'
]

alt_colors = [
    'dark_gray',
    'light_red',
    'light_green',
    'light_yellow',
    'light_blue',
    'light_purple',
    'light_cyan',
    'white'
]

# Create foreground and background colors...
for lcode, lname in [('3', ''), ('4', 'bg_')]:
    # ...with the list of colors...
    for code, name in enumerate(colors):
        code = str(code)
        # ...and both normal and bold versions of each color
        escape_codes[lname + name] = esc(lcode + code)
        escape_codes[lname + "bold_" + name] = esc(lcode + code, "01")

# Create foreground and background colors...
for lcode, lname in [('3', ''), ('4', 'bg_')]:
    # ...with the list of colors...
    for code, name in enumerate(alt_colors):
        code = str(code)
        # ...and both normal and bold versions of each color
        escape_codes[lname + name] = esc_alt(lcode + code)
        escape_codes[lname + "bold_" + name] = esc_alt(lcode + code, "01")