# p56.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
Type and run the following program
You are given the encrypted sentence: CLGUBA VF TERNG
Using a Shift of 13, what is the original (decyphered) message?
'''

# write a loop to show the 'original alphabet'
alphabet = ''
for i in range(65, 91, 1):
    alphabet += chr(i)
print('alphabet = ', alphabet)

shift = 3
# show the shift 'key'
print('shift = ', shift, 'letters')

# write a loop to show alphabet shifted by 3
encrypted = ''
for i in range (65, 91, 1):
    if i + shift < 91:
        encrypted += chr(i+shift)
    if i + shift >= 91:
        encrypted += chr(65 +(i+shift-91))

# show encrypted alphabet
print('encrypted = ', encrypted)

encrypt = { } # make empty dictionary
decypher = { }
encrypt [ ' ' ] = ' ' # add to dictionary
decypher [ ' ' ] = ' '
#           ^^KEY   ^^VALUE ASSOCIATED WITH KEY

for i in range(0, len(alphabet), 1):
    encrypt [alphabet[i] ] = encrypted [i]
    decypher [ encrypted [i] ] = alphabet [i]

original_message = 'HELLO WORLD'
encrypted_message = ''
for i in range (0, len(original_message), 1):
    if original_message[i] == ' ':
        encrypted_message += ' '
    else:
        encrypted_message += encrypt [original_message [i]]

print('original sentence:', original_message) # HELLO WORLD
print('encrypted sentence:', encrypted_message)
print('... decyphered:', end='')
for i in range(0, len(encrypted_message), 1):
    print(decypher[encrypted_message[i]], end='')



# write a loop to show the 'original alphabet'
alphabet = ''
for i in range(65, 91, 1):
    alphabet += chr(i)
print('\n\nalphabet = ', alphabet)

shift = 13
# show the shift 'key'
print('shift = ', shift, 'letters')

# write a loop to show alphabet shifted by 13
encrypted = ''
for i in range (65, 91, 1):
    if i + shift < 91:
        encrypted += chr(i+shift)
    if i + shift >= 91:
        encrypted += chr(65 +(i+shift-91))

# show encrypted alphabet
print('encrypted = ', encrypted)

encrypt = { } # make empty dictionary
decypher = { }
encrypt [ ' ' ] = ' ' # add to dictionary
decypher [ ' ' ] = ' '
#           ^^KEY   ^^VALUE ASSOCIATED WITH KEY

for i in range(0, len(alphabet), 1):
    encrypt [alphabet[i] ] = encrypted [i]
    decypher [ encrypted [i] ] = alphabet [i]

encrypted_message2 = 'CLGUBA VF TERNG'
decyphered_message = ''
for i in range (0, len(encrypted_message2), 1):
    if encrypted_message2[i] == ' ':
        decyphered_message += ' '
    else:
        decyphered_message += decypher [encrypted_message2 [i]]

print('encrypted sentence:', encrypted_message2)
print('... decyphered:', end='')
for i in range(0, len(decyphered_message), 1):
    print(decypher[encrypted_message2[i]], end='')

'''
================== RESTART: /Users/lailabahman/Desktop/p56.py ==================
alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
shift =  3 letters
encrypted =  DEFGHIJKLMNOPQRSTUVWXYZABC
original sentence: HELLO WORLD
encrypted sentence: KHOOR ZRUOG
... decyphered:HELLO WORLD

alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
shift =  13 letters
encrypted =  NOPQRSTUVWXYZABCDEFGHIJKLM
encrypted sentence: CLGUBA VF TERNG
... decyphered:PYTHON IS GREAT
'''

