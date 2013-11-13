
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
    symptom(Patient,fever), symptom(Patient,cough),
    symptom(Patient,conjunctive), symptom(Patient,runnynose),
    symptom(Patient,rash).

hypothesis(Patient,germanmeasles):-
    symptom(Patient,fever), symptom(Patient,headache),
    symptom(Patient,runnynose),symptom(Patient,rash).

hypothesis(Patient,flu) :-
    symptom(Patient,fever), symptom(Patient,headache),
    symptom(Patient,bodyache), symptom(Patient,chills),
    symptom(Patient,sorethrought), symptom(Patient,cough),
    symptom(Patient,conjunctive), symptom(Patient,conjunctive),
    symptom(Patient,runnynose).

hypothesis(Patient,commoncold) :-
    symptom(Patient,headache), symptom(Patient,runnynose),
    symptom(Patient,snuzing), symptom(Patient,chills),
    symptom(Patient,sorethrought).

hypothesis(Patient,mumps) :-
    symptom(Patient,fever), symptom(Patient,swallenglands).

hypothesis(Patient,chikenpox) :-
    symptom(Patient,fever), symptom(Patient,rash),
    symptom(Patient,bodyache).

hypothesis(Patient,whooping-cough) :-
    symptom(Patient,runnynose), symptom(Patient,snuzing),
    symptom(Patient,cough).
