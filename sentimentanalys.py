import os
from google.cloud import language_v1

# Correct path to the downloaded service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "notify.json"

class sentimentanalys:
    def analyze_sentiment(self,text):
            client = language_v1.LanguageServiceClient()

            document = language_v1.Document(
                content=text,
                type=language_v1.Document.Type.PLAIN_TEXT
            )

            sentiment = client.analyze_sentiment(
                request={"document": document}
            ).document_sentiment

            result = {}
            result["Text"] = text
            result["Sentiment Score"] = sentiment.score
            result["Sentiment Magnitude"] = sentiment.magnitude
            return result