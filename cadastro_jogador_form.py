import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
from PyQt5 import uic 
from conexao_mysql import ConexaoMySQL


class CadastroDialog(QDialog):
    def __init__(self):
        self.nome_clube=''
        self.cidade=''
        super().__init__()
        # Carrega o arquivo design
        uic.loadUi("cadastro.ui", self)
        # Ação dos botões
        self.btnCadastrar.clicked.connect(lambda:self.salvar())

    # Tipos: QMessageBox.Warning,QMessageBox.Information e QMessageBox.Critical
    def exibir_status(self, titulo, mensagem, icone):
        """
        Exibe uma mensagem para o usuário
        informando o status da operação.
        """
        dialog = QMessageBox(self)
        dialog.setWindowTitle(titulo)
        dialog.setText(mensagem)
        dialog.setIcon(icone)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.exec_()
        

    def salvar(self):
        #1- Pegar os dados do formulário
        self.nome_clube=''
        self.cidade=''
        self.nome_clube=self.txtNomeClube.text().strip()
        self.cidade=self.txtCidade.text().strip()
        #2 - Realizar a validação
        #Usuário não digitou os valores no formulário
        if (self.nome_clube=='' or self.cidade==''):
            self.exibir_status('Erro','Há dados incompletos', QMessageBox.Warning)
        else: 
            try:
                con=ConexaoMySQL(host="localhost",database="campeonato",user="root",password="")
                con.conectar()
                con.inserir("INSERT INTO time (nome, cidade) VALUES (%s, %s)", (self.nome_clube, self.cidade)) 
                self.exibir_status('Cadastrado', 'Time cadastrado com sucesso!', QMessageBox.Information)
            except Exception as erro:
            # Se falhar, este bloco vai te dizer exatamente o motivo na tela!
                self.exibir_status('Erro critico', erro, QMessageBox.Critical)

            finally:
            # 5. Garante que vai fechar a conexão acontecendo erro ou não
                con.desconectar()       
            # Configurações de acesso

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    janela = CadastroDialog()
    janela.show()
    sys.exit(app.exec_())