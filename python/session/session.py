# A session is a client connection to the game server

import logging
import threading

from python.comms import client

class Session (client.Client):
	def __init__(self, tradeAddr, tradePort):
		super(Session, self).__init__(tradeAddr, tradePort)
		self.logger         =   logging.getLogger('Session')
		self.thread			=	None
		self.live			=	True


	def __del__(self):
		super(Session, self).__del__()



	# Initialise
	def initialise(self):
		super(Session, self).initialise()
		#Create the threads needed
		self.thread = threading.Thread(target=self.run)



	# Play a game on the game server
	def start(self):
		self.logger.info("Starting...")
		self.thread.start()


	# Finish the game
	def shutdown(self):
		self.logger.info("Shutting down...")
		self.live = False
		self.thread.join()


	# Session Running
	def run(self):
		self.logger.info("Thread running")
		while (self.live):
			self.logger.debug("Running the trading game")
