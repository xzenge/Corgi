from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/resume')
def resume():
    return render_template('/resume/index.html')
    # return 'resume'

if __name__ == '__main__':
    app.run()
