from setuptools import setup, find_packages

setup(
    name = "myPackage",
    version = "0.1",
    packages = find_packages(exclude = ["*tests*"]),
    license = "MIT",
    description = "EDSA python package example",
    long_description = open("README.md").read(),
    install_requires = ["numpy"],
    url = "https://github.com/<username>/<package-name",
    author = "Efugha Chibuikem Godwin",
    author_email= "chykegce@gmail.com")