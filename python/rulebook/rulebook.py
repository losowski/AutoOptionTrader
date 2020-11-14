# Rulebook learning
#	The entire model for this is to see what "Changes in observational Data" yield in terms of reward
# Inputs will be a mixture of:
#	Hardcoded rulebook rules
#	Some arbitrary explorations of scenarios (TODO)

import logging

from python.model import base

class Rulebook (base.BaseModel):
	def __init__(self, xsize, ysize):
		super(Rulebook, self).__init__(xsize, ysize)
		self.logger         =   logging.getLogger('Rulebook')


	def __del__(self):
		super(Rulebook, self).__del__()
