# ☕ Coffee Machine Simulation

Este projeto é uma simulação de uma máquina de café digital baseada em linha de comando (CLI). Ele foi desenvolvido como parte do desafio **100 Days of Code - Python**, focado em lógica de programação, manipulação de dicionários e loops.

## 📋 Funcionalidades

O programa simula as operações reais de uma máquina de café automática:

* **Menu de Bebidas:** Oferece 3 opções: Espresso, Latte e Cappuccino.
* **Gerenciamento de Recursos:** Verifica se há água, leite e café suficientes antes de aceitar o pedido.
* **Processamento de Moedas:** Calcula o valor inserido pelo usuário e verifica se é suficiente para a bebida escolhida.
* **Sistema de Troco:** Devolve o troco exato se o valor inserido for maior que o custo.
* **Relatório Administrativo:** Permite visualizar o estoque atual de ingredientes e o lucro total da máquina (comando `report`).
* **Manutenção:** Opção para desligar a máquina (comando `off`).

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Estruturas de dados (Dicionários e Listas)
* Funções e Escopo

## 📂 Estrutura do Projeto

* `main.py`: Contém a lógica principal do programa (o "cérebro" da máquina).
* `data.py`: Armazena os dados de configuração, como o cardápio (ingredientes e custos) e o estado inicial dos recursos.

## 🚀 Como Executar

Certifique-se de ter o Python instalado em sua máquina.

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/CaioGiacon/Coffee_Machine.git](https://github.com/CaioGiacon/Coffee_Machine.git)
    ```
2.  Entre na pasta do projeto:
    ```bash
    cd Coffee_Machine
    ```
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

## 🎮 Exemplo de Uso

```text
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickels?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
