# Observation base class
#	Observations are lists of values
import logging

class Observation (object):
	def __init__(self):
		self.logger					=   logging.getLogger('Observation')
		self.observation			=	list()
		self.previousObservation	=	list()
		self.deltaObservation		=	list()
		self.changed				=	False


	def __del__(self):
		pass


	# Set the current observation
	#	Only update the previous Observation pattern if this has changed
	def updateObservation(self, observation):
		# Store the current observation locally
		obs	=	observation
		# Check if has changed
		self.__diffObservations(obs)
		if (self.hasChanged() == True):
			self.previousObservation = self.observation
			self.observation = observation


	# Confirm if the state has changed
	def hasChanged(self):
		return self.changed


	# Diff the observations
	def __diffObservations(self, newObservation):
		self.changed = False
		if(len(self.observation) == len(newObservation)):
			self.logger.debug("Comparison in length OK")
			diff = list()
			for i,x in enumerate(self.observation):
				# Element comparator
				try:
					# Try a numerical comparator
					d  = int(newObservation[i]) - int(x)
				except:
					# For WTF moments of bad encoding
					self.logger.warning("Bad comparator: %s - %s", newObservation[i], x)
					d = -1	# -1 represents default change
				# Check for changes
				if (diff == 0):
					self.changed = True
				# Build the self.changed
				diff.append(d)
			if (self.changed == True):
				self.deltaObservation = diff
		else:
			self.logger.error("Observations of different lengths")
			self.changed = True


	# Get the change in observation
	def getDeltaObservation(self, observation):
		#Return the calculated differences
		return self.deltaObservation


	# Generic BaseClass function for parsing a response
	def parseResponse(self, message):
		# Implement custom code here
		pass
