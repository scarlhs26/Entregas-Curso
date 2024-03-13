from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# Ruta para eliminar un usuario por su ID
@app.route('/usuarios/<usuario_id>', methods=['DELETE'])
def eliminarUsuario(usuario_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si el usuario existe antes de eliminarlo
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()

        if not usuario:
            return jsonify({'mensaje': 'No se puede encontrar el usuario'}), 404

        # Eliminar el usuario
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/resenas/<resena_id>', methods=['DELETE'])
def eliminarResena(resena_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si la reseña existe antes de eliminarla
        cursor.execute("SELECT * FROM resenas WHERE id = %s", (resena_id,))
        resena = cursor.fetchone()

        if not resena:
            return jsonify({'mensaje': 'No se puede encontrar la reseña'}), 404

        # Eliminar la reseña
        cursor.execute("DELETE FROM resenas WHERE id = %s", (resena_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Reseña eliminada correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/libros/<libro_id>', methods=['DELETE'])
def eliminarLibro(libro_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si el libro existe antes de eliminarlo
        cursor.execute("SELECT * FROM libros WHERE id = %s", (libro_id,))
        libro = cursor.fetchone()

        if not libro:
            return jsonify({'mensaje': 'No se puede encontrar el libro'}), 404

        # Eliminar el libro
        cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Libro eliminado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/autores/<autor_id>', methods=['DELETE'])
def eliminarAutor(autor_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si el autor existe antes de eliminarlo
        cursor.execute("SELECT * FROM autores WHERE id = %s", (autor_id,))
        autor = cursor.fetchone()

        if not autor:
            return jsonify({'mensaje': 'No se puede encontrar el autor'}), 404

        # Eliminar el autor
        cursor.execute("DELETE FROM autores WHERE id = %s", (autor_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Autor eliminado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generos/<genero_id>', methods=['DELETE'])
def eliminarGenero(genero_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si el género existe antes de eliminarlo
        cursor.execute("SELECT * FROM generos WHERE id = %s", (genero_id,))
        genero = cursor.fetchone()

        if not genero:
            return jsonify({'mensaje': 'No se puede encontrar el género'}), 404

        # Eliminar el género
        cursor.execute("DELETE FROM generos WHERE id = %s", (genero_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Género eliminado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/editoriales/<editorial_id>', methods=['DELETE'])
def eliminarEditorial(editorial_id):
    try:
        cursor = mysql.connection.cursor()

        # Verificar si la editorial existe antes de eliminarla
        cursor.execute("SELECT * FROM editoriales WHERE id = %s", (editorial_id,))
        editorial = cursor.fetchone()

        if not editorial:
            return jsonify({'mensaje': 'No se puede encontrar la editorial'}), 404

        # Eliminar la editorial
        cursor.execute("DELETE FROM editoriales WHERE id = %s", (editorial_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Editorial eliminada correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7500)
