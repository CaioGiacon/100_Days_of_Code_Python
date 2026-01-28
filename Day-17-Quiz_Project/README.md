# 🧠 Quiz Game (OOP)

Este projeto é um jogo de perguntas e respostas (Quiz) desenvolvido em Python. Ele foi criado como parte do desafio **100 Days of Code**, com foco principal em **Programação Orientada a Objetos (POO)**.

## 📋 Funcionalidades

O programa roda no terminal e apresenta as seguintes características:

* **Banco de Questões:** Uma lista de perguntas de Verdadeiro ou Falso (True/False).
* **Verificação de Respostas:** O sistema valida a entrada do usuário instantaneamente.
* **Pontuação ao Vivo:** Mostra a pontuação atual após cada rodada.
* **Fim de Jogo:** Exibe a pontuação final e o total de acertos ao terminar as perguntas.
* **Estrutura Modular:** Código dividido em classes lógicas para melhor organização e manutenção.

## 🛠️ Tecnologias e Conceitos

* **Python 3**
* **Programação Orientada a Objetos (POO):** Criação de Classes, Objetos, Atributos e Métodos.
* **Modularização:** Separação de responsabilidades em arquivos diferentes.

## 📂 Estrutura do Projeto

O código está organizado em quatro arquivos principais, cada um com uma função específica:

* `main.py`: O ponto de entrada do programa. Inicializa o jogo e gerencia o loop principal.
* `question_model.py`: Define a classe `Question`, que estrutura como cada pergunta deve ser (texto + resposta).
* `data.py`: Contém a lista de perguntas (dados brutos) que alimenta o jogo.
* `quiz_brain.py`: Contém a classe `QuizBrain`, responsável pela lógica do jogo (fazer a próxima pergunta, checar resposta, contar pontuação).

## 🚀 Como Executar

Certifique-se de ter o Python instalado em sua máquina.

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/CaioGiacon/Quiz.git](https://github.com/CaioGiacon/Quiz.git)
    ```
2.  Entre na pasta do projeto:
    ```bash
    cd Quiz
    ```
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

## 🎮 Exemplo de Uso

```text
Q.1: A slug's blood is green. (True/False): True
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): False
You got it right!
...
```

## 👤 Autor
Desenvolvido por Caio Giacon durante a jornada de aprendizado em Python.

Este projeto é apenas para fins educacionais.
