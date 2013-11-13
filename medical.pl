
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
