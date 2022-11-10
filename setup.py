"""setup file for ALAT (Advanced Linear Algebra Toolkit)"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

# Long description (README.md) file
long = pathlib.Path(__file__).parent.resolve()
long_description = (long / "README.md").read_text("utf-8")

# setup part
setup(
   name="alat", 
   version="0.1", 
   description="ALAT: Advanced Linear Algebra Toolkit", 
   long_description=long_description, 
   url="https://github.com/", 
   author="Can Gulmez",
   author_email="ahmetcangulmez02@gmail.com", 
   classifiers=[
      "Development Status :: 4 - Beta", 
      "Intendend Audience :: Developers", 
      "Topic :: Sofware Development :: Math :: Linear Algebra", 
      "License :: OSI Approved :: MIT License", 
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6", 
      "Programming Language :: Python :: 3.7", 
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9", 
      "Programming Language :: Python :: 3.10", 
      "Programming Language :: Python :: 3.11",
      "Programming Language :: Python :: 3 :: Only", 
   ], 
   keywords="math, linear algebra, matrices, vectors", 
   package_dir={"": "src"}, 
   packages=find_packages(where="src"),
   python_requires=">= 3.6", 
   project_urls = {
      "Source": "https://github.com/CanGulmez/alat",
   }
)
