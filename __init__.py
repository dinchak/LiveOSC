import sys

path = "/Users/mac/src/node-liveosc"
errorLog = open(path + "/stderr.txt", "w")
errorLog.write("Starting Error Log")
sys.stderr = errorLog
stdoutLog = open(path + "/stdout.txt", "w")
stdoutLog.write("Starting Standard Out Log")
sys.stdout = stdoutLog

from LiveOSC import LiveOSC

def create_instance(c_instance):
    return LiveOSC(c_instance)
