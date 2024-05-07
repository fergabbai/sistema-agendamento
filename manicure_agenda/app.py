from flask import Flask, request, jsonify
from database import Database
from datetime import datetime

app = Flask(__name__)
db = Database()  # Inicializa o banco de dados

@app.route('/agendar', methods=['POST'])
def agendar_horario():
    data = request.get_json()
    try:
        cliente = data['cliente']
        data_horario_str = data['data_horario']
        data_horario = datetime.strptime(data_horario_str, "%d/%m/%Y %H:%M")
    except (KeyError, ValueError):
        return jsonify({'erro': 'Dados inválidos. Certifique-se de enviar cliente e data_horario no formato correto (dd/mm/yyyy hh:mm).'}), 400

    # Verificar se o horário está disponível
    if db.verificar_disponibilidade(data_horario):
        db.agendar_horario(cliente, data_horario)
        return jsonify({'mensagem': 'Agendamento realizado com sucesso!'})
    else:
        return jsonify({'erro': 'Horário não disponível.'}), 409

@app.route('/desmarcar', methods=['DELETE'])
def desmarcar_horario():
    data = request.get_json()
    try:
        data_horario_str = data['data_horario']
        data_horario = datetime.strptime(data_horario_str, "%d/%m/%Y %H:%M")
    except (KeyError, ValueError):
        return jsonify({'erro': 'Dados inválidos. Certifique-se de enviar data_horario no formato correto (dd/mm/yyyy hh:mm).'}), 400

    if db.desmarcar_horario(data_horario):
        return jsonify({'mensagem': 'Horário desmarcado com sucesso!'})
    else:
        return jsonify({'erro': 'Horário não encontrado.'}), 404

@app.route('/agenda', methods=['GET'])
def mostrar_agenda():
    agenda = db.obter_agenda()
    return jsonify(agenda)

if __name__ == '__main__':
    app.run(debug=True)