from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Update(MethodView):
    def get(self):
        return render_template('update.html')

    def get(self, id):
        model = gbmodel.get_model()
        row = model.selectById(id)
        review = dict(review_id = row[0], gameName = row[1], genre = row[2], image_url = row[3], author = row[4],  review_date = row[5],
                    review_title = row[6], review_message = row[7], overall_score = row[8])
        return render_template('update.html', review=review)

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.update(request.form['review_id'], request.form['gameName'], request.form['genre'], request.form['image_url'], request.form['author'], request.form['review_title'], request.form['review_message'], request.form['overall_score'])
        return redirect(url_for('review'))
