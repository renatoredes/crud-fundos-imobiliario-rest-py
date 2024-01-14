# crud/crud_fiis.py
from models.models import db, Ticker


class TickerCRUD:
    @staticmethod
    def to_dict(ticker):
        return {'id': ticker.id, 'nome': ticker.name}

    @staticmethod
    def get_all_tickers():
        tickers = Ticker.query.all()
        tickers_list = [TickerCRUD.to_dict(ticker) for ticker in tickers]
        return {'Ativo': tickers_list}

    @staticmethod
    def get_ticker(ticker_id):
        ticker = Ticker.query.get_or_404(ticker_id)
        return TickerCRUD.to_dict(ticker)

    @staticmethod
    def create_ticker(data):
        new_ticker = Ticker(name=data['nome'])
        db.session.add(new_ticker)
        db.session.commit()
        return {'message': 'Ticker criado com sucesso!'}

    @staticmethod
    def update_ticker(ticker_id, data):
        ticker = Ticker.query.get_or_404(ticker_id)
        ticker.name = data['nome']
        db.session.commit()
        return {'message': 'Ticker atualizado com sucesso!'}

    @staticmethod
    def delete_ticker(ticker_id):
        ticker = Ticker.query.get_or_404(ticker_id)
        db.session.delete(ticker)
        db.session.commit()
        return {'message': 'Ticker excluído com sucesso!'}
