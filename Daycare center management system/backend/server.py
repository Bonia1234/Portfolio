from flask import Flask, jsonify
from creds import Creds

app = Flask(__name__)

# Route to expose database credentials
@app.route('/credentials')
def get_credentials():
    return jsonify({
        "conString": Creds.conString,
        "userName": Creds.userName,
        "password": Creds.password,
        "dbname": Creds.dbname
    })

if __name__ == '__main__':
    app.run(debug=True)
