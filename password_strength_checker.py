#Password Strength checker
def Pass_Gen(pswd):
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
    return "Password Generated Succesfully..."    

pswd=input("Enter your password : ")
print(Pass_Gen(pswd))
