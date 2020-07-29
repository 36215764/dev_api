from flask import Flask, request, jsonify
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0, 'nome': 'Rafael', 'habilidades':['python', 'Flask']},
    {'id':1, 'nome': 'Richard', 'habilidades':['python', 'Django']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            
        except IndexError:
            mensagem = 'Não foi possivel encontrar esse ID {}'.format(id)
            response = jsonify({'status':'Erro', 'mensagem':mensagem})
        
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API.'
            response = jsonify({'status':'Erro', 'mensagem':mensagem})

        return response

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados

        return desenvolvedores[id]

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)

        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido!'})


@app.route('/dev/', methods=['GET', 'POST'])
def list_developers():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao

        desenvolvedores.append(dados)

        return desenvolvedores[posicao]

    else:
        return jsonify(desenvolvedores)
        
        
    
        
    
    
    



if __name__ == "__main__":
    app.run(debug=True)
    
