from cryptography.fernet import Fernet
import imports.fileReader as reader
import imports.CONSTS as CONSTS
import imports.dataHandler as jdata
import imports.passwordManager as login

# import win32ui
# wnd = win32ui.GetForegroundWindow()
# print(wnd.GetWindowText())



tt = login.passwordManager("data/")