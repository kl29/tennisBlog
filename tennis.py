from flask import Flask, request, make_response, redirect, url_for, render_template, session

app = Flask(__name__, template_folder='.')
app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    html = render_template('home.html')
    response = make_response(html)
    return response

# @app.route('/poly', methods=['GET'])
# def home():
#     html = render_template('poly.html')
#     response = make_response(html)
#     return response

# @app.route('/hybrid', methods=['GET'])
# def home():
#     html = render_template('hybrid.html')
#     response = make_response(html)
#     return response

# @app.route('/multi', methods=['GET'])
# def home():
#     html = render_template('multi.html')
#     response = make_response(html)
#     return response

# @app.route('/overgrips', methods=['GET'])
# def home():
#     html = render_template('overgrips.html')
#     response = make_response(html)
#     return response

# @app.route('/strats', methods=['GET'])
# def home():
#     html = render_template('strats.html')
#     response = make_response(html)
#     return response

# @app.route('/st', methods=['GET'])
# def home():
#     html = render_template('st.html')
#     response = make_response(html)
#     return response

# @app.route('/about', methods=['GET'])
# def home():
#     html = render_template('about.html')
#     response = make_response(html)
#     return response