# from app.llm.gpt_handler import ask_llm


# class LLM_Agent:

#     def process(self, prompt, context=None):

#         response = ask_llm(
#             prompt,
#             context
#         )

#         return response


from app.llm.gpt_handler import ask_llm


class LLM_Agent:

    def process(self, user_input, context=""):

        prompt = f"""
You are a helpful AI assistant.

Respond clearly and briefly.

Conversation Context:
{context}

User:
{user_input}

AI:
"""

        response = ask_llm(prompt)

        return response