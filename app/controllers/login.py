
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
                return redirect(url_for('login.login', registered=True, username=username))
        
        #GET
        else:
            return render_template('register.html')


    def login():
        
        if session.get('user'):
            return redirect(url_for('home.index'))
        
        #POST
        if request.method == 'POST':
            
            username = request.form.get('username')
            password = request.form.get('password')
            remember = request.form.get('remember')

            if not len(username) or not len(password):
                context = dict(
                    error = 'All fields must be filled.'
                )
                return render_template('login.html', **context)
            
            if User.validate_login(username, password):
                session['user'] = username

                if remember:
                    session.permanent = True
                else:
                    session.permanent = False

                return redirect(url_for('home.index'))
            
            else:
                context = dict(
                    error = 'Invalid username or password.'
                )
                return render_template('login.html', **context)
        
        #GET
        else:
            context = dict(
                registered = request.args.get('registered'),
                username = request.args.get('username'),
            )
            return render_template('login.html', **context)


    def logout():
        
        if session.get('user'):
            session.clear()
        
        return redirect(url_for('home.index'))
