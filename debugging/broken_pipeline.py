import random
import time

def retriever(query):
    print("Retriever running...")
    time.sleep(1)
    return {"documents": ["AI improves healthcare", "AI assists doctors"]}


def researcher(data):
    print("Research Agent running...")

    # Simulate intermittent timeout
    if random.choice([True, False]):
        raise TimeoutError("Research Agent timed out")

    return {"research": data["documents"]}


def analyst(data):
    print("Analysis Agent running...")

    # Simulate malformed output
    if random.choice([True, False]):
        return "INVALID_OUTPUT"

    return {"analysis": "AI improves diagnosis accuracy."}


def writer(data):
    print("Writer Agent running...")

    # Silent wrong data
    if "analysis" not in data:
        return {"result": "No useful analysis found."}

    return {"result": data["analysis"]}


def run_pipeline(query):
    retrieved = retriever(query)
    researched = researcher(retrieved)
    analyzed = analyst(researched)
    result = writer(analyzed)

    print(result)


if __name__ == "__main__":
    run_pipeline("Explain AI in healthcare")