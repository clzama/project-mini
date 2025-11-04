from tkinter import*
import random

def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])

def get_guess():
    return ''.join(e.get() for e in entries)

def clear_entries():
    for e in entries:
        e.delete(0,END)

def check_guess():
    guess = get_guess()

    if len(guess) != 4 or not guess.isdigit():
        hint_label.config(text="Hint: กรุณาใส่ตัวเลข 4 หลัก")
        return
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    if bulls == 4:
        hint_label.config(text="*** CORRECT ***")
    else:
        hint_label.config(text=f"Hint: Bulls:{bulls} and Cows:{cows}")
        clear_entries()

def reset_game():
    global secret_number
    secret_number = generate_number()
    hint_label.config(text="Hint: ")
    clear_entries()


window =Tk()
window.title("Bull and Cow guessing game")

label_guess =Label(window, text="Guessing:")
label_guess.grid(row=0,column=0,padx=5,pady=5)

entries = []
for i in range(4):
    e =Entry(window,width=3,justify="center",font=("Arial", 10))
    e.grid(row=0,column=i+1,padx=3)
    entries.append(e)

btn_submit =Button(window,text="Submit",command=check_guess,width=8)
btn_submit.grid(row=0, column=5, padx=5)

hint_label =Label(window,text="Hint: ",font=("Arial", 11))
hint_label.grid(row=0, column=6,columnspan=7,pady=10)

secret_number = generate_number()

window.mainloop()
