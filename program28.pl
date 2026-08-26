symptom(fever, flu).
symptom(cough, cold).
symptom(headache, flu).
symptom(sneezing, cold).

diagnosis(Disease) :-
    symptom(fever, Disease),
    symptom(headache, Disease).