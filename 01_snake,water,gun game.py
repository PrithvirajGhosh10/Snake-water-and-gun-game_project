#snake,water,gun game
import random
'''
1 for snake ,water lose,gun win
-1 for water ,gun lose,snake win
0 for gun ,snake lose,water win

'''
computer=random.choice([1,-1,0])
a=input("Enter your choice: ")
dict={"s":1,"w":-1,"g":0}
revdict={1:"Snake",-1:"Water",0:"Gun"}
you=dict[a]
#by now we have 2 numbers (variables),you and computer
print(f"You chose {revdict[you]}\ncomputer chose {revdict[computer]}")
if (computer==you):
    print("It's a draw")
else:
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You lose!")
    else:
        print("Someting went wrong!")