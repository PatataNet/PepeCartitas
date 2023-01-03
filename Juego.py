from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Pepe challenge")
root.geometry("800x600")
root.configure(background="white")

img=ImageTk.PhotoImage(Image.open ("boton.png"))

def cerrar():
    root.destroy()

Ramiro =ImageTk.PhotoImage(Image.open ("Ramiro.png"))
Pez =ImageTk.PhotoImage(Image.open ("Pez.png"))
PezAdmin =ImageTk.PhotoImage(Image.open ("PezAdmin.png"))
Pepe =ImageTk.PhotoImage(Image.open ("Pepe.png"))
Manolo =ImageTk.PhotoImage(Image.open ("Manolo.png"))
ElBoceto =ImageTk.PhotoImage(Image.open ("ElBoceto.png"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

Carta_list=[Ramiro, Pez, PezAdmin, Pepe, Manolo, ElBoceto]

Poder_list=[50, 50, 200, 200, 100, 200]

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,5)
    random_pokemon = Carta_list[random_no]
    label["image"]=random_pokemon
    
    random_power_list = Poder_list[random_no]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str( player1_score)

player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
    
player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(0,5)
    random_pokemon2 = Carta_list[random_no2]
    label["image"]=random_pokemon2
    
    random_power_list2 = Poder_list[random_no2]
    player2_score = player2_score + random_power_list2 
    player_2_score_label["text"] = str( player2_score)

player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)

btn=Button(root,text="Cerrar",command=cerrar)
btn.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()