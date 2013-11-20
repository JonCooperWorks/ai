hypothesis(patient, infanthydrocephalus) :-
    age_group(patient, infant),
    symptom(patient, sunseteyes), symptom(patient, seizures),
    symptom(patient, sleepiness), symptom(patient, vomiting),
    symptom(patient, largehead), symptom(patient, softspot).

hypothesis(patient, childhydrocephalus) :-
    age_group(patient, child),
    symptom(patient, sunseteyes), symptom(patient, seizures),
    symptom(patient, sleepiness), symptom(patient, vomiting),
    symptom(patient, largehead), symptom(patient, softspot),
    symptom(patient, poorcoordination), symptom(patient, impairedvision).

hypothesis(patient, adulthydrocephalus) :-
    age_group(patient, adult),
    symptom(patient, headache), symptom(patient, sleepiness),
    symptom(patient, poorcoordination), symptom(patient, nobladdercontrol),
    symptom(patient, impairedvision), symptom(patient, memoryloss).

hypothesis(patient, oldadulthydrocephalus) :-
    age_group(patient, oldadult),
    symptom(patient, nobladdercontrol), symptom(patient, memoryloss),
    symptom(patient, diffcultywalking), symptom(patient, poorcoordination).

hypothesis(patient,measles) :-
    symptom(patient,fever), symptom(patient,cough),
    symptom(patient,runnynose),
    symptom(patient,rash).

hypothesis(patient,germanmeasles):-
    symptom(patient,fever), symptom(patient,headache),
    symptom(patient,runnynose),symptom(patient,rash).

hypothesis(patient,flu) :-
    symptom(patient,fever), symptom(patient,headache),
    symptom(patient,bodyache), symptom(patient,chills),
    symptom(patient,sorethroat), symptom(patient,cough),
    symptom(patient,runnynose).

hypothesis(patient,commoncold) :-
    symptom(patient,headache), symptom(patient,runnynose),
    symptom(patient,sneezing), symptom(patient,chills),
    symptom(patient,sorethroat).

hypothesis(patient,mumps) :-
    symptom(patient,fever), symptom(patient,swollenglands).

hypothesis(patient,chikenpox) :-
    symptom(patient,fever), symptom(patient,rash),
    symptom(patient,bodyache).

hypothesis(patient,whooping-cough) :-
    symptom(patient,runnynose), symptom(patient,sneezing),
    symptom(patient,cough).
