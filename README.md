# BackEnd MVP

Este é o projeto referente a parte do backEnd do MVP da sprint **Desenvolvimento Full Stack Básico**.

O projeto consiste em uma lista de tarefas, em conjunto com o frontEnd, através do browser é possível executar operações de inserção, exclusão e listagem das atividades a serem realizadas no futuro.

A aplicação também pode ser executa de forma independente, e realizar as mesmas operações, para isso basta executar os endPoint fornecidos na documentação Swagger.

---

## Como executar

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

O ambiente virtual pode ser instalado e utilizado através dos comandos abaixo, os comandos apresentados são compatíveis com o sistema operacional Windows.

```
python -m venv venv
```

para ativar o ambiente virtual:

```
.\venv\scripts\activate
```

Posteriormente, será necessário instalar todas as dependências listadas em `requirements.txt`, através do seguinte comando:

```
(env)$ pip install -r requirements.txt
```

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status e ter acesso a documentar da API.
