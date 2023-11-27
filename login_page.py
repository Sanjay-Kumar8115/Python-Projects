#Program to Create Login page
#type:ignore
def sign_in(Password,Username):
    print("Please sign in...")
    un=input("please Enter your user name : ")
    pw=input("please Enter your Account Password : ")
    if un==Username and pw==Password :
        print("Login Successfully...")
        exit(0)
    else :
        print("Account not found!")
        print("Or May be password or username is incorrect")
        print(" (1):sign up\n (2):Try again\n (3):Forget Password\n (4) Exit")
        ch=int(input("Enter your choice--->"))
        if ch==1:
            sign_up(Password,Username)
        elif ch==2:
            sign_in(Password,Username)
        elif ch==3:
            Paasword=input("Re-Enter your password : ")

            print(forget_Password(Password,data))
        else:
          print("Thanks for visiting...")
          exit(0)

def sign_up(Password,Username):
    NM=input("Enter your name : ")
    EM=input("Enter your email : ")
    Nu=input("Enter your number : ")
    UN=input("Create your username :")
    PW=input("Enter your Password : ")
    data={"Name":NM,
          "Email":EM,
          "Number":Nu,
          "Username":UN,
          "Password":PW
         }
    #Saving info in file
    f=open("Login_page_info.txt","w+")
    for key,value in data.items():
        f.write("%s : %s\n" % (key,value))
    f.close()
    #Changing Username and password
    Username=NM
    Password=PW
    print("Sign Up successfully...")
    sign_in(Password,Username)

def forget_Password(pswd,data):
    if (len(pswd)>=8):
     if any(char.isupper() for char in pswd):
        pass
     else :
        print("Atleast 1 character in uppercase...")
     if any(char.islower() for char in pswd):
        pass
     else :
        print("Atleast 1 character in lowercase...")
     if any(char.isdigit() for char in pswd):
        pass
     else :
        print("Atleast 1 character is digit 1 to 9...")
     if any(char in "@#$%^&*_?" for char in pswd):
        pass
     else :
        print("Atleast 1 character is special...")
    else:
        print("Password length should be equal or more than 8")
    return "Password Changed Succesfully..."
    #changing the saving password in file
    data["Password"]=pswd
    
        
print(":::::: (^.^) Welcome (^.^) :::::::")
Username="Sanjay Kumar"
Password="Sanjay@1234"
data={}
if Password!=None and Username!=None:
    sign_in(Password,Username)
else:
    sign_up(Password,Username)


    





