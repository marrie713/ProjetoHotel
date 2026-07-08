from flask import Flask, render_template, request, redirect, flash
from classes.hotel import Hotel

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.secret_key = "hotel123"

hotel = Hotel()

@app.route("/")
def index():

    print("Hóspedes:", len(hotel.hospedes))
    print("Funcionários:", len(hotel.funcionarios))
    print("Quartos:", len(hotel.quartos))
    print("Reservas:", len(hotel.reservas))

    return render_template(
        "index.html",
        total_hospedes=len(hotel.hospedes),
        total_funcionarios=len(hotel.funcionarios),
        quartos_disponiveis=len([q for q in hotel.quartos if not q.ocupado]),
        quartos_ocupados=len([q for q in hotel.quartos if q.ocupado]),
        total_reservas=len(hotel.reservas)
    )


@app.route("/cadastrar_hospede", methods=["POST"])
def cadastrar_hospede():

    nome = request.form["nome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]

    if hotel.cadastrar_hospede(nome, cpf, telefone):
        flash("Hóspede cadastrado com sucesso!", "success")
    else:
        flash("Já existe um hóspede com esse CPF.", "danger")

    return redirect("/")

@app.route("/cadastrar_funcionario", methods=["POST"])
def cadastrar_funcionario():

    nome = request.form["nome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    cargo = request.form["cargo"]

    if hotel.cadastrar_funcionario(nome, cpf, telefone, cargo):
        flash("Funcionário cadastrado com sucesso!", "success")
    else:
        flash("Já existe um funcionário com esse CPF.", "danger")

    return redirect("/")

@app.route("/realizar_reserva", methods=["POST"])
def realizar_reserva():

    cpf = request.form["cpf"]
    numero_quarto = int(request.form["quarto"])
    dias = int(request.form["dias"])

    if hotel.realizar_reserva(cpf, numero_quarto, dias):
        flash("Reserva cadastrada com sucesso!", "success")
    else:
        flash("Este quarto já está ocupado ou os dados são inválidos.", "danger")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)