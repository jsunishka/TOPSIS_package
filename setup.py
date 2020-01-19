import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TOPSIS_package", 
    version="0.0.1",
    author="Sunishka Jain",
    author_email="sunishkajain15@gmail.com",
    description="Python package for TOPSIS implementation using Vector Normalization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsunishka/TOPSIS_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
