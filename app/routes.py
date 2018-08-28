from app import APP

@APP.route('/')
@APP.route('/index')

def index():
    return "Hello, World!"
