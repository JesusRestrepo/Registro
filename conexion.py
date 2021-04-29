from index import app
from flask_mysqldb import MySQL

#conexion base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jesus-Restrepo.2003'
app.config['MYSQL_DB'] = 'registro'
mysql=MySQL(app)