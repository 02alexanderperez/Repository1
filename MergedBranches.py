# Programmer: Alexander Perez
# Date:2/21/22
#Version: 1.1


#Libraries Imported Here
from time import sleep#Print to one line with time delay between prints
import colorama
import random
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

#WELCOME BRANCH
# Code Name - Hornet

print("\033[1;34m Welcome To Hornets InfoTech Center! \n");sleep(1.5)
print(Fore.WHITE + "Hornet's Operating System Booting Up");sleep(0.6)
print(Fore.RED + "Initializing.");sleep(0.5)
print(Fore.RED + " Initializing..");sleep(0.5)
print(Fore.RED + "  Initializing...\n");sleep(0.5)

# GAS BRANCH


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
    randomnumbgen = (random.randint(1,25))
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
