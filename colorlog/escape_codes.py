"""
Generates a dictionary of ANSI escape codes

http://en.wikipedia.org/wiki/ANSI_escape_code
"""

__all__ = ['escape_codes']

class AttrDict (dict):
	"""	A dict that can access values both as attributes and as keys """

	def __getattr__ (self, name):
		if name in self:
			return self[name]
		else:
			raise KeyError("'{}' is neither an attribute of a key of the {}".format(name, self.__class__.__name__))

dict = AttrDict

# Returns escape codes from format codes
esc = lambda *x: '\033[' + ';'.join(x) + 'm'

# The initial list of escape codes
escape_codes = AttrDict({
	'reset': esc('39', '49', '0'),
	'bold':  esc('01'),
})

colors = [
	'black',
	'red',
	'green',
	'yellow',
	'blue',
	'purple',
	'cyan',
	'white'
]

# Dicts for the foreground and background colors
escape_codes['fg'] = AttrDict()
escape_codes['bg'] = AttrDict()

# Create foreground and background colors...
for container, layer in [(escape_codes['fg'], '3'), (escape_codes['bg'], '4')]:
	# ...with the list of colors...
	for code, name in enumerate(colors):
		# ...and both normal and bold versions of each color
		code = str(code)
		container[name] = esc(layer + code)
		container["bold_" + name] = esc(layer + code, "01")
