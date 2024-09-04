from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/templates')
def index():
    return render_template('base.html')

@app.route('/user/<username>')
def profile(username):
    return f'{username} profile'

if __name__=='__main__':
    app.run(debug=True)