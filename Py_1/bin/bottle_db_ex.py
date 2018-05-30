import bottle

app = bottle.Bottle()

'''
@app.route('/')
def index():
    return 'Welcome Page'


@app.route('/Hello')
def hellopage():
    return 'Hello Page'


@app.route('/abc/<name>')
def namepage(name):
    return 'Hello' + name

'''
@app.route('/query')
def query():
    s = ''' <form action='/query1' method='post'>Query: <input type='text' name='qname'/>
            <input type='Submit' value='submit'/> </form>'''
    return s


@app.post('/query1')
def query1():
    query = bottle.request.forms.get('qname')
    import sqlite3
    con = sqlite3.connect('mydb')
    cur = con.cursor()
    cur.execute(query)
    r = cur.fetchall()
    s = '<table border=10>'
    for i,j,k,l in r:
        s = s+'<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i,j,k,l)
    s = s+'</table>'
    return s


app.run()