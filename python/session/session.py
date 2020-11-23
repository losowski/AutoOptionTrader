# A session is a client connection to the game server

import logging
import threading

from python.comms import client
# Actions Handler
#TODO: Use the derived class (that outputs this info)
from python.actions import actions

# Observation handler
#TODO: Use the derived class (that interprets this info)
from python.observation import trader_observation


from python.proto import game_pb2

class Session (client.Client):
	def __init__(self, tradeAddr, tradePort):
		super(Session, self).__init__(tradeAddr, tradePort)
		self.logger         =   logging.getLogger('Session')
		self.thread			=	None
		self.live			=	True
		# Game variables
		self.gameMeta		=	game_pb2.gameMeta()
		self.gameResponse	=	None
		self.gameRequest	=	game_pb2.gameRequest()
		# Actions
		self.actions		=	actions.Actions()
		# Observations
		self.observations	=	trader_observation.TraderObservation()

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


	# Reset Game data except for metadata
	def resetRequest(self):
		# Reset the main request
		self.gameRequest	=	game_pb2.gameRequest()
		# Restore the metaData
		self.gameRequest.meta.CopyFrom(self.gameMeta)


	# Send the request to the game Server
	#	Also process the response into a protocol buffer message
	#	Handle the metadata too
	def sendGameRequest(self):
		msg = self.gameRequest.SerializeToString()
		self.send(msg)
		# Get the response too
		data = self.receive()
		self.gameResponse = game_pb2.gameResponse.FromString(data)
		# Get the metadata stored safely for the reset
		if (self.gameResponse.HasField('meta')):
			# Store the response meta data
			self.gameMeta.CopyFrom(self.gameResponse.meta)
		# Ensure the response is OK
		if (self.gameResponse.status != game_pb2.gameStatus.OK):
			self.logger.info("Response Bad - Killing Session")
			# Kill the session
			self.live = False
		# live will only be true if we are OK.


	# Parse the response
	def parseResponse(self):
		# Hand data to the observation
		self.observation.parseResponse(self.gameResponse)


	# Session Running
	def run(self):
		self.logger.info("Thread running")
		# Send the metadata to choose the game to play
		self.resetRequest()
		# Get response and store the metadata we are playing on
		self.sendGameRequest()
		# Now process the loop of actions
		while (self.live):
			self.logger.debug("Running the trading game")
			# If sending was OK, parse the response
			# Check the response
			#	Internalise Observations
			#	Internalise state
			self.parseResponse()
			#	Decide Actions
			#TODO: Write this code
			#	Send the response
			self.sendGameRequest()
