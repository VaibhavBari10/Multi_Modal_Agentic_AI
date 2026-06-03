from app.memory.memory_manager import MemoryManager


class MemoryAgent:

    def __init__(self):

        self.memory = MemoryManager()

    def retrieve_context(self):

        return self.memory.get_recent_context()

    def save(self, user_input, ai_response):

        self.memory.save_interaction(
            user_input,
            ai_response
        )