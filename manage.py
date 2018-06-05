from flask import Flask

import settings
from apis import init_api
from dao import init_db

app = Flask(__name__)
#初始化app
app.config.from_object(settings.Config)

#初始化api
init_api(app)

#初始化db或dao
init_db(app)

if __name__ == '__main__':
    app.run()
