from tkinker import *
import random
root = Tk()
root title('guess the number game')
root.geometry('500x250')
root.config(bg='yellow')
Label(root, text = 'guess the number between 1 to 10', font=('arial', 15), bg='yellow').place(x=150, y=10)
def guess_number():
  secret_number = random.randint(1,10)
  attempts = 0

print('welcome to number guessing game')
print('i have selected a number betweem 1 to 10')
while True:
  guess = int(input('enter your guess:')
    attempts += 1
  if user_guess == secret_number:
   print('congratulations! you guessed the number in', attempts,'attempts')
    
