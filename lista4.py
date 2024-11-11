# 1) Crie uma classe "Pessoa" com um atributo privado "nome" e um método getter para acessá-lo.
# 2) Adicione um setter para o atributo "nome" da clase "Pessoa" para garantir que o nome não esteja vazio.

# class Pessoa:
#     def _init_(self, nome):
#         self.__nome = nome
    
#     def get_nome(self):
#         return self.__nome
    
#     def set_nome(self, nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print('Nome inválido')

# # Testar a função
    
# abc = Pessoa("Bruno 5555n")
# print(abc.get_nome())

# abc.set_nome("Rafael")
# print(abc.get_nome())


# 3) Crie uma clase "Carro" com um atributo privado "modelo" e use getter e setter para acessá-lo e modificá-lo.

# class Carro:
#     def _init_(self, modelo):
#         self.__modelo = modelo
    
#     def get_modelo(self):
#         return self.__modelo
    
#     def set_modelo(self, modelo):
#         if isinstance(modelo, str) and len(modelo) > 0:
#             self.__modelo = modelo
#         else:
#             print('Nome inválido')

# Testar a função
    
# abc = Carro("Palio Economy")
# print(abc.get_modelo())

# abc.set_modelo("Nissan Kicks")
# print(abc.get_modelo())

# 4) Crie uma classe "ContaBancaria" com um atributo privado "saldo" e métodos para depositar e sacar, garantindo
# que o saldo nunca seja negativo.

# class ContaBancaria:
#     def _init_(self, saldo):
#         self.__saldo = saldo if saldo >= 0 else 0 #inicializa o saldo, garantindo que não seja negativo

# Método para depositar valor na conta
    
#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#         else:
#             print("Valor depositado inválido")

# Método para sacar valor da conta

#     def sacar(self, valor):
#         if 0 < valor <= self.__saldo:
#             self.__saldo -= valor
#         else:
#             print("Valor de saque inválido")

# Método para obter o saldo atual

#     def get_saldo(self):
#         return self.__saldo

# Testar código pela entrada de dados 

# conta = ContaBancaria(1000) # Inicializa a conta com saldo de 1000

# conta.depositar(500) # Deposita 800 na conta

# print(conta.get_saldo()) # Exibe o saldo atual

# conta.sacar(2000) # Tenta sacar 2000, mas o saldo é insuficiente

# print(conta.get_saldo()) # Exibe o saldo atual

# 5) Crie uma classe "Aluno" com atributos privados "nome" e "nota". Crie getters e setters para ambos os atributos.

# class Aluno:
#     def _init_(self, nome, nota):
#         self.__nome = nome
#         self.__nota = nota

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print('Nome inválido')

#     def get_nota(self):
#         return self.__nota

#     def set_nota(self, nota):
#         if isinstance(nota, (int, float)) and 0 <= nota <= 10:
#             self.__nota = nota
#         else:
#             print('Nota inválida')

# Testar a função

# aluno = Aluno("Bruno", 9.5)
# print("Nome:", aluno.get_nome())
# print("Nota:", aluno.get_nota())

# aluno.set_nome("Rafael")
# aluno.set_nota(10)
# print("Nome:", aluno.get_nome())
# print("Nota:", aluno.get_nota())

# 6) Crie uma classe "Produto" com um atributo privado "preço". Adicione validação no setter para que o preço seja sempre positivo.

# class Produto:
#     def _init_(self, preco):
#         self.__preco = preco if preco >= 0 else 0 #inicializa o preco, garantindo que seja positivo

#     def get_preco(self):
#         return self.__preco

#     def set_preco(self, preco):
#         if isinstance(preco, (int, float)) and preco >= 0:
#             self.__preco = preco
#         else:
#             print('Preço inválido')

# Testar a função

# p1 = Produto(100)
# print("Preço:", p1.get_preco())

# p1.set_preco(-50)
# print("Preço:", p1.get_preco())

# p1.set_preco(50)
# print("Preço:", p1.get_preco())

# 7) Crie uma classe "Livro" com atributos privados "titulo" e "autor". Crie métodos para acessar e modificar
# esses atributos.

# class Livro:
#     def _init_(self, titulo, autor):
#         self.__titulo = titulo
#         self.__autor = autor

#     def get_titulo(self):
#         return self.__titulo

#     def set_titulo(self, titulo):
#         self.__titulo = titulo

#     def get_autor(self):
#         return self.__autor

#     def set_autor(self, autor):
#         self.__autor = autor

# Testar a função

# livro = Livro("Física para o ensino médio", "Kazuhito & Fuke")
# print("Título:", livro.get_titulo())
# print("Autor:", livro.get_autor())

# livro.set_titulo("O Senhor dos Aneis")
# livro.set_autor("J. R. R. Tolkien")
# print("Título:", livro.get_titulo())
# print("Autor:", livro.get_autor())

# 8) Crie uma classe "Funcionário" com um atributo privado "salário" e métodos getter e setter para modificar
# o salário, garantindo que o valor seja positivo.

# class Funcionario:

#     def _init_(self, salario):
#         self.__salario = salario if salario >= 0 else 0

#     def get_salario(self):
#         return self.__salario

#     def set_salario(self, salario):
#         if isinstance(salario, (int, float)) and salario >= 0:
#             self.__salario = salario
#         else:
#             print('Salário inválido')

# Testar a função

# func = Funcionario(1000)
# print("Salário:", func.get_salario())

# func.set_salario(-50)
# print("Salário:", func.get_salario())

# func.set_salario(50)
# print("Salário:", func.get_salario())

# 9) Crie uma classe "Casa" com atributos privados "endereço" e "valor". Crie métodos para acessar e modificar
# esses atributos.

# class Casa:

#     def _init_(self, endereco, valor):
#         self.__endereco = endereco
#         self.__valor = valor

#     def get_endereco(self):
#         return self.__endereco

#     def set_endereco(self, endereco):
#         self.__endereco = endereco

#     def get_valor(self):
#         return self.__valor

#     def set_valor(self, valor):
#         self.__valor = valor

# Testar a função

# casa = Casa("Via Ubaldo Veloso Pereira", 100000)
# print("Endereço:", casa.get_endereco())
# print("Valor:", casa.get_valor())

# casa.set_endereco("Rua do Imperador")
# casa.set_valor(250000)
# print("Endereço:", casa.get_endereco()) 
# print("Valor:", casa.get_valor())

# 10) Crie uma classe "Celular" com um atributo privado "marca" e métodos para definir e obter a marca.

# class Celular:

#     def _init_(self, marca):
#         self.__marca = marca

#     def get_marca(self):
#         return self.__marca

#     def set_marca(self, marca):
#         self.__marca = marca

# Testar a função

# celular = Celular("Samsung")
# print("Marca:", celular.get_marca())

# celular.set_marca("Xiaomi")
# print("Marca:", celular.get_marca())

# celular.set_marca("Apple")
# print("Marca:", celular.get_marca())

# 11) Crie uma classe "Animal" com um atributo privado "idade" e um método setter que garante que a idade seja
# um número inteiro positivo.

# class Animal:

#     def _init_(self, idade):
#         self.__idade = idade

#     def get_idade(self):
#         return self.__idade

#     def set_idade(self, idade):
#         if isinstance(idade, int) and idade >= 0:
#             self.__idade = idade
#         else:
#             print('Idade inválido')

# Testar a função   

# animal = Animal(5) 
# print("Idade:", animal.get_idade())

# animal.set_idade(-10)
# print("Idade:", animal.get_idade())

# animal.set_idade(10)
# print("Idade:", animal.get_idade())

# 12) Crie uma classe "Estudante" com atributos privados "nome" e "matrícula". Use getters e setters para
# modificar e acessar os atributos.

# class Estudante:

#     def _init_(self, nome, matricula):
#         self.__nome = nome
#         self.__matricula = matricula

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_matricula(self):
#         return self.__matricula

#     def set_matricula(self, matricula):
#         self.__matricula = matricula

# Testar a função

# estudante = Estudante("Bruno", 123456)
# print("Nome:", estudante.get_nome())
# print("Matricula:", estudante.get_matricula())  

# estudante.set_nome("Rafael")
#estudante.set_matricula(654321)
# print("Nome:", estudante.get_nome())
# print("Matricula:", estudante.get_matricula())

# 13) Crie uma classe "Veículo" com um atributo privado "velocidade_maxima" e um método getter retorne esse valor.

# class Veiculo:

#     def _init_(self, velocidade):
#         self.__velocidade = velocidade

#     def get_velocidade(self):
#         return self.__velocidade
    
#     def set_velocidade(self, velocidade):
#         self.__velocidade = velocidade

# Testar a função

# carro = Veiculo(200)  
# print("Velocidade máxima:", carro.get_velocidade())

# carro.set_velocidade(300)
# print("Velocidade máxima:", carro.get_velocidade())

# 14) Crie uma classe "Computador" com um atributo privado "memoria_ram" e um método setter que só permita
# valores maiores que zero.

# class Computador:

#     def _init_(self, memoria):
#         self.__memoria = memoria

#     def get_memoria(self):
#         return self.__memoria

#     def set_memoria(self, memoria):
#         if memoria > 0:
#             self.__memoria = memoria
#         else:
#             print("Memória inválida")

# Testar a função

# computador = Computador(8)
# print("Memória:", computador.get_memoria())

# computador.set_memoria(16)
# print("Memória:", computador.get_memoria())

# computador.set_memoria(0)
# print("Memória:", computador.get_memoria())

# computador.set_memoria(-4)
# print("Memória:", computador.get_memoria())

# 15) Crie uma classe "Curso" com atributos privados "nome" e "duração". Crie métodos para modificar e acessar
# esses atributos.

# class Curso:

#     def _init_(self, nome, duracao):
#         self.__nome = nome
#         self.__duracao = duracao

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_duracao(self):
#         return self.__duracao

#     def set_duracao(self, duracao):
#         self.__duracao = duracao

# Testar a função

# curso = Curso("Python", 10)
# print("Nome:", curso.get_nome())
# print("Duração:", curso.get_duracao())

# curso.set_nome("Física")  
# curso.set_duracao(20)
# print("Nome:", curso.get_nome())
# print("Duração:", curso.get_duracao())

# 16) Crie uma classe "Jogo" com um atributo privado "pontuação" e um método getter para acessar a pontuação.

# class Jogo:

#     def _init_(self, pontuacao):
#         self.__pontuacao = pontuacao

#     def get_pontuacao(self):
#         return self.__pontuacao

#     def set_pontuacao(self, pontuacao):
#         self.__pontuacao = pontuacao

# Testar a função

# jogo = Jogo(100)
# print("Pontuação:", jogo.get_pontuacao())

# jogo.set_pontuacao(200)
# print("Pontuação:", jogo.get_pontuacao())

# jogo.set_pontuacao(-50)
# print("Pontuação:", jogo.get_pontuacao())

# jogo.set_pontuacao(50)
# print("Pontuação:", jogo.get_pontuacao())

# 17) Crie uma classe "Empresa" com atributos privados "nome" e "numero_funcionarios". Crie métodos para acessar
# e modificar esses atributos.

# class Empresa:

#     def _init_(self, nome, numero_funcionarios):
#         self.__nome = nome
#         self.__numero_funcionarios = numero_funcionarios

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_numero_funcionarios(self):
#         return self.__numero_funcionarios

#     def set_numero_funcionarios(self, numero_funcionarios):
#         self.__numero_funcionarios = numero_funcionarios

# Testar a função

# empresa = Empresa("Empresa A", 100)
# print("Nome:", empresa.get_nome())
# print("Número de Funcionários:", empresa.get_numero_funcionarios())

# empresa.set_nome("Empresa B")
# print("Nome:", empresa.get_nome())
# print("Número de Funcionários:", empresa.get_numero_funcionarios())

# empresa.set_numero_funcionarios(200)
# print("Nome:", empresa.get_nome())
# print("Número de Funcionários:", empresa.get_numero_funcionarios()) 

# 18) Crie uma classe "Filme" com atributos privados "titulo" e "ano_lancamento". Use getters e setters para
# esses atributos.

# class Filme:

#     def _init_(self, titulo, ano_lancamento):
#         self.__titulo = titulo
#         self.__ano_lancamento = ano_lancamento

#     def get_titulo(self):
#         return self.__titulo

#     def set_titulo(self, titulo):
#         self.__titulo = titulo

#     def get_ano_lancamento(self):
#         return self.__ano_lancamento

#     def set_ano_lancamento(self, ano_lancamento):
#         self.__ano_lancamento = ano_lancamento

# Testar a função

# filme = Filme("Filme A", 2020)
# print("Título:", filme.get_titulo())
# print("Ano de Lancamento:", filme.get_ano_lancamento())

# filme.set_titulo("Filme B")
# print("Título:", filme.get_titulo())
# print("Ano de Lancamento:", filme.get_ano_lancamento())

# filme.set_ano_lancamento(2021)
# print("Título:", filme.get_titulo())
# print("Ano de Lancamento:", filme.get_ano_lancamento())

# 19) Crie uma classe "Cidade" com atributos privados "nome" e "população". Adicione métodos para acessar e modificar
# esses atributos.

# class Cidade:

#     def _init_(self, nome, populacao):
#         self.__nome = nome
#         self.__populacao = populacao

#     def get_nome(self):
#         return self.__nome

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_populacao(self):
#         return self.__populacao

#     def set_populacao(self, populacao):
#         self.__populacao = populacao

# Testar a função

# cidade = Cidade("Cidade A", 100000)
# print("Nome:", cidade.get_nome())
# print("População:", cidade.get_populacao())

# cidade.set_nome("Cidade B")
# print("Nome:", cidade.get_nome())
# print("População:", cidade.get_populacao())

# cidade.set_populacao(200000)
# print("Nome:", cidade.get_nome())
# print("População:", cidade.get_populacao())

# 20) Crie uma classe "Professor" com atributos privados "nome" e "disciplina". Crie métodos para modificar e
# acessar esses atributos.

class Professor:

    def _init_(self, nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

# Testar a função

professor = Professor("Professor A", "Matematica")
print("Nome:", professor.get_nome())
print("Disciplina:", professor.get_disciplina())

professor.set_nome("Professor Bruno")
print("Nome:", professor.get_nome())
print("Disciplina:", professor.get_disciplina())

professor.set_disciplina("Física")
print("Nome:", professor.get_nome())
print("Disciplina:", professor.get_disciplina())