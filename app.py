import threading

from flask import Flask, render_template, request

import questions


app = Flask(__name__)

# Set up PyHamlJinja
app.jinja_env.add_extension('pyhaml_jinja.HamlExtension')

# HACK WARNING:
# We use this object to talk between the threads and this.
diagnosis = None
lock = object()


def diagnose_condition(*symptoms):
  """Prevents the segfault from bringing the entire process down.

  This function *MUST* be run in a background thread.

  For example:

    symptoms = ['fever', 'swollenglands']
    t = threading.Thread(target=diagnose_condition, args=(symptoms))
    t.start()
    wait_for_value(diagnosis)
    do_other_stuff()
    >>> 'mumps'
  """

  global diagnosis
  diagnosis = lock
  from doctor import Doctor

  d = Doctor('medical.pl')
  diagnosis = d.diagnose(symptoms)
  return


def wait_for_value(obj):
  # Busy wait until object is ready.
  while obj == lock:
    pass


@app.route('/')
def home():
  return render_template('home.haml')

@app.route('/question/')
def question():
  return render_template('question.haml',questions=questions,
                         names=filter(lambda x: not x.startswith('__'), dir(questions)))

@app.route('/question/hypothesis', methods=['GET', 'POST'])
def hypothesis():
  if request.method == 'POST':
    selected = request.form['selected']
    hypothesis = diagnose_condition(selected)

    return render_template('advice.haml', hypothesis=hypothesis)


@app.route('/admin/diseases', methods=['GET', 'POST'])
def add_disease():
  if request.method == 'POST':
    disease_name = request.form['disease']
    symptoms = request.form.getlist('symptoms[]')
    filename = '%s.pl' % disease_name

    facts = []
    for symptom in symptoms:
      fact = 'symptom(patient, %s).' % symptom
      facts.append(fact)

    facts = ''.join(facts)

    entry = '''
hypothesis(patient, {disease}) :-
age_group(patient, none).
{facts}
    '''.format(disease=disease_name, facts=facts)

    with open(filename, 'w') as f:
      f.write(entry)

  return render_template('admin.haml')


if __name__ == '__main__':
  app.run(port=8004, debug=True)
