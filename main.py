from tkinter import *
import random

root = Tk()
root.title('number guessing game')
root.geometry("500x250")

secret_number = None

def start_game():
    global secret_number
    for button in button_list:
        button.config(text=str(random.randint(0, 100)))
    randomButton = random.choice(button_list)
    secret_number = randomButton.cget('text')
    print('secret number is:', secret_number)

def onclick(event):
    btn = event.widget
    button_text = btn.cget('text')
    if secret_number == button_text:
        answer_label.config(text='Yes, it was ' + secret_number)
    else:
def on_answer_button_click():
    answer_label.config(text="Answer: " + secret_number)

# GUI components

title_label = Label(root, text='Guess the Secret Number', font=('helvetica', 12), pady=8, justify='center')
button_one = Button(root, text='00', font=('helvetica', 15), width=6, pady=15, bg='palegreen')
button_two = Button(root, text='00', font=('helvetica', 15), width=6, pady=15, bg='skyblue')
button_three = Button(root, text='00', font=('helvetica', 15), width=6, pady=15, bg='coral')
button_list = [button_one, button_two, button_three]

answer_label = Label(root, text='Answer', font=('helvetica', 15), pady=9, fg='purple', justify='center')

answer_button = Button(root, text='Answer', font=('helvetica', 15), width=6, pady=15, bg='palegreen', command=on_answer_button_click)

# Event bindings
for button in button_list:
    button.bind("<Button-1>", onclick)

# Grid placement
title_label.grid(row=0, column=0, columnspan=3)
button_one.grid(row=1, column=0)
button_two.grid(row=1, column=1)
button_three.grid(row=1, column=2)
answer_label.grid(row=2, column=0, columnspan=3)
answer_button.grid(row=3, column=0, columnspan=3)

start_game()
root.mainloop()