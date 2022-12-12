class MenuItem:
	def __init__(sef, name, price):
		self.name = name
		self.price = price
		HOSTNAME = ""
		USER = ""
		DBANME = ""
		PASSWORD = ""
		import psycopg2
		connection = psycopg2.connect(hostname=HOSTNAME, USER=username, PASSWORD, password, DBANME=db_name)
		cur = connection.cursor

	def save(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass