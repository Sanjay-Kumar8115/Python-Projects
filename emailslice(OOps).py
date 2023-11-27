class email_slicer:
    def __init__(self,email,email_dic):
        self.email=email
        self.email_dic={}
    def Em_slice(self):
        username,domain=email.split("@")
        print("Username:",username ,"\nDomain:",domain)
        email_dic.update({"Username ": username})
        email_dic.update({"Domain ": domain})
        print(email_dic)
    def Em_store_file(self):
        f=open("EmailFile2.txt","a+")
        for username,domain in email_dic.items():
          f.write("%s : %s\n" % (username,domain))
        f.close()
class informaion(email_slicer):
    pass
ch="Y"
while(ch=="Y"):
    email=input("Enter your email : ")
    email_dic={}
    person=informaion(email,email_dic)
    person.Em_slice()
    person.Em_store_file()
    ch=input("Do you want to continue Press Y or N :")
        
