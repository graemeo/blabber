import subprocess
import os

from recorder_abstract import RecorderAbstract

class SoxRecorderImpl(RecorderAbstract):

     def record(self):
         print "Recording..."
         command = "rec -r 16000 -b 16 -V4 resources/capture.wav silence 1 0.1 3% 1 3.0 3%"
         subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).wait()
