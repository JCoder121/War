from Tkinter import *
import time
import sys
import random
import Queue

## Global var
TableSize = 400
Comp_Cards = 10
You_Cards = 10
file_list = ['do not use',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_ace.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_two.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_three.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_four.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_five.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_six.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_seven.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_eight.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_nine.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_ten.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_jack.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_queen.gif',
             'C:\Python27\Jeff_home\Games\Pictures\gif_d_king.gif'] 
    
def convertcards(index):
    if index == 1:
        ret = str('A')        
    elif index == 11:
        ret = str('J')
    elif index == 12:
        ret = str('Q')    
    elif index == 13:
        ret = str('K')
    else:
        ret = str(index) 
    return ret

## Main
root = Tk()
board = Canvas(root, width=TableSize, height=TableSize)
board.configure(background = '#26C913')
root.configure(background = 'blue')
board.create_line(0, TableSize/2, TableSize, TableSize/2)

#cards
board.create_rectangle(150, 30, 250, 155, fill="#891C38", outline = 'black')
board.create_rectangle(150, 240, 250, 365, fill = "#891C38",outline="black")

t_Comp = board.create_text(200, 90, text = ':(', font = ('Arial', 60))
t_You = board.create_text(200, 300, text = ':)', font = ('Arial', 60))
t_Result = board.create_text(200, TableSize/2, text = "GOOD LUCK!", font = ('Arial', 40))
eYouCards = Entry(root)
eCompCards = Entry(root)

you_image = PhotoImage(file=file_list[1])
comp_image = PhotoImage(file=file_list[10])
#t_You = board.create_image(165,255, anchor = NW, image=comp_image)
#t_Comp = board.create_image(165,42, anchor = NW, image=you_image)

def Flipclick():
    global q_Comp, q_You
    global t_Comp, t_You, t_Result
    global Comp_Cards, You_Cards
    global eYouCards,eCompCards
    global you_image, comp_image
    global FlipCard
    global TableSize

    #diable button at first, wait finish
    FlipCard.config(state="disabled")
    
    board.delete(t_Comp)
    board.delete(t_You)
    
    #before get queue, always check if empty
    if q_You.empty():
        print "done lose"
        board.delete(t_Result)
        t_Result = board.create_text(200, TableSize/2, text = "GAME OVER! YOU LOSE!", font = ('Arial', 60))
        time.sleep(1)
        sys.exit()
        
    if q_Comp.empty():
        print "done win"
        board.delete(t_Result)
        t_Result = board.create_text(200, TableSize/2, text = "GAME OVER! YOU WIN!", font = ('Arial', 60))
        time.sleep(1)
        sys.exit()

    temp_You = q_You.get()
    temp_Comp = q_Comp.get()
    
    you_image = PhotoImage(file=file_list[temp_You])
    t_You = board.create_image(165,255, anchor = NW, image=you_image)
    comp_image = PhotoImage(file=file_list[temp_Comp])
    t_Comp = board.create_image(165,42, anchor = NW, image=comp_image)
    
    #comparison
    board.delete(t_Result)
    
    if temp_You == temp_Comp:
         t_Result = board.create_text(200, TableSize/2, text = "TIE!", font = ('Arial', 40))
    if temp_You > temp_Comp:
        You_Cards = You_Cards + 1
        q_You.put(temp_Comp)
        q_You.put(temp_You)
        Comp_Cards = Comp_Cards - 1
        t_Result = board.create_text(200, TableSize/2, text = "YOU WIN!", font = ('Arial', 40))                
    if temp_You < temp_Comp:
        Comp_Cards = Comp_Cards + 1
        q_Comp.put(temp_You)
        q_Comp.put(temp_Comp)
        You_Cards = You_Cards - 1
        t_Result = board.create_text(200, TableSize/2, text = "YOU LOSE!", font = ('Arial', 40))

    # update result
    eYouCards.delete(0, END)
    eCompCards.delete(0, END)
    eYouCards.insert(0, "You have: " + str(You_Cards) + " cards")
    eCompCards.insert(0, "Comp has: " + str(Comp_Cards) + " cards")
    eYouCards.update()
    eCompCards.update()

    #Check one more time after update
    if q_You.empty():
        print "done lose"
        board.delete(t_Result)
        t_Result = board.create_text(200, TableSize/2, text = "GAME OVER! YOU LOSE!", font = ('Arial', 25))
        board.update()
        time.sleep(1)
        print "done lose_222"
        sys.exit()
        
    if q_Comp.empty():
        print "done win"
        board.delete(t_Result)
        t_Result = board.create_text(200, TableSize/2, text = "GAME OVER! YOU WIN!", font = ('Arial', 25))
        board.update()
        time.sleep(1)
        print "done win_7896"
        sys.exit()

    #enable back the button
    time.sleep(0.5)
    FlipCard.config(state="normal")
    
#flipbutton, add command later
FlipCard = Button(root, text = "Flip Card", command = Flipclick)
FlipCard.pack()

#create gameboard

eCompCards.grid(row = 25, column = 20)
eCompCards.pack()
eCompCards.insert(0, "Comp has: " + str(Comp_Cards) + " cards")

board.pack()

eYouCards.grid(row = 25, column = 20)
eYouCards.pack()
eYouCards.insert(0, "You have: " + str(You_Cards) + " cards")

#create queue for cards

q_Comp = Queue.Queue()
for i in range(Comp_Cards):
    q_Comp.put(random.randint(1,13))

q_You = Queue.Queue()
for i in range(You_Cards):
    q_You.put(random.randint(1,13))

print "Start", (random.randint(1,13))

#Start playing portion
root.mainloop()
