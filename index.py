from flask import redirect, url_for, render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        reviews = [dict(review_id = row[0], name = row[1], genre = row[2], image_url = row[3], author = row[4],  review_date = row[5],
                    review_title = row[6], review_message = row[7]) for row in model.select()]
        return render_template('index.html',reviews=reviews)
