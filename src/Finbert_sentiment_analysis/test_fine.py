from finbert_model import predict_sentiment

texts = [
    "Reliance shares surged after reporting strong quarterly profits.",
    "The company reported huge losses this quarter.",
    "The company announced its annual board meeting."
]

for text in texts:
    print(predict_sentiment(text))