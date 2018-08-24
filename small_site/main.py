import sqlite3
from flask import Flask, g, render_template, request

app = Flask(__name__)
SQLITE_DB_PATH = 'data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(SQLITE_DB_PATH)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price', methods=['POST'])
def price():
        cur = get_db().cursor()
        stockId = request.form.get('stock_id', 'NO_ID')
        t = (stockId,)
        cur.execute('SELECT stock_id,date,開盤價,收盤價 FROM price WHERE stock_id=?', t)
        #return str(cur.fetchall()[len(cur.fetchall())-1])

        result = cur.fetchall()
    
        if len(result) == 0:
            return 'No Data'
        
        result = result[len(result)-1]
        return render_template(
            'price.html',
            stock_id = str(result[0]),
            data_date = str(result[1]),
            start_price = str(result[2]),
            final_price = str(result[3])
        )

@app.route('/map')
def mymap():
        return render_template('my_map.html')

if __name__ == '__main__':
    app.run(debug=True)