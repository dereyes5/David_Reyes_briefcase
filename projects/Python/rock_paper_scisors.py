"""
0=draw
1=player wins
2=pc wins
player/pc        rock    paper   scisors
rock               0       2        1
paper              1       0        2
scisors            2       1        0
"""
import random
def juego(player,pc):
    options_table=[[0,2,1],[1,0,2],[2,1,0]]
    score=0
    if(options_table[player][pc]==0):
        print("draw")
    if(options_table[player][pc]==1):
        print("player wins")
        score=1
    if(options_table[player][pc]==2):
        print("pc wins")
    return score
options=['rock', 'paper', 'scisors']
answer=0
score=0
while(answer==0):
    print("Rock=1, paper=2, scisors=3")
    player=int(input("Choose an option: "))
    print(f"Your choose is: {options[player-1]}")
    pc=random.randint(0,2);
    if(juego(player-1,pc)==1):
        score=score+1
        print(score)
    print(f"pc choose is: {options[pc]}")
    answer=int(input("still playing? - 1: no - 0: yes --> "))