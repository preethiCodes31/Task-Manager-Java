from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😔"
    else:
        return "Neutral 😐"

print("Welcome to the Sentiment Analyzer!")
print("Type 'exit' to quit the program.\n")

while True:
    review = input("Enter your text: ")
    if review.lower() == 'exit':
        print("Goodbye!")
        break
    print("Sentiment:", analyze_sentiment(review))
    print()