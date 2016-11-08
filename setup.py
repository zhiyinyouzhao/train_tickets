#!/usr/bin/env python
#coding = utf-8

from setuptools import setup

setup(
	name = 'train_ticket_inquiries',
	version = '1.0',
	packages = ['train_ticket_inquiries'],
	include_package_data = True,
	zip_safe = True,
	install_requires = ['requests','docopt','prettytable'],
	entry_points = {
		'console_scripts':['tickets = train_ticket_inquiries.train_data:click_information']
		}
		)
