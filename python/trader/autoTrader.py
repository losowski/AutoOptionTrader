# AutoTrader main application
#	Responsible for the flow of operations 
#	https://gym.openai.com/docs/
#		- Observe
#		- Act
#		Repeat

import logging

class AutoTrader (object):
	def __init__(self, tradeAddr, tradePort):
		self.logger         =   logging.getLogger('AutoTrader')
		self.tradeAddr		=	tradeAddr
		self.tradePort		=	tradePort
		pass


	def __del__(self):
		pass


	# Initialise
	def initialise(self):
		pass


	# Start the "service"
	def start(self):
		pass


	# Shutdown the "service"
	def shutdown(self):
		pass


