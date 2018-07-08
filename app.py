from bottle import route, run, error, abort, static_file
import sys
import os

sys.argv.reverse()
sys.argv.pop()

@route('/')
def index():
    print('heyhey')
    return '''
<!DOCTYPE html>
<html>
  <head><title>ins</title></haed>
  <body>
    <ul>{}</ul>
  </body>
</html>
'''.format(''.join(['<li><a href="/file/{0}">{0}</a></li>'.format(path) for path in sys.argv]))

@route('/file/<filepath:re:.*>')
def reserve(filepath):
    currentfilepath = './{}'.format(filepath)
    if filepath in sys.argv:
        pass
    elif currentfilepath in sys.argv:
        filepath = currentfilepath
    else:
        abort(404)

    if not os.path.exists(filepath):

        abort(404)

    basedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath)

    return static_file(filename, basedir, download=True)

@error(404)
def error404(error):
    return 'NotFound'

run(host='0.0.0.0', port=8080, debug=True)
