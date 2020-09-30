
# Log formatting with colors! -- An amazing project

[![](https://img.shields.io/pypi/v/colorlog.svg)](https://warehouse.python.org/project/colorlog/)
[![](https://img.shields.io/pypi/l/colorlog.svg)](https://warehouse.python.org/project/colorlog/)
[![](https://img.shields.io/travis/borntyping/python-colorlog/master.svg)](https://travis-ci.org/borntyping/python-colorlog)

`colorlog.ColoredFormatter` is a formatter for use with Python's `logging`
module that outputs records using terminal colors.

* [Source on GitHub](https://github.com/borntyping/python-colorlog)
* [Packages on PyPI](https://pypi.python.org/pypi/colorlog)
* [Builds on Travis CI](https://travis-ci.org/borntyping/python-colorlog)

Installation
------------

Install from PyPI with:

```bash
pip install colorlog
```

Several Linux distributions provide official packages ([Debian], [Gentoo],
[OpenSuse] and [Ubuntu]), and others have user provided packages ([Arch AUR],
[BSD ports], [Conda], [Fedora packaging scripts]).

Usage
-----

```python
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
```

The `ColoredFormatter` class takes several arguments:

- `format`: The format string used to output the message (required).
- `datefmt`: An optional date format passed to the base class. See [`logging.Formatter`][Formatter].
- `reset`: Implicitly adds a color reset code to the message output, unless the output already ends with one. Defaults to `True`.
- `log_colors`: A mapping of record level names to color names. The defaults can be found in `colorlog.default_log_colors`, or the below example.
- `secondary_log_colors`: A mapping of names to `log_colors` style mappings, defining additional colors that can be used in format strings. See below for an example.
- `style`: Available on Python 3.2 and above. See [`logging.Formatter`][Formatter].

Color escape codes can be selected based on the log records level, by adding
parameters to the format string:

- `log_color`: Return the color associated with the records level.
- `<name>_log_color`: Return another color based on the records level if the formatter has secondary colors configured (see `secondary_log_colors` below).

Multiple escape codes can be used at once by joining them with commas when
configuring the color for a log level (but can't be used directly in the format
string). For example, `black,bg_white` would use the escape codes for black
text on a white background.

The following escape codes are made available for use in the format string:

- `{color}`, `fg_{color}`, `bg_{color}`: Foreground and background colors.
- `bold`, `bold_{color}`, `fg_bold_{color}`, `bg_bold_{color}`: Bold/bright colors.
- `thin`, `thin_{color}`, `fg_thin_{color}`: Thin colors (terminal dependent).
- `reset`: Clear all formatting (both foreground and background colors).

The available color names are `black`, `red`, `green`, `yellow`, `blue`,
`purple`, `cyan` and `white`.

Examples
--------

![Example output](doc/example.png)

The following code creates a `ColoredFormatter` for use in a logging setup,
using the default values for each argument.

```python
from colorlog import ColoredFormatter

formatter = ColoredFormatter(
	"%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
	datefmt=None,
	reset=True,
	log_colors={
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red,bg_white',
	},
	secondary_log_colors={},
	style='%'
)
```

Using `secondary_log_colors`
------------------------------

Secondary log colors are a way to have more than one color that is selected
based on the log level. Each key in `secondary_log_colors` adds an attribute
that can be used in format strings (`message` becomes `message_log_color`), and
has a corresponding value that is identical in format to the `log_colors`
argument.

The following example highlights the level name using the default log colors,
and highlights the message in red for `error` and `critical` level log messages.

```python
from colorlog import ColoredFormatter

formatter = ColoredFormatter(
	"%(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s%(message)s",
	secondary_log_colors={
		'message': {
			'ERROR':    'red',
			'CRITICAL': 'red'
		}
	}
)
```

With [`dictConfig`][dictConfig]
-------------------------------

```python
logging.config.dictConfig({
	'formatters': {
		'colored': {
			'()': 'colorlog.ColoredFormatter',
			'format': "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
		}
	}
})
```

A full example dictionary can be found in `tests/test_colorlog.py`.

With [`fileConfig`][fileConfig]
-------------------------------

```ini
...

[formatters]
keys=color

[formatter_color]
class=colorlog.ColoredFormatter
format=%(log_color)s%(levelname)-8s%(reset)s %(bg_blue)s[%(name)s]%(reset)s %(message)s from fileConfig
datefmt=%m-%d %H:%M:%S
```

An instance of ColoredFormatter created with those arguments will then be used
by any handlers that are configured to use the `color` formatter.

A full example configuration can be found in `tests/test_config.ini`.

With custom log levels
----------------------

ColoredFormatter will work with custom log levels added with
[`logging.addLevelName`][addLevelName]:

```python
import logging, colorlog
TRACE = 5
logging.addLevelName(TRACE, 'TRACE')
formatter = colorlog.ColoredFormatter(log_colors={'TRACE': 'yellow'})
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('example')
logger.addHandler(handler)
logger.setLevel('TRACE')
logger.log(TRACE, 'a message using a custom level')
```

Compatibility
=============

colorlog works on Python 2.6 and above, including Python 3.

On Windows, [colorama] is required for `colorlog` to work properly.  It will
automatically be included when installing `colorlog` on windows.

Tests
=====

Tests similar to the above examples are found in `tests/test_colorlog.py`.

[`tox`][tox] will run the tests under all compatible python versions.


Projects using colorlog
-----------------------

- [Counterparty]
- [Errbot]
- [Pythran]
- [zenlog]

Licence
-------

Copyright (c) 2012 Sam Clements <sam@borntyping.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[dictConfig]: http://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
[fileConfig]: http://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
[addLevelName]: https://docs.python.org/3/library/logging.html#logging.addLevelNam[addLevelN]e
[Formatter]: http://docs.python.org/3/library/logging.html#logging.Formatter
[tox]: http://tox.readthedocs.org/
[Arch AUR]: https://aur.archlinux.org/packages/python-colorlog/
[BSD ports]: https://www.freshports.org/devel/py-colorlog/
[colorama]: https://pypi.python.org/pypi/colorama
[Conda]: https://anaconda.org/auto/colorlog
[Counterparty]: https://counterparty.io/
[Debian]: https://packages.debian.org/jessie/python-colorlog
[Errbot]: http://errbot.io/
[Fedora packaging scripts]: https://github.com/bartv/python-colorlog
[Gentoo]: https://packages.gentoo.org/packages/dev-python/colorlog
[OpenSuse]: http://rpm.pbone.net/index.php3?stat=3&search=python-colorlog&srodzaj=3
[Pythran]: http://pythonhosted.org/pythran/DEVGUIDE.html
[Ubuntu]: https://launchpad.net/python-colorlog
[zenlog]: https://github.com/ManufacturaInd/python-zenlog
