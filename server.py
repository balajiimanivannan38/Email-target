from fastapi import FastAPI, Header
from environment import EmailTriageEnv,Action
from auth import verify_token,create_token
from ml_model import Model

app=FastAPI()
envs={}
model=Model()
sample=[{"text":"Urgent security alert","label":"urgent"},{"text":"Buy now!!!","label":"spam"},{"text":"Meeting tomorrow","label":"normal"}]
model.train(sample)

@app.post("/login")
def login():
    return {"token":create_token("user")}

def get_env(token):
    uid=verify_token(token)
    if uid not in envs: envs[uid]=EmailTriageEnv()
    return envs[uid]

@app.post("/start")
def start(Authorization:str=Header(...)):
    return get_env(Authorization).reset()

@app.post("/auto")
def auto(Authorization:str=Header(...)):
    env=get_env(Authorization)
    obs=env.state()
    pred=model.predict(obs.email_text)
    action=Action(category=pred,action="ignore")
    obs,r,done,_=env.step(action)
    return {"pred":pred,"reward":r,"done":done}