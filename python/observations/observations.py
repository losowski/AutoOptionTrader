# Observation base class
import logging

class Observations (object):
	def __init__(self):
		self.logger         =   logging.getLogger('Observations')
		self.observations		=	None
		self.deltaObservations	=	None


	def __del__(self):
		pass


	# Get the change in observation
	def getDeltaObservations(self, observations):
		# - used for iterative differences in values across the board
		#	NOTE: might need proper implementation
		self.deltaObservations = observations - self.observations
		#Return the calculated differences
		return self.deltaObservations
