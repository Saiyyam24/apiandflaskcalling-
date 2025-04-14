from transformers import pipeline

class abusedetect:
    def detect_abuse(self,text):        
        pipe = pipeline("text-classification", model="Hate-speech-CNERG/english-abusive-MuRIL")     
        # pipe = pipeline("text-classification", model="distilbert-base-uncased-finet

        text = "you are such a idiot I have never seen"
        result = pipe(text)[0]
        return result
    
# text = " you sucks in computer science"
# val = abusedetect().detect_abuse(text)
# # print(val['label'])
# if val['label']== "LABEL_1":
#     print("Abuse detected")
# else:
#     print("No abuse detected")

# print(f"confidence: {val[0]['score']}")