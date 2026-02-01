## Snake Game (Part 2) 🐍🍎
Este projeto refere-se ao Day 21 do desafio 100 Days of Code. Aqui, finalizamos a implementação do clássico jogo "Snake" (o jogo da cobrinha), adicionando lógica de colisão, sistema de pontuação e mecânicas de crescimento.

## 📋 Sobre o Projeto
Enquanto a Parte 1 focou na animação e controle da cobra, a Parte 2 transforma o projeto em um jogo jogável. O código foi modularizado utilizando Programação Orientada a Objetos (POO), introduzindo conceitos importantes como Herança de Classes (Class Inheritance).

Funcionalidades Implementadas
- Comer a Comida: A cobra detecta colisão com a comida, cresce de tamanho e a pontuação aumenta.

- Placar (Scoreboard): Um placar no topo da tela rastreia a pontuação atual.

- Game Over (Paredes): O jogo termina se a cobra colidir com as bordas da tela.

- Game Over (Cauda): O jogo termina se a cobra colidir com o próprio corpo.

- Herança: As classes Food e Scoreboard herdam funcionalidades da classe Turtle para renderização gráfica.

## 🚀 Tecnologias e Conceitos
- Python

- Turtle Graphics

- Herança (Inheritance): Criar classes que herdam atributos e métodos de outras (ex: class Food(Turtle)).

- Slicing (Fatiamento): Uso de list slicing para verificar colisões com o corpo da cobra (ex: ignorar a cabeça ao checar os segmentos).

## 📂 Estrutura de Arquivos
O projeto é dividido em módulos para manter o código limpo:

```/Day-21-Snake_Game_Pt2
    ├── main.py        # Orquestrador do jogo (Game Loop)
    ├── snake.py       # Lógica da cobra (movimento, criação, controle)
    ├── food.py        # Lógica da comida (aparecimento aleatório, herança)
    └── scoreboard.py  # Gerencia o texto do placar e Game Over
```

## 🎮 Como Executar
Certifique-se de ter o Python instalado em sua máquina.

Clone o repositório:

```Bash
git clone https://github.com/CaioGiacon/100_Days_of_Code_Python.git
```
Navegue até a pasta do projeto:

```Bash
cd 100_Days_of_Code_Python/Day-21-Snake_Game_Pt2
```
Execute o jogo:

```Bash
python main.py
```
## 🕹️ Controles
Utilize as setas do teclado para guiar a cobra:

```
↑ -> Mover para Cima
↓ -> Mover para Baixo
↓ -> Mover para Esquerda
↓ -> Mover para Direita
```

## 👤 Autor
Caio Giacon

Projeto desenvolvido para consolidar conhecimentos em POO em Python.

