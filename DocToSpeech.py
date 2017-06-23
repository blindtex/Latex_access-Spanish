#Two functions to use latex_access to translate a document or a string with LaTeX code to speech.
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from LtxAcsDoc import *
import string

def documentToSpeech(fileName):
	docString = openFile(fileName)
	docList = extractContent(docString)
	docList[1] = replaceMath(docList[1])
	return string.join(docList)
#EndOfFunction

def stringToSpeech(stringFile):
	docList = extractContent(stringFile)
	docList[1] = replaceMath(docList[1])
	return string.join(docList)
#EndOfFunction
