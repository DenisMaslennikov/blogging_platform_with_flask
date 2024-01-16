from flask import send_from_directory
from flask_debugtoolbar import DebugToolbarExtension

from backend.core.app import get_app
from backend.core.config import DebugConfig

app = get_app(DebugConfig)

toolbar = DebugToolbarExtension(app)

# db.init_app(app)

@app.route('/uploads/<name>')
def download_file(name: str):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        use_reloader=True,
        passthrough_errors=True,
        debug=True
    )
