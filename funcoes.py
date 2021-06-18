import os, time, sys

def monster():
  print('Você foi invadido pelo Fahad reverso, prepara-se para a destruição!')

  myList = ['Loading…\n█▒▒▒▒▒▒▒▒▒', '10%\n███▒▒▒▒▒▒▒', '30%\n█████▒▒▒▒▒', '50%\n███████▒▒▒', '100%\n██████████']
  for s in myList:
    print(s)
    time.sleep(0.8)
  goodbye = '\nDesligando...'
  for char in goodbye:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.4)
  os.system("shutdown /s /t 0")
