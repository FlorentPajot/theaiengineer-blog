from app import APP


@APP.route('/')
@APP.route('/index')
def index():
    return "This is my blog"
