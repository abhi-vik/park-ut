import routes
import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)
app = routes.register(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
