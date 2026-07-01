# pip install tiktoken
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

SAMPLE_PROMPT = """
You are a GreenCart FAQ assistant.
Answer ONLY from the context below.

=== CONTEXT START ===
Refunds are processed within 7 business days for eligible orders.
=== CONTEXT END ===

Question: What is the refund timeline?
"""

FULL_HISTORY = [
    {"role": "user", "content": "Use only GreenCart policy FAQ facts."},
    {"role": "assistant", "content": "Understood — grounded answers only."},
    {"role": "user", "content": "What is standard shipping time?"},
    {"role": "assistant", "content": "5-7 days in metro cities per FAQ."},
    {"role": "user", "content": "And refund timeline?"},
    {"role": "assistant", "content": "7 business days for eligible orders."},
    {"role": "user", "content": "What about warranty on electronics?"},
]

MAX_MESSAGES = 4


# TODO 1 — Write count_tokens(text) using encoding.encode(text)
def count_tokens(text: str) -> int:
    return len(encoding.encode(text))


# TODO 2 — Return (kept, dropped). If history fits, dropped = [].
#          kept = last max_messages items; dropped = everything before that.
def windowed_history(history: list, max_messages: int) -> tuple[list, list]:
    if len(history)<=max_messages:
        return history
    dropped= history[:-max_messages]
    kept= history[-max_messages:]

    return (kept,dropped)


def main():
    word_count = len(SAMPLE_PROMPT.split())
    token_count = count_tokens(SAMPLE_PROMPT)

    print("=== Token check ===")
    print("Word count:", word_count)
    print("Token count:", token_count)

    kept, dropped = windowed_history(FULL_HISTORY, MAX_MESSAGES)

    print("\n=== Windowed history (max 4 messages) ===")
    print("Messages sent to model:", len(kept))
    print("Messages dropped:", len(dropped))
    if dropped:
        print("First dropped message:", dropped[0]["content"])


if __name__ == "__main__":
    main()
