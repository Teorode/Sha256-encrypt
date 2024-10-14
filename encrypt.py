import hashlib

sha256hash = hashlib.sha256()

input = input("Co chcesz zamienić na hash sha256?" + " ")

input_bytes = input.encode('utf-8')
sha256hash.update(input_bytes)

result = sha256hash.hexdigest()

print(result)