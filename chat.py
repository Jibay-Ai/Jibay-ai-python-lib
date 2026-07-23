from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="سلام، هوش مصنوعی را ساده توضیح بده.",
    model="jibay-4.1",
)

print(result)
