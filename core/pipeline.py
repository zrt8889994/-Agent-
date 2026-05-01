
class Pipeline:

    def __init__(self, agents):
        self.agents = agents

    def run(self, context):
        for agent in self.agents:
            print(f"Running {agent.__class__.__name__}")
            context = agent.run(context)
        return context
