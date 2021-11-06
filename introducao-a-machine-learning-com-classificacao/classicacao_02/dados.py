import csv


def load_access():
    """
    Load access.csv file and return a list of tuples
    """
    X = []
    y = []
    with open('introducao-a-machine-learning-com-classificacao/classicacao_02/acesso.csv', 'r') as f:
        reader = csv.reader(f)
        access = list(reader)
        for home, funciona, contato, comprou in access:
            try:
                X.append([int(home), int(funciona), int(contato)])
                y.append(int(comprou))
            except Exception as e:
                pass
    return X, y
