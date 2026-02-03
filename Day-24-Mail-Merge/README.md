## Mail Merge Automation ✉️📝
Este projeto é o desafio do Day 24 do 100 Days of Code. Trata-se de um script de automação que gera cartas personalizadas para múltiplos destinatários, substituindo marcadores de texto em um modelo padrão.

## 📋 Sobre o Projeto
O Mail Merge resolve uma tarefa repetitiva comum: enviar a mesma carta para várias pessoas, mudando apenas o nome. O programa lê uma lista de convidados e um modelo de carta, e então cria um arquivo de texto individual para cada pessoa na pasta de saída.

Funcionalidades
- Leitura de Arquivos: Carrega uma lista de nomes (invited_names.txt) e um modelo de carta (starting_letter.txt).

- Processamento de Texto: Remove quebras de linha indesejadas e substitui o placeholder [name] pelo nome real do convidado.

- Geração de Arquivos: Salva cada carta personalizada como um novo arquivo .txt em um diretório específico.

Objetivos de Aprendizado
- Manipulação de Arquivos e Caminhos (File Paths).

- Métodos de leitura (.readlines(), .read()) e escrita (.write()).

- Métodos de string (.replace(), .strip()).

- Automação de tarefas repetitivas.

## 🚀 Tecnologias Utilizadas
Python

Manipulação de I/O de arquivos (Built-in)

## 📂 Estrutura de Diretórios
A estrutura de pastas é crucial para este projeto funcionar corretamente:

```/Day-24-Mail-Merge
    ├── Input
    │   ├── Letters
    │   │   └── starting_letter.txt  # Modelo com o placeholder "[name]"
    │   └── Names
    │       └── invited_names.txt    # Lista de nomes
    ├── Output
    │   └── ReadyToSend             # Onde as cartas geradas são salvas
    └── main.py                     # Script de automação
```

## 🎮 Como Executar
Certifique-se de ter o Python instalado e de manter a estrutura de pastas intacta.

Clone o repositório:

```Bash
git clone https://github.com/CaioGiacon/100_Days_of_Code_Python.git
```
Navegue até a pasta do projeto:

```Bash
cd 100_Days_of_Code_Python/Day-24-Mail-Merge
```
Verifique os arquivos de entrada (Opcional):

Você pode editar o invited_names.txt para adicionar mais nomes.

Certifique-se de que o starting_letter.txt contém o texto [name] onde o nome deve aparecer.

Execute o script:

```Bash
python main.py
```
Verifique o resultado: Abra a pasta Output/ReadyToSend. Você verá arquivos como letter_for_Aang.txt, letter_for_Zuko.txt, etc.

## 📝 Exemplo de Processamento
```Entrada (Modelo):

Dear [name], You are invited to my birthday...

Entrada (Lista):

Aang Zuko

Saída (Arquivos Gerados):

Arquivo 1: "Dear Aang, You are invited..." Arquivo 2: "Dear Zuko, You are invited..."
```

## 👤 Autor
Caio Giacon

Projeto desenvolvido para praticar automação e manipulação de sistema de arquivos em Python.

