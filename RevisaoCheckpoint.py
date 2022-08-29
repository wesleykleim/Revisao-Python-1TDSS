def grava_arquivo(lista):
    arquivo = open("cadastro.txt", mode='w')
    for registro in lista:
        arquivo.write('{nome=' + registro[0] + ', email=' + registro[1] + ', celular= ' + registro[2] + '}')



cadastro = []


for i in range(2):
    pessoa =[]
    nome = input("Informe o nome: ")
    email = input("Email: ")
    celular =input("Celular: ")
    curso = input("Curso: ")
    ano = int(input("Ano do curso: "))
    idade = int(input("Idade: "))
    ano_conclusao = int(input("Ano de conclusão: "))


    pessoa.append(nome)
    pessoa.append(email)
    pessoa.append(celular)
    pessoa.append(curso)
    pessoa.append(ano)
    pessoa.append(ano_conclusao)
    pessoa.append(idade)

    cadastro.append(pessoa)
grava_arquivo(cadastro)
print("Arquivo gravado com sucesso! ")
for pes in cadastro:
    print(pes)