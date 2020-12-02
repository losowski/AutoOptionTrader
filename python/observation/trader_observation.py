# Observation Trader class
#	Trader state:
#	-	gameStockState			-	Stock figures
#	-	gamePredictionState		-	Prediction
#	-	gamePlayerState			-	Player balance

import logging

# Observation base class
from python.observation import observation

# Message handling
from python.proto import game_pb2

class TraderObservation (observation.Observation):
	def __init__(self):
		super(TraderObservation, self).__init__()
		self.logger					=   logging.getLogger('TraderObservation')
		self.gameState				=	game_pb2.gameState()

	def __del__(self):
		super(TraderObservation, self).__del__()


	# Generic BaseClass function for parsing a response
	# Passed in game_pb2.gameResponse
	def parseResponse(self, message):
		if (message.HasField('state')):
			self.gameState.CopyFrom(message.state)
