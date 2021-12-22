from server.flask_server import FlaskServer
from server.data_dragon import DataDragon

flask_server = FlaskServer()
data_dragon = DataDragon()
data_dragon.download_if_needed()
flask_server.run()
