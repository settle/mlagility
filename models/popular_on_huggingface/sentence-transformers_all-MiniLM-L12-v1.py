# labels: test_group::monthly author::sentence-transformers name::all-MiniLM-L12-v1 downloads::2,594 license::apache-2.0 task::Natural_Language_Processing sub_task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v1')
embeddings = model.encode(sentences)
print(embeddings)
