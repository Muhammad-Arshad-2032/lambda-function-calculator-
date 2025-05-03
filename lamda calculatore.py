char=int(input("Enter the option (add(1) sub(2)multiplication(3)div(4) moduls(5))"))
match char:
    case 1:
        add=lambda x,y:x+y
        x=int(input("Enter the first value for add"))
        y=int(input("Enter the second  value for add"))
        print(add(x,y))
    case 2:    
        sub=lambda x,y:x-y
        x=int(input("Enter the first value for subtarction"))
        y=int(input("Enter the second  value for subtarction"))
        print(sub(x,y))
    case 3:    
        multiplication=lambda x,y:x*y
        x=int(input("Enter the first value for subtarction"))
        y=int(input("Enter the second  value for subtarction"))
        print(multiplication(x,y))
    case 4:    
        divsion=lambda x,y:x/y if y!=0 else " canot divsibale by zero "
        x=int(input("Enter the first value for subtarction"))
        y=int(input("Enter the second  value for subtarction"))
        print(divsion(x,y))
    case 5:    
        modulus=lambda x,y:x%y
        x=int(input("Enter the first value for subtarction"))
        y=int(input("Enter the second  value for subtarction"))
        print(modulus(x,y))
        
    
    case _ :
        print("defoult case is envocked")
        
        
    



