from server.flask_server import FlaskServer
from server.data_dragon import DataDragon

data_dragon = DataDragon()
flask_server = FlaskServer(data_dragon.get_version())
data_dragon.download_if_needed()
flask_server.run()
