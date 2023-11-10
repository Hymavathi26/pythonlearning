#match
#similar to switch in java

number=int(input("Enter number:\n"))

match number:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")
    case _:                       #nothing is matching,it will run the code
        print("no idea")

#2
name=input("Enter name : \n")
match name:
    case "hyma":
        print("welcome hymavathi")
    case "raj":
        print("welcome raj")
    case "caitra":
        print("welcome chaitra")
    case _:
        print("welcome nothing name is there")


number=int(input("enter number:\n"))
match number:
     case 10:
         print(10)