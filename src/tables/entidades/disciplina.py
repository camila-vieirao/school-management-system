from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tables.base import Base  # Importa a classe Base de outro arquivo

# Tabela Disciplina
class Disciplina(Base):
    __tablename__ = 'disciplina'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    carga_horaria = Column(Integer)
    docente_id = Column(Integer, ForeignKey('docente.docente_id'))

    docente = relationship("Docente", back_populates="disciplinas")
