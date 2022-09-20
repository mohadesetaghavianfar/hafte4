bread_line = ['Ali','Atefe','Reza','Homa','Amir','Fatemeh']

for i in range (3):
    aghazade = input('please enter your name:\n')
    number = int(input('what is your number in the queue?\n'))
    bread_line.insert(number,aghazade)

print(bread_line)
