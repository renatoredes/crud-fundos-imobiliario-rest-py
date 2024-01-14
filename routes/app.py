# routes/app.py
from flask import Flask, request
from models.models import db
from crud.crud_fiis import TickerCRUD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_fiis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Criação do banco de dados
with app.app_context():
    db.create_all()

# Rotas CRUD


@app.route('/tickers', methods=['GET'])
def get_all_tickers():
    return TickerCRUD.get_all_tickers()


@app.route('/tickers/<int:ticker_id>', methods=['GET'])
def get_ticker(ticker_id):
    return TickerCRUD.get_ticker(ticker_id)


@app.route('/tickers', methods=['POST'])
def create_ticker():
    data = request.get_json()
    return TickerCRUD.create_ticker(data)


@app.route('/tickers/<int:ticker_id>', methods=['PUT'])
def update_ticker(ticker_id):
    data = request.get_json()
    return TickerCRUD.update_ticker(ticker_id, data)


@app.route('/tickers/<int:ticker_id>', methods=['DELETE'])
def delete_ticker(ticker_id):
    return TickerCRUD.delete_ticker(ticker_id)


if __name__ == '__main__':
    app.run(debug=True)
