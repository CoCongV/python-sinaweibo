from setuptools import setup, find_packages
from os.path import dirname, join


with open(join(dirname(__file__), "VERSION.txt"), "rb") as f:
    version = f.read().decode("ascii").strip()


setup(
    name="python-sinaweibo",
    version=version,
    description="",
    packages=find_packages(exclude=[]),
    author="Cong Lv",
    author_email="cong.lv@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
