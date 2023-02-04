# Criando uma API com Flask para gerenciar um inventário de discos.
# A Interação será feita por Postman através do: http://localhost:5000/discos
# É uma API, por isso não haverá comunicação com banco de dados.

from flask import Flask, jsonify, request


app = Flask(__name__)

discos = [
{
    'id': 1,
    "Título": 'Rocket to Russia',
    'Artista': 'Ramones'
},
{
    'id': 2,
    'Título': 'Famous Monsters',
    'Artista': 'Misfits'
},
{
    'id': 3,
    'Título': 'October Rust',
    'Artista': 'Type O Negative'
},
{
    'id': 4,
    'Título': 'Pior Cenário Possível',
    'Artista': 'Matanza'
},
{
    'id': 5,
    'Título': 'Facelift',
    'Artista': 'Alice in Chains'
},
]
@app.route('/discos', methods=['GET'])
def ver_discos():
    return jsonify(discos)

# Função para consultar os discos por ID:
@app.route('/discos/<int:id>', methods=['GET'])
def find_dscid(id):
    for disco in discos:
        if disco.get('id') == id:
            return jsonify(disco)

# Função para editar os parâmetros dos discos(Pela ID):
@app.route('/discos/<int:id>', methods=['PUT'])
def edita_disco(id):
    disco_edit = request.get_json()
    for indice, disco in enumerate(discos):
        if disco.get('id') == id:
            discos[indice].update(disco_edit)
            return jsonify(discos[indice])    

# Função para add novos itens:
@app.route('/discos', methods=['POST'])
def add_novo():
    novo_disco = request.get_json()
    discos.append(novo_disco)
    return jsonify(discos)                 

# Função para remover itens:
@app.route('/discos/<int:id>', methods=['DELETE'])
def excluir_disco(id):
    for indice, disco in enumerate(discos):
        if disco.get('id') == id:
            del discos[indice]
    return jsonify(discos)        


app.run(port=5000,host='localhost',debug=True)


