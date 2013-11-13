from flask import Flask, render_template

from doctor import Doctor

app = Flask(__name__)
doctor = Doctor('medical.pl')

# Set up PyHamlJinja
app.jinja_env.add_extension('pyhaml_jinja.HamlExtension')


@app.route('/')
def home():
  return render_template('home.haml')


if __name__ == '__main__':
  app.run(port=8004, debug=True)
