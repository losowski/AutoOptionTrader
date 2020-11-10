# Base model for all the sub-models that make up the AI
#	Each model will use this as a standard framework
#	This will facilitate transfer learning between the models
#	Theory is that this will lead to a better outcome

# NOTE:
#	https://www.tensorflow.org/api_docs/python/tf/keras/Model

import logging


class BaseModel (object):
	def __init__(self, xsize, ysize):
		self.xsize		=	xsize
		self.ysize		=	ysize
		# Model Object
		self.model		=	None

	def __del__(self):
		pass

	# Training steps
	# Random Initialiser
	def initialiseRandom(self):
		pass

	#Load models
	def loadModel(self, filename):
		pass


	#Save model
	def saveModel(self, filename):
		pass


	# Training a single new sample to existing model
	def trainSample(self, data, output):
		pass

	#Train Bulk
	def train(self, dataSet, outputSet):
		pass

	# Get a prediction using the model
	def makePrediction(self, data):
		pass

	

