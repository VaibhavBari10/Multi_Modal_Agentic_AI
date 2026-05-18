from app.agents.router import AIRouter

router = AIRouter()

# Test TTS
response = router.route(
    "text",
    "Hello Vaibhav"
)

print(response)