
from models.user import User
from classes.errors import ValidationError
from flask import render_template, redirect, url_for, request, session

class LoginController:

    def register():
        
        if session.get('user'):
            return redirect(url_for('home.index'))
        
        #POST
        if request.method == 'POST':
            
            username = request.form.get('username')
            password = request.form.get('password')

            try:
                user = User(username, password)
            
            except ValidationError as error:
                context = dict(
                    error = error
                )
                return render_template('register.html', **context)

            if not user.register():
                context = dict(
                    error = 'Username already registered.'
                )
                return render_template('register.html', **context)
            
            else:
                return redirect(url_for('home.index'))
        
        #GET
        else:
            return render_template('register.html')
