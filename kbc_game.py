#Program to implement quize question using only lists
def kbc(name):
    print("""*** Rules ***\n 1.wrong answer and will be out
        from the game\n 2.If you start the game there is no
        going back button \n if you agree!""")
    ch=int(input("Press...\n(1)Play Game\n(2)Quite Game\n---> "))
    if (ch==1):
        play_game(name)
    else:
        exit()

def play_game(name):
    ques_count=0
    
    print("Mr: {} \n Your {} Question is.\n".format(name,ques_count+1))
    ques_list=["Which data type is mutable?",
               "What does the /'%'/ operator in python?",
               "Which keyword is used to define functions in python?",
               "Which function is used to get the length of a list i pyhton?",
               "Which operator is used for exponantiation in python?"
              ]
    if (ques_count==0):
        print(ques_list[0])
        ques_count=options(ques_count)
    if (ques_count==1):
        print(ques_list[1])
        ques_count=options(ques_count)
    if (ques_count==2):
        print(ques_list[2])
        ques_count=options(ques_count)
    if (ques_count==3):
        print(ques_list[3])
        ques_count=options(ques_count)
    if (ques_count==4):
        print(ques_list[4])
        ques_count=options(ques_count)
    #if (ques_count>4):
      #  print("Game over")
    
    #ques_count=ques_count+1

def options(ques_count):
    opt_list=["(1)tuple","(2)int","(3)string","(4)list",
              "(1)Division","(2)Exponentiation","(3)Modulo","(4)Multiplication",
              "(1)method","(2)def","(3)function","(4)define",
              "(1)lenth()","(2)size()","(3)len()","(4)count",
              "(1)^","(2)**","(3)//","(4)%"
             ]
    if  (ques_count==0):
        print(opt_list[0:4])
        return(answers(ques_count))
        #return (ques_count+1)
    if  (ques_count==1):
        print(opt_list[4:8])
        return( answers(ques_count))
        #return (ques_count+1)
    if  (ques_count==2):
        print(opt_list[8:12])
        return(answers(ques_count))
        #return (ques_count+1)
    if  (ques_count==3):
        print(opt_list[12:16])
        return(answers(ques_count))
        #return (ques_count+1)
    if  (ques_count==4):
        print(opt_list[16:20])
        return(answers(ques_count))
        #return (ques_count+1)
    
def answers(ques_count):
    ans_list=[4,3,2,3,2]
    ch_op=int(input("Select a option(integer)  ---> "))
    if  (ques_count==0):
        if (ch_op==ans_list[0]):
            print("Correct answer! conggratualtion You won 5k")
            return (ques_count+1)
        else:
            print("Wrong Answer!")
    if  (ques_count==1):
        if (ch_op==ans_list[1]):
            print("Correct answer! conggratualtion You won 10k")
            return (ques_count+1)
        else:
            print("Wrong Answer! Game Over you won only 10K")
    if  (ques_count==2):
        if (ch_op==ans_list[2]):
            print("Correct answer! conggratualtion You won 20k")
            return (ques_count+1)
        else:
            print("Wrong Answer!Game Over you won only 20K")
    if  (ques_count==3):
       if (ch_op==ans_list[3]):
            print("Correct answer! conggratualtion You won 30k")
            return (ques_count+1)
       else:
            print("Wrong Answer!Game Over you won only 30K")
    if  (ques_count==4):
       if (ch_op==ans_list[4]):
            print("Correct answer! conggratualtion You won 50k")
            return (ques_count+1)
       else:
            print("Wrong Answer!Game Over you won only 50K")
     
    

print("-----------------------------------------\n",("Welcome to KBC").center(40),"\n-----------------------------------------")
name=input("Enter your name : ")
kbc(name)
