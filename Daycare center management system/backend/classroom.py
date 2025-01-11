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

# Route to create a new classroom
@app.route('/classroom', methods=['POST'])
def create_classroom():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            capacity = request.json['capacity']
            name = request.json['name']
            facility_id = request.json['facility_id']
            query = "INSERT INTO classroom (capacity, name, facility_id) VALUES (%s, %s, %s)"
            cursor.execute(query, (capacity, name, facility_id))
            connection.commit()
            return jsonify({"message": "Classroom created successfully"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to get all classrooms
@app.route('/classroom', methods=['GET'])
def get_classrooms():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM classroom"
            cursor.execute(query)
            classrooms = cursor.fetchall()
            return jsonify(classrooms), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to update a classroom
@app.route('/classroom/<int:id>', methods=['PUT'])
def update_classroom(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            capacity = request.json['capacity']
            name = request.json['name']
            facility_id = request.json['facility_id']
            query = "UPDATE classroom SET capacity = %s, name = %s, facility_id = %s WHERE id = %s"
            cursor.execute(query, (capacity, name, facility_id, id))
            connection.commit()
            return jsonify({"message": "Classroom updated successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to delete a classroom
@app.route('/classroom/<int:id>', methods=['DELETE'])
def delete_classroom(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM classroom WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            return jsonify({"message": "Classroom deleted successfully"}), 200
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
    #https://stackoverflow.com/questions/54769603/python-flask-api-restful
    #https://forums.mysql.com/read.php?50,685798,685798