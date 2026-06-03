"""from app.agents.router import AIRouter

router = AIRouter()

# Test TTS
response = router.route(
    "text",
    "Hello Vaibhav"
)

print(response)"""


"""from app.agents.router import AIRouter

router = AIRouter()

response = router.route(
    "text",
    "What is machine learning?"
)

print("\nAI RESPONSE:\n")
print(response["output"])"""


"""from app.agents.router import AIRouter

router = AIRouter()

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = router.route(
        "text",
        user_input
    )

    print("\nAI:")
    print(response["output"])"""
    

from app.agents.router import AIRouter

router = AIRouter()

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = router.route(
        "text",
        user_input
    )

    print("\nAI:")
    print(response["response"])