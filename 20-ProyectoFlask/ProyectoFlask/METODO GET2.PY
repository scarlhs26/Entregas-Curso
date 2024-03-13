from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# Ruta para obtener información detallada de una reseña por el ID del libro
@app.route('/detalle_resena/<libro_id>', methods=['GET'])
def obtenerDetalleResena(libro_id):
    try:
        cursor = mysql.connection.cursor()

        # Realizar una consulta SQL uniendo las tablas necesarias
        cursor.execute("""
            SELECT
                libros.id AS id_libro,
                libros.titulo AS nombre_libro,
                autores.nombre AS nombre_autor,
                generos.nombre AS nombre_genero,
                resenas.contenido AS texto_resena,
                usuarios.nombre AS usuario_resena
            FROM libros
            JOIN autores ON libros.autor_id = autores.id
            JOIN generos ON libros.genero_id = generos.id
            JOIN resenas ON libros.id = resenas.libro_id
            JOIN usuarios ON resenas.usuario_id = usuarios.id
            WHERE libros.id = %s
        """, (libro_id,))

        detalle_resena = cursor.fetchone()

        cursor.close()

        if not detalle_resena:
            return jsonify({'mensaje': 'No se puede encontrar la información solicitada'}), 404

        # Convertir los resultados a un formato JSON y retornar la respuesta
        respuesta = {
            'id_libro': detalle_resena[0],
            'nombre_libro': detalle_resena[1],
            'nombre_autor': detalle_resena[2],
            'nombre_genero': detalle_resena[3],
            'texto_resena': detalle_resena[4],
            'usuario_resena': detalle_resena[5]
        }

        return jsonify(respuesta), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7500)
