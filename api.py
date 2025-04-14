import nlpcloud

client = nlpcloud.Client("finetuned-llama-3-70b", "<nlpcloud api key>", gpu=True)

class ner_text:
    def ner_text(self,text):
        try:
            response = client.entities(text, searched_entity="programming languages")
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
        
