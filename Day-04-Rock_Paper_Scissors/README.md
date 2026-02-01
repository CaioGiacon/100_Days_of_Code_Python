## Rock Paper Scissors 🪨📄✂️
Este é o projeto do Day 4 do desafio 100 Days of Code. É uma implementação clássica do jogo "Pedra, Papel e Tesoura" (Jokenpô) jogado contra o computador no terminal.

## 📋 Sobre o Projeto
O Rock Paper Scissors é um jogo de sorte e lógica simples. O objetivo principal deste projeto foi praticar a aleatoriedade e o uso de listas em Python. O programa pede ao usuário para fazer uma escolha, gera uma escolha aleatória para o computador e determina o vencedor com base nas regras clássicas.

Objetivos de Aprendizado
- Módulo Random: Uso de random.randint() para gerar a jogada do computador.

- Listas (Lists): Armazenamento das artes ASCII em uma lista para fácil acesso baseado no índice (0, 1, 2).

- Condicionais Complexas: Lógica para comparar todas as combinações possíveis de vitória, derrota e empate.

- Tratamento de Erros: Verificação básica se o usuário inseriu um número válido.

## 🚀 Tecnologias Utilizadas
Python

Módulo random

## 📂 Estrutura de Arquivos
```/Day-04-Rock_Paper_Scissors
    └── main.py  # Arquivo principal do jogo
```

## 🎮 Como Executar
Certifique-se de ter o Python instalado em sua máquina.

Clone o repositório:

```Bash
git clone https://github.com/CaioGiacon/100_Days_of_Code_Python.git
```
Navegue até a pasta do projeto:

```Bash
cd 100_Days_of_Code_Python/Day-04-Rock_Paper_Scissors
```
Execute o jogo:

```Bash
python main.py
```
## 🕹️ Exemplo de Gameplay
O jogo roda no terminal e exibe as mãos (arte ASCII) para cada jogada:

```Plaintext
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
> 0

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You lose!
```
(Regras: Pedra quebra Tesoura, Tesoura corta Papel, Papel embrulha Pedra).

## 👤 Autor
Caio Giacon

Projeto desenvolvido durante o quarto dia da jornada de aprendizado em Python.
