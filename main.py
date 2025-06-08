from flask import *
from service import spread_sheet

app = Flask(__name__, static_folder='static', template_folder='templates')
api = spread_sheet(id='1-w-sizFV2i0BTeEd-PzQ9oQojd3A2Y_pvm2XJ4e35z8')

"""
    El archivo index.html y match.html no existen ahorita
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/App/match', methods=['GET','POST'])
def match():
    if request.form == 'POST':
        DATA = request.form.getlist('data[]')
        api.post([[DATA]], 2, 0)
        return redirect(url_for('match'))
    
    return render_template('match.html')