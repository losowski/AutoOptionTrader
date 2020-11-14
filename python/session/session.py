# A session is a client connection to the game server

import logging

class Session (object):
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


	# Play a game on the game server
	def start(self):
		pass


	# Finish the game
	def shutdown(self):
		pass


