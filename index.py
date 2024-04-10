import pandas as pd

def imprimir(m):
    for i, linha in enumerate(m):
        for j, coluna in enumerate(linha):
            print(m[i, j])
            # print(m[linha, coluna])

def Simplex(eqs, restricoes, func_obj, variaveis):
    ei = 0
    ai = 0
    rest = 0
    excessos = list()
    artificiais = list()
    print(variaveis)
    for i, linha in enumerate(eqs):
        if restricoes[i] == ">=":
            ei += 1
            ai += 1
            print(f"Como a restrição {i} é do tipo '≥' é necessária a variável de excesso E{ei} e a variável artificial A{ai}.")
            excessos.append(f'E{ei}')
            artificiais.append(f'A{ai}')
        if restricoes[i] == "<=":
            ei += 1
            print(f"Como a restrição {i} é do tipo '≤' é necessária a variável de folga E{ei}.")
            excessos.append(f'E{ei}')
    for i in excessos:
        variaveis.append(i)
    for i in artificiais:
        variaveis.append(i)
    print(variaveis)
    

def main():
    df = pd.read_csv("restricoes.csv")
    m = df.values
    restricoes = ['>=', '>=', '>=', '>=', '>=', '>=', '>=', '>=', '>=', '<=']
    func_obj = [9.6, 3.2, 1.92, 1.6, 1.6, 5.12]
    Simplex(m, restricoes, func_obj, ['X1', 'X2', 'X3', 'X4'])



if __name__ == '__main__':
    main()