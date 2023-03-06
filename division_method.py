def hash_division(key, size):
    # Возвращает индекс хэш-таблицы для заданного ключа методом деления
    return key % size

hash_table = [None] * 10 # создаем хэш-таблицу из 10 элементов
keys = [3, 7, 12, 15, 21, 27, 31, 42, 56, 63] # список ключей
for key in keys:
    index = hash_division(key, len(hash_table)) # вычисляем индекс для ключа
    hash_table[index] = key # сохраняем ключ в хэш-таблицу
print(hash_table)
