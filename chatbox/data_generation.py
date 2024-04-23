import random

# Symptoms
symptoms = [
    "itching", "redness", "discharge", "blurred_vision", "tearing",
    "pain", "foreign_body_sensation", "dryness", "itchiness", "burning",
    "sensitivity_to_light", "blurred_and_distorted_vision", "yellowing_of_eyes",
    "visual_disturbances", "high_fever", "headache", "redness_of_eyes",
    "watery_eyes", "dryness_of_eyes", "burning_sensation_in_eyes",
    "swelling_around_eyes", "eye_pain", "sensitivity_to_light", "eye_alignment_issues",
    "double_vision", "squinting", "reduced_vision_in_one_eye", "lazy_eye",
    "blurry_vision_in_one_eye", "blurred_or_distorted_vision", "eye_strain",
    "headaches", "difficulty_focusing_on_close_objects", "blurred_vision_at_normal_reading_distance",
    "eye_strain_when_reading", "difficulty_seeing_in_low_light_conditions",
    "poor_vision_at_night", "impaired_dark_adaptation", "flashing_lights_or_zigzag_patterns",
    "temporary_blindness_in_one_eye", "progressive_vision_loss", "night_blindness",
    "tunnel_vision", "redness_and_blurring_of_vision", "sudden_vision_loss_or_changes",
    "eye_pain_that_worsens_with_eye_movement", "blurred_vision_or_loss_of_color_vision",
    "involuntary_spasms_of_eyelid_muscles", "eye_irritation_and_discomfort",
    "increased_stress_or_fatigue"
]

# Eye diseases
eye_diseases = [
    "Cataracts", "Glaucoma", "Macular degeneration", "Diabetic retinopathy",
    "Retinal detachment", "Conjunctivitis", "Dry eye syndrome", "Blepharitis",
    "Keratitis", "Strabismus", "Amblyopia", "Astigmatism", "Presbyopia",
    "Night blindness", "Ocular migraines", "Retinitis pigmentosa",
    "Uveitis", "Optic neuritis", "Corneal abrasion", "Eyelid twitching"
]

# Generate dataset
dataset = []

for _ in range(4000):
    symptoms_present = [random.randint(0, 1) for _ in range(len(symptoms))]
    disease_index = random.randint(0, len(eye_diseases) - 1)
    disease_name = eye_diseases[disease_index]
    dataset.append(symptoms_present + [disease_name])

# Write dataset to file
with open("eye_disease_dataset.csv", "w") as f:
    # Write header
    f.write(",".join(symptoms + ["prognosis"]) + "\n")
    # Write data
    for entry in dataset:
        f.write(",".join(str(symptom) for symptom in entry) + "\n")

print("Dataset generated successfully!")
