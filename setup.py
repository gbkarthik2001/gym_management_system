from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym/__init__.py
from gym import __version__ as version

setup(
	name="gym",
	version=version,
	description="This is GYM app",
	author="Karthik",
	author_email="karthik.gb@promantia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
