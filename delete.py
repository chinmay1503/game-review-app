from flask import redirect, url_for, render_template
from flask.views import MethodView
import gbmodel

class Delete(MethodView):

    def get(self, id):
        """
        Accepts DELETE request;
        Redirect to reviews when completed.
        """
        model = gbmodel.get_model()
        model.delete(id)
        return redirect(url_for('review'))
