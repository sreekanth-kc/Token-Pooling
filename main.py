import json
from flask import Response
from app.utils.db_initializer import db
from flask import Flask, request, jsonify
from app.utils.sql_connection import ConnectSqlClient
from app.models.tokens import Tokens, TokenListSchema
from app.utils.token_generator import generate_token, cache, save_token
import threading

app = Flask(__name__, static_folder='public')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ConnectSqlClient.connection_string()
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/post_token', methods=['POST'])
def post_token():
    """Post token into the Pool"""
    token_name = request.args.get('token_name')
    token = db.session.query(Tokens).filter(Tokens.token_name == token_name).first()
    if token:
        response = Response(json.dumps({"Response": "Token name already used"}), status=409,
                            mimetype='application/json')
        return response
    else:
        tokens = Tokens(
            token_name=token_name
        )
        tokens.save()
        response = Response(json.dumps({"Response": "Created Token"}), status=201, mimetype='application/json')
        return response


@app.route('/get_token', methods=['GET'])
def get_token():
    """Get a random Token from the Pool"""
    token = generate_token()
    response = Response(json.dumps({"token": token}), status=200, mimetype='application/json')
    return response


@app.route('/token_status', methods=['GET'])
def get_token_status():
    """Get status of all tokens"""
    queue = cache.get('token_queue')
    threads = list()
    for tokens in queue:
        execution_thread = threading.Thread(target=save_token(), args=(tokens,))
        threads.append(execution_thread)
        execution_thread.start()
    for index, thread in enumerate(threads):
        thread.join()
    response = Response(json.dumps({"token_status": queue}), status=200, mimetype='application/json')
    return response


@app.route('/')
def root():
    return jsonify({'message': 'Success'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8083, debug=True)
