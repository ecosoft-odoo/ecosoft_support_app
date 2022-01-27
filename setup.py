from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecosoft_support_app/__init__.py
from ecosoft_support_app import __version__ as version

setup(
	name="ecosoft_support_app",
	version=version,
	description="Ehanced support features for Ecosoft",
	author="Ecosoft",
	author_email="kittiu@ecosoft.co.th",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
