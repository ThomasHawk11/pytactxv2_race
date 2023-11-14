import api.j2l.pytactx.agent as pytactx
import os
from dotenv import load_dotenv

load_dotenv()
ARBITRE = os.getenv("ARBITRE")
ARENA = os.getenv("ARENA")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SERVER = os.getenv("SERVER")

agent = pytactx.Agent(playerId=ARBITRE,
						arena=ARENA,
						username=USERNAME,
						password=PASSWORD,
						server=SERVER,
						verbosity=2)



while True:
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)