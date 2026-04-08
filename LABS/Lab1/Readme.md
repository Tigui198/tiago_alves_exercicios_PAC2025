## README.md

# LAB 1 - Sistema de Chat com Deteção de Dados Pessoais (GDPR) para Multiusuários em Python

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema de chat multiusuário em Python que permite a comunicação em tempo real entre vários clientes conectados a um servidor central. O sistema implementa funcionalidades de deteção de dados pessoais em conformidade com o Regulamento Geral de Proteção de Dados (GDPR) e deteção de padrões de engenharia social.

## Requisitos do Sistema

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (utiliza apenas módulos nativos)

## Estrutura do Projeto

```
projeto_chat_gdpr/
│
├── servidor.py          # Código fonte do servidor
├── cliente.py           # Código fonte do cliente
├── README.md            # Documentação do projeto
└── logs/                # Pasta criada automaticamente
    ├── gdpr.txt         # Registo de violações GDPR
    └── eng_social.txt   # Registo de tentativas de engenharia social
```

## Tecnologias e Bibliotecas Utilizadas

| Tecnologia                    | Descrição                                     |
| ----------------------------- | ----------------------------------------------- |
| Python 3                      | Linguagem principal de desenvolvimento          |
| Módulo socket                | Comunicação entre cliente e servidor          |
| Threading                     | Suporte a múltiplos utilizadores simultâneos  |
| Expressões regulares (regex) | Deteção de dados pessoais nas mensagens       |
| Logging                       | Registo de eventos e violações de privacidade |

## Funcionalidades Implementadas

### Servidor

- Aceitação de múltiplas conexões simultâneas de clientes utilizando threading
- Manutenção de lista de todos os clientes conectados
- Repasse de mensagens para todos os outros utilizadores
- Deteção de dados pessoais nas mensagens (emails, telefones, IPs, etc.)
- Bloqueio de mensagens que contenham dados pessoais
- Envio de alertas aos clientes sobre violações de privacidade
- Registo de logs de conexões, desconexões e violações

### Cliente

- Conexão ao servidor e envio de mensagens de texto
- Exibição de mensagens recebidas do servidor
- Alerta quando uma mensagem é bloqueada por conter dados pessoais
- Comandos especiais: /users (listar utilizadores) e /sair (desconectar)

### Deteção de Dados Pessoais (GDPR)

O sistema deteta e bloqueia mensagens que contenham:

- Endereços de email
- Números de telefone (9 dígitos)
- Endereços IP
- Nomes completos
- Datas de nascimento
- Números de cartões de crédito

### Engenharia Social

O sistema regista tentativas suspeitas de engenharia social baseadas em palavras-chave como: urgente, grátis, oferta, clica, ganhaste, promoção, confia.

### Multiusuários

- Suporte a múltiplos utilizadores conectados simultaneamente
- Gerenciamento de threads para cada cliente
- Notificações de entrada e saída de utilizadores

## Como Executar o Projeto

### No CMD

#### 1. Iniciar o Servidor

Abra um terminal e execute o seguinte comando:

```bash
python servidor.py
```

Deverá visualizar a mensagem:

```
Servidor a correr em 127.0.0.1:12340
```

#### 2. Iniciar os Clientes

Abra terminais separados para cada cliente que deseja conectar:

```bash
python cliente.py
```

Para cada cliente, será solicitado um nome de utilizador. Utilize nomes diferentes para cada cliente.

### No VS Code

#### 1. Abrir o Projeto

- File -> Open Folder -> selecionar a pasta do projeto

#### 2. Executar o Servidor

- Clique com o botão direito no ficheiro `servidor.py`
- Selecione "Run Python File in Terminal"

OU

- Abra o terminal integrado (Ctrl + `)
- Digite: `python servidor.py`

#### 3. Executar os Clientes

- Abra novos terminais (Ctrl + Shift + `)
- Em cada terminal, digite: `python cliente.py`

## Guia de Utilização

### Comandos Disponíveis

| Comando    | Descrição                                   |
| ---------- | --------------------------------------------- |
| `/users` | Lista todos os utilizadores online no momento |
| `/sair`  | Desconecta o cliente do servidor              |

### Exemplo de Utilização

**Cliente 1 (João):**

```
Nome: João
Conectado! Comandos: /users, /sair
> Olá a todos!
```

**Cliente 2 (Maria):**

```
Nome: Maria
Conectado! Comandos: /users, /sair
> Olá João!
```

**Mensagem Bloqueada (contém dados pessoais):**

```
> O meu email é joao@email.com

[SISTEMA] ALERTA: Mensagem bloqueada (contem dados pessoais)
```

**Listar Utilizadores:**

```
> /users
[SISTEMA] Utilizadores: João, Maria
```

## Sistema de Logs

Todos os eventos importantes são registados na pasta `logs/`:

### gdpr.txt

Regista todas as tentativas de envio de dados pessoais:

```
2024-01-15 10:30:45.123456 | João | O meu email é joao@email.com
2024-01-15 10:35:20.654321 | Maria | O meu telemóvel é 912345678
```

### eng_social.txt

Regista mensagens que contêm padrões de engenharia social:

```
2024-01-15 10:40:10.789012 | Carlos | Clica aqui para ganhares um prémio urgente
```

## Como Encerrar o Sistema

1. Em cada cliente: digite `/sair` ou feche o terminal
2. No servidor: pressione `Ctrl + C`
