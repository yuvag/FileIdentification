""" This module will help to scrap information from web"""

"""Information provided will be shortdescription,applications associated,
programming paradigm,category of file,language family"""

from lxml import html
import requests

class webScrapper(object):

	tree = None 
	def __init__(self,extension):
		"""This function will fetch html content of webpage"""

		url = 'https://www.fileinfo.com/extension/' + extension
		headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
		page = requests.get(url,headers=headers)
		webScrapper.tree = html.fromstring(page.content)
	
	def shortDescription(self):
		"""This function will return short description of the extension"""
		description = webScrapper.tree.xpath('//span[@itemprop="description"]/text()')
		return ''.join(description)


	def fileType(self):
		"""This function will return category of the file"""
		type = webScrapper.tree.xpath('//span[@itemprop="name"]/text()')
		return ''.join(type)

	def associatedApplications(self):
		"""This function will return associated applications for the file"""
		applications = webScrapper.tree.xpath('//table[@class="programs"]//table[@class="apps"]//a/text()')
		return ','.join(applications)		 

