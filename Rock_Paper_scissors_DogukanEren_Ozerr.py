# TAŞ KAĞIT MAKAS
# OYUNCU BİLGİSAYAR
# ROUND KAZANAN
import random

OPTION = ['rock', 'paper', 'scissors']

player1 = input('Plase choose one Rock, Paper, or Scissors')
computer = random.choice(OPTION)

print('Oyuncunun Seçimi : ' + player1)
print('Bilgisayarın Seçimi ' + computer)

if  player1 == computer :
    print('Scoreless')



