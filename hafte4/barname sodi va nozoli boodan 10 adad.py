#برنامه دریافت ده عدد و مشخص کردن صعودی و نزولی مطلق یا بله یا خیر

numbers = []

for i in range(10):
    user_number = int(input('enter 10 numbers:\n'))
    numbers.append(user_number)

for number1 in range(len(numbers) - 1):
    if (numbers[number1] < numbers[number1 + 1]):
        count = True
        continue
    else:
        count = False
        break
if count == False:
    print('NO!!')
else:
    print('YES.')

