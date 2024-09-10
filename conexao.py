import psycopg2


def conecta_db():
    con = psycopg2.connect(host="localhost",
                            database="projeto_agenda",
                            user="postgres",
                            password="postgres",
                            port=5432)
    return con