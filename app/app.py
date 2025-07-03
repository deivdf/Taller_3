from flask import Flask
from prometheus_client import Counter, generate_latest


app = Flask(__name__)
visits = Counter('website_visits', 'total de visitas en el sitio web')


@app.route('/')
def hello():
    visits.inc()
    return '¡Hola, mundo de prometheus!'


@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)