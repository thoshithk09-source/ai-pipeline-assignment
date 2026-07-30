from token_counter import count_tokens

SYSTEM_PROMPT = """
You are an advanced AI assistant.
Always answer professionally.
Provide detailed reasoning.
Use examples whenever possible.
Think step by step before answering.
""" * 80

DOCUMENT = """
Artificial Intelligence is transforming healthcare, education,
finance, transportation, cybersecurity, manufacturing,
retail, and many other industries.
""" * 600

CONVERSATION_HISTORY = """
User: Tell me about AI.
Assistant: AI is the simulation of human intelligence...
""" * 250


def run_pipeline(query):
    agents = [
        "Retriever",
        "Research Agent",
        "Analysis Agent",
        "Writer Agent"
    ]

    total_tokens = 0

    for agent in agents:
        prompt = (
            SYSTEM_PROMPT
            + DOCUMENT
            + CONVERSATION_HISTORY
            + query
        )

        tokens = count_tokens(prompt)

        print(f"{agent}: {tokens} tokens")

        total_tokens += tokens

    print("-" * 40)
    print(f"TOTAL TOKENS: {total_tokens}")


if __name__ == "__main__":
    run_pipeline("Explain how AI is changing healthcare.")