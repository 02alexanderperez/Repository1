import random
# Gas Level Function
def gasLevelGauge():
    gasLevelList =["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable Calls the value of the gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

#Create If-ELIF-ELSE statements using Comparative Operators to display gas level messages == In order to display messages
def gasLevelAlert():
    gasStationList = ["Shell","BP","CircleK","Citgo","Mobile","Speedway","Marathon","Love's","Meijer","Costco","Sunoco",""]
    randomnumbgen = round(random.uniform(1,25), 1)
    if gasLevelIndicator == "Empty":
        print("******WARNING******\n ****No Gas****\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("**WARNING**\n *Low Gas*\n Nearest Gas Station Is " + random.choice(gasStationList) + " Which is " + str(randomnumbgen) + " Miles Away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Quarter Tank Of Gas Remaining\n Nearest gas station is " + random.choice(gasStationList) + " Which is " + str(randomnumbgen) + " Miles Away")
    elif gasLevelIndicator == "Half Tank":
        print("Half A tank Of Gas Remaining\n 150 miles remaining")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Three Quarters Tank Remaining\n 200 miles remaining ")
    else:
        print("Full Tank Of Gas\n You have 300 Miles Left")

#Call Functions Here
gasLevelAlert()

gasLevelGauge()
