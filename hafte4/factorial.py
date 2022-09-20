num = int(input('please enter your number:(please make sure that the entered number is intiger.)\n'))
conclusion=1

for i in range(1 , num):
    entrance = num / i
    if entrance == 1:
        conclusion = 1 #conclusion = True
        break
    else:
        conclusion != 1  #conclusion = False
        continue
    
if conclusion == 1:
    print('in factorial adad vared shode nist :(')

else:
    print('in foctorial adad vared shode ast :)')
     
    
