#get principal
print("Enter principal:")
principal = int(input())

#get interest rate
print("Enter interest rate as a percentage:")
interestrateperc = int(input())

#convert interest rate into a decimal
interestrate = interestrateperc / 100

#get n
print("Enter number of compoundment periods:")
number = int(input())

#get elapsed time
print("Enter time elapsed:")
time = int(input())

#check if information is correct
print("Principal:", principal)
print("Interest rate:", interestrate)
print("Number of compoundment periods:", number)
print("Time elapsed:", time)
print("Is this information correct? (y/n)")
confirmation = input()

if confirmation == "y":
    #run equation: A = P(1+(r/n))^nt
    amount = principal*(1+(interestrate/number))**(number*time)
    print("Final Amount:", amount)

elif confirmation == "n":
    print("Restart program")
else:
    print("Not a valid input.")