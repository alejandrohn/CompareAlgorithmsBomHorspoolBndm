import subprocess
from decimal import *
from subprocess import PIPE,Popen
import string
import random
import gc

GENOMEPATH = './hs_ref_GRCh38.p12_chr1.fa'
BOMFILENAME = './bom.txt'
HORSPOOLFILENAME = './horspool.txt'
BNDMFILENAME = './bndm.txt'

def bndmAlgorithm(genomePath, pattern):
	bndn = Popen(['./bndm.out',genomePath , pattern], stdout=PIPE)
	result = float(bndn.communicate()[0].split()[-1])
	return result

def bomAlgorithm(genomePath, pattern):
	bom = Popen(['./bom.out', genomePath,pattern], stdout=PIPE)
	result = float(bom.communicate()[0].split()[-1])
	return result

def horspoolAlgorithm(genomePath, pattern):
	horspool = Popen(['./horspool.out', genomePath,pattern], stdout=PIPE)
	result = float(horspool.communicate()[0].split()[-1])
	return result

def getRandomLetter():
	return random.choice(['C','G','A','T'])

def generateSequence(size):
	result =''
	for x in range(size):
		result += getRandomLetter()
	return result

def compareTimeOfAlgorithmToN(size):
	for size in range(1, size + 1):
		compareTimeOfAlgorithmSizeN(size)


def compareTimeOfAlgorithmToN(startSize, endSize):
	for size in range(startSize, endSize + 1):
		compareTimeOfAlgorithmSizeN(size)



def compareTimeOfAlgorithmSizeN(size):
		sequencePattern = generateSequence(size)
		bomCalculateAndWrite(sequencePattern, size)
		horspoolCalculateAndWrite(sequencePattern, size)
		bndmCalculateAndWrite(sequencePattern, size)


def bndmCalculateAndWrite(sequencePattern, size):
		bndmTime = bndmAlgorithm(GENOMEPATH, sequencePattern)
		writeInTxt(BNDMFILENAME, size, bndmTime)

def bomCalculateAndWrite(sequencePattern, size):
		bomTime = bomAlgorithm(GENOMEPATH, sequencePattern)
		writeInTxt(BOMFILENAME, size, bomTime)


def horspoolCalculateAndWrite(sequencePattern, size):
		horspoolTime = horspoolAlgorithm(GENOMEPATH, sequencePattern);
		writeInTxt(HORSPOOLFILENAME, size, horspoolTime)

def writeInTxt(fileName, sizeSequence,time):
	f = open(fileName, "a")
	f.write(sizeSequence.__str__() + ':' + ' ' + time.__str__() + '\n')
	f.close()

def generateSequenceToN(start, end):
	for i in range(start, end + 1):
		print generateSequence(i)



#compareTimeOfAlgorithmSizeN(100)
#compareTimeOfAlgorithmToN(246,250)
#generateSequenceToN(186,197)




















