import nlpcloud

client = nlpcloud.Client("finetuned-llama-3-70b", "c9d2afa731c4b91148c312fb414789e466a17c3e", gpu=True)

class ner_text:
    def ner_text(self,text):
        try:
            response = client.entities(text, searched_entity="programming languages")
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
        