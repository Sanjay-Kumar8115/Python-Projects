#fibonacci series
def fibo(num):
    fib_res=[0,1]
    if (num<=0):
        return []
    elif (num==1):
        return [0]
    elif (num==2):
        return fib_res

    for i in range(2,num):
      res=fib_res[i-1]+fib_res[i-2]
      fib_res.append(res)
    return fib_res

num=int(input("Enter a Number : "))
print("fibonacci series of {} is ".format(num),fibo(num))
