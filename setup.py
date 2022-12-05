from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in copycatesd/__init__.py
from copycatesd import __version__ as version

setup(
	name="copycatesd",
	version=version,
	description="ERPNext Integration to the Copy Cat Group ESD Gadget",
	author="Geoffrey Karani",
	author_email="geoffrey.kamundi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
