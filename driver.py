import nbc
from nbc import message
# using naive baise classifer

x,y,z = nbc.getInputs()
# get user inputs

sms = nbc.predictClass(x,y,z)
# it will give you the predicted class 
# using given inputs

for i in range(0, len(sms.cls)):
    print("Class ",sms.cls[i]," have " ,sms.prob[i]," probability")
print("Hence,")
print("Predicted Class is ",sms.preclass," with highest probability ", sms.preprob)
