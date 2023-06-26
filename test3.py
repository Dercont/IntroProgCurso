import random

def f_while_if():
  numeroWhile = 0

  while numeroWhile < 3:
    numeroWhile += 1
    print("numeroWhile equals to: ", numeroWhile)

    numeroIf = random.randint(-5, 5)

    if numeroIf > 0:
      print("numeroIf it's a positive number: ", numeroIf)
    elif numeroIf == 0:
      print("numeroIf it's equals to 0: ", numeroIf)
    else:
      print("numeroIf it's a negative number: ", numeroIf)

def f_do_while():
  numeroWhile = 2
  while True:
    numeroWhile += 1
    if numeroWhile == 3:
      print("numeroWhile equals to: ", 3)
      break

def f_for():
  numeroFor = 0
  for numeroFor in range(4):
      print("numeroFor it's equals to: ", numeroFor)
      
def f_switcher():
    def spring():
        print("spring")
    def summer():
        print("summer")
    def autumn():
        print("autumn")
    def winter():
        print("winter")    
    def default():
        print("Are you sure? It's not a valid season.")
    switch = {
        0: spring,
        1: summer,
        2: autumn,
        3: winter,
        4: default

    }
    season = 1
    if season in switch:
        switch[season]()
    else:
        default()

#Calling functions
f_while_if()
print("===========================================")
f_do_while()
print("===========================================")
f_for()
print("===========================================")
f_switcher()
