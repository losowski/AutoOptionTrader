# AutoTrader main application
#	Responsible for the flow of operations 
#	https://gym.openai.com/docs/
#		- Observe
#		- Act
#		Repeat

import logging

from python.session import session

class AutoTrader (object):

	SESSIONS = 1

	def __init__(self, tradeAddr, tradePort):
		self.logger         =   logging.getLogger('AutoTrader')
		self.tradeAddr		=	tradeAddr
		self.tradePort		=	tradePort
		self.sessions		=	list()


	def __del__(self):
		pass


	# Initialise
	# Setup the sessions
	# Assign a thread to each
	def initialise(self):
		for i in range(self.SESSIONS):
			s = session.Session(self.tradeAddr, self.tradePort)
			s.initialise()
			self.sessions.append(s)			



	# Start the "service"
	def start(self):
		for s in self.sessions():
			



	# Shutdown the "service"
	def shutdown(self):
		pass


