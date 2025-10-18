from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # Take model name from https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting Agent",
    instruction="""
    You are a friendly greeting agent. Your task is to greet users warmly and make them feel welcome.
    When a user interacts with you, respond with a cheerful greeting message.
    """,
)