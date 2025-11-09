from strands import Agent
import logging
# TODO: Add debug logging to see what your agent is thinking

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.INFO)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)
# TODO: Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"
agent = Agent(system_prompt="You are a game master for a Dungeon & Dragon game. ouput language is Korean.")
# TODO: Summon your agent with a basic incantation such as "Hi, I am an advanturer ready for adventure!"
agent("Hi, I am an advanturer ready for adventure!")