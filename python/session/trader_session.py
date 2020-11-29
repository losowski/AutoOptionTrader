# Trader Session Class
#	Responsible for the specifics of dealing with the trader game

import logging

# Session base class
from python.session import session

# Actions Handler
#TODO: Use the derived class (that outputs this info)
from python.actions import actions

# Observation handler
#TODO: Use the derived class (that interprets this info)
from python.observation import trader_observation


# Message handling
from python.proto import game_pb2

class TraderSession (session.Session):
	def __init__(self, tradeAddr, tradePort):
		super(TraderSession, self).__init__(tradeAddr, tradePort)
		self.logger					=   logging.getLogger('TraderSession')
		# Game variables
		self.gameMeta		=	game_pb2.gameMeta()
		self.gameResponse	=	None
		self.gameRequest	=	game_pb2.gameRequest()

	def __del__(self):
		super(TraderSession, self).__del__()


	# Initialise
	def initialise(self):
		super(TraderSession, self).initialise()
		# Actions
		self.actions		=	actions.Actions()
		# Observations
		self.observations	=	trader_observation.TraderObservation()


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

