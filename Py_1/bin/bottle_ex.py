import bottle

app = bottle.Bottle()


@app.route('/')
def index():
    return 'Welcome Page'


@app.route('/Hello')
def hellopage():
    return 'Hello Page'


@app.route('/abc/<name>')
def namepage(name):
    return 'Hello' + name


@app.route('/login')
def login():
    s = ''' <form action='/login1' method='post'>user: <input type='text' name='uname'/>
            <input type='Submit' value='submit'/> </form>'''
    return s


@app.post('/login1')
def login1():
    user = bottle.request.forms.get('uname')
    return 'Hello' + user


app.run()
