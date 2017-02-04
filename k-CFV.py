import csv
import random

class DCln(object):

	def __init__(self):
		
		self.dataList = []
		self.atrlst = []
		self.minAttrVal = []
		self.maxAttrVal = []
		self.dataClass = None


	
	def getDL(self, fileName, classIndex):
		with open(fileName, 'rU') as file:

			reader = csv.reader(file)
			isFirstRow = True
			for row in reader:
				if isFirstRow:
					isFirstRow = False
					index = 0
					for data in row:
						if index == classIndex:
							self.dataClass = row[index]
							index += 1
						else:
							self.atrlst.append(row[index])
							self.minAttrVal.append(None)
							self.maxAttrVal.append(None)
							index += 1
				else:
					rowObject = {}
					index = 0
					for  data in row:
						if index == classIndex:
							rowObject[self.dataClass] = row[index];
							index += 1
						else:
							rowObject[self.atrlst[index]] = row[index]
							if self.minAttrVal[index] is None:
								self.minAttrVal[index] = row[index]
							elif self.minAttrVal[index] < row[index]:
								self.minAttrVal[index] = row[index]

							if self.maxAttrVal[index] is None:
								self.maxAttrVal[index] = row[index]
							elif self.maxAttrVal[index] > row[index]:
								self.maxAttrVal[index] = row[index]
							index += 1
					self.dataList.append(rowObject)

	
			return self.dataList

	def getAtrL(self):
		return self.atrlst
	
	def getDClsAtr(self):
		return self.dataClass

	def normData(self, dataList):

		nDataL = []
		for row in dataList:
			rowObject = {}
			index = 0
			for attr in self.atrlst:
				
				rowObject[attr] = (float(row[attr]) - float(self.minAttrVal[index]))/(float(self.maxAttrVal[index]) - float(self.minAttrVal[index]))

				index += 1
			rowObject[self.dataClass] = row[self.dataClass]
			nDataL.append(rowObject)
		# print nDataL
		return nDataL
	
	
	def kfcv(self, dataList, k):

		noOfSamples = len(dataList)
		if k > noOfSamples or k < 1:
			print "unacceptable k value :", k
			return None
		shuffleList = []
		for x in range(0,noOfSamples):
			shuffleList.append(x)

		random.shuffle(shuffleList)
		shuffuledKList = []
	
		i = 0
		for y in range(0,k):
			if y ==  k-1:

				singlePartition = [];
				j = i
				for z in range(0, (noOfSamples - j)):
					singlePartition.append(dataList[shuffleList[i]])
					# print 'z--', i
					i += 1
				shuffuledKList.append(singlePartition)
			else:
				singlePartition = [];
				for a in range(0,(noOfSamples/k)):

					singlePartition.append(dataList[shuffleList[i]])
					# print 'a--', i
					i += 1
				shuffuledKList.append(singlePartition)
			# print '\n'
		# print len(shuffuledKList[0])
		return { 'kFoldPartition': shuffuledKList}

	

