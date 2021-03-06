'''
yy grad proj utils
find files in csv that dont exist in source(feature) dir
input
	csv path
	feature path
'''

import os
import pandas
import sys


def selectFile(csvPath, featurePath):
	f = open(csvPath, 'r')
	csv = pandas.read_csv(f)
	csvdirs = csv['dirname']
	defects = csv['bug']
	f.close()
	defectNum = 0
	for defect in defects:
		if defect == 1:
			defectNum += 1
	print defectNum
	featuredirs = os.listdir(featurePath)
	for csvdir in csvdirs:
		fileName = csvdir.split('.')[-1]
		num = 0
		fileList = []
		for featuredir in featuredirs:
			featurefileName = featuredir.split('.')[-2]
			if fileName == featurefileName:
				num += 1
				fileList.append(featuredir)
		if num == 0:
			print csvdir


if __name__ == '__main__':
	selectFile(sys.argv[1], sys.argv[2])