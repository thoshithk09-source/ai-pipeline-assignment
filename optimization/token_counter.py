import tiktoken

# Using GPT-4 tokenizer for realistic token estimation
encoding = tiktoken.encoding_for_model("gpt-4")


def count_tokens(text: str) -> int:
    """
    Count tokens in a string.
    """
    return len(encoding.encode(text))