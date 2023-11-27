#Factorial program
def fact(num):
    if (num==0 or num==1):
        return 1
    else:
        res=num *fact(num-1)
        return res

num=int(input("Enter a Integer number : "))
print("factorail of {} is".format(num),fact(num))
