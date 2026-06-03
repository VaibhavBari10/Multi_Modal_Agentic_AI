from app.agents.router import AIRouter

router = AIRouter()

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    response = router.route(
        "text",
        query
    )

    print("\nAI:\n")

    print(response["response"])