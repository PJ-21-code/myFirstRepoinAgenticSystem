import os
import shutil
from pprint import pprint
import chromadb
from sentence_transformers import SentenceTransformer

def main():
    # Clean up any existing store from previous runs to ensure a clean slate
    if os.path.exists("./chroma_store"):
        shutil.rmtree("./chroma_store")

   
    client = chromadb.PersistentClient(path="./chroma_store")
    
   
    collection = client.get_or_create_collection(
        name="support_knowledge_base", 
        embedding_function=None
    )

    knowledge_base = [
        {"id": "doc1", "text": "Customers can return products within 30 days of delivery.", "metadata": {"category": "returns"}},
        {"id": "doc2", "text": "Refunds are processed within 5 to 7 business days after the return is approved.", "metadata": {"category": "returns"}},
        {"id": "doc3", "text": "Orders above 499 rupees qualify for free shipping.", "metadata": {"category": "shipping"}},
        {"id": "doc4", "text": "You can reset your password from the account settings page.", "metadata": {"category": "account"}},
        {"id": "doc5", "text": "Express delivery orders usually arrive within 24 to 48 hours.", "metadata": {"category": "shipping"}}
    ]

    
    model = SentenceTransformer("all-MiniLM-L6-v2")

    ids = [item["id"] for item in knowledge_base]
    documents = [item["text"] for item in knowledge_base]
    metadatas = [item["metadata"] for item in knowledge_base]
    
    # Generate embeddings and convert the resulting numpy array to a list
    document_embeddings = model.encode(documents).tolist()

  
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=document_embeddings
    )

    print("=== Collection Verification ===")
    print(f"Collection Name: {collection.name}")
    print(f"Collection Count: {collection.count()}\n")

    print("--- Peek Result ---")
    pprint(collection.peek(limit=2))
    print("\n--- Get doc4 Result ---")
    
    pprint(collection.get(ids=["doc4"]))
    print("\n" + "="*40 + "\n")

   
    queries = [
        {"text": "I want to return my shoes and get my money back", "n_results": 3},
        {"text": "How do I change my login password?", "n_results": 2},
        {"text": "Can I pay with UPI?", "n_results": 3}
    ]

    for i, q_info in enumerate(queries, 1):
        query_text = q_info["text"]
        n_res = q_info["n_results"]
        
        # Encode the user query using the same model
        query_embedding = model.encode(query_text).tolist()
        
        # Perform top-k semantic search
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_res
        )
        
        print(f"### Query {i}: '{query_text}' (n_results={n_res})")
        
        # Safely parse and display the results matrix
        for rank in range(len(results["ids"][0])):
            r_id = results["ids"][0][rank]
            r_doc = results["documents"][0][rank]
            r_meta = results["metadatas"][0][rank]
            r_dist = results["distances"][0][rank] if results["distances"] else "N/A"
            
            print(f"  Rank {rank + 1}:")
            print(f"    ID: {r_id}")
            print(f"    Document: {r_doc}")
            print(f"    Metadata: {r_meta}")
            print(f"    Distance: {r_dist:.4f}" if isinstance(r_dist, float) else f"    Distance: {r_dist}")
        print()

       
        if i == 3:
            # Capture top match details dynamically for the analysis
            top_id = results["ids"][0][0]
            top_category = results["metadatas"][0][0]["category"]
            
            print("--- Gap analysis ---")
            print(f"The document that ranked first is {top_id}, which belongs to the '{top_category}' category.")
            print(f"Even though {top_id} is mathematically the closest vector in this tiny store, it represents a weak business answer because the query is about payment methods (UPI), and our knowledge base currently contains zero information regarding payments or billing.")
            print()

if __name__ == "__main__":
    main()