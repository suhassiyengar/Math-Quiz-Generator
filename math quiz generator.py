import random
import time

TOTAL_QUESTIONS=10

def storage_ofusers():
    with open("player.txt","a") as f:
        f.write(name+":"+str(total_time)+"seconds.\n")

def leadboard_():
    print("\n📊 Leaderboard:")
    print("-" * 25)
    with open("player.txt","r") as f:
        for line in f.readlines():
            print(line.rstrip())


def question_():
    OPERATORS=["+","-","*"]
    MIN_=1
    MAX_=10
    letf=random.randint(MIN_,MAX_)
    operand=random.choice(OPERATORS)
    right=random.randint(MIN_,MAX_)
    exp=str(letf)+""+operand+""+str(right)
    answer=eval(exp)
    return exp,answer


def user_interface():
    wrong=0
    for i in range(TOTAL_QUESTIONS):
        exp,answer=question_()
        while True:
            guess=input("question number#"+str(i+1)+" "+exp+"=")
            if guess==str(answer):
                break
            else:
                print("Your Answer is wrong TRY AGAIN! TIME'S RUNNING")
            wrong+=1
    return wrong

name=input("ENTER UR NAME: ")
START=input("PRESS ENTER TO START THE GAME:")

start_time=time.time()
wrong=user_interface()
end_time=time.time()
total_time=round(end_time-start_time,2)
storage_ofusers()
print("HURRAY!",name,"You Finished The Quiz With ",wrong,"errors in ",total_time,"SECONDS")
f=input("do u wanna see the previous plays(y):")
if f.lower()!="y":
    print("Thank you for playing!.")

else:
    leadboard_()













