a = str(input ("Цена за ремонт в ванной и на кухне (True/False)"))
b = str(input ("Цена за ремонт в гостиной и спальне (True/False)"))
c = str(input ("Цена за ремонт всех комнат (True/False)"))
if a == 'True' and b == 'True' and c == 'True':
    print("Можно обновить всю квартиру!")
elif a == 'True' and b == 'True' and c == 'False':
    print("Можно обновить гостиную и спальню")
elif a == 'True' and b == 'False' and c == 'False':
    print("Можно обновить ванную и кухню")
elif a == 'False' and b == 'False' and c == ('False'):
    print("Надо больше зарабатывать...(")