
from agents.requirement_agent import RequirementAgent
from agents.backend_agent import BackendAgent
from agents.database_agent import DatabaseAgent
from agents.test_agent import TestAgent
from core.pipeline import Pipeline

def main():
    context = {
        "requirement": "用户管理模块，包含用户增删改查"
    }

    pipeline = Pipeline([
        RequirementAgent(),
        DatabaseAgent(),
        BackendAgent(),
        TestAgent()
    ])

    result = pipeline.run(context)

    print("\n===== FINAL OUTPUT =====")
    for k, v in result.items():
        print(f"{k}:\n{v}\n")

if __name__ == "__main__":
    main()
