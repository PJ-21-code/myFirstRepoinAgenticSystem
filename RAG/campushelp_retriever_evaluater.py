# Mini corpus for retrieval evaluation
CORPUS = [
    {
        "doc_id": "D1",
        "title": "Attendance Policy",
        "text": (
            "Students must maintain at least 75% attendance. "
            "Below 75%, the student cannot sit for the end-term exam "
            "unless a medical certificate is approved by the dean."
        ),
    },
    {
        "doc_id": "D2",
        "title": "Late Submission Policy",
        "text": (
            "Assignments submitted up to 2 days late receive a 10% penalty per day. "
            "Submissions after 2 days are not accepted."
        ),
    },
    {
        "doc_id": "D3",
        "title": "Library Hours",
        "text": (
            "The main library is open Monday to Saturday from 8 AM to 10 PM. "
            "It is closed on Sundays and public holidays."
        ),
    },
    {
        "doc_id": "D4",
        "title": "Hostel Mess Refund",
        "text": (
            "Mess fees are refundable only if a student applies at least 7 days "
            "before leaving the hostel. Same-day refunds are not allowed."
        ),
    },
    {
        "doc_id": "D5",
        "title": "Wi-Fi Access",
        "text": (
            "Campus Wi-Fi is available to enrolled students using college email login. "
            "Guests need a temporary pass from the IT desk."
        ),
    },
]

EVAL_SET = [
    {"qid": "Q1", "question": "What is the minimum attendance required?", "expected_docs": ["D1"]},
    {"qid": "Q2", "question": "Can I submit an assignment 1 day late?", "expected_docs": ["D2"]},
    {"qid": "Q3", "question": "Is the library open on Sunday?", "expected_docs": ["D3"]},
    {"qid": "Q4", "question": "How do I get a mess fee refund?", "expected_docs": ["D4"]},
    {"qid": "Q5", "question": "Can a guest use campus Wi-Fi?", "expected_docs": ["D5"]},
    {"qid": "Q6", "question": "What is the hostel room rent?", "expected_docs": []},
]
import re
def tokenize(text: str):
    tokens= re.findall(r"\w+", text.lower())

    return tokens

def score_doc(query,doc_text):
    c=0
    query_token= set(tokenize(query))
    doc_token= set(tokenize(doc_text))
    c= len(query_token.intersection(doc_token))

    return c

def retrieve_top_k(query,corpus,k):
    scores=[]
    for cor in corpus:
        score= score_doc(query,cor['text'])
        scores.append((cor['doc_id'],score))

    scores.sort(key= lambda x:x[1], reverse=True)

    return [doc_id for doc_id,score in scores[:k]]

def is_hit(retrieved_doc_ids, expected_docs):
    
    if not expected_docs:
        return None

    return any(doc in retrieved_doc_ids for doc in expected_docs)


def retrieval_hit_rate(rows):

    valid = [row for row in rows if row["hit"] is not None]

    hits = sum(row["hit"] for row in valid)

    return hits / len(valid)      

def main():
    results = []

    for item in EVAL_SET:

        retrieved = retrieve_top_k(item["question"], CORPUS, k=3)

        hit = is_hit(retrieved, item["expected_docs"])

        results.append({
            "qid": item["qid"],
            "question": item["question"],
            "expected_docs": item["expected_docs"],
            "retrieved_docs": retrieved,
            "hit": hit
        })

        status = "N/A" if hit is None else ("Hit" if hit else "Miss")

        print(f"QID: {item['qid']}")
        print(f"Question: {item['question']}")
        print(f"Expected Docs: {item['expected_docs']}")
        print(f"Retrieved Docs: {retrieved}")
        print(f"Result: {status}")
        print("-"*50)

    hit_rate = retrieval_hit_rate(results)

    print(f"Overall Hit Rate: {hit_rate:.2f}")
    print(f"Percentage: {hit_rate*100:.2f}%")  


if __name__ == '__main__':
    main()

    




