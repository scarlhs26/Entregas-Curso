from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# Ruta para actualizar parcialmente un usuario
@app.route('/usuarios/<int:user_id>', methods=['PATCH'])
def actualizarUsuario(user_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE usuarios SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar el usuario específico
        consulta += f" WHERE id = {user_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Usuario actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/autores/<int:autor_id>', methods=['PATCH'])
def actualizarAutor(autor_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE autores SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar el autor específico
        consulta += f" WHERE id = {autor_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Autor actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generos/<int:genero_id>', methods=['PATCH'])
def actualizarGenero(genero_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE generos SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar el género específico
        consulta += f" WHERE id = {genero_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Género actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/editoriales/<int:editorial_id>', methods=['PATCH'])
def actualizarEditorial(editorial_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE editoriales SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar la editorial específica
        consulta += f" WHERE id = {editorial_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Editorial actualizada correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/libros/<int:libro_id>', methods=['PATCH'])
def actualizarLibro(libro_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE libros SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar el libro específico
        consulta += f" WHERE id = {libro_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Libro actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/resenas/<int:resena_id>', methods=['PATCH'])
def actualizarResena(resena_id):
    try:
        datos_actualizados = request.get_json()

        if not datos_actualizados:
            return jsonify({'mensaje': 'No se proporcionaron datos para actualizar'}), 400

        cursor = mysql.connection.cursor()

        # Construir la consulta SQL dinámicamente basada en los datos proporcionados
        consulta = "UPDATE resenas SET "
        parametros = []

        for clave, valor in datos_actualizados.items():
            consulta += f"{clave} = %s, "
            parametros.append(valor)

        # Eliminar la última coma y espacio
        consulta = consulta[:-2]

        # Agregar la condición para actualizar la reseña específica
        consulta += f" WHERE id = {resena_id}"

        cursor.execute(consulta, tuple(parametros))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'mensaje': 'Reseña actualizada correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=7500)
