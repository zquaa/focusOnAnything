from time import sleep
import sys
import pyautogui 


def focusOn():
    list = pyautogui.getWindowsWithTitle('your process name')
    if len(list) == 0 :
        print('\n' + list + 'isnt active rn')
        print('Exiting in 5 sec ',end='')
        for i in range(4):
            sleep(1)
            print('. ',end='')
        sys.exit()
    else: 
        process = list[0]
        if process.isMinimized == True:
            process.restore() #run
            print("Done.")
        else:
            print("Done.")

focusOn()