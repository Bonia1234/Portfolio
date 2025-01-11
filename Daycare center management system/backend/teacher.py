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

# Route to create a new teacher
@app.route('/teacher', methods=['POST'])
def create_teacher():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            room = request.json['room']
            query = "INSERT INTO teacher (firstname, lastname, room) VALUES (%s, %s, %s)"
            cursor.execute(query, (firstname, lastname, room))
            connection.commit()
            return jsonify({"message": "Teacher created successfully"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to get all teachers
@app.route('/teacher', methods=['GET'])
def get_teachers():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM teacher"
            cursor.execute(query)
            teachers = cursor.fetchall()
            return jsonify(teachers), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to update a teacher
@app.route('/teacher/<int:id>', methods=['PUT'])
def update_teacher(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            room = request.json['room']
            query = "UPDATE teacher SET firstname = %s, lastname = %s, room = %s WHERE id = %s"
            cursor.execute(query, (firstname, lastname, room, id))
            connection.commit()
            return jsonify({"message": "Teacher updated successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to delete a teacher
@app.route('/teacher/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM teacher WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            return jsonify({"message": "Teacher deleted successfully"}), 200
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
    #https://github.com/jacklevin74/xenminer/blob/main/gpage.py
    #https://gist.github.com/jslvtr/139cf76db7132b53f2b20c5b6a9fa7ad?permalink_comment_id=2377381
    