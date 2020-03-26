import pandas as pd


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
        result *= len(data.loc[(data[col] == vars[index])
                                  & (data['o'] == cls)]) / total
        index += 1
    result *= total/len(data)
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
