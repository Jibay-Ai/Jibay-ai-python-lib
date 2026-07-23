from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.image(
    "یک ربات هوش مصنوعی واقع‌گرایانه در آزمایشگاه مدرن"
)

print(result)
