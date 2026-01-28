from caesar_cipher import caesar_cipher
from art import logo

print(logo)
encrypt_or_decrypt = True
while encrypt_or_decrypt:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caesar_cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)
    reset_cipher = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()

    if reset_cipher == 'no':
        encrypt_or_decrypt = False