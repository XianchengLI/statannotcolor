from distutils.core import setup
from setuptools import find_packages
import re

with open("readme.md", "r") as f:
    long_description = f.read()

VERSIONFILE = "statannotcolor/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="statannotcolor",
    version=version,
    author="Xiancheng LI",
    author_email="Xiancheng.li@hotmail.com",
    description="add color to statannot",
    long_description_content_type="text/markdown",
    long_description=long_description,   
    url="https://github.com/XianchengLI/statannotcolor",
    download_url = "https://github.com/XianchengLI/statannotcolor/archive/refs/tags/v0.1.1.tar.gz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open("requirements.txt").readlines(),
    python_requires='>=3.5',
)
