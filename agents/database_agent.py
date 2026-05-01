
from agents.base_agent import BaseAgent

class DatabaseAgent(BaseAgent):

    def run(self, context):
        ddl = '''
        CREATE TABLE users (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            email VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX idx_email ON users(email);
        '''

        context["database_sql"] = ddl
        return context
