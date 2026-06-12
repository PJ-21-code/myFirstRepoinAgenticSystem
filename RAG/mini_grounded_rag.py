CORPUS = [
    {
        "text": (
            "NovaTech Annual Report 2022 — Financial Highlights. "
            "Total revenue for fiscal year 2022 was 48.2 billion dollars, "
            "representing 19 percent year-over-year growth."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 12},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Operating Income. "
            "Operating income reached 6.1 billion dollars in 2022. "
            "Cloud services contributed the largest share of margin improvement."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 18},
    },
    {
        "text": (
            "NovaTech Annual Report 2023 — Outlook. "
            "Management expects continued investment in AI infrastructure through 2024. "
            "No weather or macro-forecast data is included in this document."
        ),
        "metadata": {"source_id": "novatech_2023.pdf", "page": 4},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Employee Count. "
            "NovaTech employed 124000 people worldwide at the end of 2022."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 31},
    },
]
import os
from groq import Groq
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

load_dotenv()
# --- Config ---
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_PATH = "./mini_report_lab"
GROQ_MODEL = "llama-3.3-70b-versatile"

SYSTEM_MESSAGE = """
You are an assistant for a financial services firm that answers user queries on annual reports.
User input will contain the context required to answer the question.
The context will begin with the token #context and contains portions of the source document.
The question will begin with the token #question.
Answer ONLY using the provided context.
If the answer is not found in the context, say: I don't know.
""".strip()


def retrieve_chunks(user_query, retriever):
    docs = retriever.invoke(user_query)
    return [
        {"index": i, "text": d.page_content, "metadata": d.metadata}
        for i, d in enumerate(docs, start=1)
    ]


def build_user_message(user_query, retrieved_chunks):
    context_text = "\n\n".join(c["text"] for c in retrieved_chunks)
    return f"#context\n{context_text}\n#question\n{user_query}"


def generate_answer(system_message, user_message):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def rag_answer(user_query, retriever):
    retrieved = retrieve_chunks(user_query, retriever)
    user_message = build_user_message(user_query, retrieved)
    answer = generate_answer(SYSTEM_MESSAGE, user_message)
    return {"answer": answer, "retrieved_chunks": retrieved, "user_message": user_message}


def main():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)
    documents= [Document(page_content=item['text'], metadata=item['metadata']) for item in CORPUS]
    vectorstore = Chroma.from_documents(documents=documents,embedding=embeddings,persist_directory=CHROMA_PATH)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )

    question = "What was NovaTech's total revenue in 2022?"
    print("Question:", question)

    result = rag_answer(question, retriever)

    print("\n--- Retrieved chunks ---")
    for chunk in result["retrieved_chunks"]:
        print(f"Chunk {chunk['index']}: {chunk['metadata']}")

    print("\n--- Generated answer ---")
    print(result["answer"])

    print("\n--- Grounding audit (you fill in) ---")
    print("List each fact in the answer and the chunk page that supports it.")


if __name__ == "__main__":
    main()
