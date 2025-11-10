from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

pacientes = [
    {
        "id": 1,
        "nome": "Eliza Sanches",
        "idade": 38,
        "condicao": "Kaka lectopirose",
        "telefone": "98 7777-7777",
        "image": "https://observatoriog.com.br/wp-content/uploads/2022/09/WhatsApp-Image-2022-09-17-at-00.10.56.jpeg"
    }
]

medicos = [
    {
        "id": 1,
        "nome": "Dr.Nefario",
        "especialidade": "Ginecologista",
        "anos_experiencia": 69,
        "email": "nefariopirocudo069@gmail.com",
        "image": "https://static.wikia.nocookie.net/despicableme/images/5/56/Dr-Nefario-despicable-me-13776694-616-315.jpg/revision/latest?cb=20160529094501"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pacientes")
def listar_pacientes():
    return render_template("listar_pacientes.html", pacientes=pacientes)

@app.route("/paciente/<int:paciente_id>")
def detalhe_paciente(paciente_id):
    # encontrar paciente
    paciente = next((p for p in pacientes if p["id"] == paciente_id), None)
    if paciente is None:
        abort(404)
    return render_template("detalhe_paciente.html", paciente=paciente)

@app.route("/medicos")
def listar_medicos():
    return render_template("listar_medicos.html", medicos=medicos)

@app.route("/medico/<int:medico_id>")
def detalhe_medico(medico_id):
    medico = next((m for m in medicos if m["id"] == medico_id), None)
    if medico is None:
        abort(404)
    # opcional: montar lista de pacientes atribuídos
    pacientes_atribuidos = [p for p in pacientes if p["id"] in medico.get("pacientes_ids", [])]
    return render_template("detalhe_medico.html", medico=medico, pacientes=pacientes_atribuidos)

# Tratamento de erro 404 customizado (opcional)
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
 