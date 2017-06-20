
import sys
import latex_access.speech as speech
import latex_access.settings as settings
import os

s=speech.speech()

while True:
	input = sys.stdin.readline()
	output=s.translate(input)
	print output
