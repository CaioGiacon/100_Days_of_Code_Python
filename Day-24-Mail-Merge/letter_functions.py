def cleaning_letter(user_letter, caracter_target, choose_replacement):
    '''
    Essa função é responsável por limpar a carta.
    user_letter = carta do usuário
    caracter_target = caracter alvo que deseja tirar
    choose_replacement = nova escolha para substituir o valor antigo   
    '''
    if caracter_target in user_letter:
        new_letter = user_letter.replace(caracter_target, choose_replacement)
    return new_letter

def personalized_and_save_letter(save_path, target, letter, names):
    '''
    Essa função personaliza a carta com o nome do convidado e salva a carta na pasta ReadyToSend
    save_path = adiciona o caminho de preferência do usuário
    target = valor alvo que deseja substituir
    letter = carta do usuário
    '''
    for guest_name in names:
        if target in letter:
            stripped_name = guest_name.strip()
            guest_letter = letter.replace('name', stripped_name)
            
            with open(f'{save_path}{guest_name}.text', 'w') as arquivo:
                arquivo.write(guest_letter)