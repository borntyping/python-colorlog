# Contributing to colorlog

## New features

Open a thread in the "[Discussions]" section of the GitHub repository before doing any significant work on a new feature. This library is over a decade old, and my priority in maintaining it is stability rather than features. See the [Status](../README.md#Status]) section of the README file for more information.

## Bugfixes

_Please_ provide a simple way to reproduce any bug you encounter when opening an issue. It's very common for bugs to be reported for this library that are actually caused by the calling code or another library being used alongside it.

## Pull requests

Open pull requests against the `main` branch.

Make sure your changes pass the test suite, which runs tests against most recent versions of Python 3 and checks the `black` formatter makes no changes.
   * You can run tests locally with `tox` if you have suitable versions of Python 3 installed...
   * ...or use the GitHub Actions pipeline which will run automatically once you open a pull request. 

[Discussions]: https://github.com/borntyping/python-colorlog/discussions
