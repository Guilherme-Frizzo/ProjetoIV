
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Tabela utilizada nos exemplos:
# 
# CREATE TABLE jogador (
#   id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
#   nome varchar(50) NOT NULL,
#   clube varchar(50) NOT NULL,
#	valor float(53) NOT NULL
# );

engine = create_engine('mysql+mysqlconnector://root:root@localhost/projetoiv')

def listarJogadores():
	sessao = Session(engine)

	try:
		jogadores = sessao.execute(text("SELECT id, nome, clube, valor FROM jogador ORDER BY nome"))

		for (id, nome, clube, valor) in jogadores:
			print(f'\nid: {id} / nome: {nome} / clube: {clube} / valor: {valor}')

	finally:
		sessao.close()

def obterJogador(id):
	sessao = Session(engine)

	try:
		parametros = {
			'id': id
		}

		jogador = sessao.execute(text("SELECT id, nome, clube, valor FROM jogador WHERE id = :id"), parametros).first()

		if jogador == None:
			print('Jogador não encontrado!')
		else:
			print(f'\nid: {jogador.id} / nome: {jogador.nome} / clube: {jogador.clube} / valor: {jogador.valor}')

	finally:
		sessao.close()

def criarJogador(nome, clube, valor):
	sessao = Session(engine)

	try:
		jogador = {
			'nome': nome,
			'clube': clube,
			'valor': valor
		}

		sessao.execute(text("INSERT INTO jogador (nome, clube, valor) VALUES (:nome, :clube, :valor)"), jogador)
		sessao.commit()
	finally:
		sessao.close()
		
if __name__ == '__main__':
	listarJogadores()
