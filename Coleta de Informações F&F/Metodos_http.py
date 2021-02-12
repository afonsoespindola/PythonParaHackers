# -*- coding: utf-8 -*-
import requests
host = "SEU ALVO"
metodos = ["GET", "POST", "OPTIONS", "PUT", "DELETE", "TRACE", "CONNECT", "HEAD", "PATCH"]
for metodo in metodos:
    resposta = requests.request(metodo, host)
    print metodo + " |--> " + resposta.reason

'''
GET
O método GET solicita a representação de um recurso específico. Requisições utilizando o método GET
devem retornar apenas dados.

POST
O método POST é utilizado para submeter uma entidade a um recurso específico,
frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.

OPTIONS
O método OPTIONS é usado para descrever as opções de comunicação com o recurso de destino.

PUT
O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.

DELETE
O método DELETE remove um recurso específico.

TRACE
O método TRACE executa um teste de chamada loop-back junto com o caminho para o recurso de destino.

CONNECT
O método CONNECT estabelece um túnel para o servidor identificado pelo recurso de destino.

HEAD
 O método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.

PATCH
O método PATCH é utilizado para aplicar modificações parciais em um recurso.

Fonte: https://developer.mozilla.org/

'''
