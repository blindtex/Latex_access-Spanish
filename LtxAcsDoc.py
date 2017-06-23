#-*-:coding:utf-8-*-
#Functions to use latex_access to translate LaTeX written strings to natural speech strings.
import re
import latex_access.speech as speech
import latex_access.settings as settings

sp = speech.speech()

#Regular expression to match anything in math mode. Modified of the one in https://stackoverflow.com/questions/14182879/regex-to-match-latex-equations/14537848#14537848
mathMode = re.compile(r'(?<!\\)(?:((?<!\$)\${1,2}(?!\$))|(\\\()|(\\\[)|(\\begin\{equation\})|(\\begin\{align\*??\}))(.*?(?:)?.*?)(?<!\\)(?(1)(?<!\$)\1(?!\$)|(?(2)\\\)|(?(3)\\\]|(?(4)\\end\{equation\}|\\end\{align\*??\}))))', re.UNICODE)


def extractContent(completeDocument):
	try:
		preamble = completeDocument[:completeDocument.index(r'\begin{document}')]
		document = completeDocument[completeDocument.index(r'\begin{document}'): completeDocument.index(r'\end{document}')+ len(r'\end{document}')]
		epilogue = completeDocument[completeDocument.index(r'\end{document}')+ len(r'\end{document}'):]
	except ValueError:
		print "\\begin{document} or \end{document} not found.\n"
	return [preamble, document, epilogue]
#EndOfFunction


def replaceMath(document):
	return mathMode.sub(toSpeech,document)
#EndOfFucntion

def toSpeech(matchFormula):
	return sp.translate(matchFormula.group(0))
#EndOfFunction

def openFile(fileName):
	try:
		myFile = open(fileName)
		stringDocument = myFile.read()
		myFile.close()
		return stringDocument
	except IOError:
		print "File could not be openned."
#EndOfFunction

