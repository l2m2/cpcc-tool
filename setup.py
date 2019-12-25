# encoding: utf-8

import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="cpcctool",
  version="0.0.1",
  author="l2m2",
  author_email="l2m2lq@gmail.com",
  description="CPCC Tool.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/l2m2/cpcc-tool",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)