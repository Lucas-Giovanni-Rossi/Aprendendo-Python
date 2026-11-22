from hashlib import sha256  # recomendado

# SHA = Secure Hash Algoritmo

text = 'Coração'
cod = text.encode('utf-8')
hash = sha256(cod).hexdigest()

print(hash)
