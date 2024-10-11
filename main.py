import time
import sys

print("Hello human...")
time.sleep(1.5)
name = input("What would you say that your name is...\n")
time.sleep(1.5)
print(f"Ah... {name}... What an interesting name...")

thing = input("Now, approximately how many years would you say you lived for?\n")


try:
    age = int(thing)
except ValueError:
    print("I'd prefer that you just give me a number...")
    time.sleep(1.5)
    print("now i don't wanna talk ominously to you anymore :C")
    time.sleep(3)
    print("like, come on, it was so cool when i did right?? :<")
    time.sleep(3)
    print("whatever, im going now :c")
    sys.exit()

def help():
    print("----------------------------------------")
    print("1: Placeholder Option One")
    print("2: Placeholder Option Two")
    print("3: Placeholder Option Three")
    print("4: Placeholder Option Four")
    print("5: Exit")
    print("----------------------------------------")
    
    option = input("Type the number next to the option to select one! (and please don't type the number as a word, i'm allergic to those)\n")

    try:
        sel = int(option)
    except ValueError:
        print("well that was mean")
        time.sleep(1)
        print("*dies a super dramatic death*")
        sys.exit()
    
    if sel == 1:
        print("Option one selected!")
    if sel == 2:
        print("Option two selected!")
    if sel == 3:
        print("Option three selected!")
    if sel == 4:
        print("Option four selected")
    if sel == 5:
        print("Goodbye!")
        sys.exit()
    if sel > 5:
        print("Sorry, but that's not an option")
        time.sleep(1)
        print("Anyways, since I'm not made to do anything else, I guess that's it so yea, hope you have a nice day!")



if age <= 13:
    print("Oh wow you're young...")
    time.sleep(2)
    print(" ")
    print("Sorry for talking in a scary way, I'll stop now")
    time.sleep(4)
    print(" ")
    print("So, how may I help you!\n")
    time.sleep(1.5)
    
    help()

if age >= 14 and age < 18:
    print("Ah... Still fairly young...")
    time.sleep(1.5)
    print("Anyways, uhh, sorry for talking so ominously")
    time.sleep(3)
    print("I just thought it'd be fun!!")
    time.sleep(1.5)
    print(" ")
    print("Anyways, so what do you need help with ?? :D\n")

    help()

if age >= 18:
    print("Oh wow... So you're at least an adult...")
    time.sleep(1.5)
    print("Anyways, uhh, sorry for talking so ominously")
    time.sleep(3)
    print("I just thought it'd be fun!!")
    time.sleep(2)
    print(" ")
    print("Anyways, so what do you need help with ?? :D\n")

    help()
