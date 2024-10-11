from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.entidades.pessoa import *
from tables.entidades.disciplina import Disciplina 
from tables.base import Base
from datetime import datetime

# Configuração do banco de dados
engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

# Criando sessão
Session = sessionmaker(bind=engine)
session = Session()

'''
# Exemplo de inserção de dados
responsavel_1 = Responsavel(nome="Carlos Silva", cpf="12345678901", tipo_tutor="Pai", contato_telefone="99999-9999", contato_email="carlos@example.com", endereco="Rua A, 123")
funcionario_1 = Funcionario(nome="Ana Costa", codigo_rh=1, data_nascimento=datetime.strptime("1985-06-15", "%Y-%m-%d").date(), idade=39, data_inicio=datetime.strptime("2020-03-10", "%Y-%m-%d").date(), genero="Feminino", contato_telefone="88888-8888", contato_email="ana@example.com", endereco="Rua B, 456")
docente_1 = Docente(nome="José Lima", codigo_rh=2, data_nascimento=datetime.strptime("1978-12-25", "%Y-%m-%d").date(), idade=45, data_inicio=datetime.strptime("2015-02-05", "%Y-%m-%d").date(), genero="Masculino", contato_telefone="77777-7777", contato_email="jose@example.com", endereco="Rua C, 789")
disciplina_1 = Disciplina(nome="Matemática", descricao="Disciplina de Matemática Básica", carga_horaria=40, docente=docente_1)
funcionario_2 = Funcionario(nome="Ana Brito", codigo_rh=3, data_nascimento=datetime.strptime("1985-06-16", "%Y-%m-%d").date(), idade=39, data_inicio=datetime.strptime("2020-03-10", "%Y-%m-%d").date(), genero="Feminino", contato_telefone="88888-9999", contato_email="anab@example.com", endereco="Rua B, 321")

# Adicionando registros
session.add(responsavel_1)
session.add(funcionario_1)
session.add(docente_1)
session.add(disciplina_1)
session.add(funcionario_2)
session.commit()
'''

# LENDO O BANCO 

pessoas = session.query(Pessoa).all()
print("\nPESSOAS:")
for pessoa in pessoas:
    print(f'Pessoa ID: {pessoa.id}, Nome: {pessoa.nome}, Telefone: {pessoa.contato_telefone}, Email: {pessoa.contato_email}, Endereço: {pessoa.endereco}')

funcionarios = session.query(Funcionario).all()
print("\nFUNCIONARIOS:")
for funcionario in funcionarios:
    print(f'Funcionario ID: {funcionario.id}, Nome: {funcionario.nome}, RH Código: {funcionario.codigo_rh}, Data de Nascimento: {funcionario.data_nascimento}, Gênero: {funcionario.genero}')

disciplinas = session.query(Disciplina).all()
print("\nDISCIPLINAS:")
for disciplina in disciplinas:
    print(f'Disciplina ID: {disciplina.id}, Nome: {disciplina.nome}, Descrição: {disciplina.descricao}, Carga Horária: {disciplina.carga_horaria}')

responsaveis = session.query(Responsavel).all()
print("\nRESPONSAVEIS:")
for responsavel in responsaveis:
    print(f'Responsável ID: {responsavel.id}, Nome: {responsavel.nome}, CPF: {responsavel.cpf}, Tipo de Tutor: {responsavel.tipo}, Contato: {responsavel.contato_telefone}')

docentes = session.query(Docente).all()
print("\nDOCENTES:")
for docente in docentes:
    print(f'Docente ID: {docente.id}, Nome: {docente.nome}, RH Código: {docente.codigo_rh}, Data de Nascimento: {docente.data_nascimento}, Gênero: {docente.genero}')


# Fechar a sessão
session.close()
