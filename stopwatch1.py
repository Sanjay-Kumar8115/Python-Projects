import time
import os
def main():
    input("Press enter to start...")
    st=time.time()
    try:
        while True:
            et=time.time()-st
            print("Elapsed Time: {:.2f} seconds".format(et),end="\r")
            time.sleep(0.1)
            os.system('cls')
    except KeyboardInterrupt:
        print("\n Stopwatch stopped...")
        pass
if __name__=="__main__":
    main()
    
