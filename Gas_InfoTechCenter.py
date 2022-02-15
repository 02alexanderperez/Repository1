import random


# Gas Level Function
def gasLevelGauge():
    gasLevelList =["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    #print(currentGasLevel)
    return currentGasLevel



#Create If-ELIF-ELSE statements using Comparative Operators to display gas level messages

def gasLevelAlert():
    if gasLevelAlert()  == "Empty":
        print("**WARNING**\n *No Gas*\n Calling Emergency Contact")

#gasLevelAlert()
