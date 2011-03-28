'''
Created on Feb 21th, 2011

@author: Dmytro Korsakov
'''

from setuptools import setup, findall, find_packages
from distutils.command.install_data import install_data
import platform


description = "Scalr-tools is a command-line interface to your Scalr account"


cfg = dict(
	name = "scalr-tools",
	version = "0.1.0",	 
	description = description,
	long_description = description,
	author = "Scalr Inc.",
	author_email = "info@scalr.net",
	url = "https://scalr.net",
	license = "GPL",
	platforms = "any",
	packages = find_packages(),
	scripts=['bin/scalrtools'],
	install_requires = ["prettytable"],
)
setup(**cfg)


