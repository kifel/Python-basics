n = input('Digite algo: ')

print('O tipo primitivo desse valor é ', format(type(n)))
print('Só tem espaços ? {}'.format(n.isspace()))
print('É um numero ? {}'.format(n.isnumeric()))
print('É alfabetico ? {}'.format(n.isalpha()))
print('É alfanumerico ? {}'.format(n.isalnum()))
print('Está em maiusculo? {}'.format(n.isupper()))
print('Está em minusculo? {}'.format(n.islower()))
print('Está captalizada? {}'.format(n.istitle()))