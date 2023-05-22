# labels: test_group::monthly author::sentence-transformers name::sentence-t5-xl downloads::252 license::apache-2.0 task::Natural_Language_Processing sub_task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/sentence-t5-xl')
embeddings = model.encode(sentences)
print(embeddings)
