import flask
from application import db

class TradesBook(db.Document):
    Trade_Id=db.StringField(unique=True,required=True)
    Underlier_Ticker=db.StringField(max_length=20)
    Product_Type=db.StringField(max_length=20)
    Payoff=db.StringField(max_length=20)
    Trade_Date=db.StringField(max_length=20)
    Trade_Maturity=db.StringField(max_length=20)
    Strike=db.DecimalField()
    Dividend=db.DecimalField()
