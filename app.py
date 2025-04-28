from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/Aboutme')
def Aboutme():
    return render_template('Aboutme.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/Project')
def Project():
    return render_template('Project.html')

if __name__ == '__main__':
    app.run(debug=True)
