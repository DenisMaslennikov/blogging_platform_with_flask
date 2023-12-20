from core.app import get_app
from core.config import DebugConfig

app = get_app(DebugConfig)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        use_reloader=True,
        passthrough_errors=True,
        debug=True
    )
