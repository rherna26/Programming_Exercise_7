import re

#defining function
def get_sentences(paragraph):
    #implementing look-ahead feature
    sentences = r'[A-Z].*?[.!?](?=\s|$)'
    m = re.findall(sentences, paragraph, flags=re.DOTALL | re.MULTILINE)
    return m

#defining function
def count_sentences(sentences):
    #returnes sentence count
    return len(sentences)

#defining function
def main():

    #user has to enter a paragraph
    paragraph = input("Enter paragraph: ")

    sentences = get_sentences(paragraph)

    #displays the individual sentences
    print("\nIndividual Sentences:")
    for sentence in sentences:
        print(f"-> {sentence}")

    sentence_count = count_sentences(sentences)
    #displays sentence count
    print(f"\nTotal number of sentences: {sentence_count}")

#recalles main function
if __name__ == "__main__":
    main()