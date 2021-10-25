import app = require("teem");

class IndexRoute {
	public async index(req: app.Request, res: app.Response) {
		let nomeDoUsuarioQueVeioDoBanco = "Rafael";

		let opcoes = {
			usuario: nomeDoUsuarioQueVeioDoBanco,
			quantidadeDeRepeticoes: 5
		};

		res.render("index/index", opcoes);
	}

	public async teste(req: app.Request, res: app.Response) {
		res.render("index/teste");
	}

	public async produtos(req: app.Request, res: app.Response) {
		let produtoA = {
			id: 1,
			nome: "Produto A",
			valor: 25
		};

		let produtoB = {
			id: 2,
			nome: "Produto B",
			valor: 15
		};

		let produtoC = {
			id: 3,
			nome: "Produto C",
			valor: 100
		};

		let produtosVindosDoBanco = [ produtoA, produtoB, produtoC ];

		let opcoes = {
			titulo: "Listagem de Produtos",
			produtos: produtosVindosDoBanco
		};

		res.render("index/produtos", opcoes);
	}
}

export = IndexRoute;
