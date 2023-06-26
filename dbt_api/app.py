from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/model', methods=['POST'])
def execute_script() -> Flask:
    model = request.args.get('model')

    os.system(f'./script.sh {model}')
    return 'Verificar os logs'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
