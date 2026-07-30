import random
import time


def retriever(query):
    print("Retriever running...")
    return {"documents": ["AI improves healthcare", "AI assists doctors"]}


def researcher(data):

    retries = 3

    for attempt in range(retries):

        try:
            print(f"Research Agent attempt {attempt + 1}")

            if random.choice([True, False]):
                raise TimeoutError("Research Agent timed out")

            return {"research": data["documents"]}

        except TimeoutError as e:
            print(e)

            if attempt == retries - 1:
                raise

            print("Retrying...\n")
            time.sleep(1)


def analyst(data):

    print("Analysis Agent running...")

    result = {
        "analysis": "AI improves diagnosis accuracy."
    }

    if "analysis" not in result:
        raise ValueError("Malformed output")

    return result


def writer(data):

    print("Writer Agent running...")

    return {
        "result": data["analysis"]
    }


def run_pipeline(query):

    try:
        retrieved = retriever(query)
        researched = researcher(retrieved)
        analyzed = analyst(researched)
        result = writer(analyzed)

        print(result)

    except Exception as e:
        print(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline("Explain AI in healthcare")