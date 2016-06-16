from flask import render_template
from app import app, db

#-------------------------------------------------------------------------------

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Disk Detective SED Home')

#-------------------------------------------------------------------------------

@app.route('/data')
def data():

    results = db.engine.execute("""SELECT * FROM sed LIMIT 20;""")

    keys = results.keys()
    rows = [row for row in results]

    return render_template('data.html', title='Disk Detective SED Data', keys=keys, rows=rows)

#-------------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(error):
    """Redirects any nonexistent URL to 404 page.

    Parameters:
        None

    Returns:
        /404.html : template

    Outputs:
        nothing
    """
    return render_template('/404.html'), 404

#-------------------------------------------------------------------------------
