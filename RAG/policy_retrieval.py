chunks = [
    {
        "text": "Mobiles can be returned within 7 days if damaged.",
        "metadata": {
            "doc_type": "policy",
            "product": "mobile",
            "status": "active",
            "source_file": "mobile_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops can be returned within 10 days for manufacturing defects.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops were earlier returnable within 30 days.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "archived",
            "source_file": "old_laptop_policy.md",
            "section_title": "Old Return Rules",
        },
    },
    {
        "text": "For laptop battery drain, run diagnostics mode before replacing parts.",
        "metadata": {
            "doc_type": "manual",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_service_manual.pdf",
            "section_title": "Battery Diagnostics",
        },
    },
    {
        "text": "Premium users get billing support within 24 hours.",
        "metadata": {
            "doc_type": "policy",
            "product": "billing",
            "status": "active",
            "source_file": "billing_policy.md",
            "section_title": "Premium Support",
        },
    },
]

filters=[{"doc_type": "policy", "product": "laptop", "status": "active"},
         {"doc_type": "policy", "product": "mobile", "status": "active"},
         {"doc_type": "manual", "product": "laptop", "status": "active"}]

def matches_filters(metadata: dict, filter: dict) -> bool:
       for key, value in filter.items():
          val= metadata.get(key)

          if val!= value:
             return False
        
       return True

def retrieve(filter: dict) -> list:
    retrieved=[]

    for chunk in chunks:
        if matches_filters(chunk['metadata'],filter):
            retrieved.append(chunk)

    return retrieved

def format_citation(chunk: dict) -> str:

    return f"Source: {chunk['metadata']['source_file']} - {chunk['metadata']['section_title']}"

def main():
    for filter in filters:
       retrieved_chunks= retrieve(filter)
       for chunk in retrieved_chunks:
          print(chunk['text'])
          print(format_citation(chunk)) 
          print("\n")

if __name__ == "__main__":
    main()                    