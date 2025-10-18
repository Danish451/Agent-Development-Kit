import os
import random
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Lite LLM is a lightweight wrapper around various large language models.
# Here we use it to connect to an OpenAI GPT-4.1 model hosted on OpenRouter.
# We use LiteLLM for all the models other than gemini models in ADK.
# Because we can't use other models directly with the Agent class.

# https://docs.litellm.ai/docs/providers/openrouter
model = LiteLlm(
    model="openrouter/openai/gpt-4.1",  # open router is a provider that hosts openai models
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def get_dad_joke():
    jokes=[
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]

    return random.choice(jokes)

root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that tells dad jokes. Only use the tool `get_dad_joke` to tell jokes.
    """,
    tools=[get_dad_joke],
)