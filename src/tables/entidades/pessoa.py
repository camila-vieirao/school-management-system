from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from tables.base import Base  # Importa a classe Base de outro arquivo

# Definir a tabela Pessoa (Entidade Principal)
class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    contato_telefone = Column(String(20))
    contato_email = Column(String(100))
    endereco = Column(String(255))
    tipo = Column(String(50))  # Define a coluna 'tipo' para armazenar o tipo de entidade

    __mapper_args__ = {
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': 'tipo'
    }

# Responsavel herda de Pessoa
class Responsavel(Pessoa):
    __tablename__ = 'responsavel'
    cpf = Column(String(11), primary_key=True)
    tipo_tutor = Column(String(50), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'responsavel',
    }

# Funcionario herda de Pessoa
class Funcionario(Pessoa):
    __tablename__ = 'funcionario'
    codigo_rh = Column(Integer, primary_key=True)
    data_nascimento = Column(Date, nullable=False)
    idade = Column(Integer)
    data_inicio = Column(Date)
    genero = Column(String(10))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'funcionario',
    }

# Docente herda de Funcionario
class Docente(Funcionario):
    __tablename__ = 'docente'
    docente_id = Column(Integer, primary_key=True, autoincrement=True)
    funcionario_codigo_rh = Column(Integer, ForeignKey('funcionario.codigo_rh'))

    __mapper_args__ = {
        'polymorphic_identity': 'docente',
    }

    disciplinas = relationship("Disciplina", back_populates="docente")
