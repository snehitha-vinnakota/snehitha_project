from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in snehitha_app/__init__.py
from snehitha_app import __version__ as version

setup(
	name="snehitha_app",
	version=version,
	description="Snehitha_App",
	author="Snehitha",
	author_email="vinnakotasnehithaa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
