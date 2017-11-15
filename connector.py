#This class will be used for database connection,insertion,search

import MySQLdb as mysql

class connector(object):
	"""Database Name : FileIdentification
	   Table Name :    Information
	  """
	cur = None
	db = None
	def __init__(self):
		"""This function will connect to database"""
		connector.db = mysql.connect(host="localhost",db="FileIdentification",user="root")
		connector.cur = connector.db.cursor()


	def search(self,extension):
		"""This function will search the database for given extension"""
		
		connector.cur.execute("SELECT * from Information where extension = %s" , [extension])
		#Simply print them as they are discrete variables
		res = connector.cur.fetchone()
		if res is None:
			return None
		else:
			return res


	def insert(self,extension,description,type,applications):
		"""This function will insert desired record into database"""		
		connector.cur.execute("INSERT INTO Information VALUES(%s,%s,%s,%s)",(extension,description,type,applications))
 		connector.db.commit()

		
