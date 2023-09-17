from sqlalchemy import Column, String, Integer
from  model import Base


class Tarefa(Base):
    __tablename__ = 'tarefa'

    id = Column("pk_tarefa", Integer, primary_key=True)
    nome = Column(String(140))
    descricao = Column(String(140))
    data_atividade = Column(String(16), unique=True)

    def __init__(self
                 , nome:str
                 , descricao:str
                 , data_atividade:str):
        """
        Cria uma tarefa

        Arguments:
            nome: Nome da tarefa.
            descricao: Descrição da tarefa.
            data_atividade: Data projetada para execução da tarefa.
        """
        self.nome = nome
        self.descricao = descricao
        self.data_atividade = data_atividade
        



