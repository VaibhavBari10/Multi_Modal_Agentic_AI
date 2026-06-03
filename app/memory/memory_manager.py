import json
import os

MEMORY_FILE = "memory.json"


class MemoryManager:

    def __init__(self):

        # Create memory file if not exists
        if not os.path.exists(MEMORY_FILE):

            with open(MEMORY_FILE, "w") as f:
                json.dump([], f)

    def save_interaction(self, user_input, ai_response):

        memory = self.load_memory()

        interaction = {
            "user": user_input,
            "assistant": ai_response
        }

        memory.append(interaction)

        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)

    def load_memory(self):

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def get_recent_context(self, limit=5):

        memory = self.load_memory()

        return memory[-limit:]