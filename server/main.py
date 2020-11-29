from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '{ "msg": "test maison" }'


@app.route('/hello')
def hello():
    return '{ "msg": "test maison", "id": 45 }'

@app.route('/test/<int:number>')
def test(number):
    number = number + 1
    return '{ "msg": "test maison", "id": %d }' % number


if __name__ == '__main__':
    app.run()