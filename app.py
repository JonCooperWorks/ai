import threading

from flask import Flask, render_template

import questions


app = Flask(__name__)

# Set up PyHamlJinja
app.jinja_env.add_extension('pyhaml_jinja.HamlExtension')

# HACK WARNING:
# We use this object to talk between the threads and this.
diagnosis = None


def get_diagnosis(symptoms):
  t = threading.Thread(target=diagnose_condition, args=(symptoms))
  t.start()
  t.join()
  return diagnosis


def diagnose_condition(*symptoms):
  """Prevents the segfault from bringing the entire process down.

  This function *MUST* be run in a background thread.

  For example:

    symptoms = ['fever', 'swollenglands']
    t = threading.Thread(target=diagnose_condition, args=(symptoms))
    t.start()
    t.join()
    print diagnosis
    >>> 'mumps'
  """

  global diagnosis
  from doctor import Doctor

  d = Doctor('medical.pl')
  diagnosis = d.diagnose(symptoms)
  return


@app.route('/')
def home():
  return render_template('home.haml', questions=questions)


if __name__ == '__main__':
  app.run(port=8004, debug=True)
