from flask import Flask, render_template, redirect, url_for, request
from service import spread_sheet

app = Flask(__name__, static_folder='static', template_folder='templates')
api = spread_sheet(id='1-w-sizFV2i0BTeEd-PzQ9oQojd3A2Y_pvm2XJ4e35z8')

def page_error(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/App/match', methods=['GET','POST'])
def match():
    if request.form == 'POST':
        data = request.form.getlist('data[]')
        api.post([[data]], 2, 0)
        return redirect(url_for('match'))
    
    return render_template('match.html', data=api.get(2))

@app.route('/App/pits', methods=['GET','POST'])
def pits():
    if request.form == 'POST':
        data = request.form.getlist('data[]')
        api.post([[data]], 2, 1)
        return redirect(url_for('pits.html'))
    
    return render_template('pits.html', data=api.get(2))

if __name__ == '__main__':
    app.register_error_handler(404, page_error)
    app.run(host='localhost', debug=True, port=5000)