# 🐍 Python Modules 00 & 01 — 42
<p align="center">
  <img src="https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" 
       alt="Python programming" 
       width="500">
</p>

Projetos desenvolvidos durante a formação da **42**, com foco na introdução à linguagem Python e na transição dos conceitos fundamentais de programação para uma abordagem orientada a objetos.

---

## 📚 Sobre os módulos

Os módulos **Python Module 00** e **Python Module 01** fazem parte da trilha de Python da 42.

O objetivo é desenvolver uma base sólida na linguagem, trabalhando desde conceitos básicos de sintaxe até os primeiros princípios de **Programação Orientada a Objetos (POO)**.

Durante os módulos, são abordados conceitos como:

* Sintaxe e estrutura do Python
* Variáveis e tipos de dados
* Funções
* Condicionais
* Loops
* Listas, tuplas, dicionários e conjuntos
* Manipulação de strings
* Argumentos de linha de comando
* Módulos e imports
* Classes e objetos
* Atributos e métodos
* Encapsulamento
* Herança
* Polimorfismo
* Métodos especiais (`__init__`, `__str__`, etc.)
* Boas práticas de organização de código

---

# 📁 Estrutura do projeto

```text
Python_Modules/
│
├── Python_Module_00/
│   ├── ex00/
│   ├── ex01/
│   ├── ex02/
│   ├── ...
│   └── README.md
│
├── Python_Module_01/
│   ├── ex00/
│   ├── ex01/
│   ├── ex02/
│   ├── ...
│   └── README.md
│
└── README.md
```

A organização pode variar de acordo com a estrutura utilizada no repositório.

---

# 🟢 Module 00

## Objetivo

O primeiro módulo apresenta os fundamentos da linguagem Python.

A ideia principal é aprender a escrever pequenos programas utilizando a sintaxe da linguagem e compreender as diferenças entre Python e linguagens como C.

### Principais conceitos

### Variáveis

```python
name = "Maria"
age = 20
```

Python possui tipagem dinâmica, portanto não é necessário declarar explicitamente o tipo da variável.

---

### Tipos básicos

Alguns dos principais tipos trabalhados:

```python
int
float
str
bool
None
```

Exemplo:

```python
age = 20
height = 1.65
name = "Maria"
student = True
```

---

### Strings

Manipulação de textos:

```python
name = "Python"

print(name.upper())
print(name.lower())
print(len(name))
```

Também são trabalhadas diferentes formas de formatação:

```python
name = "Maria"
print(f"Hello, {name}!")
```

---

### Condicionais

Estruturas de decisão:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Também são utilizados:

```python
if
elif
else
```

---

### Loops

Repetição utilizando `for` e `while`.

```python
for number in range(5):
    print(number)
```

E:

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```

---

### Listas

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

Operações comuns:

```python
append()
remove()
pop()
sort()
```

---

### Tuplas

Tuplas são estruturas semelhantes às listas, porém imutáveis.

```python
coordinates = (10, 20)
```

---

### Dicionários

Estrutura baseada em chave e valor:

```python
student = {
    "name": "Maria",
    "age": 20
}

print(student["name"])
```

---

### Funções

Criação e utilização de funções:

```python
def greet(name):
    return f"Hello, {name}!"
```

Uso:

```python
print(greet("Maria"))
```

---

### Argumentos de linha de comando

Os exercícios também introduzem o acesso aos argumentos fornecidos pelo terminal.

Exemplo:

```bash
python3 program.py hello world
```

Podemos acessar esses argumentos utilizando:

```python
import sys

print(sys.argv)
```

---

# 🔵 Module 01

## Objetivo

O Module 01 introduz conceitos mais avançados da linguagem, principalmente **Programação Orientada a Objetos (POO)**.

A partir deste módulo, o foco passa a ser a criação de estruturas utilizando **classes e objetos**.

---

# 🧱 Classes e objetos

Uma classe funciona como um modelo para criar objetos.

Exemplo:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Criando um objeto:

```python
person = Person("Maria")

print(person.name)
```

---

# 🔧 Métodos

Métodos são funções pertencentes a uma classe.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")
```

Uso:

```python
person = Person("Maria")
person.greet()
```

---

# 🏗️ Constructor — `__init__`

O método `__init__` é executado quando um objeto é criado.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Então:

```python
person = Person("Maria", 20)
```

faz com que os atributos sejam inicializados automaticamente.

---

# 🧩 Encapsulamento

O Python permite controlar a forma como determinados atributos são acessados.

Por exemplo:

```python
class Person:
    def __init__(self, name):
        self._name = name
```

O `_` indica que o atributo é destinado ao uso interno da classe por convenção.

Também podem ser utilizados métodos `@property` para controlar o acesso:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

---

# 🧬 Herança

Uma classe pode herdar características de outra classe.

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")
```

Nesse exemplo, `Dog` herda de `Animal`.

---

# 🔄 Polimorfismo

Classes diferentes podem implementar o mesmo método de maneiras diferentes.

```python
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")
```

Podemos trabalhar com ambos através da mesma interface:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Resultado:

```text
Woof!
Meow!
```

---

# ⭐ Métodos especiais

Python possui métodos especiais, também conhecidos como **dunder methods**.

Exemplo:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

Agora:

```python
person = Person("Maria")
print(person)
```

utiliza automaticamente o método `__str__`.

Alguns métodos importantes:

```text
__init__
__str__
__repr__
__len__
__eq__
```

---

# 🎯 Objetivos de aprendizagem

Ao finalizar os módulos 00 e 01, os principais objetivos são:

* [x] Compreender a sintaxe básica do Python
* [x] Trabalhar com diferentes tipos de dados
* [x] Utilizar condicionais
* [x] Utilizar loops
* [x] Criar e utilizar funções
* [x] Trabalhar com listas e dicionários
* [x] Manipular strings
* [x] Utilizar módulos
* [x] Trabalhar com argumentos de terminal
* [x] Criar classes
* [x] Criar objetos
* [x] Utilizar atributos e métodos
* [x] Entender encapsulamento
* [x] Utilizar herança
* [x] Compreender polimorfismo
* [x] Trabalhar com métodos especiais

---

# ▶️ Como executar

## Requisitos

* Python 3
* Terminal
* Git

Verifique a instalação:

```bash
python3 --version
```

---

## Executando um exercício

Entre na pasta correspondente:

```bash
cd Python_Module_00/ex00
```

Execute:

```bash
python3 script.py
```

Ou, dependendo do nome do arquivo:

```bash
python3 nome_do_exercicio.py
```

---

# 🧪 Testando

Uma boa prática durante os exercícios é testar diferentes entradas.

Exemplo:

```bash
python3 script.py
python3 script.py "hello"
python3 script.py "hello world"
python3 script.py 42
```

Também é importante testar casos inesperados, como:

* Nenhum argumento
* Muitos argumentos
* Strings vazias
* Valores inválidos
* Tipos diferentes
* Valores negativos
* Valores extremos

---

# 🧠 O que este projeto representa

Estes módulos representam a transição dos fundamentos de programação para uma linguagem de alto nível e para a **Programação Orientada a Objetos**.

O foco não é apenas fazer os exercícios funcionarem, mas compreender:

```text
Entrada
   ↓
Processamento
   ↓
Estrutura dos dados
   ↓
Lógica
   ↓
Saída
```

E, no Module 01, começar a pensar em:

```text
Classe
   ↓
Objeto
   ↓
Atributos
   ↓
Métodos
   ↓
Interação entre objetos
```

---

# 🚀 Próximos passos

Após os módulos 00 e 01, os próximos estudos podem aprofundar:

* Exceções
* Iteradores
* Generators
* Decorators
* Abstract Base Classes
* Type hints
* Manipulação de arquivos
* Pacotes Python
* APIs
* Testes automatizados
* Boas práticas de arquitetura

---

## 👩‍💻 Projeto

Desenvolvido como parte da formação da **42**.

```text
42 São Paulo
Python Modules
Module 00 + Module 01
```

> Aprender Python não é apenas aprender uma nova sintaxe.
> É aprender a resolver problemas utilizando uma nova forma de pensar.
