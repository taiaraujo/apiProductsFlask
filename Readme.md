# Api de Cadastro de Produtos em Flask

## Para acessar o repositorio do projeto

[https://github.com/taiaraujo/apiProductsFlask/tree/master](https://github.com/taiaraujo/apiProductsFlask/tree/master)

## Principais pacotes utilizados
- [https://flask.palletsprojects.com/en/2.2.x/](https://flask.palletsprojects.com/en/2.2.x/)
- [https://marshmallow.readthedocs.io/en/stable/](https://marshmallow.readthedocs.io/en/stable/)
- [https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/](https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/)
- [https://flask.palletsprojects.com/en/2.2.x/tutorial/views/](https://flask.palletsprojects.com/en/2.2.x/tutorial/views/)
- [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)
- [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)

### Para instalação dos pacotes
> pip install -r requirements.txt

### Tratativa das exceções

- A exceções foram desenvolvidas em cada função dentro do controllers.product, utilizando o ```ValidationError``` do Marshmallow e o ```try ... except ``` : [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html).

- Para a requisição 
> [PUT] http://127.0.0.1:5000/api/product/5
> 
> [body] {"sku": "5173826661"}

- Têm-se a resposta:
> [400 - BAD REQUEST]
> 
> {
	"message": {
		"price": [
			"Missing data for required field."
		],
		"name": [
			"Missing data for required field."
		]
	}
}