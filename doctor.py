from pyswip.prolog import Prolog


class Doctor(object):
  """A Python adapter to the prolog medical system."""

  def __init__(self, prolog_file):
    self.prolog_file = prolog_file

  def __repr__(self):
    return 'Doctor("%s")' % self.prolog_file

  def diagnose(self, symptoms, age_group=None):
    """Returns a list of possible diagnosis, if any, given a list of symptoms.

    For example, if german measles has the symptoms 'runny nose', 'fever',
    'headache' and 'rash', the system will return a list containing a dict with
    the diagnosis.

      symptoms = ['runnynose', 'fever', 'headache', 'rash']
      doctor = Doctor('medical')
      results = doctor.diagnose(symptoms)

      results
      >>> [{'Diagnosis': 'germanmeasles'}]

    The diagnosis can be accessed with the key 'Diagnosis'.
    NOTE: The capital D is important.

      diagnosis = results[0]
      diagnosis['Diagnosis']
      >>> 'germanmeasles'
    """

    prolog = Prolog()

    if age_group is None:
      age_group = 'none'

    patient = 'patient'
    self._query_and_log(prolog.assertz, 'age_group(%s,%s)' % (patient, age_group))
    for symptom in symptoms:
      self._query_and_log(prolog.assertz, 'symptom(%s,%s)' % (patient, symptom))

    prolog.consult(self.prolog_file)
    return list(self._query_and_log(prolog.query, 'hypothesis(%s,Diagnosis)' % patient))

  def diagnose_one(self, symptoms, age_group=None):
    """Convenience wrapper around diagnose that returns only one result.
    If no results are found, this returns None."""

    try:
      return self.diagnose(symptoms, age_group=age_group)[0]

    except IndexError:
      return None

  def _query_and_log(self, fn, query):
    with open('patient.pl', 'w') as f:
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

  d = Doctor('medical.pl')

  mumps_symptoms = ['fever', 'swollenglands']
  diagnosis = d.diagnose_one(mumps_symptoms)
  fail_unless(diagnosis['Diagnosis'] == 'mumps', 'mumps', diagnosis)

  chickenpox_symptoms = ['fever', 'rash', 'bodyache']
  diagnosis = d.diagnose_one(chickenpox_symptoms)
  fail_unless(diagnosis['Diagnosis'] == 'chickenpox', 'chickenpox', diagnosis)

  adult_symptoms = ['headache', 'sleepiness', 'poorcoordination',
                    'impairedvision', 'nobladdercontrol', 'memoryloss',
                    'difficultywalking']

  diagnosis = d.diagnose_one(adult_symptoms, age_group='adult')
  fail_unless(
      diagnosis['Diagnosis'] == 'adulthydrocephalus',
      'adulthydrocephalus',
      diagnosis)

  child_symptoms = ['sunseteyes', 'seizures', 'sleepiness', 'vomiting',
                    'largehead', 'softspot', 'poorcoordination',
                    'impairedvision']

  diagnosis = d.diagnose_one(child_symptoms, age_group='child')
  fail_unless(
      diagnosis['Diagnosis'] == 'childhydrocephalus',
      'childhydrocephalus',
      diagnosis)
