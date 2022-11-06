from flask import Flask,render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)
db = pd.read_csv('bank_branches.csv')

@app.route('/', methods=['GET'])
def index():
    banks = db.drop_duplicates(subset='bank_id')
    return render_template('index.html', banks=banks.to_dict(orient='records'))

@app.route('/bank/<int:id>')
def get_branches(id):
    bank_branches = db.loc[db['bank_id'] == id]
    return render_template('branches.html', branches=bank_branches.to_dict(orient='records'))

@app.route('/<id>')
def get_bank(id):
    bank = db.loc[db['ifsc'] == id]
    return render_template('bank.html', bank=bank.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True, port=3500)

