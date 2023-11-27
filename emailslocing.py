ch="Y"
while (ch=="Y"):
 email=input("Enter your email : ")
 username,domain=email.split("@")
 print("Username:",username ,"Domain:",domain)
 ch=input("Do you want to continue Press Y or N :")
