import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="setuz",
    version="1.0.1",
    author="Sadullayev Bekhzod",
    author_email="begymrx@gmail.com",
    description="SetUz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests'],
    url="https://github.com/set-uz/setuz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)