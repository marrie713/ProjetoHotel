# ProjetoHotel
# Sistema de Gerenciamento de Hotel

Trabalho Final da disciplina de Programação Orientada a Objetos (POO) desenvolvido em Python.

Este projeto consiste em um sistema completo de gerenciamento hoteleiro executado via terminal, desenvolvido para aplicar conceitos de Programação Orientada a Objetos como encapsulamento, herança, polimorfismo, composição, persistência de dados e modularização.

---

# Objetivo

Desenvolver um sistema funcional para gerenciamento básico de um hotel utilizando os conceitos estudados na disciplina.

O sistema permite:

- Cadastro de hóspedes
- Cadastro de funcionários
- Controle de quartos
- Reservas
- Check-out
- Emissão de relatórios
- Persistência automática dos dados

---

# Requisitos Atendidos

## Programação Orientada a Objetos

✔ Utilização de classes  
✔ Criação de objetos  
✔ Encapsulamento  
✔ Métodos  
✔ Atributos  

---

## Herança

Foi utilizada uma classe base chamada Pessoa.

Estrutura:

```plaintext
Pessoa
├── Hospede
└── Funcionario
```

---

## Polimorfismo

O polimorfismo foi aplicado através do método:

```python
exibir_dados()
```

Cada classe filha implementa sua própria forma de exibir informações.

---

## Composição

A composição foi aplicada na classe Reserva.

Uma reserva depende diretamente de:

- Hospede
- Quarto

Exemplo:

```python
Reserva(hospede, quarto, dias)
```

---

## Persistência de Dados

Os dados permanecem disponíveis mesmo após o encerramento do sistema através de arquivos JSON.

Classe responsável:

```plaintext
Persistencia
```

Métodos utilizados:

```python
Persistencia.salvar()
Persistencia.carregar()
```

Arquivos gerados automaticamente:

```plaintext
dados/
├── hospedes.json
├── funcionarios.json
├── quartos.json
└── reservas.json
```

As alterações são salvas automaticamente após:

- Cadastro de hóspedes
- Cadastro de funcionários
- Realização de reservas
- Finalização de reservas

Ao iniciar novamente o sistema, os dados são carregados automaticamente.

---

## Modularização

O sistema foi organizado em múltiplos arquivos.

---

# Funcionalidades Implementadas

## Hóspedes

- Cadastrar hóspedes
- Listar hóspedes

## Funcionários

- Cadastrar funcionários
- Listar funcionários

## Quartos

- Listar quartos disponíveis
- Listar quartos ocupados

## Reservas

- Realizar reserva
- Listar reservas
- Finalizar reserva (Check-out)

## Relatórios

- Gerar relatório geral

## Comprovantes

- Emissão automática de comprovante ao realizar reserva

---

# Conceitos Aplicados

## Classes e Objetos

Classe principal:

```python
hotel = Hotel()
```

Responsável pelo gerenciamento das operações.

---

## Encapsulamento

Foram utilizados:

```python
@property
@setter
```

Exemplos:

```python
__nome
__cpf
__telefone
__cargo
__ocupado
```

---

# Estrutura do Projeto

```plaintext
ProjetoHotel/
│
├── main.py
│
├── classes/
│   ├── hotel.py
│   ├── pessoa.py
│   ├── hospede.py
│   ├── funcionario.py
│   ├── quarto.py
│   └── reserva.py
│
├── utils/
│   └── persistencia.py
│
├── dados/
│   ├── hospedes.json
│   ├── funcionarios.json
│   ├── quartos.json
│   └── reservas.json
│
└── README.md
```

---

# Relatório

Exemplo:

```plaintext
===== RELATÓRIO =====

Hóspedes cadastrados
Funcionários cadastrados
Quantidade de quartos
Reservas ativas
Quartos disponíveis
Quartos ocupados
```

---

# Modelo de Comprovante

```plaintext
================================

RESERVA REALIZADA

================================

Hóspede: [Nome do hóspede]
Quarto: [Número do quarto]
Diárias: [Quantidade]
Valor Total: R$ [Calculado automaticamente]

================================
```

---

# Tecnologias Utilizadas

- Python 3.x
- JSON
- Biblioteca os
- Programação Orientada a Objetos

---

# Instalação e Execução

1. Baixe ou extraia os arquivos do projeto

2. Abra a pasta do projeto

3. Execute:

```bash
python main.py
```

---

# Exemplo de Uso

1. Iniciar sistema
2. Cadastrar hóspede
3. Cadastrar funcionário
4. Realizar reserva
5. Emitir comprovante
6. Finalizar reserva
7. Gerar relatório

---

# Integrantes

- Maria Tereza
- Ana Julia
- Gustavo Henrique
- Mariely

Projeto desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.

