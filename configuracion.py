import os

class DevelopmentConfig():
    DEBUG=True
    #puerto de conexion
    PORT=3000
    #host de conexion
    HOST="0.0.0.0"
    MYSQL_HOST="167.71.26.121"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = 'Camaleon_12' 
    #os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_DB = "Colppy"
    USER=os.environ.get('usuarioItiers')
    PASSWORD= os.environ.get('passwordItiers')
    URLBASE = "https://login.colppy.com/lib/frontera2/service.php"


class ProductionConfig():
    DEBUG=True
    #puerto de conexion
    PORT=3000
    #host de conexion
    HOST="0.0.0.0"
    MYSQL_HOST="167.71.26.121"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = 'Camaleon_12' 
    #os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_DB = "Colppy"
    USER = os.environ.get('usuarioItiers')
    PASSWORD = os.environ.get('passwordItiers')
    URLBASE = "https://login.colppy.com/lib/frontera2/service.php"



configuracion={
    'development':DevelopmentConfig,
    'production':ProductionConfig
}