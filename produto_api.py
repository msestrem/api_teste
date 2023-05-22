from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular-produto', methods=['POST'])
def calcular_produto_endpoint():
    quantidade = request.json['quantidade']
    produto = quantidade * 1.68
    return jsonify({'resultado': produto})

if __name__ == '__main__':
    app.run()





def calcular_produto(quantidade):
    produto = quantidade * 1.68
    return produto

# Solicita ao usuário a quantidade
quantidade = int(input("Digite a quantidade: "))

# Chama a função para calcular o produto
resultado = calcular_produto(quantidade)

# Imprime o resultado
print("O produto da quantidade por 1.68 é:", resultado)