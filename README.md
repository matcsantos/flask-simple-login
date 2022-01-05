<h1 align="center">🔐 Flask Simple Login</h1>
<p align="center">A simple login system written in pure Flask. No extensions needed.</p>

<p align="center">
  <img src="https://img.shields.io/badge/-Python-232529?style=flat&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/-Flask-232529?style=flat&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/-SQLite-232529?style=flat&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/-HTML5-232529?style=flat&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/-CSS3-232529?style=flat&logo=css3&logoColor=white">
</p>

<h2>🎥 Demonstration</h2>

https://user-images.githubusercontent.com/71465661/148295107-681e9c60-9597-4c57-9aef-8185e3c778f6.mp4

<h2>📌 Objective</h2>

My objective with this project was to create a login system without using extensions like flask-login, to solidify my knowledge on the base framework.

<h2>⭐ Features</h2>

- Secure password storage using SHA-256 hashing algorithm.
- Modern Flask patterns such as Blueprints and Application Factories, making the project easily extendable.
- Support to either permanent or temporary sessions.
- Custom MVC architecture, delegating database and validation duties to Models.
- Reduced database queries using validation-first concept.

<h2>🚀 Running this project</h2>

<p>Clone this repository using git clone</p>
<code>git clone https://github.com/matcsantos/flask-simple-login.git</code>

<ul>
  <li>
    <h3>Using Docker</h3>
    <p>Create an image using the .Dockerfile in the root directory of this repository</p>
    <code>docker build -t flask-simple-login .</code>
    <p>Run the image you just created in a new container</p>
    <code>docker run -d -p 5000:5000 flask-simple-login</code>
  </li>
  <hr>
  <li>
    <h3>Using a virtual environment</h3>
    <p>Create a virtual environment in the root directory</p>
    <code>python3 -m venv venv</code>
    <p>Activate the virtual environment</p>
    <code>./venv/Scripts/activate</code>
    <p>Install dependencies using the requirements.txt file</p>
    <code>pip install -r requirements.txt</code>
    <p>Navigate to the app folder</p>
    <code>cd ./app</code>
    <p>Finally, run the application</p>
    <code>flask run</code>
  </li>
</ul>

<h3>Testing</h3>
<p>If you got the application up and running without errors, navigate to <code>http://127.0.0.1:5000/</code> to test it.</p>

<h2>📃 Information</h2>

This project was originally created in January 2021, i'm currently reuploading it with a demonstration video to be part of my porfolio as a web developer.</br>
