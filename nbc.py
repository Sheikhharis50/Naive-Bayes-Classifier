import pandas as pd

class LIST:
    def __init__(self):
        self.lst = []
        super().__init__()
    def addToList(self, num):
        if num in self.lst:
            return
        # Sorted Insertion List
        size = len(self.lst)   
        for i in range(0, size):
            prev = i
            if self.lst[i] > num:
                self.lst.insert(prev, num)
                return
        self.lst.append(num)
        return
    def getLength(self):
        return len(self.lst)

class message(object):
    def __init__(self):
        self.cls = []
        self.prob = []
        self.preclass = ''
        self.preprob = 0.0
        super().__init__()
    def create(self, cls, prob):
        self.cls.append(cls)
        self.prob.append(prob)
    def predClass(self, c, p):
        self.preclass = c
        self.preprob = p

def readDataset():
    #   Read data from csv file
    data = pd.read_csv(filepath_or_buffer="data/dataset.csv")
    return data

def getInputs():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    return x,y,z

def readClasses():
    classes = pd.read_csv(filepath_or_buffer="data/classes.csv")
    return classes

def findLikelihood(data, cls, vars):
    result, index = 1.0, 0
    # Get total occurance of a Class
    total = len(data.loc[(data['o'] == cls)])
    # Finding P(x=x,y=y,z=z | output = cl )
    for col in data.columns:
        if col == 'o': break
        ans = len(data.loc[(data[col] == vars[index])
                           & (data['o'] == cls)]) / total
        # if prior become 0
        if ans == 0:
            # geting t which is number of integers
            # and we need it for p = 1/t
            slist = LIST()
            for i in range(0, len(data)):
                slist.addToList(int(data['x'][i]))
                slist.addToList(int(data['y'][i]))
                slist.addToList(int(data['z'][i]))
            # (a + m*p)/(b + m) <= m-estimation formula
            p = (1/slist.getLength())
            ans = (0 + (len(data)*p))/(total+len(data))
        result *= ans
        index += 1
    result *= (total/len(data))
    
    return result

def predictClass(x, y, z):

    # convert inputs into list
    vars = []
    vars.append(int(x))
    vars.append(int(y))
    vars.append(int(z))

    # read dataset
    data = readDataset()
        

    # get Classes
    classes = readClasses()
    
    predictedClass = ''
    sms = message()
    max = 0.0
    # below loop will sending classes, inputs and dataset
    for cl in classes.columns:
        result = findLikelihood(data, cl, vars)
        sms.create(cl, result)
        if result > max: 
            max = result
            predictedClass = cl
    sms.predClass(predictedClass, max)
    return sms
