#!/usr/bin/env/ pyhton3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aleblucher",
    version="0.0.1",
    author="Alessandra Blucher",
    author_email="emaildaalessandra@example.com",
    description="Descricao",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aleblucher/project-structure",
    scripts = ['scripts/hello.py'],
    packages=setuptools.find_packages(),
    install_requires = ['decorator==4.4.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7'
)