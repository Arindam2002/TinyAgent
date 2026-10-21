from src.tinyagent.llm import LLM


def main():
    # Re-initialize the LLM with the updated class
    llm = LLM(model="gemma4:e4b")
    
    # Generate a `Response` dataclass
    response = llm.generate([{"role": "user", "content": "Hi! How's life?"}])
    print(response)


if __name__ == "__main__":
    main()
