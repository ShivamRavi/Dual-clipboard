import keyboard
import threading
import clipboard
import time

cp1 = None
cp2 = None
Activated = " ~~~ ACTIVATED ~~~"


def copy_c1():
    global cp1
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.2)  
    cp1 = clipboard.paste()
    

def copy_c2():
    global cp2
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.2)  
    cp2 = clipboard.paste()

def paste_c1():
    global cp1
    clipboard.copy(cp1)
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+v')
   
def paste_c2():
    global cp2
    clipboard.copy(cp2)
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+v')

#EDIT SHORTCUTS HERE
keyboard.add_hotkey('ctrl+shift+1', copy_c1)
keyboard.add_hotkey('ctrl+shift+2', copy_c2)
keyboard.add_hotkey('ctrl+alt+1', paste_c1)
keyboard.add_hotkey('ctrl+alt+2', paste_c2)


print("DUAL CLIPBOARD 📋📎 ", end="")
for char in Activated:
    print(char, end="", flush=True)
    time.sleep(0.2)

print("\nPress ESC to exit.")

      
keyboard.wait('esc')
for i in range(4, 0, -1):  
    print(f"\rDual Clipboard is assimilating {'.' * i}", end=" ", flush=True)
    time.sleep(1)
print("\rDual Clipboard terminated.    ") 
keyboard.unhook_all_hotkeys()  


