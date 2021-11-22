
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
	
	with Session(engine) as sessao:
		jogadores = sessao.execute(text("SELECT id, nome, clube, valor FROM jogador ORDER BY nome"))

		for (id, nome, clube, valor) in jogadores:
			print(f'\nid: {id} / nome: {nome} / clube: {clube} / valor: {valor}')

def obterJogador(id):
	with Session(engine) as sessao:
		parametros = {
			'id': id
		}

		jogador = sessao.execute(text("SELECT id, nome, clube, valor FROM jogador WHERE id = :id"), parametros).first()

		if jogador == None:
			print('Jogador não encontrado!')
		else:
			print(f'\nid: {jogador.id} / nome: {jogador.nome} / clube: {jogador.clube} / valor: {jogador.valor}')

def criarJogador(nome, clube, valor):
	
	with Session(engine) as sessao:
		with sessao.begin():
			jogador = {
				'nome': nome,
				'clube': clube,
				'valor': valor
			}

			sessao.execute(text("INSERT INTO jogador (nome, clube, valor) VALUES (:nome, :clube, :valor)"), jogador)
		
if __name__ == '__main__':
	criarJogador('Teste', 'Teste C', 123.5)


