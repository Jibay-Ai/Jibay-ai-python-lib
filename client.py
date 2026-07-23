from jibayai import JibayAI, JibayError

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
    retries=2,
)

try:
    chat_result = client.chat(
        text="سلام، خودت را معرفی کن.",
        model="jibay-5",
    )

    image_result = client.image(
        "یک آزمایشگاه پیشرفته هوش مصنوعی"
    )

    music_result = client.music(
        "موسیقی الکترونیک آرام و آینده‌نگر"
    )

    video_result = client.video(
        "یک سفینه فضایی در حال عبور از کنار زمین"
    )

    print("Chat:", chat_result)
    print("Image:", image_result)
    print("Music:", music_result)
    print("Video:", video_result)

except JibayError as error:
    print("JibayAI error:", error)

finally:
    client.close()
