import pymysql

class ConexaoMySQL:
    def __init__(self, host="localhost", database="seu_banco", user="root", password=""):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                autocommit=True
            )
            self.cursor = self.conexao.cursor()
            print("-> Conectado ao MySQL com PyMySQL (Sem conflitos)!")
        except Exception as e:
            print(f"-> ERRO AO CONECTAR: {e}")
            raise e

    def inserir(self, query, valores):
        # CORREÇÃO AQUI: Verificamos apenas se self.conexao existe
        if not self.conexao:
            print("❌ ERRO CRÍTICO: Você tentou inserir dados, mas ESQUECEU de chamar o método .conectar() primeiro!")
            return False

        try:
            self.cursor.execute(query, valores)
            print(f"🎉 Sucesso! Registro inserido. ID: {self.cursor.lastrowid}")
            return True
        except Exception as e:
            print(f"❌ ERRO NA QUERY DE INSERÇÃO: {e}")
            raise e

    def desconectar(self):
        # Já corrigido por você!
        if self.conexao:
            try:
                self.cursor.close()
                self.conexao.close()
                print("-> Conexão ao MySQL foi encerrada com sucesso.")
            except Exception as e:
                print(f"Erro ao fechar conexão: {e}")
            finally:
                self.conexao = None
                self.cursor = None
