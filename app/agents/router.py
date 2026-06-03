''''from app.agents.speech_agent import SpeechAgent
from app.agents.tts_agent import TTSAgent
from app.agents.vision_agent import VisionAgent
from app.llm.gpt_handler import ask_llm
from app.memory.memory_manager import MemoryManager

from app.agents.memory_agent import MemoryAgent
from app.agents.llm_agent import LLM_Agent
from app.agents.translation_agent import TranslationAgent
from app.agents.response_agent import ResponseAgent
from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.action_agent import ActionAgent

class AIRouter:

    def __init__(self):

        self.speech_agent = SpeechAgent()
        self.tts_agent = TTSAgent()
        self.vision_agent = VisionAgent()
        self.memory = MemoryManager()
        self.memory_agent = MemoryAgent()
        self.llm_agent = LLM_Agent()
        self.translation_agent = TranslationAgent()
        self.response_agent = ResponseAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.action_agent = ActionAgent()

    def route(self, input_type, data=None):

        # Speech Input
        if input_type == "audio":

            return self.speech_agent.process(data)

        # Text Input
                
        elif input_type == "text":

            #1. return self.tts_agent.process(data)
        
            #2. # Ask LLM
            # ai_response = ask_llm(data)

            # # Speak response
            # self.tts_agent.process(ai_response)

            # return {
            #     "type": "llm_response",
            #     "output": ai_response
            # }
            
        
            # 3# Load memory context
            # context = self.memory.get_recent_context()

            # # Ask LLM with memory
            # ai_response = ask_llm(data, context)

            # # Save interaction
            # self.memory.save_interaction(
            #     data,
            #     ai_response
            # )

            # # Speak response
            # self.tts_agent.process(ai_response)

            # return {
            #     "type": "llm_response",
            #     "output": ai_response
            # }
            
        
        
            # # Retrieve memory
            # context = self.memory_agent.retrieve_context()

            # # LLM reasoning
            # ai_response = self.llm_agent.process(
            #     data,
            #     context
            # )

            # # Optional translation
            # translated_response = self.translation_agent.translate(
            #     ai_response,
            #     language="Hindi"
            # )

            # # Save interaction
            # self.memory_agent.save(
            #     data,
            #     translated_response
            # )

            # # Final response
            # return self.response_agent.respond(
            #     translated_response,
            #     speak_output=True
            # )
            
            # Retrieve memory
            context = self.memory_agent.retrieve_context()

            knowledge_keywords = [
                "document",
                "pdf",
                "notes",
                "explain",
                "what is",
                "define",
                "research"
            ]

            is_knowledge_query = any(
                keyword in data.lower()
                for keyword in knowledge_keywords
            )

            # Route to Knowledge Agent
            if is_knowledge_query:

                ai_response = self.knowledge_agent.answer(
                    data
                )

            # Route to LLM Agent
            else:

                ai_response = self.llm_agent.process(
                    data,
                    context
                )

            # Translate response
            translated_response = self.translation_agent.translate(
                ai_response,
                language="Hindi"
            )

            # Save memory
            self.memory_agent.save(
                data,
                translated_response
            )

            # Final response
            return self.response_agent.respond(
                translated_response,
                speak_output=True
            )

        # Vision Input
        elif input_type == "vision":

            return self.vision_agent.process()

        else:

            return {
                "type": "error",
                "output": "Unsupported input type"
            }'''
            
            
# from app.agents.speech_agent import SpeechAgent
# from app.agents.tts_agent import TTSAgent
# from app.agents.vision_agent import VisionAgent
# from app.llm.gpt_handler import ask_llm
# from app.memory.memory_manager import MemoryManager

# from app.agents.memory_agent import MemoryAgent
# from app.agents.llm_agent import LLM_Agent
# #from app.agents.translation_agent import TranslationAgent
# from app.agents.response_agent import ResponseAgent
# from app.agents.knowledge_agent import KnowledgeAgent
# from app.agents.action_agent import ActionAgent
# from app.agents.web_agent import WebAgent
# from app.agents.planner_agent import PlannerAgent


# class AIRouter:

#     def __init__(self):

#         self.speech_agent = SpeechAgent()
#         self.tts_agent = TTSAgent()
#         self.vision_agent = VisionAgent()

#         self.memory = MemoryManager()
#         self.memory_agent = MemoryAgent()

#         self.llm_agent = LLM_Agent()
#         #self.translation_agent = TranslationAgent()
#         self.response_agent = ResponseAgent()

#         self.knowledge_agent = KnowledgeAgent()

#         # ACTION AGENT
#         self.action_agent = ActionAgent()

#         # WEB AGENT
#         self.web_agent = WebAgent()
        
#         self.planner_agent = PlannerAgent()

#     def route(self, input_type, data=None):

#         # Speech Input
#         if input_type == "audio":

#             return self.speech_agent.process(data)

#         # Text Input
#         elif input_type == "text":

#             # Retrieve memory
#             context = self.memory_agent.retrieve_context()

#             # KNOWLEDGE KEYWORDS
#             knowledge_keywords = [
#                 "document",
#                 "pdf",
#                 "notes",
#                 "explain",
#                 "what is",
#                 "define",
#                 "research"
#             ]

#             # ACTION KEYWORDS
#             action_keywords = [
#                 "open",
#                 "search",
#                 "create",
#                 "launch",
#                 "run",
#                 "list files"
#             ]

#             # WEB KEYWORDS
#             web_keywords = [
#                 "internet",
#                 "web",
#                 "google",
#                 "latest",
#                 "news",
#                 "online"
#             ]

#             # DETECT KNOWLEDGE QUERY
#             is_knowledge_query = any(
#                 keyword in data.lower()
#                 for keyword in knowledge_keywords
#             )

#             # DETECT ACTION QUERY
#             is_action_query = any(
#                 keyword in data.lower()
#                 for keyword in action_keywords
#             )

#             # DETECT WEB QUERY
#             is_web_query = any(
#                 keyword in data.lower()
#                 for keyword in web_keywords
#             )

#             # ACTION AGENT
#             if is_action_query:

#                 ai_response = self.action_agent.execute(
#                     data
#                 )

#             # WEB SEARCH
#             elif is_web_query:

#                 ai_response = self.web_agent.answer_from_web(
#                     data
#                 )

#             # KNOWLEDGE AGENT
#             elif is_knowledge_query:

#                 ai_response = self.knowledge_agent.answer(
#                     data
#                 )

#             # NORMAL LLM
#             else:

#                 ai_response = self.llm_agent.process(
#                     data,
#                     context
#                 )

#             # Translate response
#             # translated_response = ai_response 
#             # self.translation_agent.translate(
#             #     ai_response,
#             #     language="Hindi"
#             # )

#             # # Save memory
#             # self.memory_agent.save(
#             #     data,
#             #     translated_response
#             # )

#             # # Final response
#             # return self.response_agent.respond(
#             #     translated_response,
#             #     speak_output=True
#             # )
            
#             # DIRECT RESPONSE (FAST + CLEAN)

#             translated_response = ai_response

#             # Save memory
#             self.memory_agent.save(
#                 data,
#                 translated_response
#             )

#             # Final response
#             return {
#                 "response": translated_response
#             }

#         # Vision Input
#         elif input_type == "vision":

#             return self.vision_agent.process()

#         else:

#             return {
#                 "type": "error",
#                 "output": "Unsupported input type"
#             }


from app.agents.speech_agent import SpeechAgent
from app.agents.tts_agent import TTSAgent
from app.agents.vision_agent import VisionAgent
from app.memory.memory_manager import MemoryManager

from app.agents.memory_agent import MemoryAgent
from app.agents.llm_agent import LLM_Agent
from app.agents.response_agent import ResponseAgent
from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.action_agent import ActionAgent
from app.agents.web_agent import WebAgent
from app.agents.planner_agent import PlannerAgent


class AIRouter:

    def __init__(self):

        self.speech_agent = SpeechAgent()
        self.tts_agent = TTSAgent()
        self.vision_agent = VisionAgent()

        self.memory = MemoryManager()
        self.memory_agent = MemoryAgent()

        self.llm_agent = LLM_Agent()
        self.response_agent = ResponseAgent()

        self.knowledge_agent = KnowledgeAgent()
        self.action_agent = ActionAgent()
        self.web_agent = WebAgent()

        # 🆕 Planner Agent (STEP 282)
        self.planner_agent = PlannerAgent()

    def route(self, input_type, data=None):

        # -------------------------
        # Speech Input
        # -------------------------
        if input_type == "audio":
            return self.speech_agent.process(data)

        # -------------------------
        # Text Input
        # -------------------------
        elif input_type == "text":

            # Get memory context
            context = self.memory_agent.retrieve_context()

            # 🧠 STEP 282 — PLANNER DECISION
            selected_tool = self.planner_agent.choose_tool(data).strip().lower()

            # 🔐 VALIDATION LAYER (CRITICAL SAFETY FIX)
            valid_tools = {
                "action_agent",
                "web_agent",
                "knowledge_agent",
                "memory_agent",
                "llm_agent"
            }

            if selected_tool not in valid_tools:
                print(f"[WARNING] Invalid tool returned: {selected_tool}")
                selected_tool = "llm_agent"

            # 🔍 DEBUG LOGGING
            print(f"\n[Planner Selected Tool]: {selected_tool}")

            # -------------------------
            # TOOL EXECUTION
            # -------------------------
            if selected_tool == "action_agent":

                ai_response = self.action_agent.execute(data)

            elif selected_tool == "web_agent":

                ai_response = self.web_agent.answer_from_web(data)

            elif selected_tool == "knowledge_agent":

                ai_response = self.knowledge_agent.answer(data)

            elif selected_tool == "memory_agent":

                ai_response = self.memory_agent.retrieve_context()

            else:

                ai_response = self.llm_agent.process(
                    data,
                    context
                )

            # -------------------------
            # MEMORY SAVE
            # -------------------------
            self.memory_agent.save(
                data,
                str(ai_response)
            )

            return {
                "response": ai_response
            }

        # -------------------------
        # Vision Input
        # -------------------------
        elif input_type == "vision":
            return self.vision_agent.process()

        # -------------------------
        # Error Handling
        # -------------------------
        else:
            return {
                "type": "error",
                "output": "Unsupported input type"
            }