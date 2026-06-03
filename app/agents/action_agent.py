import os
import webbrowser
import subprocess


class ActionAgent:

    def execute(self, command):

        command = command.lower()

        # Open Notepad
        if "open notepad" in command:

            os.system("notepad")

            return "Opening Notepad"

        # Open Calculator
        elif "open calculator" in command:

            os.system("calc")

            return "Opening Calculator"

        # Open Chrome
        elif "open chrome" in command:

            os.system("start chrome")

            return "Opening Chrome"

        # Open YouTube
        elif "open youtube" in command:

            webbrowser.open(
                "https://www.youtube.com"
            )

            return "Opening YouTube"

        # Open Google
        elif "open google" in command:

            webbrowser.open(
                "https://www.google.com"
            )

            return "Opening Google"

        # Google Search
        elif "search" in command:

            query = command.replace(
                "search",
                ""
            )

            url = f"https://www.google.com/search?q={query}"

            webbrowser.open(url)

            return f"Searching Google for {query}"

        # Create File
        elif "create file" in command:

            filename = "generated_file.txt"

            with open(filename, "w") as f:

                f.write(
                    "This file was created by AI."
                )

            return f"{filename} created successfully"

        # List Directory
        elif "list files" in command:

            files = os.listdir()

            return "\n".join(files)

        # Safe terminal command
        elif "show current directory" in command:

            result = subprocess.check_output(
                "cd",
                shell=True
            )

            return result.decode()

        else:

            return "Action not recognized."