import random

while True:
    ch=int(input("Press...\n(1)for play\n(2)for exit\n--->"))
    if ch==1:
        choices=["rock","peper","scissor"]
        print(choices)
        your_choice=input("Enter your choice from the above-->").lower()
        computer_choice=random.choice(choices)
        if your_choice==computer_choice:
            print("Game Tie...")
        elif (your_choice=="rock" and computer_choice=="scissor") or\
              (your_choice=="peper" and computer_choice=="rock") or\
              (your_choice=="scissor" and computer_choice=="peper"):
               print("You win...")
        else:
            print("Computer wins...")
    else:
        print("Thanks for playing...Bye!")
        exit(0)
        
