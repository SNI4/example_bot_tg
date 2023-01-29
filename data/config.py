from environs import Env 

env = Env()
end.read_env()

TOKEN = env.str("EXAMPLEBOT_TOKEN")