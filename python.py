02.22.20



first = 'Sakib'
second = 'Shahid'
print(first + '(' + second + ')')
print(f'{first}({second})is a good boy')
topic = 'Sakib Shahid is a doctor'
print(len(topic))
print(topic.find('k'))
print(topic.replace('a doctor','an engineer'))
print(topic.upper())
print(topic.lower())
print('SAKIB'in topic)
print(topic.title())

num = 5
num = num + 4
num = num + 2
num -= 6
print(num)
print(30%4) =2
print(30//4) =7
print((1+1)*2**3)
print(round(3.499))
print(abs(-2.8))
import math
print(math.floor(7.8))  =7
print(math.ceil(8.5)) =9
good_boy =  False
if good_boy:
   print('studies hard')
   print('offers salat')
else:
   print('not obident');
good_credit = True
if good_credit:
   print('10%')
else:
   print('20%')

winter = False
summer = False
if winter:
   print("It's cool")
if summer:
   print('too hot')
else:
   print('nice weather')
house = 1000000
good_credit = True
if good_credit:
   print(int(house) * (0.1))
else:
   print(int(house) * (0.2))





03p.11.20





if len(name)<4:
   print("your name must be at least 4 digits")
elif len(name)>8:
   print("your name must be less than eighit digits")
else:
   print('your name is good')
sakib = 'a'
print(sakib.upper())




 04.11.20




wt = int(input('weight: '))
convertor = input("Type 'k' for kg or,type 'l' for lbs ")
if convertor.upper()== "K":
   print(f"your weight is {wt * 2.2} lbs 60")
elif convertor.upper() == "L":
   print(f"Your weight is {wt * 0.45} kg")
else:
   print("'k' or, 'l' ") 

income = int(input("What is your annual income? "))
Tax = 'Your annual tax is'
if income < 250000:
   print(f'{Tax} {income*0 } taka')
elif income >=250000< 400000:
   print(f'{Tax} {income * 0.05} taka')
elif income >= 400000 < 1200000:
   print(f'{Tax} {income * 0.10} taka')
if income > 1200000:
   print(f'{Tax} {income * 0.20} taka')




06.11.20




is_hot = True
is_cold = False

if is_hot and is_cold:
   print('OK')
else:
   print('No problem')


number = 1
desired = 5
while number <= desired:
   print(number)
   number=number+1
print('done')

secret_number = 9
counting_starting = 0
counting_ending = 3
desired = 5
while counting_starting < counting_ending:
   guess = int(input("Type your guess: "))
   counting_starting = counting_starting + 1
   if guess == secret_number:
       print('Congratulations! You succeeded ')
       break
   else: print('Sorry, you failed! ')
   print('You lost')




08.11.20




ban = [2, 2, 2, 6]
for look in (ban):
   dog=""
   for cat in range(look):
       dog = dog + "a"
   print(dog)

price = [15, 20, 30, 35]
total = 0
for calc in price:
   total += calc
print(total)

for x in range(3):
   for y in range(2):
      print(f'({x}:{y})')


started = False
while True:
   challange= input()
   if challange == 'start':
       if started:
           print('Already started...')
       else:
           started=True
           print("started..")
   elif challange == 'menu':
       print('Rules are here')
   elif challange== 'stop':
       if not started:
          print('already stopped')
       else:
           started=False
           print("stopped")
   elif challange== 'exit':
       print('exit')
       break




9.11.20




items = [6,4,2,7,5,8]
max = items[0]

for choice in items:
   if choice >  max:
       max = choice
print(max)





13.11.20




charc = ['tamim', 'sakib']
print(charc[-1])

list = ['rat', 'cat', 'bat', 'hat', 'mat']
list[1]='mango'
print(list[:])




14.11.20




mango = [1, 2, 5, 3]
print(2 in mango)

mango = [1, 2, 4, 1, 3]
print(mango.count(1))
 mango = [1, 2, 4, 1, 3]
mango.sort()
mango.reverse()
print(mango)

mango = [1, 2, 4, 1, 3]
banana = mango.copy()
mango.append(90)
print(banana

mango = [1, 2, 4, 1, 3]
mango.append(90)
print(mango)

mango.insert()
mango.append()
mango.clear()
mango.index()
print(mango.index(3))
mango.pop()

mango = [1, 5, 2, 4, 1, 4, 2, 1, 5]
no_duplication = []
for serial in mango:
   if serial not in no_duplication:
       no_duplication.append(serial)
print(no_duplication)

#tuples
mango = (1, 3, 4)

mango = (1, 3, 4)
x,y,z = mango
result = x * y * z
print(result)

value = {
   '1' : 'one'
}
print(value.get('1'))
print(value['1'])
print(value.get('5', 'five'))
value['1']='exceptional one'
print(value['1'])


topic = input("Number: ")
dictionary = {
  '1': 'one',
  '2': 'two',
  '3': 'three'
}

output = ""
for data in topic:
   output += dictionary.get(data, "!") + " "
print(output)


  

mango = 'he is a good boy'
orange = mango.split()
change = {
   'boy': 'man'
}
output = ''
for next in orange:
   output += change.get(next, next)+ " "
print(output)

mango = 'he is a good boy'
orange = mango.split()
print(orange)


def new_topic(name, qualification):
   print(f'Hi {name} { qualification}')
   print('how are you')
new_topic('tamim', 'engineer')
new_topic('sakib', 'doctor')




15.11.20



def square(digit):
   return digit * digit
print(square(int(input(">"))))

def square(digit):
   return digit * digit
print(square(3))


topic = input(">")
split = topic.split()
dictionary = {
  'good': 'bad',
  'brave': 'coward',
  'honest': 'corrupted'
}
output = ""
for data in split:
  output += dictionary.get(data, data) + " "
print(output)

def first_time(topic):
   split = topic.split()
   dictionary = {
       'good': 'bad',
       'brave': 'coward',
       'honest': 'corrupted'
   }
   output = ""
   for data in split:
       output += dictionary.get(data, data) + " "
   return output

topic = input(">")
print(first_time(topic))

