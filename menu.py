import functions
#use number of the function to activate the function.
def mainmenu():
    print("1. vertical line function")
    print("2. horizontal line function")
    print("3. staircase function")
    print("4. pixel function")
    print("5. clear screen function")
  while True:
   try:
    selection=int(input("enter choice: "))
    if selection==1:
        vertical_line()
    elif selection==2:
       horizontal_line() 
    elif selection==3:
        onestep()
        staircase()
    elif selection==4:
        pixel()
    elif selection==5:
        backlightclear()
    else:
        print("invalid choice. enter 1-5")
    mainmenu()
except ValueError:
    print("invalid choice. enter 1-5")

    