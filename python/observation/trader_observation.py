# Observation base class
#	Observations are lists of values
import logging

from python.observation import observation

class TraderObservation (observation.Observation):
	def __init__(self):
		self.logger					=   logging.getLogger('TraderObservation')
		super(TraderObservation, self).__init__()

	def __del__(self):
		super(TraderObservation, self).__del__()
		pass

	# Generic BaseClass function for parsing a response
	def parseResponse(self, message):
		# Implement custom code here
		pass
