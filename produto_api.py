from flask import Flask, request, jsonify

app = Flask(__name__)

preco_unit = [{'cpfCnpj': '40238802000159', 'preco': float(0.58)},
                   {'cpfCnpj': '10423979000164', 'preco': float(0.62)},
                   {'cpfCnpj': '37789234000170', 'preco': float(0.88)},
                   {'cpfCnpj': '14991918000154', 'preco': float(0.83)},
                   {'cpfCnpj': '40988513000177', 'preco': float(0.45)},
                   {'cpfCnpj': '44765328000174', 'preco': float(0.29)}]


@app.route('/calcular-produto', methods=['POST'])
def calcular_produto_endpoint():
    cpf_cnpj = request.json.get('cpfCnpj')
    if cpf_cnpj is None:
        return jsonify({'error': 'cpfCnpj não fornecido'}), 400

    # Busca o valor do 'preco' correspondente ao 'cpfCnpj'
    preco = None
    for item in preco_unit:
        if item['cpfCnpj'] == cpf_cnpj:
            preco = item['preco']
            break

    if preco is None:
        return jsonify({'error': 'cpfCnpj não encontrado'}), 404

    quantidade = request.json.get('quantidade')
    if quantidade is None:
        return jsonify({'error': 'Quantidade não fornecida'}), 400

    try:
        quantidade = float(quantidade)
    except ValueError:
        return jsonify({'error': 'Quantidade inválida'}), 400

    produto = quantidade * preco
    return jsonify({'resultado': produto})


if __name__ == '__main__':
    app.run()




