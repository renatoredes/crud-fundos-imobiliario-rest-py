from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_fiis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


# Criação do banco de dados
with app.app_context():
    db.create_all()

# Rotas CRUD


@app.route('/tickers', methods=['GET'])
def get_all_tickers():
    tickers = Ticker.query.all()
    tickers_list = []
    for ticker in tickers:
        tickers_list.append({'id': ticker.id, 'nome': ticker.name})
    return jsonify({'Ativo': tickers_list})


@app.route('/tickers/<int:ticker_id>', methods=['GET'])
def get_ticker(ticker_id):
    ticker = Ticker.query.get_or_404(ticker_id)
    return jsonify({'id': ticker.id, 'nome': ticker.name})


@app.route('/tickers', methods=['POST'])
def create_ticker():
    data = request.get_json()
    new_ticker = Ticker(name=data['nome'])
    db.session.add(new_ticker)
    db.session.commit()
    return jsonify({'message': 'Ticker criado com sucesso!'})


@app.route('/tickers/<int:ticker_id>', methods=['PUT'])
def update_ticker(ticker_id):
    ticker = Ticker.query.get_or_404(ticker_id)
    data = request.get_json()
    ticker.name = data['nome']
    db.session.commit()
    return jsonify({'message': 'Ticker atualizado com sucesso!'})


@app.route('/tickers/<int:ticker_id>', methods=['DELETE'])
def delete_ticker(ticker_id):
    ticker = Ticker.query.get_or_404(ticker_id)
    db.session.delete(ticker)
    db.session.commit()
    return jsonify({'message': 'Ticker excluído com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)
