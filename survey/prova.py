import pandas as pd

class SurveyElement:
    def __init__(self, id, related_id, name, language, text=None):
        self.id = id
        self.related_id = related_id
        self.name = name
        self.language = language
        self.text = text

    def to_dict(self):
        return {
            "id": self.id,
            "related_id": self.related_id,
            "name": self.name,
            "language": self.language,
            "text": self.text,
        }

class Group(SurveyElement):
    def __init__(self, id, name, language, text=None):
        super().__init__(id, None, name, language, text)
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({"class": "G"})
        return base_dict

class Question(SurveyElement):
    def __init__(self, id, related_id, name, language, type_scale, relevance, text=None):
        super().__init__(id, related_id, name, language, text)
        self.type_scale = type_scale
        self.relevance = relevance

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "class": "Q",
            "type_scale": self.type_scale,
            "relevance": self.relevance,
        })
        return base_dict

class Survey:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def export_to_csv(self, file_name):
        df = pd.DataFrame([elem.to_dict() for elem in self.elements])
        df.to_csv(file_name, index=False, encoding='utf-8')

# Esempio di utilizzo
survey = Survey()
group = Group(id=1, name="Informazioni Demografiche", language="it")
question = Question(id=2, related_id=1, name="question1", language="it", type_scale="X", relevance=1, text="Testo della domanda")

group.add_question(question)
survey.add_element(group)
survey.add_element(question)

# Esportazione in CSV
survey.export_to_csv("survey_output.csv")
