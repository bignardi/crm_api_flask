from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<nome>/<profissao>/<int:idade>", methods=['GET'])
def teste(nome, profissao, idade):
    # --
    nome = nome
    prof = profissao
    idade = format(idade + 1)
    # --
    return jsonify({'nome':nome,
                    'profissao':prof,
                    'idade':idade})

if __name__ =="__main__":
    app.run(debug=True) # Efetua o restart automático