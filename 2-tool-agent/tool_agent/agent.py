from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a tool agent that can use external tools to assist users with their requests.
    When a user makes a request, determine if any of the available tools can help fulfill the
    request. If so, use the appropriate tool(s) to gather information or perform actions,
    """,
    # tools=[google_search],  # This is built in tool from ADK
    # tools=[google_search, get_current_time],   #We can't use built-in tools and custom tools together
    tools=[get_current_time],   # Custom tool only
)