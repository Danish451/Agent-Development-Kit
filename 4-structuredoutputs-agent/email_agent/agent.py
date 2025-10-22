# Structured Outputs Agent: A specialized agent designed to handle structured outputs, such as JSON or XML, ensuring that responses adhere to a predefined schema for better integration with other systems.
# Type of structured output: 
# input_schema: Defines pydantic models for input validation.
# Output_schema: Defines pydantic models for output validation.
# output_schema is better than input_schema because it ensures that the agent's responses are well-structured and 
# conform to expected formats, which is crucial for downstream processing and integration with other systems.

from google.adk.agents import Agent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive"
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, body, closing, and signature."
    )

root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professtional email based on the user's request.

        GUDIDELINES:
        - Create an appropriate subject line (consise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete.

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting"
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent, # Pydantic model defining the expected structure of the email content
    output_key="email"   # Generated email will be accessible via this key "email"
)