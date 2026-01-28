alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    final_text = ''
    for letter in original_text:
        if encode_or_decode == 'decode':
            if letter not in alphabet:
                final_text += letter
                continue
            text = alphabet.index(letter) - shift_amount
        elif encode_or_decode == 'encode':
            if letter not in alphabet:
                final_text += letter
                continue
            text = alphabet.index(letter) + shift_amount
        text %= len(alphabet)
        final_text += alphabet[text]

    print(f'Here is the {encode_or_decode}d result: {final_text}')

