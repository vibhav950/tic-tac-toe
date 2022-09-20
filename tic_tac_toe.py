#displaying tic-tac-toe grid
def display(x):
    for i in range(0,3):
        for j in range (0,3):
            if(x[i][j]=='-'):
                print("   ",end="")
            else:
                print(f"{x[i][j]}",end="")
            if (j in [0,1]):
                print("|",end="")
        print("")
        if (i in [0,1]):
            print("-----------")
    print()

#placing turn-by-turn
def place(pos):
        if pos not in ['11','12','13','21','22','23','31','32','33']:
                inp_pos=input('Enter a valid position (eg. 11 for R1 C1): ')
                print()
                place(inp_pos)
        else:
                row, column=int(pos[0])-1, int(pos[1])-1
                if i%2==0:
                        if grid[row][column]!='-':
                                inp_pos=input('Enter an empty position: ')
                                print()
                                place(inp_pos)
                        else:
                            grid[row][column]='X'
                            display(grid)
                            return
                elif i%2!=0:
                        if grid[row][column]!='-':
                                inp_pos=input('Enter an empty position: ')
                                print()
                                place(inp_pos)
                        else:
                            grid[row][column]='O'
                            display(grid)
                            return
#win message
def win_msg(player):
        print(f"Player {player} Wins!")
        print()

#evaluating grid
def check(x):
        #check row
        for l in x:
                if l==['X','X','X']:
                        win_msg('X')
                        return True
                elif l==['O','O','O']:
                        win_msg('O')
                        return True

        #check column
        for m in range(len(x[0])):
                if x[0][m]=='X' and x[0][m]==x[1][m] and x[0][m]==x[2][m]:
                        win_msg('X')
                        return True
                elif x[0][m]=='O' and x[0][m]==x[1][m] and x[0][m]==x[2][m]:
                        win_msg('O')
                        return True

        #check left to right diag
        X_diag, O_diag=0, 0
        for l in range(len(x)):
                if x[l][l]=='X':
                        X_diag+=1
                elif x[l][l]=='O':
                        O_diag+=1
        if X_diag==3:
                win_msg('X')
                return True
        elif O_diag==3:
                win_msg('O')
                return True

        #check right to left diag
        X_diag, O_diag=0, 0
        for l in range(len(x)):
                if x[l][2-l]=='X':
                        X_diag+=2
                if x[l][2-l]=='O':
                        O_diag+=2
        if X_diag==6:
                win_msg('X')
                return True
        elif O_diag==6:
                win_msg('O')
                return True
        else:
                return False

#gameplay
def play():
        #initial grid display
        global grid
        grid=[['-','-','-'],['-','-','-'],['-','-','-']]
        display(grid)
        global i

        #gameplay loop begins
        for i in range(9):
            if i%2==0:
                    print('Place X')
                    print()
            else:
                    print('Place O')
                    print()
            inp_pos=input('Enter position (eg. 11 for R1 C1): ')
            print()
            place(inp_pos)
            if i>=4:
                         if check(grid)==True:
                              cho=input('Play again? (y/n): ')
                              print()
                              if cho=='y':
                                      play()
                              else:
                                return
        else:
            print("It's a Draw!")
            print()
            cho=input('Play again? (y/n): ')
            print()
            if cho=='y':
                    play()
            else:
                    return
                

play()
        
                                        
                                        
                        



