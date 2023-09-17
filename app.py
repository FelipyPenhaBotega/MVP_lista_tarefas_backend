from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Tarefa
from schemas import *
from flask_cors import CORS
from service.utils import Utils

info = Info(title="Gerenciamento de Tarefas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação Swagger")
tarefa_tag = Tag(name="Tarefa", description="Adição, visualização e remoção de tarefas")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a api com estilo Swagger.
    """
    return redirect('/openapi/swagger')


@app.get('/tarefas', tags=[tarefa_tag], responses={"200": ListagemTarefasSchema, "404": ErrorSchema})
def get_tarefas():
    """Busca todas as tarefas cadastradas

    Retorna uma representação da listagem de tarefas.
    """
    session = Session()
    tarefas = session.query(Tarefa).all()

    return apresenta_tarefas(tarefas), 200



@app.post('/tarefa', tags=[tarefa_tag], responses={"200": TarefaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_tarefa(form: TarefaSchema):
    """Adiciona uma nova tarefa à base de dados

    Retorna uma representação da tarefa.
    """
    tarefa = Tarefa(
        nome=form.nome,
        descricao=form.descricao,
        data_atividade=form.data_atividade
        )
    
    if (not Utils.validar_formato_data_hora(tarefa.data_atividade)):
        error_msg = "A data não está no formato correto."
        return {"message": error_msg}, 400       
    
    if (not Utils.validar_data_maior_que_atual(tarefa.data_atividade)):
        error_msg = "A data deve ser maior que a data atual."
        return {"message": error_msg}, 400    

    try:
        session = Session()
        print(session.add(tarefa))
        session.commit()
        print(session.commit())
        return apresenta_tarefa(tarefa), 200

    except IntegrityError as e:
        error_msg = "Já existe uma tarefa cadastrada para a data indicada!"
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível cadastrar uma nova tarefa!"
        return {"message": error_msg}, 400



@app.delete('/tarefa', tags=[tarefa_tag], responses={"200": TarefaDelSchema, "404": ErrorSchema})
def del_tarefa(query: TarefaBuscaSchema):
    """Deleta uma tarefa a partir da data informada

    Retorna uma mensagem de confirmação da remoção.
    """

    tarefa_data_atividade = query.data_atividade
    session = Session()
    count = session.query(Tarefa).filter(Tarefa.data_atividade == tarefa_data_atividade).delete()
    session.commit()

    if count:
        error_msg = "Tarefa removida!"
        return {"message": error_msg}, 200
    else:
        error_msg = "Tarefa não encontrado na base de dados"
        return {"message": error_msg}, 404


