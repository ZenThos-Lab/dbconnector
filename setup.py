# setup.py
from setuptools import setup
from Cython.Build import cythonize
import pathlib

HERE = pathlib.Path(__file__).parent

setup(
    name="dbconnector",
    version="0.1.0",
    ext_modules=cythonize(
        ["dbconnector/**/*.py"],
        compiler_directives={"language_level": "3"},
        annotate=False,
    ),
    zip_safe=False,
    include_package_data=False,
)
