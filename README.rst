+ 项目结构

- app/  主目录，包含整个应用程序的代码。
  - api/    包含处理 API 路由的代码。
    - __init__.py
    - routes.py
  - services/   包含处理业务逻辑的代码，例如数据库操作、外部 API 调用等。
    - __init__.py
    - some_service.py
  - database/   目录来管理数据库相关的代码。
    - __init__.py
    - connection.py   用于创建数据库连接和会话的文件。
    - models.py     用于定义数据库模型和表结构的文件。
  - main.py     应用程序的入口文件，包含 FastAPI 应用的初始化和配置。

- 生成项目包文件
    pip freeze > requirements.txt