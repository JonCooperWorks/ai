import glob

from pyswip.prolog import Prolog


class Nurse(object):
  """The Nurse."""

  def __init__(self, prolog_file):
    self.prolog_files = glob.glob('*.pl')
    self.prolog_files.remove('medical.pl')

  def __repr__(self):
    return 'Nurse("%s")' % self.prolog_file

  def partial_diagnosis(self, symptoms):

    prolog = Prolog()

    for file in self.prolog_files:
      prolog.consult(file)

    differntial_diagnosis = []

    for symptom in symptoms:
      for result in prolog.query('hasSymptom(Illness, %s)' % symptom):
        differntial_diagnosis.append(result['Illness'])

    sick_list = []
    sick_list = list(set(differntial_diagnosis))

    return sick_list

  def _query_and_log(self, fn, query):
    with open('diagnosis.log', 'a') as f:
      rv = fn(query)
      f.write(query + '\n')
    return rv

if __name__ == '__main__':
  """If we're running this directly, run the 'unit tests'."""

  def fail_unless(test, expected, got):
    try:
      assert test
      print 'PASS'

    except AssertionError:
      print 'FAIL: Expected %s, got %s' % (expected, got)

    n = Nurse('symptoms.pl')

    # ye coop, write this lol
