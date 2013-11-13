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

    if age_group is not None:
      prolog.assertz('age_group(patient,%s)' % age_group)

    for symptom in symptoms:
      prolog.assertz('symptom(patient,%s)' % symptom)

    prolog.consult(self.prolog_file)
    return list(prolog.query('hypothesis(patient,Diagnosis)'))

  def diagnose_one(self, symptoms, age_group=None):
    """Convenience wrapper around diagnose that returns only one result.
    If no results are found, this returns None."""

    try:
      return self.diagnose(symptoms, age_group=age_group)[0]

    except IndexError:
      return None


if __name__ == '__main__':
  """If we're running this directly, run the 'unit tests'.
  """

  adult_symptoms = ['headache', 'sleepiness', 'poorcoordination',
                    'impairedvision', 'nobladdercontrol', 'memoryloss',
                    'difficultywalking']

  d = Doctor('medical.pl')
  diagnosis = d.diagnose_one(adult_symptoms, age_group='adult')
  assert diagnosis['Diagnosis'] == 'adulthydrocephalus'
