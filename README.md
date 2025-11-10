# Vida & Cuidado – Sistema de Gestão de Médicos & Pacientes 🏥

## 📄 Descrição  
Este é um sistema web simples desenvolvido em Flask que permite visualizar listas de pacientes e de médicos, além de consultar detalhes individuais de cada um. O objetivo é oferecer uma interface clara, funcional e agradável para a gestão básica de dados de saúde.


## Utilizar o código ja feito em aula:

```bash
  from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

alunos = [
    {
        "id": 1,
        "nome":"Gabriel Moia",
        "idade": 16,
        "curso": "Python Intermediário",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e3/DavidGogginsMay08.jpg" 
    },
    {
        "id": 2,
        "nome":"Justin Bieber",
        "idade": 23,
        "curso": "Python Intermediário",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Justin_Bieber_20161111_009-2_%28cropped%29.jpg" 
    }
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/alunos")
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route("/aluno/<int:aluno_id>")
def detalhe_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return render_template('detalhe_aluno.html', aluno=aluno)
    return "Aluno nao encontrado", 404


if __name__ == '__main__':
    app.run(debug=True)

```
## ⭐ Funcionalidades principais  
- Página inicial (rota `/`) com boas-vindas e explicação do sistema.  
- Lista de **pacientes** (rota `/pacientes`) com nome, idade, condição médica, imagem em miniatura.  
- Lista de **médicos** (rota `/medicos`) com nome, especialidade, anos de experiência, imagem em miniatura.  
- Detalhe de um paciente (rota `/paciente/<int:paciente_id>`) com informações completas e imagem em tamanho maior.  
- Detalhe de um médico (rota `/medico/<int:medico_id>`) com informações completas, imagem maior e (opcional) lista de pacientes atribuídos.  
- Tratamento de erro 404 para IDs que não existem (paciente ou médico).  
- Uso de templates Jinja2 para renderização das páginas HTML, com layout comum (`base.html`) para cabeçalho e rodapé.  
- Dados de exemplo usando listas de dicionários em Python — podendo ser estendido para banco de dados mais completo.

## 🛠 Tecnologias utilizadas  
- Python 3.x  
- Flask  
- Jinja2 (templating)  
- HTML / CSS (e, opcionalmente, Bootstrap para estilização)  

## 📁 Estrutura sugerida de pastas  
/projeto‑vida‑e‑cuidado  
│  
├─ app.py  
├─ requirements.txt  
├─ templates/   
│   ├─ index.html  
│   ├─ listar_pacientes.html  
│   ├─ detalhe_paciente.html  
│   ├─ listar_medicos.html  
│   └─ detalhe_medico.html  
├─ static/  
│   ├─ css/  
│   └─ images/  

## Crítico
- Realização do arquivo app.py

## Desejável
- Realização das paginas (templates) html


## ⚙️ Instalação e execução  
1. Faça **fork** deste repositório para sua conta GitHub.  
2. Clone sua cópia (o fork) localmente:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
