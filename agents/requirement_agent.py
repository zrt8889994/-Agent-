
from agents.base_agent import BaseAgent

class RequirementAgent(BaseAgent):

    def run(self, context):
        requirement = context.get("requirement")

        api_design = {
            "endpoints": [
                {"method": "GET", "path": "/users"},
                {"method": "POST", "path": "/users"},
                {"method": "PUT", "path": "/users/{id}"},
                {"method": "DELETE", "path": "/users/{id}"}
            ]
        }

        context["api_design"] = api_design
        return context
