from flask import Flask , render_template

app = Flask(__name__)
@app.route('/')
def hello():
  return render_template('blog.html')

@app.route('/home')
def home():
  return "<h1>Welcome</h1>"

app.run()
