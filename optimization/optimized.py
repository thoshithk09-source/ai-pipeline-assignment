from token_counter import count_tokens

# Optimization 1:
# Use a much shorter shared system prompt instead of repeating a huge one.
SYSTEM_PROMPT = """
You are an advanced AI assistant.
Answer accurately and concisely.
"""

# Retriever still sees the full document.
DOCUMENT = """
Artificial Intelligence is transforming healthcare, education,
finance, transportation, cybersecurity, manufacturing,
retail, and many other industries.
""" * 600

# Optimization 2:
# Trim conversation history before passing it to later agents.
FULL_HISTORY = """
User: Tell me about AI.
Assistant: AI is the simulation of human intelligence...
""" * 250

TRIMMED_HISTORY = """
User: Tell me about AI.
Assistant: AI is the simulation of human intelligence...
""" * 40


def run_pipeline(query):
    agents = [
        "Retriever",
        "Research Agent",
        "Analysis Agent",
        "Writer Agent",
    ]

    total_tokens = 0

    for agent in agents:

        # Retriever needs the complete context.
        if agent == "Retriever":
            prompt = (
                SYSTEM_PROMPT
                + DOCUMENT
                + FULL_HISTORY
                + query
            )

        # Later agents only receive summarized history.
        else:
            prompt = (
                SYSTEM_PROMPT
                + DOCUMENT
                + TRIMMED_HISTORY
                + query
            )

        tokens = count_tokens(prompt)

        print(f"{agent}: {tokens} tokens")
        total_tokens += tokens

    print("-" * 40)
    print(f"TOTAL TOKENS: {total_tokens}")


if __name__ == "__main__":
    run_pipeline("Explain how AI is changing healthcare.")