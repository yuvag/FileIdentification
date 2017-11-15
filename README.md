FileIdentification is a software designed to fetch details about extensions from web. Details include :

	*	Short Description
	*	Category of file
	*	Associated Applications
	*	Programming Paradigm
	*	Language family


Input : A file containing various extensions(One input file is given for the reference).

Output : A file containing detailed information about the extensions.


REQUIREMENT :

	*	Python 2.0 or more
	*	Working Internet connection


HOW TO USE :
	Start mysql server on your localhost.Following command is used for debian distro:
		service mysql start

	Or you can host online(Change accordingly in connector.py) 
	
	Create a database named 'FileIdentification'. Following command is used for debian distro.
		create database FileIdentification

	run Table.sql file or copy that to make tables.

	Type following command on terminal :
		python main.py

	and follow the instructions


		OR


	Run main.py and follow the instructions.	


