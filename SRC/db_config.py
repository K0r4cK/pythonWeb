from app import app
from flskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations

app.config['MYSQL_DATABE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Am0rc17016+&Mum1n05116'
app.config['MUSQL_DATABASE_DB'] = 'schedule'
app.config['MUSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)