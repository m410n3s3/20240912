import _sqlite3 as sq

def criarBD():
    conexao = sq.connect("Funcionario.db")
    cursor = conexao.cursor()
    return conexao, cursor

def criar_tabela():
    tabela = """
    create table if not exists Funcionarios (
        id integer primary key,
        nome text not null,
        cargo text not null,
        dataContratacao text not null);
        """
    return tabela

def inserir_dados(conexao, cursor,i):
    nome = input("Digite um nome: ")
    cargo = input("Digite um cargo: ")
    data = input("Digite uma data no formato aaaa-mm-dd: ")
    cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",(i, nome, cargo, data))
    conexao.commit()


if __name__=="__main__":
    conexao, cursor = criarBD()
    tabela = criar_tabela()
    cursor.execute(tabela)
    conexao.commit()
    for i in range(2):
        inserir_dados(conexao,cursor,i)
