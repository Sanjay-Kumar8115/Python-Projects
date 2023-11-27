#A python program which take emails as
#input slice it store in dictionary
#further in a text file
ch="Y"
emails={}
while (ch=="Y"):
 email=input("Enter your email : ")
 username,domain=email.split("@")
 print("Username:",username ,"\nDomain:",domain)
 emails.update({"Username ": username})
 emails.update({"Domain ": domain})
 print(emails)
 f=open("EmailFile.txt","a+")
 for username,domain in emails.items():
     f.write("%s : %s\n" % (username,domain))
 f.close()
 ch=input("Do you want to continue Press Y or N :")
