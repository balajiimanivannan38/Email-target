from pydantic import BaseModel

class Observation(BaseModel):
    email_text:str
    subject:str

class Action(BaseModel):
    category:str
    action:str

class EmailTriageEnv:
    def __init__(self):
        self.data=[
            {"text":"Urgent security alert","label":"urgent"},
            {"text":"Buy now!!!","label":"spam"},
            {"text":"Meeting tomorrow","label":"normal"}
        ]
        self.i=0

    def reset(self):
        self.i=0
        return self.state()

    def state(self):
        if self.i>=len(self.data): return None
        d=self.data[self.i]
        return Observation(email_text=d["text"], subject=d["text"])

    def step(self,action):
        d=self.data[self.i]
        reward=1 if action.category==d["label"] else -1
        self.i+=1
        return self.state(),reward,self.i>=len(self.data),{}