from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="create a python package",
    version="2.0",
    description="A Python package to learn to create one",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/deeptij2007/python_package.git",
    author="Deepti Joshi",
    author_email="deeptij2007@gmail.com",
    license="MIT",
    
    packages=["mypackage"],
    include_package_data=True,
)