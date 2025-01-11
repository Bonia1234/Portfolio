from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from creds import Creds

app = Flask(__name__)

# Function to create a MySQL connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=Creds.conString,
            user=Creds.userName,
            password=Creds.password,
            database=Creds.dbname
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' has occurred")
    return connection

# Route to create a new child
@app.route('/child', methods=['POST'])
def create_child():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            age = request.json['age']
            room = request.json['room']
            query = "INSERT INTO child (firstname, lastname, age, room) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (firstname, lastname, age, room))
            connection.commit()
            return jsonify({"message": "Child created successfully"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to get all children
@app.route('/child', methods=['GET'])
def get_children():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM child"
            cursor.execute(query)
            children = cursor.fetchall()
            return jsonify(children), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to update a child
@app.route('/child/<int:id>', methods=['PUT'])
def update_child(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            age = request.json['age']
            room = request.json['room']
            query = "UPDATE child SET firstname = %s, lastname = %s, age = %s, room = %s WHERE id = %s"
            cursor.execute(query, (firstname, lastname, age, room, id))
            connection.commit()
            return jsonify({"message": "Child updated successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to delete a child
@app.route('/child/<int:id>', methods=['DELETE'])
def delete_child(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM child WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            return jsonify({"message": "Child deleted successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

if __name__ == '__main__':
    app.run(debug=True)

#References:
    #https://discuss.python.org/t/mysql-query-error-with-config-py-file/29657
    #https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python3_Flask.html