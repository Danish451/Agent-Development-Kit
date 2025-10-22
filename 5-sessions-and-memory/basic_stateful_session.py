import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent.agent import root_agent

load_dotenv()  # take environment variables from .env file

# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Brandon Hancock",
    "user_preference": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican,
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

# Create a NEW session
APP_NAME = "Brandon Bot"
USER_ID = "brandon_hancock"
SESSION_ID = str(uuid.uuid4())

# 2. Wrap your logic in an async function
async def main():
    stateful_session = await session_service_stateful.create_session(  # <-- 3. Add 'await'
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,    # it is optional to provide an initial state
    )
    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {SESSION_ID}")

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful
    )

    new_message = types.Content(
        role="user", parts=[types.Part(text="What is Brandon's favorite TV show?")]
    )

    # runner.run() is synchronous, so no 'await' here.
    # It handles its own async loop in a separate thread.
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("FINAL RESPONSE:")
                print(f"\t{event.content.parts[0].text}")

    print("=== Session Event Exploration ===")
    session = await session_service_stateful.get_session(  # <-- 4. Add 'await'
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log final Session state
    print("=== Final Session State ===")
    # This will now work because 'session' is a Session object, not a coroutine
    for key, value in session.state.items():
        print(f"{key}: {value}")

# 5. Run the async main function
if __name__ == "__main__":
    asyncio.run(main())