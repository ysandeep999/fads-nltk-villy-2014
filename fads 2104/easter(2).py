# Sandeep Yalamanchili
# Easter date

def main():

    try:
        year = eval(input(" Enter year between 1900 - 2099 :"))

    
        
        if year >= 1900 and year <= 2099:
            a = year % 19
            b = year % 4
            c = year % 7
            d = (19 * a + 24) % 30
            e = (2 * b + 4 * c + 6 * d + 5) % 7

            print(a , b , c, d, e)

            if (22 + d + e) > 31 and (22 + d + e) < 55:
                print("April ",(22 + d + e - 31))
            elif (22 + d + e) >=55:
                print("April ",(22 + d + e - 31 - 7))
            else:
                print("March ", (22 + d + e))

        else:
            print("Wrong input: Enter year between 1900 and 2099")

    except :
            print("Wrong input: Enter year in numbers")

    

main()
