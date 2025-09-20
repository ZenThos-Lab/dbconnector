# setup.py
from setuptools import setup, Extension, find_packages
from setuptools.command.build_py import build_py as _build_py
from Cython.Build import cythonize
import glob
import os

# 1) Construir la lista de extensiones a partir de todos los .py
exts = []
for path in glob.glob("dbconnector/**/*.py", recursive=True):
    # nombre de módulo estilo paquete (dbconnector.core.factory, etc.)
    modname = path[:-3].replace(os.sep, ".")
    exts.append(Extension(modname, [path]))

# 2) Cythonize
ext_modules = cythonize(
    exts,
    compiler_directives={"language_level": "3"},
    annotate=False,
)


# 3) Evitar que setuptools copie los .py al wheel
class build_py_no_sources(_build_py):
    def find_package_modules(self, package, package_dir):
        # No retornamos módulos puros (.py);
        # ya existen como extensiones compiladas
        return []


setup(
    name="dbconnector",
    version="0.1.0",
    packages=find_packages(include=["dbconnector", "dbconnector.*"]),
    ext_modules=ext_modules,
    cmdclass={"build_py": build_py_no_sources},
    include_package_data=False,
    zip_safe=False,
)
