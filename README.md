# List of files
- Task 1: `Diffie_Hellman_key_exchange.py`
- Task 2: `simple_box_sipher.py`
- Task 3: `hybrid_system.py`

# Improvements
All bugs from previous modules are fixed. 
There still was a bug in adding points (yeah I know shame on me), 
as I didn't round one of the multiplications to a FF.

# Hybrid system
To start the *conversation* start the `hybrid_system.py` file 
and wait for the environment to initialize the keys and other elements.

The current hybrid system works for all ASCII characters.

The flow is the following:

PLAIN TEXT > ASCII > BINARY > ENCODED > BINARY (decoded) > ASCII > PLAIN TEXT

To use Chat GPT for generating responses to your messages:
- pip install openai
- replace `YOUR_API_KEY` in `generateResponse()` in `hybrid_system.py` with your API key,
  that can be generated at https://beta.openai.com/account/api-keys

Enjoy 😄.