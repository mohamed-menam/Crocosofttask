from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:(Password123##!)@localhost:3306/CROCOSOFT"


db = SQLAlchemy(app)


@app.route('/customers/', methods=["GET"])
def get_all():
    customers = db.engine.execute('SELECT * FROM customer;')
    return jsonify(customers)


@app.route('/customers/<int:pk>', methods=['DELETE'])
def delet_id(pk):
    customers = db.engine.execute('DELETE FROM Customers WHERE id=%s;', [pk])
    return " customer deleted"


@app.route('/customers/<int:pk>', methods=["GET"])
def get_id(pk):
    customers = db.engine.execute('SELECT * FROM Customers WHERE id=%s;', [pk])
    return jsonify(customers)


@app.route('/customers/<int:pk>', methods=["PUT"])
def update(pk):
    record = json.loads(request.data)
    customer_name = record["name"]
    customer_email = record["email"]

    customers = db.engine.execute(
        'UPDATE Customers SET name = %(name)s, email=%(id)s  WHERE id=%(id)s;', {"name": customer_name, "email": customer_email, "id": pk})
    return jsonify(customers)


@app.route('/customers/', methods=["post"])
def post():
    record = json.loads(request.data)
    customer_name = record["name"]
    customer_email = record["email"]
    customers = db.engine.execute(
        'INSERT INTO numbers VALUES (%s, %s);', [customer_name, customer_email])
    return jsonify(customers)


if __name__ == "__main__":
    app.run(debug=True)
