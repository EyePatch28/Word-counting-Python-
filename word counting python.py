def count_words(sentence):
    # Check if the input sentence is empty
    if not sentence.strip():
        raise ValueError("Input cannot be empty")

    # Split the sentence into words and count them
    words = sentence.split()
    return len(words)

def main():
    try:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")

        # Count words and display the result
        word_count = count_words(user_input)
        print(f"Word count: {word_count}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()