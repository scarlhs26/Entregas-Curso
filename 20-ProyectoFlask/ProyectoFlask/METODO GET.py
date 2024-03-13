from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# Ruta para obtener todos los libros
@app.route('/libros', methods=['GET'])
def obtenerLibros():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()
        cursor.close()
        res = jsonify(libros)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener un libro por su ID
@app.route('/libros/<libro_id>', methods=['GET'])
def obtener_informacion_especifica_libro(libro_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM libros WHERE id = %s", (libro_id,))
        libro = cursor.fetchone()
        cursor.close()

        if libro:
            return jsonify(libro)
        else:
            return jsonify({'mensaje': 'No se puede encontrar el libro'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los autores
@app.route('/autores', methods=['GET'])
def obtenerAutores():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM autores")
        autores = cursor.fetchall()
        cursor.close()
        res = jsonify(autores)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener un autor por su ID
@app.route('/autores/<autor_id>', methods=['GET'])
def obtener_informacion_especifica_autor(autor_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM autores WHERE id = %s", (autor_id,))
        autor = cursor.fetchone()
        cursor.close()

        if autor:
            return jsonify(autor)
        else:
            return jsonify({'mensaje': 'No se puede encontrar el autor'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})
# Ruta para obtener todas las editoriales
@app.route('/editoriales', methods=['GET'])
def obtenerEditoriales():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM editoriales")
        editoriales = cursor.fetchall()
        cursor.close()
        res = jsonify(editoriales)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener una editorial por su ID
@app.route('/editoriales/<editorial_id>', methods=['GET'])
def obtener_informacion_especifica_editorial(editorial_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM editoriales WHERE id = %s", (editorial_id,))
        editorial = cursor.fetchone()
        cursor.close()

        if editorial:
            return jsonify(editorial)
        else:
            return jsonify({'mensaje': 'No se puede encontrar la editorial'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los géneros
@app.route('/generos', methods=['GET'])
def obtenerGeneros():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM generos")
        generos = cursor.fetchall()
        cursor.close()
        res = jsonify(generos)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener un género por su ID
@app.route('/generos/<genero_id>', methods=['GET'])
def obtener_informacion_especifica_genero(genero_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM generos WHERE id = %s", (genero_id,))
        genero = cursor.fetchone()
        cursor.close()

        if genero:
            return jsonify(genero)
        else:
            return jsonify({'mensaje': 'No se puede encontrar el género'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todas las reseñas
@app.route('/resenas', methods=['GET'])
def obtenerResenas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM resenas")
        resenas = cursor.fetchall()
        cursor.close()
        res = jsonify(resenas)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener una reseña por su ID
@app.route('/resenas/<resena_id>', methods=['GET'])
def obtener_informacion_especifica_resena(resena_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM resenas WHERE id = %s", (resena_id,))
        resena = cursor.fetchone()
        cursor.close()

        if resena:
            return jsonify(resena)
        else:
            return jsonify({'mensaje': 'No se puede encontrar la reseña'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtenerUsuarios():
    try:
        # Establece una conexión con la base de datos
        cursor = mysql.connection.cursor()
        # Ejecuta la consulta SQL para seleccionar todos los usuarios
        cursor.execute("SELECT * FROM usuarios")
        # Recupera todos los resultados de la consulta
        usuarios = cursor.fetchall()
        # Cierra el cursor
        cursor.close()
        # Convierte los resultados a JSON y agrega la cabecera para permitir solicitudes desde cualquier origen
        res = jsonify(usuarios)
        res.headers.add("Access-Control-Allow-Origin", "*")
        # Retorna la respuesta JSON
        return res
    except Exception as e:
        # Maneja cualquier excepción y retorna un mensaje de error
        return jsonify({'error': str(e)})

# Ruta para obtener un usuario por su ID
@app.route('/usuarios/<usuario_id>', methods=['GET'])
def obtener_informacion_especifica_usuario(usuario_id):
    try:
        # Establece una conexión con la base de datos
        cursor = mysql.connection.cursor()
        # Ejecuta la consulta SQL para seleccionar al usuario por su ID
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        # Recupera el resultado de la consulta
        usuario = cursor.fetchone()
        # Cierra el cursor
        cursor.close()

        if usuario:
            # Si se encuentra el usuario, lo convierte a JSON y lo retorna
            return jsonify(usuario)
        else:
            # Si no se encuentra el usuario, retorna un mensaje de error con código 404
            return jsonify({'mensaje': 'No se puede encontrar el usuario'}), 404
    except Exception as e:
        # Maneja cualquier excepción y retorna un mensaje de error
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=7500)
