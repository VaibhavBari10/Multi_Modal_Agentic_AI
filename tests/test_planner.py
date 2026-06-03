from app.agents.planner_agent import PlannerAgent

planner = PlannerAgent()

while True:

    query = input("\nQuery: ")

    tool = planner.choose_tool(query)

    print("\nSelected Tool:")

    print(tool)