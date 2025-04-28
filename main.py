import telebot
import time
import sys
import os
from count import last_num as ln
dp = telebot.TeleBot('6452918965:AAHEq10Qy44G0vbRq9gN_YEhNdS88J577Ko')



countd = ln
at_ses = 0


os.system('color 3')

def mainscr():
    a = dp.set_chat_title(-1001973130675, "! Count")
    global countd, at_ses
    
    print('Started! Now delete edit-title msg')
    while True:
      at_ses+=1
      countd+=1

      cou = open('count.py', 'w')
      cou.write(f"last_num = {str(countd)}")
      cou.close()
      print(f"Now {str(countd)}; This session {str(at_ses)};")

      dp.send_message(-1001973130675, str(countd))
      time.sleep(5)

mainscr()
dp.infinity_polling()
