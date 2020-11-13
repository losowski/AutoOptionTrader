#!/usr/bin/python3
# Run the Auto Trading server 

import sys
import logging
import argparse
import time
import datetime
import signal

# Import the protocol buffer libraries
sys.path.append('python/proto')

# Game Server Session
from python.service import service

#Messages
from python.proto import game_pb2


def main():
	blurb = "Options Trading Game Server"
	print (blurb)
	#Build a datetime object with Current time
	dt = datetime.datetime.now()
	#Make the logging file
	loggingfile = "/tmp/options_trading_game_{timestamp}.log".format(timestamp = dt.now().isoformat())
	#Setup logging
	logging.basicConfig(format='%(asctime)s\t%(name)-16s\t%(funcName)-16s\t[%(levelname)-8s] %(message)s', level=logging.DEBUG)
	#Let everyone know where we logged tp
	print ("Logfile: {logfile}".format(logfile = loggingfile))
	logger = logging.getLogger('main')
	#Begin normal application
	logger.warning(blurb)
	# Parse the args
	parser = argparse.ArgumentParser(description = blurb)
	# Generate the parsed arguments
	args = parser.parse_args()
	logger.info("Args: %s", args)
	# Server
	s = service.Service(10001)
	s.initialise()
	s.start()
	#Clean up everything else...
	#Signal handler needed here to wait before exiting
	sigset = [signal.SIGINT, signal.SIGTERM]
	signal.sigwait(sigset) #3.3 only
	signal.pause()
	#Finally shutdown the server
	ps.shutdown()
	logging.shutdown()
	print("Exiting...")


# Assign a start point to the executable
if __name__ == "__main__":
	main()
