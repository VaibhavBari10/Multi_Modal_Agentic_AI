from app.agents.action_agent import ActionAgent

agent = ActionAgent()

while True:

    command = input("\nCommand: ")

    if command.lower() == "exit":
        break

    result = agent.execute(command)

    print("\nAI:\n")

    print(result)