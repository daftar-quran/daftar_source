
import setuptools
from daftar_common import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    install_requires = [line.strip() for line in f.readlines()]

setuptools.setup(
    name="daftar-common",
    version=__version__,
    author="Daftar-Quran Team",
    author_email="contact.apps.deen@gmail.com",
    description="daftar-common contains all the code source used in the backend app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
