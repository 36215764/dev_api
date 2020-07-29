from flask import request
from flask_restful import Resource
import json



lista_habilidades = ['python', 'java', 'flask', 'php']

class Ability(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        try:
            habilidade = json.loads(request.data)
            

            for h in habilidade:
                if h.lower() not in lista_habilidades:
                    lista_habilidades.append(h.lower())

            mensagem = 'As habilidades {} foram adicionadas com sucesso!'.format(habilidade)
            response = {'status':'sucesso', 'mensagem':mensagem}   

        except Exception:
            mensagem = 'Erro ao adicionar as habilidades, contate o adiministrador da API.'
            response = {'status':'erro', 'mensagem':mensagem}  
        
        return response



class AbilityById(Resource):
    def get(self, id):
        try:
            habilidade = lista_habilidades[id]
            response = {'habilidade':habilidade}

        except IndexError:
            mensagem = 'Não foi possivel encontrar a habilidade de id {}'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}

        except Exception:
            mensagem = 'Erro desconhecido, contate o adiministrador da API.'
            response = {'status':'erro', 'mensagem':mensagem}  
            
        return response

    def put(self, id):
        try:
            habilidade = json.loads(request.data)
            lista_habilidades[id] = habilidade['habilidade']

            mensagem = 'A habilidade de id {}, foi alterada para {}!'.format(id, habilidade['habilidade'])
            response = {'status':'sucesso', 'mensagem':mensagem}

        except IndexError:
            mensagem = 'Não foi possivel encontrar a habilidade de id {}'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido, contate o adiministrador da API.'
            response = {'status':'erro', 'mensagem':mensagem}  

        return response



    def delete(self, id):
        try:
            lista_habilidades.pop(id)

            mensagem = 'A habilidade de id {}, foi excluida com sucesso!'.format(id)
            response = {'status':'sucesso', 'mensagem':mensagem}

        except IndexError:
            mensagem = 'Não foi possivel encontrar a habilidade de id {}'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido, contate o adiministrador da API.'
            response = {'status':'erro', 'mensagem':mensagem}  

        return response
