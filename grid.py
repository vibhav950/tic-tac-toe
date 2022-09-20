l=[['X','',''],['','O',''],['','','X']]
def print_grid(l):
    for i in range(0,3):
        for j in range (0,3):
            if(l[i][j]==''):
                print("   ",end="")
            else:
                print("",l[i][j],"",end="")
            if (j in [0,1]):
                print("|",end="")
        print("")
        if (i in [0,1]):
            print("-----------")
            
        
    
print_grid(l)
