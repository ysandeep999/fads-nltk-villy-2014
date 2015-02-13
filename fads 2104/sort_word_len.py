# Sandeep Yalamanchili

#program sots the list of words based on their length and using function cmp_len

import time
def cmp_len(a):
    return sorted(a,key=len);

def main():
        x=['Employees','and','Students']
        b = cmp_len(x)
        print(b)

main()        


