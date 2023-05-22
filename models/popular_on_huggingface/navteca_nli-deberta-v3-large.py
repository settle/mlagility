# labels: test_group::monthly author::navteca name::nli-deberta-v3-large downloads::218 license::apache-2.0 task::Natural_Language_Processing sub_task::Zero-Shot_Classification
from sentence_transformers import CrossEncoder
model = CrossEncoder('cross-encoder/nli-deberta-v3-large')
scores = model.predict([('A man is eating pizza', 'A man eats something'), ('A black race car starts up in front of a crowd of people.', 'A man is driving down a lonely road.')])

#Convert scores to labels
label_mapping = ['contradiction', 'entailment', 'neutral']
labels = [label_mapping[score_max] for score_max in scores.argmax(axis=1)]
