from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)

result = client.music(
    "یک موسیقی آرام و احساسی با پیانو، ویولن و فضای سینمایی"
)

print(result)
