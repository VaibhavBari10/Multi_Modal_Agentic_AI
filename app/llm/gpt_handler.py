"""import ollama


def ask_llm(prompt):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]"""
    
    
    
# import ollama


# def ask_llm(prompt, context=None):

#     messages = []

#     # Add previous context
#     if context:

#         for item in context:

#             messages.append({
#                 "role": "user",
#                 "content": item["user"]
#             })

#             messages.append({
#                 "role": "assistant",
#                 "content": item["assistant"]
#             })

#     # Current user prompt
#     messages.append({
#         "role": "user",
#         "content": prompt
#     })

#     response = ollama.chat(
#         model="llama3" ,
#         #model="phi3:mini",   #ollama pull phi3:mini        
#         #model='tinyllama'   #ollama pull tinyllama
#         messages=messages
#     )

#     return response["message"]["content"]


import ollama


MODEL_NAME = "phi3:mini"


def ask_llm(prompt, context=""):

    full_prompt = f"""
{context}

{prompt}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return response["message"]["content"]