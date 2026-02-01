## Treasure Island 🏴‍☠️🗺️
Este é o projeto do Day 3 do desafio 100 Days of Code. É um jogo de aventura baseado em texto ("Choose Your Own Adventure") onde suas escolhas determinam se você encontra o tesouro ou enfrenta um destino terrível.

## 📋 Sobre o Projeto
O Treasure Island é um jogo de lógica condicional. O objetivo principal deste projeto foi dominar o fluxo de controle em Python. O programa apresenta uma narrativa e solicita que o usuário tome decisões (ir para esquerda ou direita, esperar ou nadar, escolher uma porta). Cada resposta leva a um novo ramo da história, utilizando condicionais aninhadas (nested if statements).

Objetivos de Aprendizado
- Controle de Fluxo: Uso avançado de if, elif e else.

- Condicionais Aninhadas: Colocar verificações dentro de outras verificações para criar árvores de decisão complexas.

- Operadores Lógicos: Gerenciamento de múltiplas condições.

- Tratamento de Strings: Uso de métodos como .lower() para garantir que o input do usuário seja aceito independentemente de maiúsculas ou minúsculas.

- Arte ASCII: Uso de arte em texto para ilustrar o jogo no terminal.

## 🚀 Tecnologias Utilizadas
Python

```## 📂 Estrutura de Arquivos
/Day-03-Treasure_Island
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
cd 100_Days_of_Code_Python/Day-03-Treasure_Island
```
Execute o jogo:

```Bash
python main.py
```

## 🕹️ Exemplo de Gameplay
O jogo roda no terminal. Você deve digitar suas escolhas para avançar:

```Plaintext
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a cross road. Where do you want to go? Type "left" or "right"
> left
You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
> wait
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
> yellow
You found the treasure! You Win! 🏆
(Nota: Escolhas erradas levam ao "Game Over", como cair em um buraco, ser atacado por trutas ou queimado por fogo).
```
👤 Autor
Caio Giacon

Projeto desenvolvido durante o terceiro dia da jornada de aprendizado em Python.

