from strands import Agent
# TODO: Import the http_request built-in tool
from strands_tools import http_request

agent = Agent( 
    model="amazon.nova-lite-v1:0",
    # TODO: Add the http_request built-in-tool
    tools=[http_request]
    )

agent("""
   Using the website https://en.wikipedia.org/wiki/Dungeons_%26_Dragons tell me the name of the designers of
   Dungeons and Dragons.
    """)
