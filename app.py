"""
A simple game review flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from form import Form
from review import Review
from delete import Delete
from update import Update

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])  

app.add_url_rule('/review',
                 view_func=Review.as_view('review'),
                 methods=['GET'])

app.add_url_rule('/form',
                 view_func=Form.as_view('form'),
                 methods=['GET', 'POST'])

app.add_url_rule('/update/<id>',
                 view_func=Update.as_view('updateApi'),
                 methods=['GET'])

app.add_url_rule('/update',
                 view_func=Update.as_view('update'),
                 methods=['GET', 'POST'])

app.add_url_rule('/delete/<id>',
                 view_func=Delete.as_view('delete'),
                 methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
