from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calcular-produto', methods=['POST'])
def calcular_produto_endpoint():
    quantidade = request.json.get('cpfCnpj', 'quantidade')
    if quantidade is None:
        error = jsonify({'error': 'Quantidade não fornecida'}), 400

    try:
        quantidade = float(quantidade)
    except ValueError:
        return error
    preco_unit = [{'cpfCnpj': '40238802000159', 'preco': float(0.58)},
                   {'cpfCnpj': '10423979000164', 'preco': float(0.62)},
                   {'cpfCnpj': '37789234000170', 'preco': float(0.88)},
                   {'cpfCnpj': '14991918000154', 'preco': float(0.83)},
                   {'cpfCnpj': '40988513000177', 'preco': float(0.45)},
                   {'cpfCnpj': '44765328000174', 'preco': float(0.29)}]
    for item in preco_unit:
        if item['cpfCnpj'] == cpfCnpj:
            preco = item['preco']
            break
    else:
        # Se não encontrar, define o valor do preço como None ou algum valor padrão
        preco = None

    # Imprime o valor do preço
    print(preco)
    produto = quantidade * preco
    return jsonify({'resultado': produto})


if __name__ == '__main__':
    app.run()


