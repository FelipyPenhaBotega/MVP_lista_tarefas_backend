from pydantic import BaseModel
from typing import Optional, List
from model.tarefa import Tarefa
from datetime import date, datetime

class TarefaSchema(BaseModel):

    """ Define como uma nova tarefa a ser inserida deve ser representada.
    """
    nome: str = "Médico"
    descricao: str ='Ir ao médico para consulta'
    data_atividade: str = "10/11/2023 13:00"



class TarefaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base na data da tarefa.
    """
    data_atividade: str = "10/11/2023 13:00"


class ListagemTarefasSchema(BaseModel):
    """ Define como uma listagem de tarefas será retornada.
    """
    Tarefas:List[TarefaSchema]


def apresenta_tarefas(tarefas: List[Tarefa]):
    """ Retorna uma representação da tarefa seguindo o schema definido em
        TarefaViewSchema.
    """
    result = []
    for tarefa in tarefas:
        result.append({
            "nome": tarefa.nome,
            "descricao": tarefa.descricao,
            "data_atividade": tarefa.data_atividade,
        })

    return {"tarefas": result}


class TarefaViewSchema(BaseModel):
    """ Define como uma tarefa será retornada
    """
    nome: str = "Médico"
    descricao: str ='Ir ao médico para consulta'
    data_atividade: str = "10/11/2023 13:00"


class TarefaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    nome: str 
    descricao: str 
    data_atividade: str

def apresenta_tarefa(tarefa: Tarefa):
    """ Retorna uma representação da tarefa seguindo o schema definido em
        TarefaViewSchema.
    """
    return {
        "id": tarefa.id,
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "data_atividade": tarefa.data_atividade
    }
