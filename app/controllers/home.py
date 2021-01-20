
from flask import render_template, session

class HomeController:

    def index():
        user = session.get('user')
        
        if user:
            context = dict(
                user = user,
                permanent = session.permanent
            )
            return render_template('user.html', **context)

        return render_template('index.html')
