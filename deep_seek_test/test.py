from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama
from typing import List

agent = Agent(
    model=Ollama(id="deepseek-r1"),
    markdown=True
)
#agent = Agent(model=DeepSeek(), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
# tst111