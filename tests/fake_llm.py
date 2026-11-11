from doc_qa_cli import LLMPort, RecordedLLM


def make() -> LLMPort:
    return RecordedLLM(['It listens on port 8080 [a.md#2: "listens on port 8080"].'])
