from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calcular-produto', methods=['POST'])
def calcular_produto_endpoint():
    quantidade = request.json.get('quantidade')
    if quantidade is None:
        return jsonify({'error': 'Quantidade não fornecida'}), 400

    try:
        quantidade = float(quantidade)
    except ValueError:
        return jsonify({'error': 'Quantidade inválida'}), 400

    produto = quantidade * 1.68
    return jsonify({'resultado': produto})


if __name__ == '__main__':
    app.run()


