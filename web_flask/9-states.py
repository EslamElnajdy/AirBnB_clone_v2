#!/usr/bin/python3
""" start a flask web application """


from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_route(state_id=None):
    states = storage.all("state")
    if state_id is not None:
        state_id = 'state.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
