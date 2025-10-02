# https://e.sfu-kras.ru/pluginfile.php/3439890/mod_assign/introattachment/0/Практическая%202.%20Основные%20структуры%20данных%20Python.pdf

import datetime

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

diary = {
  'понедельник': {
    'утро': ['погулять с собакой'],
    'день': [],
    'вечер': ['погулять с собакой']
  },
  'вторник': {
    'утро': ['погулять с собакой'],
    'день': [],
    'вечер': ['погулять с собакой']
  },
  'среда': {
    'утро': ['погулять с собакой'],
    'день': [],
    'вечер': ['погулять с собакой']
  },
  'четверг': {
    'утро': ['погулять с собакой'],
    'день': [],
    'вечер': ['погулять с собакой']
  },
  'пятница': {
    'утро': ['заехать в шиномонтаж', 'помыть машину'],
    'день': [],
    'вечер': ['поход в театр', 'ужин в кафе']
  },
  'суббота': {
    'утро': [],
    'день': [],
    'вечер': []
  },
  'воскресенье': {
    'утро': [],
    'день': [],
    'вечер': []
  }
}

# 1)

diary.pop('суббота')
diary.pop('воскресенье')

diary[
  ('суббота', 'воскресенье')
] = ['Посадить цветы']

print('1)', diary)

try:
  diary[
    ['суббота', 'воскресенье']
  ] = ['Посадить цветы']
except:
  print('Нельзя сделать ключ суббота,воскресенье списком')

# 2)

diary['вторник']['утро'].append('поход к зубному')
print('2)', diary['вторник']['утро'])

# 3)

diary['пятница']['вечер'][
  diary['пятница']['вечер'].index('поход в театр')
] = 'поход в кино'

print('3)', diary['пятница']['вечер'])

# 4)

for time in diary['четверг']:
  if 'погулять с собакой' in diary['четверг'][time]:
    diary['четверг'][time].remove('погулять с собакой')

print('4)', diary['четверг'])

# 5)

print('5)', diary['пятница']['утро'][1])

# 6)

diary.pop('понедельник')
print('6)', diary)

try:
  print(diary['понедельник'])
except:
  print('Нельзя получить дела на день, которого нет в словаре')

# 7)

def tasks(day):
  print(f'{day}: ', end='')
  if day not in days:
    return print('Такого дня не бывает!')
  if day not in diary:
    return print('Свободный день')
  if sum([len(diary[day][time]) for time in diary[day]]) == 0:
    return print('Свободный день')
  print()
  for time in diary[day]:
    print(time.capitalize() + ':', ', '.join(diary[day][time]) + '.',)

print('7)')
tasks('вторник')
tasks('повторник')
tasks('четверг')

# 8)

print('8)')
tasks(days[datetime.datetime.now().weekday()])

# 9)

def clear_diary():
  for day in diary:
    diary[day] = []

clear_diary()
print('9)', diary)

# 10)

print('10)')

def add_task():
  day = input('Введите день недели: ')
  time = input('Введите время суток: ')
  task = input('Введите задачу: ')
  if day not in diary or type(diary[day]) is not dict:
    diary[day] = {}
  if time not in diary[day]:
    diary[day][time] = []
  diary[day][time].append(task)

add_task()
add_task()

print(diary)
