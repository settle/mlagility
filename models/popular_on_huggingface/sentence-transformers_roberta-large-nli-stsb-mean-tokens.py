# labels: test_group::monthly author::sentence-transformers name::roberta-large-nli-stsb-mean-tokens downloads::7,488 license::apache-2.0 task::Natural_Language_Processing sub_task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/roberta-large-nli-stsb-mean-tokens')
embeddings = model.encode(sentences)
print(embeddings)
