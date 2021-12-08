import setuptools

with open("README.txt", "r") as fn:
    long_description = fn.read()

setuptools.setup(
    name="wxmp",
    version="0.1",
    author="Christopher Phillips of UAH, Huntsville, Alabama",
    author_email="cephillips574@gmail.com",
    description="A python package for accessing and visualizing numerical model output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sodoesaburningbus/atmos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires='>=3.0',
)
