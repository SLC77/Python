### Chiffrement César

phrase = ("HUE")
shift = 10
encoded = ''
result = []

for character in phrase:
    x = ord(character)
    encoded += chr(x+shift)

for character in phrase:
    x = ord(character)
    result.append(x+shift)

print('')
print(encoded)
print('')
print(result)

