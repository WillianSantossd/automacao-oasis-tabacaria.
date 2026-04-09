import sqlite3

def criar_banco():
    # Conecta ao arquivo (se não existir, ele cria na hora)
    conn = sqlite3.connect('estoque_oasis.db')
    cursor = conn.cursor()
    
    # Cria a tabela com as mesmas colunas que usamos na planilha
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            marca TEXT,
            valor TEXT,
            disponibilidade TEXT,
            link TEXT,
            data_coleta TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_no_banco(dados):
    conn = sqlite3.connect('estoque_oasis.db')
    cursor = conn.cursor()
    
    # Inserindo os dados capturados
    for item in dados:
        cursor.execute('''
            INSERT INTO produtos (nome, marca, valor, disponibilidade, link, data_coleta)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (item['PRODUTO'], item['MARCA'], item['VALOR'], item['DISPONIBILIDADE'], item['LINK'], item['DATA']))
    
    conn.commit()
    conn.close()
    print("[SQL] Dados salvos com sucesso no banco de dados!")