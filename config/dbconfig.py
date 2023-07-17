import toml

# 读取配置文件
config = toml.load("config.toml")
# 获取数据库配置信息
db_host = config["database"]["host"]
db_port = config["database"]["port"]
db_username = config["database"]["username"]
db_password = config["database"]["password"]
db_name = config["database"]["database_name"]
# 使用获取到的配置信息进行数据库连接等操作
# ...
