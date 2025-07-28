from agent import root_agent

class MyAgentOrchestrator:
    def __init__(self):
        # You can initialize extra configs here if needed
        self.agent = root_agent

    def run(self, query: str) -> str:
        """
        Runs the root agent with the given query.
        """
        response = self.agent(query)
        # ADK LlmAgent returns a dict-like object; extract text
        if isinstance(response, dict):
            return response.get("seminal_paper", str(response))
        return str(response)
