from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('blog.html')


@app.route('/home')
def home():
    return render_template('page.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact_form',methods=['GET','POST'])
def contact_form():
    print(request.form['name'])

app.run()
