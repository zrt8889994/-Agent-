
from agents.base_agent import BaseAgent

class TestAgent(BaseAgent):

    def run(self, context):
        test_code = '''
def test_users():
    assert True
'''
        context["test_code"] = test_code
        return context
