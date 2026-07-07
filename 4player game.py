import random
import time


#--dice roll--
def dice():
    roll=random.randint(1,6)
    return(roll)
 
 
 #---board-----
def board(user_pos,bot_pos,user3_pos=0,user4_pos=0):
    print("========================================")
    print("\n")
    for i in range(100,90,-1):
        if(user_pos == i):
            print("","🔴","",end="")
        elif(bot_pos == i):
            print("","🟡","",end="")
        elif(user3_pos ==i):
            print("","🟢","",end="")
        elif(user4_pos == i):
            print("","🔵","",end="")        
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print("",i,end=" ")
    print("\n")
    for i in range(81,91,1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")       
        elif(user_pos == bot_pos):
            print(" ♦️",end="")    
        else:    
            print(" ",i,end="")
    print("\n")
    for i in range(80,70,-1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")              
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(" ",i,end="")
    for i in range(71,80,-1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")            
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(f"  {i}",end="")
    print("\n")
    for i in range(61,71,1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="") 
        elif(user4_pos == i):
            print(" ","🔵",end="")            
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(" ",i,end="")
    print("\n")
    for i in range(60,50,-1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")             
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(" ",i,end="")
    print("\n")
    for i in range(41,51,1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")               
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(" ",i,end="")
    print("\n")
    for i in range(40,30,-1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="")  
        elif(user4_pos == i):
            print(" ","🔵",end="")                    
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:
            print(" ",i,end="")
    print("\n")
    for i in range(21,31,1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="") 
        elif(user4_pos == i):
            print(" ","🔵",end="")                
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:    
            print(f"  {i}",end="")
    print("\n")
    for i in range(20,10,-1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="") 
        elif(user4_pos == i):
            print(" ","🔵",end="")                     
        elif(user_pos == bot_pos):
            print(" ♦️",end="")
        else:        
            print(f"  {i}",end="")
    print("\n")
    for i in range(1,11,1):
        if(user_pos == i):
            print(" ","🔴",end="")
        elif(bot_pos == i):
            print(" ","🟡",end="")
        elif(user3_pos ==i):
            print(" ","🟢",end="") 
        elif(user4_pos == i):
            print(" ","🔵",end="")                
        elif(user_pos == bot_pos):
            print(" ♦️",end="")   
        else:
            print(f"  {i} ",end="")
    print("\n")        
    print("=======================================")        
    print("\n")
     
  
  
 #----snake----
def snake(user_pos, bot_pos,user3_pos=0,user4_pos=0):

    snakes = {
        91:65,
        75:68,
        45:25,
        11:7,
        21:8,
        31:3,
        55:19,
        81:60,
        99:2
     }
    if(prince==1):
        if user_pos in snakes:
            print("🐍 Player bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("🐍 Bot bitten by snake!")
            bot_pos = snakes[bot_pos]
        return user_pos, bot_pos
    elif(prince == 2):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        return user_pos, bot_pos
    elif(prince==3):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        if user3_pos in snakes:
            print("😁player_3 bitten by snake!")
            user3_pos=snakes[user3_pos]
        return user_pos, bot_pos,user3_pos
    elif(prince==4):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        if user3_pos in snakes:
            print("😁player_3 bitten by snake!")
            user3_pos=snakes[user3_pos]
        if user4_pos in snakes:
            print("😆Player_4 bitten by a snake")
            user4_pos=snake[user4_pos]   
        return (user_pos, bot_pos,user3_pos ,user4_pos)  
            
            
    

def ladder(user_pos, bot_pos,user3_pos=0,user4_pos=0):
    
    ladder={
        9:32,
        14:88,
        40:80,
        85:92,
        54:64
     }
    if(prince== 1):
        if user_pos in ladder:
            print("❇️Player got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("❇️bot got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        return (user_pos,bot_pos)   
    elif(prince == 2):
        if user_pos in ladder:
            print("👤Player1 got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        return (user_pos,bot_pos)
    elif(prince== 3):
        if user_pos in ladder:
            print("👤Player_1 got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player_2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        if user3_pos in ladder:
            print("😁Player_3 got a ladder 🪜") 
            user3_pos=ladder[user3_pos]   
        return (user_pos,bot_pos,user3_pos)
    elif(prince==4):
        if user_pos in ladder:
            print("👤player_1 got a ladder 🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player_2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        if user3_pos in ladder:
            print("😁player_3 got a ladder 🪜")
            user3_pos=ladder[user3_pos]
        if user4_pos in ladder: 
            print("😆player_4 got a ladder 🪜")
            user4_pos=ladder[user4_pos]
        return(user_pos,bot_pos,user3_pos,user4_pos)          
            
#---4 player engine 
def playeruno(user_position,bot_position,user3_position,user4_position):
    user=dice()
    bot=dice()
    user3=dice()
    user4=dice()
    print("----------------------------------------")
    input(",👤player_1:-For Rolling dice..[Press Enter]")
    print("Player_1 dice=",user)
    input("😛player_2:- rolling the dice..[press Enter]")
    print("player_2 dice=",bot)
    input("😁player_3:- rolling the dice..[Press Enter]")
    print("Player_3 dice=",user3)
    input("😆player_4:- rolling the dice..[Press Enter]")
    print("Player_3 dice=",user4)
    print("\n")
    print("----------------------------------------")
    user_pos=user_position+user
    bot_pos=bot_position+bot
    user3_pos=user3_position+user3
    user4_pos=user4_position+user4
    print("\n")
    print("Player_pos:-",user_pos)
    print("bot_pos:-",bot_pos)
    print("Player_3 pos:-",user3_pos)
    print("Player_4 pos:-",user4_pos)
    user_position+=user
    bot_position+=bot
    user3_position+=user3
    user4_position+=user4
    user_pos,bot_pos,user3_pos,user4_pos=ladder(user_pos,bot_pos,user3_pos,user4_pos)
    user_position=user_pos
    bot_position=bot_pos
    user3_position=user3_pos
    user4_position=user4_pos
    user_pos,bot_pos,user3_pos,user4_pos=snake(user_pos,bot_pos,user3_pos,user4_pos)
    user_position=user_pos
    bot_position=bot_pos
    user3_position=user3_pos
    user4_position=user4_pos
    board(user_pos,bot_pos,user3_pos,user4_pos)
    return (user_position,bot_position,user3_position,user4_position)
     
 
        
              
#---3 Player functions---    
def player(user_position,bot_position,user3_position):
    user=dice()
    bot=dice()
    user3=dice()
    print("----------------------------------------")
    input(",👤player_1:-For Rolling dice..[Press Enter]")
    print("Player_1 dice=",user)
    input("😛player_2:- rolling the dice..[press Enter]")
    print("player_2 dice=",bot)
    input("😁player_3:- rolling the dice..[Press Enter]")
    print("Player_3 dice=",user3)
    print("\n")
    print("----------------------------------------")
    user_pos=user_position+user
    bot_pos=bot_position+bot
    user3_pos=user3_position+user3
    print("\n")
    print("Player_pos:-",user_pos)
    print("bot_pos:-",bot_pos)
    print("Player_3 pos:-",user3_pos)
    user_position+=user
    bot_position+=bot
    user3_position+=user3
    user_pos,bot_pos,user3_pos=ladder(user_pos,bot_pos,user3_pos)
    user_position=user_pos
    bot_position=bot_pos
    user3_position=user3_pos
    user_pos,bot_pos,user3_pos=snake(user_pos,bot_pos,user3_pos)
    user_position=user_pos
    bot_position=bot_pos
    user3_position=user3_pos
    board(user_pos,bot_pos,user3_pos)
    return (user_position,bot_position,user3_position)
    
    
    
#----player v/s player engine---    
def playerplayer(user_position,bot_position):
    user=dice()
    bot=dice()
    print("----------------------------------------")
    input("👤Player1:-For Rolling dice..[Press Enter]")
    print("Player dice=",user)
    input("😛Player2:- rolling the dice..[press Enter]")
    print("bot dice=",bot)
    print("\n")
    print("----------------------------------------")
    user_pos=user_position+user
    bot_pos=bot_position+bot
    print("\n")
    print("Player_1_pos:-",user_pos)
    print("Player_2_pos:-",bot_pos)
    user_position+=user
    bot_position+=bot
    user_pos,bot_pos=ladder(user_pos,bot_pos)
    user_position=user_pos
    bot_position=bot_pos
    user_pos,bot_pos=snake(user_pos,bot_pos)
    user_position=user_pos
    bot_position=bot_pos
    board(user_pos,bot_pos)
    return (user_position,bot_position)
        
    
    
#---Player V/S BOT engine-----    
def Playerbot(user_position,bot_position):
    user=dice()
    bot=dice()
    print("----------------------------------------")
    input("For Rolling dice..[Press Enter]")
    print("Player dice=",user)
    print("🤖:- rolling the dice")
    print("bot dice=",bot)
    print("\n")
    print("----------------------------------------")
    user_pos=user_position+user
    bot_pos=bot_position+bot
    print("\n")
    print("Player_pos:-",user_pos)
    print("bot_pos:-",bot_pos)
    user_position+=user
    bot_position+=bot
    user_pos,bot_pos=ladder(user_pos,bot_pos)
    user_position=user_pos
    bot_position=bot_pos
    user_pos,bot_pos=snake(user_pos,bot_pos)
    user_position=user_pos
    bot_position=bot_pos
    board(user_pos,bot_pos)
    return (user_position,bot_position)
        

user_position=0
bot_position=0
user3_position=0
user4_position=0
print("========================================")
print("|            ⚔️ Welcome To⚔️             |")
print("|       Snake 🐍 and Ladder 🪜 Game     |")
print("========================================")
time.sleep(1)
print("Establishing Board")
time.sleep(1)
print("Establishing ladder🪜")
time.sleep(1)
print("Snakes are waking up 🐍")
time.sleep(1)
print("Allmost Done 👍🏻")
time.sleep(1)
print("⚔️ Battle Begins ⚔️")
time.sleep(1)
name=input("Please Enter Your Name:-")
print("🐍:- Welcome 👤",name)
print("===============MENU=================")
print("""
🔹PLAYER V/S BOT           [Press 1]
🔹PLAYER V/S PLAYER        [Press 2]
🔹3 PLAYER Game            [Press 3]
🔹4 PLAYER Game            [Press 4]
🔹For Exit                 [Press 5]

====================================""")
prince=int(input("You Want:- "))
if(prince==1):
    print("Game")
    print("Start")
    print("Bot Token:🟡")
    print("Player Token:🔴")
    while True:
        user_position,bot_position=Playerbot(user_position,bot_position)
        if(user_position>=100):
            print("  👑            ")
            print("==👤 USER WINS ==")
        elif(bot_position >=100):
            print("  👑            ")
            print("==🤖 BOT WINS==") 
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            break   
        continue
elif(prince == 2):
    print("Player_1 Token 🟡")
    print("Player_2 Token 🔴")
    while True:
        user_position,bot_position=playerplayer(user_position,bot_position)
        if(user_position>=100):
            print("  👑            ")
            print("==👤 Player1 WINS ==")
        elif(bot_position >=100):
            print("  👑            ")
            print("==😛 Player2 WINS==") 
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            break   
        continue
elif(prince==3):
    print("Player_1 Token 🔴 ")
    print("Player_2 Token 🟡 ")
    print("Player_3 Token 🟢 ")
    while True:
        user_position,bot_position,user3_position=player(user_position,bot_position,user3_position)
        if(user_position>=100):
            print("  👑            ")
            print("==👤 Player_1 WINS ==")
        elif(bot_position >=100):
            print("  👑            ")
            print("==😛 Player_2 WINS==")
        elif(user3_position>=100):
            print("  👑            ")
            print("==😁 Player_3 WINS==")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            break   
        continue
elif(prince==4):
    print("Player_1 Token 🔴 ")
    print("Player_2 Token 🟡 ")
    print("Player_3 Token 🟢 ")
    print("Player_4 Token 🔵 ")
    while True:
        user_position,bot_position,user3_position,user4_position=playeruno(user_position,bot_position,user3_position,user4_position)
        if(user_position>=100):
            print("  👑            ")
            print("==👤 Player_1 WINS ==")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        elif(bot_position >=100):
            print("  👑            ")
            print("==😛 Player_2 WINS==")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        elif(user3_position>=100):
            print("  👑            ")
            print("==😁 Player_3 WINS==")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        elif(user4_position>=100):
            print("  👑            ")
            print("==😆 Player_4 WINS==")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            break   
        continue
        
        
    
    
    
    
elif(prince==5):
    print("Thank You For Using App🐍")        
    
    
    
    
    