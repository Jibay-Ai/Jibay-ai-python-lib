# JibayAI Python SDK

[![PyPI](https://img.shields.io/pypi/v/jibayai.svg)](https://pypi.org/project/jibayai/)
[![Python](https://img.shields.io/pypi/pyversions/jibayai.svg)](https://pypi.org/project/jibayai/)
[![License](https://img.shields.io/pypi/l/jibayai.svg)](https://pypi.org/project/jibayai/)

A validated, developer-friendly Python SDK for the JibayAI chat, image, music, and video APIs.

- PyPI: <https://pypi.org/project/jibayai/>
- JibayAI: <https://jibay.ir/>
- API documentation: <https://platform.jibay.ir/docs/>
- Package name: `jibayai`
- Current release: `0.1.0`
- Required Python version: `3.9+`

---

# English

## Overview

`jibayai` provides a clean Python interface for working with JibayAI services. It includes a reusable HTTP client, direct convenience functions, parameter validation, structured exceptions, retry and timeout handling, a command-line interface, offline help, and a media downloader.

The SDK currently supports four main operations:

| Capability | Python method | Description |
|---|---|---|
| Chat | `client.chat()` | Send text prompts and conversation context to a JibayAI model |
| Image | `client.image()` | Generate an image from a text prompt |
| Music | `client.music()` | Generate music from a style or description |
| Video | `client.video()` | Generate a video from a text prompt |

## Features

- Simple installation from PyPI
- Chat, image, music, and video generation
- Reusable `requests.Session` for repeated calls
- JSON chat requests and compatibility with the older form-encoded format
- API key loading from an argument or environment variable
- Automatic retry for transient HTTP failures
- Configurable request timeout
- Input validation before network requests
- Strict or flexible model-name validation
- Structured exception hierarchy
- Automatic image `device` identifier generation
- Temporary media file downloader
- Context-manager support
- Direct package-level helper functions
- Command-line interface
- Built-in offline help
- Pure Python package
- Python `3.9+` support

## Installation

Install the latest release from PyPI:

```bash
python -m pip install --upgrade jibayai
```

You may also use:

```bash
pip install jibayai
```

Verify the installation:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

Inside a Python file or Pydroid editor, use normal Python code instead:

```python
import jibayai

print(jibayai.__version__)
```

## Requirements and compatibility

The package declares:

```text
Python >= 3.9
requests >= 2.31, < 3
```

Because the SDK is distributed as a pure Python `py3-none-any` wheel, it can be installed on supported Windows, Linux, macOS, and Android Python environments. Python `3.14` is accepted by the package's `Requires-Python` rule; users should keep `pip` and `requests` updated for the best compatibility.

Upgrade packaging tools when needed:

```bash
python -m pip install --upgrade pip setuptools wheel
```

## API key

Create an API key through the JibayAI platform, then pass it directly:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
```

For production projects, keep the key outside source code.

### Linux, macOS, or Termux

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

### Windows PowerShell

```powershell
$env:JIBAYAI_API_KEY="YOUR_API_KEY"
```

### Windows Command Prompt

```cmd
set JIBAYAI_API_KEY=YOUR_API_KEY
```

Then create the client without passing the key:

```python
from jibayai import JibayAI

client = JibayAI()
```

## Quick start

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    "Hello, how are you?",
    model="jibay-5",
)

print(result)
```

The SDK returns decoded JSON when the server response is JSON. If the server returns plain text, the SDK returns a string.

## Creating a reusable client

For multiple requests, create one client and reuse it. This allows the underlying HTTP connection to be reused.

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=60,
    retries=2,
)

chat_result = client.chat("Explain artificial intelligence simply.")
image_result = client.image("A futuristic AI laboratory")
music_result = client.music("Calm cinematic electronic music")
video_result = client.video("A cinematic view of a futuristic city")

client.close()
```

You can also use a context manager:

```python
from jibayai import JibayAI

with JibayAI(api_key="YOUR_API_KEY") as client:
    result = client.chat("Hello", model="jibay-5")
    print(result)
```

The internally created HTTP session is closed automatically when the context block ends.

## Chat

### Basic chat

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="What is machine learning?",
    model="jibay-5",
)

print(result)
```

The default model used by the SDK is `jibay-4.1` when `model` is omitted.

### System instruction

```python
result = client.chat(
    text="Explain neural networks.",
    model="jibay-5",
    system="Answer clearly, accurately, and in simple language.",
)
```

### Conversation history

```python
result = client.chat(
    text="What is my name?",
    model="jibay-5",
    chats=[
        {
            "role": "user",
            "text": "My name is Ali.",
        },
        {
            "role": "assistant",
            "text": "Nice to meet you, Ali.",
        },
    ],
)
```

A history message may use `text` or `content` for its message body.

```python
chats = [
    {"role": "user", "content": "My favorite language is Python."},
    {"role": "assistant", "content": "Python is a great choice."},
]
```

The `chats` parameter may also be supplied as a JSON string.

### Web search and additional options

```python
result = client.chat(
    text="Find and summarize recent AI developments.",
    model="jibay-5",
    search_web=True,
    signal=False,
    mode_official=False,
    saved_memories={
        "language": "en",
        "answer_style": "concise",
    },
)
```

Supported chat parameters:

| Parameter | Type | Default | Description |
|---|---:|---:|---|
| `text` | `str` | Required | User message or prompt |
| `model` | `str` | `jibay-4.1` | JibayAI model identifier |
| `system` | `str` or `None` | `None` | System instruction |
| `chats` | list, JSON string, or `None` | `None` | Previous conversation messages |
| `search_web` | boolean-like | `False` | Enable web-search behavior when supported by the API |
| `signal` | boolean-like | `False` | Optional API signal flag |
| `saved_memories` | JSON-like value | `None` | Optional saved memory data |
| `mode_official` | boolean-like | `False` | Optional official-mode flag |
| `encoding` | `json`, `form`, or `None` | Client default | Select the chat request encoding |

Common string boolean values are accepted by validation, including conventional true/false forms.

### JSON and legacy form encoding

The default chat encoding is JSON:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="json",
)
```

To support an older form-encoded integration:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="form",
)

result = client.chat("Hello", model="jibay-5")
```

You can override the encoding for only one request:

```python
result = client.chat(
    "Hello",
    model="jibay-5",
    encoding="form",
)
```

## Image generation

Generate an image from a prompt:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.image(
    "A realistic futuristic city at night, cinematic lighting"
)

print(result)
```

The image endpoint requires a positive numeric `device` identifier. If it is omitted, the SDK generates a valid random identifier automatically.

```python
result = client.image(
    "A modern artificial intelligence laboratory",
    device=12345,
)
```

## Music generation

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.music(
    "Calm emotional cinematic music with piano and violin"
)

print(result)
```

The text may describe a genre, mood, instruments, tempo, or overall musical direction.

```python
result = client.music(
    "Energetic electronic music, fast tempo, futuristic atmosphere"
)
```

## Video generation

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.video(
    "A cinematic autumn forest with slow camera movement"
)

print(result)
```

A more detailed prompt may improve control over the scene:

```python
result = client.video(
    "A futuristic city at night, aerial camera movement, rain, neon reflections, cinematic style"
)
```

## Direct convenience functions

For small scripts, you can call the four features directly from the package:

```python
import jibayai

chat_result = jibayai.chat(
    "Hello",
    api_key="YOUR_API_KEY",
    model="jibay-5",
)

image_result = jibayai.image(
    "A futuristic city",
    api_key="YOUR_API_KEY",
)

music_result = jibayai.music(
    "Calm Persian jazz",
    api_key="YOUR_API_KEY",
)

video_result = jibayai.video(
    "A cinematic autumn forest",
    api_key="YOUR_API_KEY",
)
```

Direct functions create a client for the operation. For repeated calls, a reusable `JibayAI` client is more efficient.

## Downloading generated media

Generated media URLs may be temporary. Save important output as soon as possible.

```python
saved_path = client.download(
    url="https://example.com/generated-video.mp4",
    destination="outputs/video.mp4",
)

print(saved_path)
```

Parent directories are created automatically.

The SDK protects existing files by default:

```python
saved_path = client.download(
    url="https://example.com/generated-image.png",
    destination="outputs/image.png",
    overwrite=True,
)
```

The download is first written to a temporary `.part` file and then moved to the final destination after completion.

## Client configuration

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    base_url="https://jibay.ir",
    timeout=60.0,
    retries=2,
    strict_models=False,
    supported_models=None,
    chat_encoding="json",
)
```

| Option | Default | Description |
|---|---:|---|
| `api_key` | Environment fallback | API key; falls back to `JIBAYAI_API_KEY` |
| `base_url` | `https://jibay.ir` | API origin |
| `timeout` | `60.0` | Per-request timeout in seconds |
| `retries` | `2` | Retry count for selected transient failures |
| `strict_models` | `False` | Enforce an explicit model allow-list |
| `supported_models` | Built-in list | Model names accepted in strict mode |
| `chat_encoding` | `json` | Default chat request encoding |
| `session` | New session | Optional custom `requests.Session` |

Automatic retries apply to selected transient statuses such as `408`, `429`, `500`, `502`, `503`, and `504`. The SDK respects the server's `Retry-After` header when available.

## Model validation

By default, the SDK validates the syntax of model identifiers while allowing future model names.

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=False,
)
```

Use strict mode when your application must allow only selected models:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=True,
    supported_models=[
        "jibay-4",
        "jibay-4.1",
        "jibay-5",
    ],
)
```

An unsupported model raises `ValidationError` before a network request is sent.

## Validation

The SDK validates important values before sending requests, including:

- API key
- Prompt text
- Model identifier
- Boolean-like flags
- Conversation history
- Saved memory data
- Image device identifier
- Base URL and download URL
- Timeout
- Retry count
- Chat encoding
- Download destination

Example:

```python
from jibayai import JibayAI, ValidationError

client = JibayAI(api_key="YOUR_API_KEY")

try:
    client.image("", device=-1)
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

## Error handling

All SDK exceptions inherit from `JibayError`.

```python
from jibayai import (
    JibayAI,
    JibayError,
    ValidationError,
    AuthenticationError,
    PermissionDeniedError,
    RateLimitError,
    TimeoutError,
    NetworkError,
    ServerError,
    InvalidResponseError,
)

client = JibayAI(api_key="YOUR_API_KEY")

try:
    result = client.chat("Hello", model="jibay-5")
    print(result)

except ValidationError as exc:
    print("Invalid parameter:", exc.parameter)
    print(exc)

except AuthenticationError:
    print("The API key is missing, invalid, expired, or disabled.")

except PermissionDeniedError:
    print("This API key is not allowed to access the requested service.")

except RateLimitError as exc:
    print("The request limit was exceeded.")
    print("Retry-After:", exc.retry_after)

except TimeoutError:
    print("The request exceeded the configured timeout.")

except NetworkError:
    print("The JibayAI API could not be reached.")

except ServerError as exc:
    print("JibayAI server error:", exc.status_code)

except InvalidResponseError:
    print("The server returned an unsafe or unreadable response.")

except JibayError as exc:
    print("JibayAI SDK error:", exc)
```

### Exception hierarchy

```text
JibayError
├── ConfigurationError
├── ValidationError
├── NetworkError
│   └── TimeoutError
├── InvalidResponseError
└── APIError
    ├── BadRequestError
    ├── AuthenticationError
    ├── PermissionDeniedError
    ├── NotFoundError
    ├── ConflictError
    ├── RateLimitError
    └── ServerError
```

### HTTP error mapping

| HTTP status | SDK exception |
|---:|---|
| `400`, `422` | `BadRequestError` |
| `401` | `AuthenticationError` |
| `403` | `PermissionDeniedError` |
| `404` | `NotFoundError` |
| `409` | `ConflictError` |
| `429` | `RateLimitError` |
| `500–599` | `ServerError` |
| Other non-success statuses | `APIError` |

API exceptions may expose:

```python
except JibayError as exc:
    print(getattr(exc, "status_code", None))
    print(getattr(exc, "response_body", None))
    print(getattr(exc, "request_id", None))
```

## Built-in offline help

The SDK includes help text that does not make an API request:

```python
from jibayai import JibayAI, sdk_help

client = JibayAI(api_key="YOUR_API_KEY")

print(client.help())
print(client.help("chat"))
print(client.help("image"))
print(client.help("music"))
print(client.help("video"))
print(client.help("download"))
print(client.help("models"))
print(client.help("errors"))
print(client.help("cli"))

print(sdk_help("errors"))
```

## Command-line interface

Installing the package adds the `jibayai` command.

```bash
jibayai --help
jibayai --version
```

Set the API key:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

Chat:

```bash
jibayai chat "Hello" --model jibay-5
```

Chat with a system instruction and web-search flag:

```bash
jibayai chat "Summarize recent AI news" \
  --model jibay-5 \
  --system "Answer briefly" \
  --search-web
```

Image:

```bash
jibayai image "A futuristic city at night"
```

Music:

```bash
jibayai music "Calm cinematic music with piano"
```

Video:

```bash
jibayai video "A cinematic autumn forest"
```

Offline help:

```bash
jibayai help
jibayai help chat
jibayai help errors
```

Each command also accepts common options such as `--api-key`, `--base-url`, `--timeout`, and `--retries`.

## Android usage

### Pydroid 3

Open Pydroid's Pip section and install:

```text
jibayai
```

Or use the Pydroid terminal:

```bash
pip install jibayai
```

Then run normal Python code in the editor:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
print(client.chat("Hello", model="jibay-5"))
```

Do not place shell commands such as `python -c "..."` directly inside a `.py` file.

### Termux

```bash
pkg update
pkg install python
python -m pip install --upgrade pip
python -m pip install jibayai
```

Test:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

## Security recommendations

- Never publish your API key in Git repositories, public channels, screenshots, or client-side JavaScript.
- Prefer the `JIBAYAI_API_KEY` environment variable on servers and development machines.
- Do not hard-code a private key in a distributed desktop or mobile application.
- Rotate a key immediately if it is exposed.
- Validate and limit user-provided prompts in public applications.
- Do not log complete API keys.

## Troubleshooting

### `ModuleNotFoundError: No module named 'jibayai'`

Install the package in the same Python environment that runs your script:

```bash
python -m pip install jibayai
```

Check both paths:

```bash
python --version
python -m pip --version
```

### `ConfigurationError: API key is required`

Pass the key:

```python
client = JibayAI(api_key="YOUR_API_KEY")
```

Or set `JIBAYAI_API_KEY` before creating the client.

### Authentication error

Confirm that the key is complete, active, and copied without extra spaces.

### Timeout

Increase the timeout for generation operations:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)
```

### Rate limit

Catch `RateLimitError` and inspect `retry_after`:

```python
from jibayai import RateLimitError

try:
    result = client.chat("Hello")
except RateLimitError as exc:
    print(exc.retry_after)
```

### Existing download file

Pass `overwrite=True` only when replacing the destination is intentional:

```python
client.download(url, "output.mp4", overwrite=True)
```

### Updating the SDK

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

## Complete example

```python
from pathlib import Path

from jibayai import (
    JibayAI,
    JibayError,
    RateLimitError,
    ValidationError,
)


def main() -> None:
    with JibayAI(
        api_key="YOUR_API_KEY",
        timeout=120,
        retries=2,
    ) as client:
        try:
            chat_result = client.chat(
                text="Write a short description of a futuristic city.",
                model="jibay-5",
                system="Answer in one concise paragraph.",
            )
            print("Chat:", chat_result)

            image_result = client.image(
                "A realistic futuristic city at night, cinematic composition"
            )
            print("Image:", image_result)

            music_result = client.music(
                "Emotional cinematic electronic music with piano"
            )
            print("Music:", music_result)

            video_result = client.video(
                "A cinematic aerial view of a futuristic city at night"
            )
            print("Video:", video_result)

        except ValidationError as exc:
            print("Invalid input:", exc.parameter, exc)
        except RateLimitError as exc:
            print("Rate limited. Retry-After:", exc.retry_after)
        except JibayError as exc:
            print("JibayAI error:", exc)


if __name__ == "__main__":
    main()
```

## Development

Clone or extract the source package, then create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

Build the package:

```bash
python -m build
```

Check release files:

```bash
python -m twine check dist/*
```

## License

This project is distributed under the MIT License.

---

# فارسی

## معرفی

`jibayai` کتابخانه پایتون جیبای برای استفاده ساده و استاندارد از سرویس‌های چت، ساخت تصویر، ساخت موسیقی و ساخت ویدیو است. این SDK علاوه بر ارسال درخواست به API، اعتبارسنجی پارامترها، مدیریت خطاهای اختصاصی، تلاش مجدد خودکار، کنترل زمان انتظار، ابزار خط فرمان، راهنمای آفلاین و دانلود فایل‌های تولیدشده را نیز فراهم می‌کند.

قابلیت‌های اصلی:

| قابلیت | متد پایتون | توضیح |
|---|---|---|
| چت | `client.chat()` | ارسال پیام و تاریخچه گفتگو به مدل‌های جیبای |
| تصویر | `client.image()` | ساخت تصویر از توضیح متنی |
| موسیقی | `client.music()` | ساخت موسیقی بر اساس سبک یا توضیح |
| ویدیو | `client.video()` | ساخت ویدیو از پرامپت متنی |

## امکانات

- نصب مستقیم از PyPI
- پشتیبانی از چت، تصویر، موسیقی و ویدیو
- استفاده مجدد از اتصال HTTP برای درخواست‌های متعدد
- پشتیبانی از JSON و فرمت قدیمی فرم برای چت
- دریافت کلید API از کد یا متغیر محیطی
- تلاش مجدد خودکار برای خطاهای موقت
- زمان انتظار قابل تنظیم
- بررسی پارامترها قبل از ارسال درخواست
- اعتبارسنجی منعطف یا سخت‌گیرانه نام مدل
- خطاهای اختصاصی و قابل مدیریت
- ساخت خودکار شناسه `device` برای تصویر
- دانلود فایل‌های موقتی تولیدشده
- پشتیبانی از Context Manager
- توابع مستقیم و ساده
- ابزار خط فرمان
- راهنمای داخلی بدون نیاز به اینترنت
- پکیج کاملاً پایتونی
- پشتیبانی از Python `3.9+`

## نصب

آخرین نسخه را از PyPI نصب کن:

```bash
python -m pip install --upgrade jibayai
```

یا:

```bash
pip install jibayai
```

بررسی نسخه در ترمینال:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

داخل فایل پایتون یا ادیتور Pydroid باید کد معمولی پایتون بنویسی:

```python
import jibayai

print(jibayai.__version__)
```

## نیازمندی‌ها و سازگاری

پکیج این نیازمندی‌ها را اعلام می‌کند:

```text
Python >= 3.9
requests >= 2.31, < 3
```

کتابخانه به‌صورت Wheel عمومی `py3-none-any` منتشر شده و روی محیط‌های سازگار Windows، Linux، macOS و Android قابل نصب است. قانون `Requires-Python` نصب روی Python `3.14` را نیز مجاز می‌کند؛ برای سازگاری بهتر، `pip` و `requests` را به‌روز نگه دار.

```bash
python -m pip install --upgrade pip setuptools wheel
```

## کلید API

کلید API را از پلتفرم جیبای دریافت کن و به Client بده:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
```

برای پروژه‌های واقعی بهتر است کلید را داخل کد قرار ندهی.

### Linux، macOS یا Termux

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

### Windows PowerShell

```powershell
$env:JIBAYAI_API_KEY="YOUR_API_KEY"
```

### Windows CMD

```cmd
set JIBAYAI_API_KEY=YOUR_API_KEY
```

بعد بدون واردکردن مستقیم کلید، Client را بساز:

```python
from jibayai import JibayAI

client = JibayAI()
```

## شروع سریع

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    "سلام، حالت چطوره؟",
    model="jibay-5",
)

print(result)
```

اگر پاسخ سرور JSON باشد، کتابخانه آن را به ساختار پایتون تبدیل می‌کند. اگر پاسخ متن ساده باشد، یک `str` برمی‌گرداند.

## ساخت Client قابل استفاده مجدد

برای چند درخواست، فقط یک Client بساز تا اتصال HTTP مجدداً استفاده شود:

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=60,
    retries=2,
)

chat_result = client.chat("هوش مصنوعی را ساده توضیح بده.")
image_result = client.image("یک آزمایشگاه هوش مصنوعی آینده‌نگر")
music_result = client.music("موسیقی الکترونیک آرام و سینمایی")
video_result = client.video("نمای سینمایی از یک شهر آینده‌نگر")

client.close()
```

یا از Context Manager استفاده کن:

```python
from jibayai import JibayAI

with JibayAI(api_key="YOUR_API_KEY") as client:
    result = client.chat("سلام", model="jibay-5")
    print(result)
```

با پایان بلوک `with`، Session داخلی خودکار بسته می‌شود.

## چت

### چت ساده

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="یادگیری ماشین چیست؟",
    model="jibay-5",
)

print(result)
```

اگر پارامتر `model` را وارد نکنی، مدل پیش‌فرض SDK برابر `jibay-4.1` است.

### دستور سیستمی

```python
result = client.chat(
    text="شبکه عصبی را توضیح بده.",
    model="jibay-5",
    system="واضح، دقیق و ساده پاسخ بده.",
)
```

### تاریخچه گفتگو

```python
result = client.chat(
    text="اسم من چیست؟",
    model="jibay-5",
    chats=[
        {
            "role": "user",
            "text": "اسم من علی است.",
        },
        {
            "role": "assistant",
            "text": "از آشنایی با شما خوشحالم علی.",
        },
    ],
)
```

متن هر پیام می‌تواند در `text` یا `content` قرار بگیرد:

```python
chats = [
    {"role": "user", "content": "زبان مورد علاقه من پایتون است."},
    {"role": "assistant", "content": "پایتون انتخاب بسیار خوبی است."},
]
```

پارامتر `chats` می‌تواند یک رشته JSON معتبر نیز باشد.

### جستجوی وب و گزینه‌های تکمیلی

```python
result = client.chat(
    text="جدیدترین پیشرفت‌های هوش مصنوعی را پیدا و خلاصه کن.",
    model="jibay-5",
    search_web=True,
    signal=False,
    mode_official=False,
    saved_memories={
        "language": "fa",
        "answer_style": "concise",
    },
)
```

پارامترهای چت:

| پارامتر | نوع | پیش‌فرض | توضیح |
|---|---:|---:|---|
| `text` | `str` | الزامی | پیام یا پرامپت کاربر |
| `model` | `str` | `jibay-4.1` | شناسه مدل جیبای |
| `system` | `str` یا `None` | `None` | دستور سیستمی |
| `chats` | لیست، JSON یا `None` | `None` | پیام‌های قبلی گفتگو |
| `search_web` | مقدار بولی | `False` | فعال‌کردن جستجوی وب در صورت پشتیبانی API |
| `signal` | مقدار بولی | `False` | فلگ اختیاری API |
| `saved_memories` | داده JSONمانند | `None` | حافظه‌های ذخیره‌شده اختیاری |
| `mode_official` | مقدار بولی | `False` | فلگ حالت رسمی |
| `encoding` | `json`، `form` یا `None` | تنظیم Client | نوع ارسال درخواست چت |

## ارسال JSON و فرمت قدیمی Form

حالت پیش‌فرض چت JSON است:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="json",
)
```

برای سازگاری با کد قدیمی فرم:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="form",
)

result = client.chat("سلام", model="jibay-5")
```

فقط برای یک درخواست:

```python
result = client.chat(
    "سلام",
    model="jibay-5",
    encoding="form",
)
```

## ساخت تصویر

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.image(
    "یک شهر آینده‌نگر واقعی در شب با نورپردازی سینمایی"
)

print(result)
```

سرویس تصویر به شناسه عددی مثبت `device` نیاز دارد. اگر آن را وارد نکنی، کتابخانه خودکار یک شناسه معتبر می‌سازد:

```python
result = client.image(
    "یک آزمایشگاه مدرن هوش مصنوعی",
    device=12345,
)
```

## ساخت موسیقی

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.music(
    "یک موسیقی آرام، احساسی و سینمایی با پیانو و ویولن"
)

print(result)
```

در پرامپت موسیقی می‌توانی سبک، حس، سازها، سرعت و فضای کلی آهنگ را مشخص کنی:

```python
result = client.music(
    "موسیقی الکترونیک پرانرژی با ریتم سریع و فضای آینده‌نگر"
)
```

## ساخت ویدیو

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.video(
    "یک جنگل پاییزی سینمایی با حرکت آرام دوربین"
)

print(result)
```

برای کنترل بهتر صحنه، پرامپت دقیق‌تر بنویس:

```python
result = client.video(
    "یک شهر آینده‌نگر در شب، نمای هوایی، باران، بازتاب نورهای نئونی و سبک سینمایی"
)
```

## توابع مستقیم

برای اسکریپت‌های کوچک می‌توانی مستقیماً از خود پکیج استفاده کنی:

```python
import jibayai

chat_result = jibayai.chat(
    "سلام",
    api_key="YOUR_API_KEY",
    model="jibay-5",
)

image_result = jibayai.image(
    "یک شهر آینده‌نگر",
    api_key="YOUR_API_KEY",
)

music_result = jibayai.music(
    "موسیقی جاز ایرانی آرام",
    api_key="YOUR_API_KEY",
)

video_result = jibayai.video(
    "یک جنگل پاییزی سینمایی",
    api_key="YOUR_API_KEY",
)
```

توابع مستقیم برای هر عملیات یک Client می‌سازند. برای درخواست‌های متعدد، استفاده از یک `JibayAI` ثابت سریع‌تر و بهینه‌تر است.

## دانلود فایل تولیدشده

لینک فایل‌های تولیدشده ممکن است موقتی باشد؛ بنابراین خروجی مهم را سریع ذخیره کن:

```python
saved_path = client.download(
    url="https://example.com/generated-video.mp4",
    destination="outputs/video.mp4",
)

print(saved_path)
```

پوشه‌های مسیر مقصد خودکار ساخته می‌شوند.

برای جایگزینی فایل موجود:

```python
saved_path = client.download(
    url="https://example.com/generated-image.png",
    destination="outputs/image.png",
    overwrite=True,
)
```

دانلود ابتدا در یک فایل موقتی با پسوند `.part` انجام می‌شود و بعد از تکمیل، به نام نهایی انتقال پیدا می‌کند.

## تنظیمات Client

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    base_url="https://jibay.ir",
    timeout=60.0,
    retries=2,
    strict_models=False,
    supported_models=None,
    chat_encoding="json",
)
```

| گزینه | پیش‌فرض | توضیح |
|---|---:|---|
| `api_key` | متغیر محیطی | کلید API یا مقدار `JIBAYAI_API_KEY` |
| `base_url` | `https://jibay.ir` | آدرس اصلی API |
| `timeout` | `60.0` | حداکثر زمان هر درخواست بر حسب ثانیه |
| `retries` | `2` | تعداد تلاش مجدد برای خطاهای موقت |
| `strict_models` | `False` | محدودکردن مدل‌ها به فهرست مشخص |
| `supported_models` | فهرست داخلی | مدل‌های مجاز در حالت سخت‌گیرانه |
| `chat_encoding` | `json` | نوع پیش‌فرض درخواست چت |
| `session` | Session جدید | امکان واردکردن `requests.Session` اختصاصی |

تلاش مجدد خودکار برای برخی خطاهای موقت مانند `408`، `429`، `500`، `502`، `503` و `504` انجام می‌شود. اگر سرور هدر `Retry-After` بفرستد، SDK آن را در نظر می‌گیرد.

## اعتبارسنجی مدل‌ها

حالت پیش‌فرض فقط ساختار نام مدل را بررسی می‌کند و اجازه می‌دهد مدل‌های جدید آینده نیز استفاده شوند:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=False,
)
```

برای محدودکردن برنامه به مدل‌های مشخص:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=True,
    supported_models=[
        "jibay-4",
        "jibay-4.1",
        "jibay-5",
    ],
)
```

در صورت واردکردن مدل نامعتبر، قبل از ارسال درخواست `ValidationError` ایجاد می‌شود.

## اعتبارسنجی پارامترها

SDK این موارد را قبل از ارسال بررسی می‌کند:

- کلید API
- متن پرامپت
- نام مدل
- فلگ‌های بولی
- تاریخچه گفتگو
- حافظه‌های ذخیره‌شده
- شناسه دستگاه تصویر
- آدرس API و لینک دانلود
- زمان انتظار
- تعداد تلاش مجدد
- نوع ارسال چت
- مسیر ذخیره فایل

مثال:

```python
from jibayai import JibayAI, ValidationError

client = JibayAI(api_key="YOUR_API_KEY")

try:
    client.image("", device=-1)
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

## مدیریت خطا

تمام خطاهای کتابخانه از `JibayError` ارث‌بری می‌کنند:

```python
from jibayai import (
    JibayAI,
    JibayError,
    ValidationError,
    AuthenticationError,
    PermissionDeniedError,
    RateLimitError,
    TimeoutError,
    NetworkError,
    ServerError,
    InvalidResponseError,
)

client = JibayAI(api_key="YOUR_API_KEY")

try:
    result = client.chat("سلام", model="jibay-5")
    print(result)

except ValidationError as exc:
    print("پارامتر نامعتبر:", exc.parameter)
    print(exc)

except AuthenticationError:
    print("کلید API وجود ندارد، اشتباه است، منقضی شده یا غیرفعال است.")

except PermissionDeniedError:
    print("این کلید اجازه استفاده از سرویس درخواستی را ندارد.")

except RateLimitError as exc:
    print("محدودیت تعداد درخواست رد شده است.")
    print("Retry-After:", exc.retry_after)

except TimeoutError:
    print("زمان انتظار درخواست تمام شد.")

except NetworkError:
    print("اتصال به API جیبای برقرار نشد.")

except ServerError as exc:
    print("خطای سرور جیبای:", exc.status_code)

except InvalidResponseError:
    print("پاسخ سرور قابل خواندن یا پردازش ایمن نبود.")

except JibayError as exc:
    print("خطای کتابخانه جیبای:", exc)
```

### ساختار خطاها

```text
JibayError
├── ConfigurationError
├── ValidationError
├── NetworkError
│   └── TimeoutError
├── InvalidResponseError
└── APIError
    ├── BadRequestError
    ├── AuthenticationError
    ├── PermissionDeniedError
    ├── NotFoundError
    ├── ConflictError
    ├── RateLimitError
    └── ServerError
```

### تبدیل وضعیت HTTP به خطا

| وضعیت HTTP | خطای SDK |
|---:|---|
| `400`، `422` | `BadRequestError` |
| `401` | `AuthenticationError` |
| `403` | `PermissionDeniedError` |
| `404` | `NotFoundError` |
| `409` | `ConflictError` |
| `429` | `RateLimitError` |
| `500–599` | `ServerError` |
| سایر پاسخ‌های ناموفق | `APIError` |

اطلاعات تکمیلی خطای API:

```python
except JibayError as exc:
    print(getattr(exc, "status_code", None))
    print(getattr(exc, "response_body", None))
    print(getattr(exc, "request_id", None))
```

## راهنمای داخلی آفلاین

```python
from jibayai import JibayAI, sdk_help

client = JibayAI(api_key="YOUR_API_KEY")

print(client.help())
print(client.help("chat"))
print(client.help("image"))
print(client.help("music"))
print(client.help("video"))
print(client.help("download"))
print(client.help("models"))
print(client.help("errors"))
print(client.help("cli"))

print(sdk_help("errors"))
```

## ابزار خط فرمان

بعد از نصب، دستور `jibayai` در ترمینال در دسترس است:

```bash
jibayai --help
jibayai --version
```

تنظیم کلید:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

چت:

```bash
jibayai chat "سلام" --model jibay-5
```

چت همراه دستور سیستمی و جستجوی وب:

```bash
jibayai chat "جدیدترین اخبار هوش مصنوعی را خلاصه کن" \
  --model jibay-5 \
  --system "مختصر پاسخ بده" \
  --search-web
```

ساخت تصویر:

```bash
jibayai image "یک شهر آینده‌نگر در شب"
```

ساخت موسیقی:

```bash
jibayai music "موسیقی سینمایی آرام با پیانو"
```

ساخت ویدیو:

```bash
jibayai video "یک جنگل پاییزی سینمایی"
```

راهنما:

```bash
jibayai help
jibayai help chat
jibayai help errors
```

هر دستور گزینه‌های مشترکی مانند `--api-key`، `--base-url`، `--timeout` و `--retries` دارد.

## استفاده در اندروید

### Pydroid 3

در بخش Pip عبارت زیر را نصب کن:

```text
jibayai
```

یا در Terminal داخلی Pydroid:

```bash
pip install jibayai
```

بعد در ادیتور کد پایتون بنویس:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
print(client.chat("سلام", model="jibay-5"))
```

دستورهای ترمینالی مانند `python -c "..."` را داخل فایل `.py` قرار نده.

### Termux

```bash
pkg update
pkg install python
python -m pip install --upgrade pip
python -m pip install jibayai
```

تست:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

## توصیه‌های امنیتی

- کلید API را در مخزن عمومی، کانال، تصویر یا JavaScript سمت کاربر منتشر نکن.
- روی سرور و سیستم توسعه از متغیر محیطی `JIBAYAI_API_KEY` استفاده کن.
- کلید خصوصی را داخل برنامه موبایل یا دسکتاپی که برای کاربران منتشر می‌شود، هاردکد نکن.
- اگر کلید افشا شد، سریع آن را تغییر بده.
- ورودی کاربران را در برنامه‌های عمومی بررسی و محدود کن.
- کلید کامل را داخل Log ذخیره نکن.

## رفع خطاهای متداول

### خطای `ModuleNotFoundError`

کتابخانه را در همان محیط پایتونی نصب کن که فایل را اجرا می‌کند:

```bash
python -m pip install jibayai
```

مسیرها را بررسی کن:

```bash
python --version
python -m pip --version
```

### خطای نیاز به API Key

کلید را مستقیم وارد کن:

```python
client = JibayAI(api_key="YOUR_API_KEY")
```

یا متغیر `JIBAYAI_API_KEY` را تنظیم کن.

### خطای احراز هویت

مطمئن شو کلید کامل، فعال و بدون فاصله اضافی کپی شده است.

### تمام‌شدن زمان انتظار

برای ساخت تصویر، موسیقی یا ویدیو زمان انتظار را بیشتر کن:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)
```

### محدودیت درخواست

```python
from jibayai import RateLimitError

try:
    result = client.chat("سلام")
except RateLimitError as exc:
    print(exc.retry_after)
```

### وجود فایل مقصد

فقط وقتی واقعاً می‌خواهی فایل قبلی جایگزین شود، `overwrite=True` بده:

```python
client.download(url, "output.mp4", overwrite=True)
```

### به‌روزرسانی کتابخانه

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

## نمونه کامل

```python
from jibayai import (
    JibayAI,
    JibayError,
    RateLimitError,
    ValidationError,
)


def main() -> None:
    with JibayAI(
        api_key="YOUR_API_KEY",
        timeout=120,
        retries=2,
    ) as client:
        try:
            chat_result = client.chat(
                text="یک شهر آینده‌نگر را کوتاه توصیف کن.",
                model="jibay-5",
                system="در یک پاراگراف مختصر پاسخ بده.",
            )
            print("Chat:", chat_result)

            image_result = client.image(
                "یک شهر آینده‌نگر واقعی در شب با ترکیب‌بندی سینمایی"
            )
            print("Image:", image_result)

            music_result = client.music(
                "موسیقی الکترونیک احساسی و سینمایی با پیانو"
            )
            print("Music:", music_result)

            video_result = client.video(
                "نمای هوایی سینمایی از یک شهر آینده‌نگر در شب"
            )
            print("Video:", video_result)

        except ValidationError as exc:
            print("ورودی نامعتبر:", exc.parameter, exc)
        except RateLimitError as exc:
            print("محدودیت درخواست؛ Retry-After:", exc.retry_after)
        except JibayError as exc:
            print("خطای جیبای:", exc)


if __name__ == "__main__":
    main()
```

## توسعه و ساخت

در پوشه سورس یک محیط مجازی بساز:

```bash
python -m venv .venv
```

وابستگی‌های توسعه را نصب کن:

```bash
python -m pip install -e ".[dev]"
```

تست‌ها را اجرا کن:

```bash
python -m unittest discover -s tests -v
```

پکیج را بساز:

```bash
python -m build
```

فایل‌های انتشار را بررسی کن:

```bash
python -m twine check dist/*
```

## لینک‌ها

- PyPI: <https://pypi.org/project/jibayai/>
- وب‌سایت جیبای: <https://jibay.ir/>
- مستندات API: <https://platform.jibay.ir/docs/>

## مجوز

این پروژه با مجوز MIT منتشر شده است.
