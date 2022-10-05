import os
from flask import Flask, request
app = Flask(__name__)


@app.route("/calc")
def calculadora():

    v1 = request.args.get('a')
    v2 = request.args.get('b')
    operacao = request.args.get('operacao')

    a = int(v1)
    b = int(v2)
    if (operacao == 'som'):
        result = a + b
    elif (operacao == 'sub'):
        result = a - b
    elif (operacao == 'mult'):
        result = a * b
    elif (operacao == 'div'):
        result = a / b

    return str(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)