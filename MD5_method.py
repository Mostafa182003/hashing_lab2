import hashlib

# Ввод текста
text = input("Введите текст для хеширования: ")

# Конвертация текста в байты
text_bytes = text.encode('utf-8')

# Создание объекта MD5
md5_hash = hashlib.md5()

# Обновление объекта с помощью текстовых байтов
md5_hash.update(text_bytes)

# Преобразование в 16тиричная систем
hash_hex = md5_hash.hexdigest()

# Вывод в консоль
print("MD5 hash текста:", hash_hex)
