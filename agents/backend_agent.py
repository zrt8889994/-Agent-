
from agents.base_agent import BaseAgent

class BackendAgent(BaseAgent):

    def run(self, context):
        code = '''
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def list_users():
    return []

@app.post("/users")
def create_user():
    return {"msg": "created"}
'''
        context["backend_code"] = code
        return context
