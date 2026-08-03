import random

runs = []

for i in range(10):
      score = 0
      while True:
            try : 
                user = int(input("Your Choice     : "))
                comp = random.randint(0,6)
                if user> 6:
                  print("Enter valid input\n\n")
                elif user == comp:
                  print(f"\nComputer Choice : {comp}")
                  runs.append(score)
                  print(f"\n Out !!\n Your score : {score}\n\n")
                  break
                else:
                  print(f"\nComputer Choice : {comp}")
                  score += user
                  print(f"\n Current score : {score}\n\n")
            except:
                 print("invalid input")

                 

              
