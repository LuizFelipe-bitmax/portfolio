from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'erro': 'JSON inválido. Envie {"nome": "...", "email": "..."}'}), 400
    usuario = {'nome': dados['nome'], 'email': dados['email']}
    usuarios.append(usuario)
    return jsonify(usuario), 201

@app.route('/usuarios/<int:indice>', methods=['DELETE'])
def remover_usuario(indice):
    if 0 <= indice < len(usuarios):
        usuario = usuarios.pop(indice)
        return jsonify({'mensagem': 'Usuário removido com sucesso', 'usuario': usuario}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
