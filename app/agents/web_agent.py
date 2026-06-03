import webbrowser


class WebAgent:

    def answer_from_web(self, query):

        query = query.replace(
            "search",
            ""
        )

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        return f"Searching web for: {query}"