import os.path

from flask import Flask
from flask import redirect
from flask import url_for
from flask_debugtoolbar import DebugToolbarExtension

from browse import urls as browse_urls
from home import urls as home_urls
import models
from settingslocal import DEBUG_MODE
from settingslocal import RELOADER_BOOL
from upload import urls as upload_urls

app = Flask(__name__)
app.debug = DEBUG_MODE
app.config.from_pyfile('settingslocal.py')
toolbar = DebugToolbarExtension(app)

@app.route("/")
#@login_required
def sandbox():
    return redirect(url_for('home'))

browse_urls.setup_urls(app)
home_urls.setup_urls(app)
upload_urls.setup_urls(app)
models.db.init_app(app)

# Initialize sqlite db if necessary (for dev)
with app.test_request_context():
    if not os.path.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
        models.db.create_all()

if __name__ == "__main__":
    app.run(use_reloader=RELOADER_BOOL)
