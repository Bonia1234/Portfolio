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

# Route to create a new facility
@app.route('/facility', methods=['POST'])
def create_facility():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            name = request.json['name']
            query = "INSERT INTO facility (name) VALUES (%s)"
            cursor.execute(query, (name,))
            connection.commit()
            return jsonify({"message": "Facility created successfully"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to get all facilities
@app.route('/facility', methods=['GET'])
def get_facilities():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM facility"
            cursor.execute(query)
            facilities = cursor.fetchall()
            return jsonify(facilities), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to update a facility
@app.route('/facility/<int:id>', methods=['PUT'])
def update_facility(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            name = request.json['name']
            query = "UPDATE facility SET name = %s WHERE id = %s"
            cursor.execute(query, (name, id))
            connection.commit()
            return jsonify({"message": "Facility updated successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to establish database connection"}), 500

# Route to delete a facility
@app.route('/facility/<int:id>', methods=['DELETE'])
def delete_facility(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM facility WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            return jsonify({"message": "Facility deleted successfully"}), 200
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
    #https://www.codementor.io/@adityamalviya/python-flask-mysql-connection-rxblpje73
    #https://hevodata.com/learn/flask-mysql/
    