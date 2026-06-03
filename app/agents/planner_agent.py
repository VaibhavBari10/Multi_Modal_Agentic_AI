# from app.agents.tool_registry import TOOLS
# from app.llm.gpt_handler import ask_llm


# class PlannerAgent:

#     def choose_tool(self, query):

#         prompt = f"""
# You are a routing AI.

# Available tools:

# {TOOLS}

# Choose ONLY one tool name.

# User Query:
# {query}

# Return ONLY:

# action_agent
# web_agent
# knowledge_agent
# memory_agent
# llm_agent
# """

#         tool = ask_llm(prompt)

#         return tool.strip().lower()


from app.agents.tool_registry import TOOLS
from app.llm.gpt_handler import ask_llm


class PlannerAgent:

    def choose_tool(self, query):

        prompt = f"""
You are a routing AI (planner agent).

You must select ONLY ONE tool.

Available tools:
{TOOLS}

STRICT RULES:
- Return ONLY the tool name
- No explanation
- No punctuation
- No extra text
- No formatting

Valid outputs:
action_agent
web_agent
knowledge_agent
memory_agent
llm_agent

User Query:
{query}
"""

        tool = ask_llm(prompt)

        # 🧠 CLEAN OUTPUT (CRITICAL FOR STABILITY)
        tool = tool.strip().lower()
        tool = tool.replace(".", "")
        tool = tool.replace("selected:", "")
        tool = tool.replace("tool:", "")
        tool = tool.replace("\n", "").strip()

        return tool