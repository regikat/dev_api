from flask import Flask, jsonify, request    #padrão
import json
app = Flask(__name__)                        #padrão

#Criando lista inicial de desenvolvedores
desenvolvedores = [
    {
            'id':'0',
            'nome':'Rafael',
            'habilidade':['Pyhon','Flask']
    },
    {
            'id': '1',
            'nome':'Reginaldo',
            'habilidade': ['Pyhon', 'Django']
    }
]

#devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor.
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])           #ROTA usando metodos get e put
def desenvolvedor(id):               #metodo
    if request.method == 'GET':      #Metodo que envia
        try:                                                               #clausula de excessão
            response = desenvolvedores[id]
        except IndexError:                                                 #clausula de excessão
            mensagem ='Desenvolvedor de ID {} não existe'.format(id)       #mensagem emitida na excessão
            response = {'status':'erro','mensagem':mensagem}               #mensagem emitida na excessão
        except Exception:
            mensagem = 'Erro desconhecido.Procure o administrador da API'   # mensagem emitida na excessão
            response = {'status': 'erro', 'mensagem': mensagem}             # mensagem emitida na excessão
        return jsonify (response)
#
    elif request.method == 'PUT':   #Metodo atualiza todos os campos
        dados = json.loads(request.data)           #
        desenvolvedores[id] = dados
        return jsonify(dados)
#Deleta
    elif request.method == 'DELETE':   #Metodo de delecao
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})

#Lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return  jsonify(desenvolvedores[posicao])
    # consultar todos os desenvolvedores
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':          #padrão
    app.run(debug=True)             #padrão