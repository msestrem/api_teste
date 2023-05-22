from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/calcular-produto/<float:quantidade>', methods=['GET'])
def calcular_produto_endpoint(quantidade):
    produto = quantidade * 1.68
    return jsonify({'resultado': produto})

if __name__ == '__main__':
    app.run()

