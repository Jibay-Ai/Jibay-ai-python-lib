from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)

result = client.video(
    "یک شهر آینده‌نگر در شب با نورهای نئونی و حرکت سینمایی دوربین"
)

print(result)
