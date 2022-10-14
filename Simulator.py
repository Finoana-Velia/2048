import model
import random
import os


def Option() :
    print("\t 8(haut) \n")
    print("4(gauche) \t 6(droite)\n")
    print("\t 2(bas)\n")
    print()
    print(" 0 (quitter la partie)")
    print()

def Printer(x) :
    print(x)
    print("Score : {}".format(x.score))
         
board = model.Board()
os.system("cls")
Option()
Printer(board)
i = 0 
while i<4 :
    response = input("Donner la direction : ")
    if response == "8" :
        os.system("cls")
        Option()
        board.move(model.UP)
        Printer(board)
        continue
    if response == "4" :
        os.system("cls")
        Option()
        board.move(model.LEFT)
        Printer(board)
        continue
    if response == "2" :
        os.system("cls")
        Option()
        board.move(model.DOWN)
        Printer(board)
        continue
    if response == "6" :
        os.system("cls")
        Option()
        board.move(model.RIGHT)
        Printer(board) 
        continue
    if response == "0" :
        print("Vous avez quitte la partie")
        break