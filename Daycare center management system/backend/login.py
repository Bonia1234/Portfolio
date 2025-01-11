from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'admin' and password == 'password':
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)

#References:
    #https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    #https://flask.palletsprojects.com/en/1.1.x/quickstart/
    