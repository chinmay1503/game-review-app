from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Form(MethodView):
    def get(self):
        return render_template('form.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to review when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['gameName'], request.form['genre'], request.form['image_url'], request.form['author'], request.form['review_title'], request.form['review_message'], request.form['overall_score'])
        return redirect(url_for('review'))
