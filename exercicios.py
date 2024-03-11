"""
Desenvolva uma versão inicial de CLI (command-line interface) para analisar se um aluno foi ou não aprovado em uma disciplina. A aplicação deve atender aos seguintes requisitos:

A CLI deve perguntar ao usuário o seu nome. Caso a resposta do usuário seja um texto vazio, o programa deve ser encerrado;
Em seguida, o programa deve calcular a média do usuário. Para isso, o programa deve ler as notas de AP1, AP2, AS e AC. Em seguida, deve exibir na tela a média final do aluno. Considere que a média é calculada como (AP1 + AP2) * 0.4 + AC * 0.2, sendo que a AS pode substituir a AP1 ou a AP2 (a menor dentre as duas);
Por fim, a aplicação deve exibir na tela se o aluno foi aprovado ou reprovado, baseado na sua média. A média para aprovação é 7.0.
Organize o seu código em funções com responsabilidades distintas (uma para o cálculo de nota, uma para exibição de informações, uma para leitura de dados, etc.). Caso as notas passadas sejam inválidas (menores que 0 ou maiores que 10), o programa não deve calcular nada e deve ser encerrado.
"""

def pergunta_nome():
    nome = input("Informe seu nome: ")
    return nome

def le_notas():
    ap1 = float(input("Informe a nota da sua AP1: "))
    ap2 = float(input("Informe a nota da sua AP2: "))
    ac = float(input("Informe a nota da sua AC: "))
    asub = float(input("Informe a nota da sua AS: "))
    return ap1, ap2, ac, asub

def valida_notas(ap1, ap2, ac, asub):
    if ap1 > 10:
        return False
    if ap1 < 0:
        return False
    if ap2 > 10:
        return False
    if ap2 < 0:
        return False
    if ac > 10:
        return False
    if ac < 0:
        return False
    if asub > 10:
        return False
    if asub < 0:
        return False

    return True

def sub_notas(ap1, ap2, asub):
    if asub > ap2:
        return ap1, asub
    if asub > ap1:
        return ap2, asub
    return ap1, ap2

def calcula_media(nota1, nota2, ac):
    media = ((nota1 + nota2) * 0.4) + (ac * 0.2)
    return media

def aprovacao(media, nome):
    if media >= 7:
        return print(nome, "sua média foi", media, ", você foi aprovado!")
    if media < 7:
        return print(nome, "sua média foi", media , ", você foi reprovado!")

def main():
    nome = pergunta_nome()
    if nome:
        ap1, ap2, ac, asub = le_notas()
        if valida_notas(ap1, ap2, ac, asub):
            nota1, nota2 = sub_notas(ap1, ap2, asub)
            media = round(calcula_media(nota1, nota2, ac), 2)
            aprovacao(media, nome)


main()
