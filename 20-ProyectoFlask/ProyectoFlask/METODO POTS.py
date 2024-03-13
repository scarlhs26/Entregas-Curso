from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# Ruta para agregar un nuevo usuario
@app.route('/nuevo_usuario', methods=['POST'])
def agregarUsuario():
    try:
        nuevo_usuario = request.get_json()

        if 'nombre' not in nuevo_usuario:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nuevo_usuario['nombre'],))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Usuario agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#{ "nombre": "Nombre del usuario"}


# Ruta para agregar un nuevo autor
@app.route('/autores', methods=['POST'])
def agregarAutor():
    try:
        nuevo_autor = request.get_json()

        if 'nombre' not in nuevo_autor:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO autores (nombre) VALUES (%s)", (nuevo_autor['nombre'],))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Autor agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#{ "nombre": "Nombre del autor"}

# Ruta para agregar un nuevo género
@app.route('/generos', methods=['POST'])
def agregarGenero():
    try:
        nuevo_genero = request.get_json()

        if 'nombre' not in nuevo_genero:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO generos (nombre) VALUES (%s)", (nuevo_genero['nombre'],))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Género agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#{ "nombre": "Nombre del genero"}


# Ruta para agregar una nueva editorial
@app.route('/editoriales', methods=['POST'])
def agregarEditorial():
    try:
        nueva_editorial = request.get_json()

        if 'nombre' not in nueva_editorial:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO editoriales (nombre) VALUES (%s)", (nueva_editorial['nombre'],))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Editorial agregada correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#{ "nombre": "Nombre del editoral"}

# Ruta para agregar un nuevo libro
@app.route('/libros', methods=['POST'])
def agregarLibro():
    try:
        nuevo_libro = request.get_json()

        if 'titulo' not in nuevo_libro or 'anno_publicacion' not in nuevo_libro \
                or 'autor_id' not in nuevo_libro or 'genero_id' not in nuevo_libro \
                or 'editorial_id' not in nuevo_libro:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO libros (titulo, anno_publicacion, autor_id, genero_id, editorial_id) "
                       "VALUES (%s, %s, %s, %s, %s)",
                       (nuevo_libro['titulo'], nuevo_libro['anno_publicacion'],
                        nuevo_libro['autor_id'], nuevo_libro['genero_id'], nuevo_libro['editorial_id']))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Libro agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
#{"titulo": "Título del Libro", "anno_publicacion": 2022, "autor_id": 1, "genero_id": 1,"editorial_id": 1}


# Ruta para agregar una nueva reseña
@app.route('/resenas', methods=['POST'])
def agregarResena():
    try:
        nueva_resena = request.get_json()

        if 'contenido' not in nueva_resena or 'libro_id' not in nueva_resena \
                or 'usuario_id' not in nueva_resena:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO resenas (contenido, libro_id, usuario_id) "
                       "VALUES (%s, %s, %s)",
                       (nueva_resena['contenido'], nueva_resena['libro_id'],
                        nueva_resena['usuario_id']))

        mysql.connection.commit()

        cursor.close()

        return jsonify({'mensaje': 'Reseña agregada correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#{ "contenido": "Contenido de la reseña",  "libro_id": 1, "usuario_id": 1}

if __name__ == '__main__':
    app.run(debug=True, port=7500)
