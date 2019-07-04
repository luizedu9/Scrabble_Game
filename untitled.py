import pickle

dicionario = set()
dicionario_ordenado = {}

with open('dicionario.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    dicionario.add(line.upper());
    dicionario_ordenado[''.join(sorted(line.upper()))] = line.upper()

output = open('dicionario.pkl', 'wb')
pickle.dump(dicionario, output)
output.close()

output = open('dicionario_ordenado.pkl', 'wb')
pickle.dump(dicionario_ordenado, output)
output.close()

