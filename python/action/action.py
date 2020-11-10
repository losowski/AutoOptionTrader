# Base Action class
#	Actions are made with the following:
#	- Clear observation data
#	- Clear reward objective
#	- Clear understanding how actions will change the observed environment
#		- Both what we see, and the amount we can see

import logging


class Actions (object):
	def __init__(self):
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

	# Generate the action
	def getAction(self, observations, reward)
		deltaObs = self.getDeltaObservations(observations)
		# TODO: pass deltaObs and reward into a model to calculate the appropriate action
