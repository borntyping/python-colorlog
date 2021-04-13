from setuptools import setup

setup(
    name="colorlog",
    version="6.0.0-alpha.2",
    description="Add colours to the output of Python's logging module.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sam Clements",
    author_email="sam@borntyping.co.uk",
    url="https://github.com/borntyping/python-colorlog",
    license="MIT License",
    packages=["colorlog"],
    setup_requires=["setuptools>=38.6.0"],
    extras_require={
        ':sys_platform=="win32"': ["colorama"],
        "development": ["black", "flake8", "mypy", "pytest", "types-colorama"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
)
