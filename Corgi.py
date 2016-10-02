from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/resume')
def resume():
    return render_template('/templates/resume/index.html')

if __name__ == '__main__':
    app.run()
