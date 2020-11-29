# A session is a client connection to the game server
#	Game specific code is added in the next level up

import logging
import threading

from python.comms import client
# Actions Handler
from python.actions import actions

# Observation handler
from python.observation import observation


class Session (client.Client):
	def __init__(self, tradeAddr, tradePort):
		super(Session, self).__init__(tradeAddr, tradePort)
		self.logger         =   logging.getLogger('Session')
		self.thread			=	None
		self.live			=	True
		# Actions
		self.actions		=	None
		# Observations
		self.observations	=	None

	def __del__(self):
		super(Session, self).__del__()



	# Initialise
	def initialise(self):
		super(Session, self).initialise()
		#Create the threads needed
		self.thread = threading.Thread(target=self.run)
		## Actions
		#self.actions		=	actions.Actions()
		## Observations
		#self.observations	=	observation.Observation()




	# Play a game on the game server
	def start(self):
		self.logger.info("Starting...")
		self.thread.start()


	# Finish the game
	def shutdown(self):
		self.logger.info("Shutting down...")
		self.live = False
		self.thread.join()


	# Reset Game data except for metadata
	def resetRequest(self):
		pass


	# Send the request to the game Server
	#	Also process the response into a protocol buffer message
	def sendGameRequest(self):
		pass


	# Parse the response
	def parseResponse(self):
		pass


	# Session Running
	def run(self):
		self.logger.info("Thread running")
		# Send the metadata to choose the game to play
		self.resetRequest()
		# Get response and store the metadata we are playing on
		self.sendGameRequest()
		# Now process the loop of actions
		while (self.live):
			self.logger.debug("Running the game")
			# If sending was OK, parse the response
			# Check the response
			#	Internalise Observations
			#	Internalise state
			self.parseResponse()
			#	Decide Actions
			#TODO: Write this code
			#	Send the response
			self.sendGameRequest()
