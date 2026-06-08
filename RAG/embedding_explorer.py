from sentence_transformers import SentenceTransformer
model_name= "sentence-transformers/all-MiniLM-L6-v2"
model= SentenceTransformer(model_name)

sentences= [
    "How do I return a product?",
    "What is the refund policy?",
    "When is the Module 3 capstone viva?",
    "Refunds are processed within seven working days.",
]

embeddings= model.encode(sentences, convert_to_numpy=True).tolist()

for sentence,vector in zip(sentences,embeddings):
    print("Sentence: ",sentence)
    print("vector length: ", len(vector))
    print("Top 5 vectors: ", vector[ :5])