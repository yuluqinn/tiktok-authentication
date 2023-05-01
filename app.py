from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'aw39m1bipscqi2i8'

oauth = OAuth(app)

tiktok = oauth.register(
    'tiktok',
    client_id='7227640142437140486',
    client_secret='9503e982118d3439d6c994cc45620fbb',
    access_token_url='https://open-api.tiktok.com/platform/oauth/connect/token/',
    authorize_url='https://open-api.tiktok.com/platform/oauth/connect/',
    api_base_url='https://open-api.tiktok.com/',
    client_kwargs={'scope': 'user.info.basic'},
)

@app.route('/')
def home():
    # return "Hello from flask"
    return render_template('home.html')

@app.route('/login')
def login():
    print("login")
    redirect_uri = url_for('authorize', _external=True)
    return tiktok.authorize_redirect(redirect_uri)

@app.route('/auth')
def authorize():
    url = 'https://www.tiktok.com/auth/authorize/'
    csrfState = "200"
    url += '?client_key=aw39m1bipscqi2i8'
    url += '&scope=user.info.basic'
    url += '&response_type=code'
    url += '&redirect_uri=https://www.example.com/login'
    url += '&state=' + csrfState
    print(url)
    return redirect(url)

@app.route('/profile')
def profile():
    return render_template('profile.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
