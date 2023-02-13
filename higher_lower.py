def print_details(names,descriptions,countries):
    return (f"{names} is a {descriptions} from {countries}")

def check(one,two,guessed):
    if guessed == "l":
        if one > two:
            return 0
        else:
            return 1
            
            
    elif guessed == "h":
        if one < two:
            return 0
        else:
            return 1
    else:
        return -1
          


from data import data
import random
from replit import clear
from art import logo,vs
def play():
    print(logo)
    score = 0
    is_done = False
    while not is_done:
        ch = []
        while len(ch) != 2:
            is_it = random.choice(data)
            if is_it not in ch:
                ch.append(is_it)

        print(print_details(ch[0]["name"],ch[0]["description"],ch[0]["country"]))
        print(vs)
        print(print_details(ch[1]["name"],ch[1]["description"],ch[1]["country"]))
        print("")
        guess = input(f'''How do u think has {ch[1]['name']}  has lower or Higher followers than {ch[0]['name']}
            Type "h" for higher Type "l" for lower: ''').lower()
        result = check(ch[0]["follower_count"],ch[1]["follower_count"],guess)
        if result == 0:
            print("You Are Right")
            score += 1
            clear()
        elif result == 1:
            print("Game Over")
            print(f"Your Score is {score}")
            is_done = True
            if input("Do You Want to continue 'y' for Yes and 'n' for No: " )== "y":
                clear()
                play()
            else:
                print("Thank You")
        else:
            print("Invalid Input")
play()                   
    