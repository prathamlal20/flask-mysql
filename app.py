from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db = mysql.connector.connect(
    host= '172.31.93.171',
    user= 'user',
    password= 'password',
    database= 'mysql_python'
)

# Route to fetch data from MySQL
@app.route('/', methods=['GET'])
def get_data():
    try:
        cursor = db.cursor()

        cursor.execute('SELECT * FROM sample_data')
        data = cursor.fetchall()

        # Return the data as JSON
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)