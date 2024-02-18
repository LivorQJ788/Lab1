users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
o = len(users)
u = len(set(users))
dicts = {"Общее количество": o, "Уникальные посещения": u}
print(dicts)
