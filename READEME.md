# Website pessoal para publicação de conteudo

Implementar um conjunto de páginas web com a capacidade de:

1. Fornecer páginas estaticas - PÚBLICAS
2. Fornecer uma estrutura de gerenciamento de arquivos de midia (tipo galeria de fotos)
3. Uma estrutura para relacionamento com outros usuarios (pode ser um falecom)

## Como o conteúdo será apresentado:

1. Formato de Blog
2. Uma timeline com todas as postagens ordenadas por data de publicação
3. Uma página com os detalhes de cada publicação


## O que eu preciso para fazer isso funcionar?

0. Criar um ambiente de isolamento do python - virtualenv

> CRIAR UM AMBIENTE ISOLADO

> python3 -m venv nome-do-ambiente

Para ativar o seu ambiente virtual use o comando a baixo:

> source nome-do-ambiente/bin/activate

1. Django - Framework para desenvolvimento ágil na Web

> INSTALAR DJANGO - Como faço isto?

Para instalar o django, bem como qualquer outro utilitário python, você pode usar o PIP.

2. Banco de dados - SQLite

> INSTALAR O SQLITE

## O que é o Django

- Framework escrito em Pyhton para desenvolver com python para Web 
- Ele permite manipular de forma simples os verbos HTTP - HyperText Transfer Protocol
  - GET
  - POST
  - UPDATE
  - DELETE
- Ele permite trabalhar com templates HTML - HyperText Markup Language 
- Permite criar projetos Web
  - O utilitário django-admin com o seguinte comando:

  > django-admin startproject nome-do-projeto