import hashlib

# Text input
text = input("Введите текст для хеширования: ")

# Convert text to bytes
text_bytes = text.encode('utf-8')

# Create an MD5 object
md5_hash = hashlib.md5()

# Update object with text bytes
md5_hash.update(text_bytes)

# Convert to hexadecimal systems
hash_hex = md5_hash.hexdigest()

# Output to console
print("MD5 hash текста:", hash_hex)
