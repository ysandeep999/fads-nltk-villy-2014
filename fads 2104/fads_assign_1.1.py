# A program to find value of investment 


def main():
        print("This prog cal future value ")
        principal = eval(input("Enter initial principal: "))
        
        year = eval(input("Enter number of years: "))
        interest = eval(input("Enter annual interest rate in decimal value: "))
        
        
        for i in range(year):
                principal = principal * (1 + (interest))

                
        print("Total value in ",year," years is: ", principal)
        input("Press enter to exit")


main()
