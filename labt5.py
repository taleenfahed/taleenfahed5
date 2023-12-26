print('select operation')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')
q='yes'
while q=='yes':
 choice=int(input('enter choice(1/2/3/4): '))
 num1=int(input('enter first number: '))
 num2=int(input('enter second number: '))
 if choice==1:
  r=num1+num2
  result='{}+{}={}'
 if choice==2:
    r=num1-num2
    result='{}+{}={}'
 if choice==3:
    r=num1*num2
    result='{}+{}={}'
 if choice==4:
    r=num1/num2
    result='{}+{}={}'
 print(result.format(num1,num2,r))
 q=input('lets do next caculation (yes/no): ')
