# How do I pass command line inputs in python and get back the exit code and standard output
# Designed for linux64 but adaptable to other systems

import os
import subprocess
import time
import datetime

#from subprocess import call

#uses IPC communication instead of creating a child terminal process
def runme(command):

	p = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	stdout_value,err = p.communicate()
	returnc = p.returncode
	return stdout_value, returnc, err

testfile = "file.wav"
array1cmp = "/home/array1cmp"

print "Running some checks"
out,code,err = runme(["./changeRate","1"])
assert code == 1
# output is now the std_out
# code is now the return code
# err is a generic error if the program IPC refused to bind

# Examples from a automated testing script

starttime = time.time()
print "basic upsample then down  x2"
out,code,err = runme(["./changeRate","upsample","polyphase","2",testfile,"sinetest1.wav"])
assert code == 0
out,code,err = runme(["./changeRate","downsample","polyphase","2","sinetest1.wav","sinetest2.wav"])
assert code == 0
out,code,err = runme([array1cmp,"-f",testfile,"-F","sinetest2.wav","-a","-m","mse"])
endtime = time.time()
print "done in (",(endtime-starttime),"s) MSE = " , out
assert code == 0
out,code,err = runme(["rm","sinetest1.wav"])
assert code == 0
out,code,err = runme(["rm","sinetest2.wav"])
assert code == 0