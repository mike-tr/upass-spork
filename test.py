# import win32ui
# wnd = win32ui.GetForegroundWindow()
# print(wnd.GetWindowText())

import win32com.client

import pythoncom, pyHook
import dde

run = True

import pyautogui
import pyperclip # pip install pyperclip required

from tkinter import Tk

def copy():
    pyautogui.click() # a random click for focusing the browser
    pyautogui.press('f6')
    pyautogui.hotkey('ctrl', 'c') # for copying the selected url
    url = pyperclip.copy()
    print(Tk().clipboard_get())

def OnKeyboardEvent(event):
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')
    if(event.Key == 'T'):
        pyautogui.hotkey('ctrl', 'c')
        print(Tk().clipboard_get())
    if(event.Key == 'A'):
        global run
        run = False;

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()

from time import sleep
# wait forever
while(run):
    pythoncom.PumpWaitingMessages()
    #print(run)
    sleep(0.1)


#shell = win32com.client.Dispatch("WScript.Shell")
#shell.SendKeys('keys to send to active window...')