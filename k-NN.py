from Asg1 import DCln
import math


def knn(k, atrlst, clsatr, dpartition, kFnct):
    # print('kFnct','----------', kFnct)
    prdctonPercent = []
    for tpIndex in range(len(dpartition['kFoldPartition'])):
        trngPartition = []
        tPartition = []
        index = 0
        for partition in dpartition['kFoldPartition']:
            if tpIndex == index:
                for dObj in partition:
                    tPartition.append(dObj)
            else:
                for dObj in partition:
                    trngPartition.append(dObj)
            index += 1

        prdctonL = []
        for item in tPartition:
            sortDL = kFnct(item,atrlst,clsatr, trngPartition)
            prdCls = getPredictedClass(k, sortDL)
            prdlObj ={'original_class': item[clsatr], 'prediction_class': prdCls}
            if prdlObj['original_class'] == prdlObj['prediction_class']:
                prdlObj['match'] = True
            else:
                prdlObj['match'] = False
            prdctonL.append(prdlObj)
        matchCount = 0
        for item in prdctonL:
            if item['match'] == True:
                matchCount += 1
        prdctonPercent.append((float(matchCount)/float(len(prdctonL)))*100)
    print k,',', reduce(lambda x, y: x + y, prdctonPercent) / len(prdctonPercent)

def calcPDistance(dObj, atrlst, clsatr, trngPartition):
    # print('Polynomial running')
    dList = []
    for data in trngPartition:
        summation = 0.0
        sum1 = 0.0
        sum2 = 0.0
        for attr in atrlst:
            sum1 += (float(dObj[attr])) *(float(dObj[attr]))
            sum2 += (float(data[attr])) * (float(data[attr]))
            summation += (float(dObj[attr]) * float(data[attr]))
        sqrSum = ((1+sum1)*(1+sum1)  - 2*(1+summation)*(1+summation) + (1+sum2)*(1+sum2))
        dList.append({'distance': sqrSum, 'dataClass': data[clsatr]})
    sortDL = sorted(dList, key = lambda data:data['distance'])
    return sortDL


def calcRbfDistance(dObj, atrlst, clsatr, trngPartition):
    # print('RBF running')
    sigma = 0.50
    dList = []
    for data in trngPartition:
        summation = 0.0
        for attr in atrlst:
            summation += (float(dObj[attr]) - float(data[attr]))*(float(dObj[attr]) - float(data[attr]))
        finalSum = math.exp(-(summation )/(sigma * sigma))
        finalSum = 2-2*finalSum
        dList.append({'distance': finalSum, 'dataClass': data[clsatr]})
    sortDL = sorted(dList, key = lambda data:data['distance'])
    return sortDL

def calEcDistance(dObj, atrlst, clsatr, trngPartition):
    dList = []
    for data in trngPartition:
        summation = 0.0
        for attr in atrlst:
            summation += (float(dObj[attr]) - float(data[attr]))*(float(dObj[attr]) - float(data[attr]))
        sqrtSum = math.sqrt(summation)
        dList.append({'distance': sqrtSum, 'dataClass': data[clsatr]})
    sortDL = sorted(dList, key = lambda data:data['distance'])
    return sortDL



def getPredictedClass(k, sortDL):
    dataClassDict = {}

    for index in range(k):
         if sortDL[index]['dataClass'] in dataClassDict:
              dataClassDict[sortDL[index]['dataClass']] += 1
         else:
             dataClassDict[sortDL[index]['dataClass']] = 1

    mcClsCnt = 0
    maxDataClass = None
    for item in dataClassDict:
        if dataClassDict[item] > mcClsCnt:
            mcClsCnt = dataClassDict[item]
            maxDataClass = item
    return maxDataClass
# main fucntion
if __name__ == "__main__" :
    while True:
        try:
            print '\n 1. Ecludian KNN \n 2. Polynomial KNN \n 3. RBF Kernel \n 4. Exit'
            x = int(raw_input("Please enter a choice: "))
            if x == 1:
                print '\n 1. Ecoli Data \n 2. Glass Data \n 3. Yeast Data'
                y = int(raw_input("Please enter a choice: "))
                k = int(raw_input("Please enter k value: "))
                if y == 1:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('ecoli.csv',7)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calEcDistance)
                elif y == 2 :
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('glass_data.csv',9)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calEcDistance)
                elif y == 3:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('yeast_data.csv',8)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calEcDistance)

                else:
                    print "please, enter correct choice!!"
                pass
            elif x == 2:
                print '\n 1. Ecoli Data \n 2. Glass Data \n 3. Yeast Data'
                y = int(raw_input("Please enter a choice: "))
                k = int(raw_input("Please enter k value: "))
                if y == 1:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('ecoli.csv',7)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcPDistance)
                elif y == 2 :
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('glass_data.csv',9)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcPDistance)
                elif y == 3:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('yeast_data.csv',8)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcPDistance)

                else:
                    print "please, enter correct choice!!"

                pass
            elif x == 3:
                print '\n 1. Ecoli Data \n 2. Glass Data \n 3. Yeast Data'
                y = int(raw_input("Please enter a choice: "))
                k = int(raw_input("Please enter k value: "))
                if y == 1:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('ecoli.csv',7)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcRbfDistance)
                elif y == 2 :
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('glass_data.csv',9)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcRbfDistance)
                elif y == 3:
                    dCllOj = DCln()
                    dataList = dCllOj.getDL('yeast_data.csv',8)
                    nDataL = dCllOj.normData(dataList)
                    kfcvObject = dCllOj.kfcv(nDataL,10)
                    atrlst = dCllOj.getAtrL()
                    clsatr = dCllOj.getDClsAtr();
                    knn(k, atrlst, clsatr, kfcvObject, calcRbfDistance)

                else:
                    print "please, enter correct choice!!"

                pass
            elif x== 4:
                break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
