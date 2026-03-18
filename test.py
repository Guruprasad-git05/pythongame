import random

while True:
 print("")
 a=input(" stone   --> 1\n paper   --> 2\n scissor --> 3\n".title())
 b=int(a)
 c=random.choice("123")
 d=int(c)
 print("")
 if b<1 or b>3:
    print("❌ Enter the valid number ❌")
    continue
 print("You Chose",b ,"✅")
 print("Comp Chose",d ,"✅")
 print("")
 if b==1 and d==3:
    print("You Won!!!😊")
 elif b==2 and d==1:
    print("You Won!!!😊")
 elif b==3 and d==2:
    print("You Won!!!😊")
 elif b==d:
    print("Play Again!!!🔁")
 else:
    print("You Lost👎")
 print("")
   
 z=input("Do You Want To Continue? \n")
 if z.lower() in ("yes" , "y"):
    print("Let's Begin😁")
    continue
 else:
    print("")
    print("Thanks for Playing!!!🙌")
    break