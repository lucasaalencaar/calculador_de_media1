

nome = input('Nome do aluno: ')
print('Digite suas notas', nome)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media_aritmedica = (nota1 + nota2 + nota3) / 3
media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5 ) / 10
print(f'Notas: {nota1}, {nota2}, {nota3} ')
print(f'Média aritmética: {media_aritmedica}')
print(f'Média ponderada: {media_ponderada}')


