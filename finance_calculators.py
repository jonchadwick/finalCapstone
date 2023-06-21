import math
print ("Investment - To calculate the amount of interest you'll receive on your investment")
print ("Bond - To calculate the amount you'll have to pay on a home loan")

selection = input("Please Enter either, Investment or Bond from the menu above to proceed: \n")

#Create an if/elif/else statement to detect if the user selects investment or bond and if not respond with the error message.
#Use the .lower function to change the users input to all lowercase.

if selection.lower() == "investment":
    interest = input("Please select either Simple or Compound: \n")

#Create another if/else statement that checks the user correctly inputted their selecion     
    
    if interest.lower() == "simple" or interest.lower == "compound":
        deposit = float(input("Please enter the amount you are depositing: \n"))
        int_rate = float(input("Please enter the interest rate: \n"))
        years = float(input("Please enter the number of years you plan to invest for: \n"))

#Create an if/else statement that carries out the calculation for either option "simple" or "compound"
        
        if interest.lower() == "simple":
            simple = float(deposit*(1 + (int_rate/100)*years))
            print ("This is the amount of your total investment: " + str(simple))
        else:
            compound = float(deposit * math.pow((1+int_rate/100), years))
            print("This is the total amount of your investment: " + str(compound))
    else:
        print("Please check you have entered either simple or compound")

#This elif statement carries out the process if the user has selected "bond" and asks for the values using the float function to allow decimals.

elif selection.lower() == "bond":
    value = float(input("Please enter the present value of the house: \n"))
    int_rate = float(input("Please enter the rate of interest: \n"))
    months = float(input("Please enter how many months you plan to repay the bond: \n"))

#Create a variable that calculates the interest rate 

    int_rate = (int_rate/100)/12

    repayment = float(int_rate * value)/(1- (1 + int_rate)**(-months))
    print ("Your monthly repayment is: " + str(repayment))
else:
    print ("Please check you have entered a valid option")
         



