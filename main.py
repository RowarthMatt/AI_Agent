import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if len(sys.argv) > 1:
    content = sys.argv[1]
else:
    print("Prompt required")
    sys.exit(1)

verbose = False
if len(sys.argv) > 2:
    if sys.argv[2] == "--verbose":
        verbose = True

messages = [
    types.Content(role="user", parts=[types.Part(text=content)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt))

promt_tokens = response.usage_metadata.prompt_token_count
resposne_tokens = response.usage_metadata.candidates_token_count

if verbose:
    print(f"User prompt: {content}")
    print(response.text)
    print(f"Prompt tokens: {promt_tokens}")
    print(f"Response tokens: {resposne_tokens}")
else:
    print(response.text)