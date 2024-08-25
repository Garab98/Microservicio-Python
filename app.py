from flask import Flask
from controllers.user_controller import user_blueprint

app = Flask(__name__)

# Registrar el controlador de usuarios
app.register_blueprint(user_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)