#!/bin/sh
#Build the protocol buffer files
protoc  --python_out=../python/proto game.proto
