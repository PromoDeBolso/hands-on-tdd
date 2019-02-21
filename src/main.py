from flask import Flask, request, jsonify
from commands.get_customer_luck_numbers import GetCustomerLuckNumbersCommand

app = Flask(__name__)


@app.route('/receber_numero_da_sorte', methods=['POST'])
def get_luck_number():
    cpf = request.values.get('cpf')
    pincode = request.values.get('pincode')

    pincode_generated = GetCustomerLuckNumbersCommand.call(cpf, pincode)

    if 'error' in pincode_generated:
        response = jsonify({ 'error': pincode_generated['error'] })
        response.status_code = 400

        return response

    response = jsonify({ 'pincode': pincode_generated })
    response.status_code = 201

    return response


if __name__ == '__main__':
    app.run()