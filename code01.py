# media minima para aprovacao e maxima para reprovacao
# informe numero de matricula
# nome completo 
# primeira, segunda e terceira nota
# para finalizar digite 'fim' no linha para informa o numero de matricula

# deseja saber os alunos acima da media de aprovacao - 's' ou 'n'


minima, maxima = input().split()
medias = (float(minima), float(maxima))

alunos = []

while True:
    matricula = input()
    if matricula == 'fim':
        break

    nome = input()
    nota = input().split()
    nota = [int(x) for x in nota]
    alunos.append([nome,matricula,nota])

def mediaAprov(xs,m):
    media = sum(xs)/len(xs)
    if media >= m[0]:
        resultado = 'APROVADO(A)'
    elif media < m[1]:
        resultado = 'REPROVADO(A)'
    else:
        resultado = 'RECUPERACAO'
    return '%.1f' % media, resultado

def acimaMedia(xs,m):
    acima = []
    for x in xs:
        if x[4][0] > m[0]:
            acima.append((xs[0],xs[4][0]))
    return acima

def formate(xs):
    if len(xs) == 2:
        texto = xs[0] + ' - ' + str(xs[1][0]) 
    elif len(xs) == 3:
        xs = [str(x) for x in xs]
        texto = xs[0] + ' | ' + xs[1] + ' | ' + xs[2]
    else:
        texto = xs[0] + ' . ' + xs[1] + ' - ' + formate(xs[2]) + ' - ' + xs[3][1] 
    return texto

mostraAcima = input()

for aluno in alunos:
    aluno.append(mediaAprov(aluno[2],medias))
    print(formate(aluno))

if mostraAcima == 's':
    print('- - - - - - - - - - - - - - ')
    for aluno in alunos:
        print(formate([aluno[0] , aluno[3]]))