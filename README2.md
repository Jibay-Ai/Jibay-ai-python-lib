# JibayAI Python SDK

[![PyPI Version](https://img.shields.io/pypi/v/jibayai.svg)](https://pypi.org/project/jibayai/)
[![Python Versions](https://img.shields.io/pypi/pyversions/jibayai.svg)](https://pypi.org/project/jibayai/)
[![Package Status](https://img.shields.io/badge/status-publication--ready-1f6feb.svg)](https://pypi.org/project/jibayai/)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Official Python SDK for JibayAI chat, image, music, and video services.**

JibayAI Python SDK provides a structured, validated, and developer-oriented interface for integrating JibayAI capabilities into Python applications. The package includes a reusable synchronous client, direct helper functions, parameter validation, typed exceptions, retry handling, timeout management, command-line utilities, and media-download support.

> **Package name:** `jibayai`  
> **Current release:** `0.1.0`  
> **Python requirement:** Python `3.9` or later  
> **Distribution:** Pure Python wheel (`py3-none-any`)  
> **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International

---

## Language

- [English Documentation](#english-documentation)
- [مستندات فارسی](#مستندات-فارسی)

---

# English Documentation

## 1. Introduction

The `jibayai` package is the official Python interface for accessing JibayAI services through a concise and consistent application programming interface.

The SDK currently exposes four primary capabilities:

| Service | Python method | Purpose |
|---|---|---|
| Chat | `client.chat()` | Submit prompts, system instructions, history, and optional chat settings |
| Image | `client.image()` | Generate an image from a text description |
| Music | `client.music()` | Generate music from a style, mood, or production description |
| Video | `client.video()` | Generate a video from a text prompt |

The package is designed for:

- Backend services
- Automation scripts
- Desktop applications
- Command-line tools
- Educational projects
- Prototypes
- Android Python environments such as Pydroid and Termux
- Server-side integrations

The SDK is synchronous and uses the Python `requests` library internally.

---

## 2. Official Resources

| Resource | Address |
|---|---|
| PyPI package | <https://pypi.org/project/jibayai/> |
| JibayAI website | <https://jibay.ir/> |
| Platform documentation | <https://platform.jibay.ir/docs/> |
| License | <https://creativecommons.org/licenses/by-nc-nd/4.0/> |

---

## 3. Main Features

The SDK includes the following functionality:

- Official package installation through PyPI
- Reusable HTTP sessions
- Chat requests using JSON
- Compatibility with legacy form-encoded chat requests
- Image generation
- Music generation
- Video generation
- API-key loading from arguments or environment variables
- Input validation before an HTTP request is sent
- Flexible or strict model validation
- Configurable timeouts
- Configurable automatic retries
- Structured exceptions for validation, authentication, authorization, rate limits, network failures, timeouts, and server failures
- JSON response decoding
- Plain-text response support
- Temporary media downloading
- Context-manager support
- Direct package-level functions
- Command-line interface
- Built-in offline help
- Python `3.9+` compatibility
- Operating-system-independent pure Python distribution

---

## 4. Installation

Install the latest public version from PyPI:

```bash
python -m pip install jibayai
```

The shorter form is also supported:

```bash
pip install jibayai
```

Upgrade an existing installation:

```bash
python -m pip install --upgrade jibayai
```

Force a clean upgrade without using the local pip cache:

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

Install a specific release:

```bash
python -m pip install jibayai==0.1.0
```

---

## 5. Verifying the Installation

From a terminal:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

Expected output for this release:

```text
0.1.0
```

Inside a Python file:

```python
import jibayai

print(jibayai.__version__)
```

Verify the command-line interface:

```bash
jibayai --version
```

Display command-line help:

```bash
jibayai --help
```

---

## 6. Requirements and Compatibility

### Python

The package requires:

```text
Python >= 3.9
```

The intended compatibility range includes:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

### Runtime dependency

```text
requests >= 2.31, < 3
```

### Supported environments

The SDK is distributed as a pure Python wheel and is suitable for compatible Python environments on:

- Windows
- Linux
- macOS
- Android with Pydroid
- Android with Termux
- Virtual environments
- Containers
- Server installations

---

## 7. API Key Configuration

A valid JibayAI API key is required.

### Direct configuration

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
```

### Environment variable

For production systems, avoid placing private API keys directly in source code.

Linux, macOS, or Termux:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:JIBAYAI_API_KEY="YOUR_API_KEY"
```

Windows Command Prompt:

```cmd
set JIBAYAI_API_KEY=YOUR_API_KEY
```

Then initialize the client without an explicit key:

```python
from jibayai import JibayAI

client = JibayAI()
```

The SDK checks the `JIBAYAI_API_KEY` environment variable when `api_key` is not supplied.

---

## 8. Quick Start

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="Hello. Introduce JibayAI in one paragraph.",
    model="jibay-5",
)

print(result)
```

The SDK returns:

- A Python `dict` when the API returns a JSON object
- A Python `list` when the API returns a JSON array
- A Python `str` when the response is plain text
- Another JSON-compatible primitive when supplied by the API

---

## 9. Reusable Client

Create one client and reuse it for multiple requests:

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=60,
    retries=2,
)

chat_result = client.chat(
    "Explain artificial intelligence in simple terms.",
    model="jibay-5",
)

image_result = client.image(
    "A modern artificial intelligence research center"
)

music_result = client.music(
    "Calm cinematic electronic music with piano"
)

video_result = client.video(
    "A futuristic city at night with cinematic camera movement"
)

print(chat_result)
print(image_result)
print(music_result)
print(video_result)

client.close()
```

Reusing one client allows the underlying HTTP session and connections to be reused.

---

## 10. Context Manager

The client supports Python context-manager syntax:

```python
from jibayai import JibayAI

with JibayAI(api_key="YOUR_API_KEY") as client:
    result = client.chat(
        text="Hello.",
        model="jibay-5",
    )

    print(result)
```

The internally created HTTP session is closed automatically after leaving the `with` block.

---

## 11. Client Configuration

```python
from jibayai import JibayAI

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

### Configuration options

| Parameter | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` or `None` | Environment fallback | JibayAI API key |
| `base_url` | `str` | `https://jibay.ir` | Base API URL |
| `timeout` | `int` or `float` | `60.0` | Request timeout in seconds |
| `retries` | `int` | `2` | Number of automatic retries |
| `strict_models` | `bool` | `False` | Enable model allow-list enforcement |
| `supported_models` | iterable or `None` | Built-in list | Models allowed in strict mode |
| `chat_encoding` | `str` | `json` | Default chat transport: `json` or `form` |
| `session` | `requests.Session` or `None` | Internal session | Optional custom HTTP session |

### Timeout limits

The timeout value must be:

```text
Greater than 0 and no greater than 600 seconds
```

### Retry limits

The retry count must be:

```text
An integer from 0 through 10
```

---

## 12. Chat API

### Basic chat request

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="What is machine learning?",
    model="jibay-5",
)

print(result)
```

### Default model

When `model` is omitted, the SDK uses:

```text
jibay-4.1
```

Example:

```python
result = client.chat(
    "Explain neural networks."
)
```

### System instruction

```python
result = client.chat(
    text="Explain neural networks.",
    model="jibay-5",
    system="Provide a precise, formal, and concise explanation.",
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
            "text": "It is a pleasure to meet you, Ali.",
        },
    ],
)
```

A history message may use `content` instead of `text`:

```python
history = [
    {
        "role": "user",
        "content": "My preferred programming language is Python.",
    },
    {
        "role": "assistant",
        "content": "Python is suitable for many software and AI projects.",
    },
]

result = client.chat(
    text="Which language did I mention?",
    chats=history,
)
```

The `chats` argument may also be supplied as valid JSON text:

```python
history_json = """
[
  {
    "role": "user",
    "text": "My name is Sara."
  },
  {
    "role": "assistant",
    "text": "Hello Sara."
  }
]
"""

result = client.chat(
    text="What is my name?",
    chats=history_json,
)
```

### Web search option

```python
result = client.chat(
    text="Summarize the requested topic using web-search capability.",
    model="jibay-5",
    search_web=True,
)
```

### Saved memories

```python
result = client.chat(
    text="Answer according to my saved preferences.",
    model="jibay-5",
    saved_memories={
        "language": "en",
        "response_style": "formal",
    },
)
```

### Additional flags

```python
result = client.chat(
    text="Hello.",
    model="jibay-5",
    search_web=False,
    signal=False,
    mode_official=False,
)
```

### Complete chat example

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=90,
    retries=2,
)

result = client.chat(
    text="Prepare a short introduction to artificial intelligence.",
    model="jibay-5",
    system="Use professional English and avoid unnecessary repetition.",
    chats=[
        {
            "role": "user",
            "text": "The target audience is software developers.",
        },
        {
            "role": "assistant",
            "text": "Understood.",
        },
    ],
    search_web=False,
    signal=False,
    saved_memories={
        "preferred_language": "en",
    },
    mode_official=False,
)

print(result)
```

### Chat parameters

| Parameter | Accepted type | Required | Description |
|---|---|---:|---|
| `text` | `str` | Yes | Current user prompt |
| `model` | `str` | No | Model identifier |
| `system` | `str` or `None` | No | System-level instruction |
| `chats` | list, JSON string, or `None` | No | Prior conversation messages |
| `search_web` | boolean-like | No | Web-search flag |
| `signal` | boolean-like | No | API signal flag |
| `saved_memories` | string, object, list, or `None` | No | Saved-memory data |
| `mode_official` | boolean-like | No | Official-mode flag |
| `encoding` | `json`, `form`, or `None` | No | Per-request chat transport |

### Accepted boolean values

Boolean parameters accept:

```text
True / False
1 / 0
"true" / "false"
"T" / "F"
"yes" / "no"
"on" / "off"
```

---

## 13. JSON and Legacy Form Encoding

The current default is JSON:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="json",
)
```

For compatibility with an older form-encoded implementation:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="form",
)

result = client.chat(
    text="Hello.",
    model="jibay-5",
)
```

Override the format for one request only:

```python
result = client.chat(
    text="Hello.",
    model="jibay-5",
    encoding="form",
)
```

The accepted values are:

```text
json
form
```

---

## 14. Image Generation

### Basic image generation

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.image(
    "A realistic futuristic city at night with cinematic lighting"
)

print(result)
```

### Device identifier

The image endpoint requires a positive numeric `device` identifier. When it is omitted, the SDK generates a valid random identifier automatically.

Manual value:

```python
result = client.image(
    "A modern artificial intelligence laboratory",
    device=12345,
)
```

The valid range is:

```text
1 through 2147483647
```

### Detailed image prompt

```python
result = client.image(
    "A photorealistic artificial intelligence laboratory, clean white architecture, "
    "advanced computing systems, realistic materials, professional lighting, 16:9"
)
```

---

## 15. Music Generation

### Basic music generation

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.music(
    "Calm cinematic music with piano and violin"
)

print(result)
```

### Detailed music prompt

```python
result = client.music(
    "A formal cinematic instrumental composition, slow tempo, emotional piano, "
    "warm strings, subtle electronic atmosphere, no vocals"
)
```

A music prompt may describe:

- Genre
- Mood
- Tempo
- Instruments
- Vocal or instrumental preference
- Production style
- Atmosphere
- Intended use

Example:

```python
result = client.music(
    "Energetic electronic instrumental music, fast tempo, futuristic atmosphere, "
    "deep bass, clear percussion, suitable for a technology presentation"
)
```

---

## 16. Video Generation

### Basic video generation

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.video(
    "A cinematic autumn forest with slow camera movement"
)

print(result)
```

### Detailed video prompt

```python
result = client.video(
    "A futuristic city at night, aerial camera movement, light rain, neon reflections, "
    "realistic architecture, cinematic composition, smooth motion"
)
```

A video prompt may describe:

- Subject
- Location
- Camera position
- Camera movement
- Lighting
- Weather
- Visual style
- Motion
- Atmosphere
- Composition

---

## 17. Direct Package Functions

For short scripts, the SDK exposes package-level functions:

```python
import jibayai

chat_result = jibayai.chat(
    text="Hello.",
    api_key="YOUR_API_KEY",
    model="jibay-5",
)

image_result = jibayai.image(
    text="A futuristic city",
    api_key="YOUR_API_KEY",
)

music_result = jibayai.music(
    text="Calm cinematic music",
    api_key="YOUR_API_KEY",
)

video_result = jibayai.video(
    text="A cinematic forest",
    api_key="YOUR_API_KEY",
)

print(chat_result)
print(image_result)
print(music_result)
print(video_result)
```

These helper functions create and close a temporary client automatically.

For repeated requests, use one persistent `JibayAI` instance.

---

## 18. Downloading Generated Media

Generated-media responses may include temporary URLs. Store required output promptly.

```python
saved_path = client.download(
    url="https://example.com/generated-file.mp4",
    destination="outputs/video.mp4",
)

print(saved_path)
```

### Replace an existing file

```python
saved_path = client.download(
    url="https://example.com/generated-image.png",
    destination="outputs/image.png",
    overwrite=True,
)
```

### Download behavior

The downloader:

- Validates the URL
- Creates missing parent directories
- Protects existing files by default
- Streams the response in chunks
- Writes to a temporary `.part` file
- Moves the completed file to the final destination
- Removes the incomplete temporary file when an error occurs
- Applies SDK timeout and error handling

---

## 19. Input Validation

The SDK validates inputs before sending requests.

Validated values include:

- API key
- Base URL
- Prompt text
- System instruction
- Model identifier
- Conversation history
- Boolean parameters
- Saved-memory data
- Device identifier
- Chat encoding
- Timeout
- Retry count
- Download URL
- Download destination

### Empty text example

```python
from jibayai import JibayAI, ValidationError

client = JibayAI(api_key="YOUR_API_KEY")

try:
    client.music("")
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

### Invalid device example

```python
try:
    client.image(
        "A city",
        device=-10,
    )
except ValidationError as exc:
    print(exc)
```

### Invalid model syntax

Model identifiers may contain:

```text
Letters
Digits
Period
Underscore
Hyphen
```

Maximum model-name length:

```text
64 characters
```

---

## 20. Model Validation

### Flexible mode

Flexible mode is enabled by default:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=False,
)
```

In flexible mode, the SDK validates the syntax of the model identifier but does not reject a future valid model name solely because it is absent from the built-in list.

### Strict mode

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

When strict mode is enabled, an unsupported model raises `ValidationError` before an HTTP request is sent.

### Built-in known models

```text
jibay-4
jibay-4.1
jibay-5
```

---

## 21. Automatic Retries

The SDK can automatically retry selected temporary failures.

Default retry count:

```text
2
```

Retryable HTTP status codes:

```text
408
429
500
502
503
504
```

The SDK also respects the `Retry-After` response header when supplied by the server.

Disable retries:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    retries=0,
)
```

Increase retries:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    retries=4,
)
```

Use higher retry values carefully, especially in user-facing applications.

---

## 22. Error Handling

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
    result = client.chat(
        text="Hello.",
        model="jibay-5",
    )

    print(result)

except ValidationError as exc:
    print("Invalid parameter:", exc.parameter)
    print(exc)

except AuthenticationError:
    print("The API key is missing, invalid, expired, or disabled.")

except PermissionDeniedError:
    print("The API key does not have permission to access this service.")

except RateLimitError as exc:
    print("The request limit has been exceeded.")
    print("Retry-After:", exc.retry_after)

except TimeoutError:
    print("The request exceeded the configured timeout.")

except NetworkError:
    print("The JibayAI API could not be reached.")

except ServerError as exc:
    print("The JibayAI server returned an error.")
    print("HTTP status:", exc.status_code)

except InvalidResponseError:
    print("The server returned a response that could not be interpreted safely.")

except JibayError as exc:
    print("JibayAI SDK error:", exc)
```

---

## 23. Exception Hierarchy

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

### Exception descriptions

| Exception | Meaning |
|---|---|
| `JibayError` | Base class for all SDK errors |
| `ConfigurationError` | Required client configuration is missing or invalid |
| `ValidationError` | A parameter is invalid before request submission |
| `NetworkError` | A connection or transport problem occurred |
| `TimeoutError` | The request exceeded its timeout |
| `InvalidResponseError` | The response could not be decoded or interpreted safely |
| `APIError` | Base class for unsuccessful API responses |
| `BadRequestError` | The server rejected the request as invalid |
| `AuthenticationError` | API authentication failed |
| `PermissionDeniedError` | Access to the requested service was denied |
| `NotFoundError` | Endpoint or resource was not found |
| `ConflictError` | The request conflicts with the current server state |
| `RateLimitError` | Request or account rate limit was exceeded |
| `ServerError` | The server failed while processing the request |

---

## 24. HTTP Status Mapping

| HTTP status | SDK exception |
|---:|---|
| `400` | `BadRequestError` |
| `401` | `AuthenticationError` |
| `403` | `PermissionDeniedError` |
| `404` | `NotFoundError` |
| `409` | `ConflictError` |
| `422` | `BadRequestError` |
| `429` | `RateLimitError` |
| `500–599` | `ServerError` |
| Other unsuccessful status | `APIError` |

API exceptions may expose:

```python
exc.status_code
exc.response_body
exc.request_id
exc.headers
```

Rate-limit exceptions also provide:

```python
exc.retry_after
```

---

## 25. Built-In Offline Help

The SDK includes help text that does not require an API request.

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

Available topics:

```text
overview
chat
image
music
video
download
models
errors
cli
```

---

## 26. Command-Line Interface

Installing the package adds the `jibayai` command.

### General help

```bash
jibayai --help
```

### Version

```bash
jibayai --version
```

### Chat

```bash
jibayai chat "Hello." --model jibay-5
```

With a system instruction:

```bash
jibayai chat "Explain artificial intelligence." \
  --model jibay-5 \
  --system "Use formal and concise English."
```

With web search:

```bash
jibayai chat "Summarize the requested subject." \
  --model jibay-5 \
  --search-web
```

With an explicit API key:

```bash
jibayai chat "Hello." \
  --model jibay-5 \
  --api-key "YOUR_API_KEY"
```

### Image

```bash
jibayai image "A futuristic city at night"
```

With a manual device value:

```bash
jibayai image "A modern AI laboratory" --device 12345
```

### Music

```bash
jibayai music "Calm cinematic music with piano"
```

### Video

```bash
jibayai video "A cinematic autumn forest"
```

### Offline help

```bash
jibayai help
jibayai help chat
jibayai help image
jibayai help music
jibayai help video
jibayai help errors
```

### Shared CLI options

The service commands support:

```text
--api-key
--base-url
--timeout
--retries
```

Use command-specific help:

```bash
jibayai chat --help
jibayai image --help
jibayai music --help
jibayai video --help
```

---

## 27. Pydroid 3

Install the package from Pydroid's Pip interface by searching for:

```text
jibayai
```

Alternatively, use the Pydroid terminal:

```bash
pip install jibayai
```

Run this code inside the Python editor:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="Hello.",
    model="jibay-5",
)

print(result)
```

Do not paste shell commands such as the following into a Python source file:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

That command belongs in a terminal.

Inside a Python file, use:

```python
import jibayai

print(jibayai.__version__)
```

---

## 28. Termux

Install Python:

```bash
pkg update -y
pkg install python -y
```

Install the SDK:

```bash
python -m pip install jibayai
```

Verify:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

Set the API key:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

Use the command-line interface:

```bash
jibayai chat "Hello." --model jibay-5
```

---

## 29. Security Requirements

API keys are confidential credentials.

Follow these requirements:

- Do not publish API keys in public source code.
- Do not place API keys in public channels or screenshots.
- Do not expose private keys in client-side browser JavaScript.
- Do not commit keys to shared project archives.
- Prefer environment variables on servers.
- Apply access control to production configuration files.
- Rotate a key immediately if it is exposed.
- Avoid writing complete API keys to logs.
- Do not return secret values in API error messages.
- Keep third-party dependencies updated.
- Validate application-level user input in addition to SDK validation.

---

## 30. Troubleshooting

### `ModuleNotFoundError`

Error:

```text
ModuleNotFoundError: No module named 'jibayai'
```

Install into the same interpreter that executes the script:

```bash
python -m pip install jibayai
```

Verify the interpreter:

```bash
python --version
python -m pip --version
```

### API key is required

Use:

```python
client = JibayAI(api_key="YOUR_API_KEY")
```

Or define:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

### Authentication failed

Confirm that:

- The key is complete
- The key contains no additional spaces
- The key is active
- The account can access the selected service

### Request timeout

Increase the timeout for long-running media operations:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)
```

Maximum accepted timeout:

```text
600 seconds
```

### Rate limit

Catch `RateLimitError`:

```python
from jibayai import RateLimitError

try:
    result = client.chat("Hello.")
except RateLimitError as exc:
    print("Retry after:", exc.retry_after)
```

### Invalid parameter

Catch `ValidationError`:

```python
from jibayai import ValidationError

try:
    client.video("")
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

### Existing download file

Use a different destination or explicitly allow replacement:

```python
client.download(
    url,
    "output/file.mp4",
    overwrite=True,
)
```

### Upgrade the package

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

---

## 31. Complete Application Example

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
                text="Write a concise description of a futuristic city.",
                model="jibay-5",
                system="Use professional English.",
            )
            print("Chat result:")
            print(chat_result)

            image_result = client.image(
                "A realistic futuristic city at night, cinematic lighting"
            )
            print("Image result:")
            print(image_result)

            music_result = client.music(
                "Cinematic electronic instrumental music with piano"
            )
            print("Music result:")
            print(music_result)

            video_result = client.video(
                "A cinematic aerial view of a futuristic city at night"
            )
            print("Video result:")
            print(video_result)

        except ValidationError as exc:
            print("Invalid parameter:", exc.parameter)
            print(exc)

        except RateLimitError as exc:
            print("Rate limit exceeded.")
            print("Retry-After:", exc.retry_after)

        except JibayError as exc:
            print("JibayAI error:")
            print(exc)


if __name__ == "__main__":
    main()
```

---

## 32. Public API Reference

### Client

```python
JibayAI(
    api_key=None,
    *,
    base_url="https://jibay.ir",
    timeout=60.0,
    retries=2,
    strict_models=False,
    supported_models=None,
    chat_encoding="json",
    session=None,
)
```

### Chat

```python
client.chat(
    text,
    *,
    model="jibay-4.1",
    system=None,
    chats=None,
    search_web=False,
    signal=False,
    saved_memories=None,
    mode_official=False,
    encoding=None,
)
```

### Image

```python
client.image(
    text,
    *,
    device=None,
)
```

### Music

```python
client.music(text)
```

### Video

```python
client.video(text)
```

### Download

```python
client.download(
    url,
    destination,
    *,
    overwrite=False,
)
```

### Help

```python
client.help(topic=None)
```

### Close

```python
client.close()
```

### Direct functions

```python
jibayai.chat(...)
jibayai.image(...)
jibayai.music(...)
jibayai.video(...)
```

---

## 33. API Endpoints Used by the SDK

| Capability | HTTP method | Endpoint |
|---|---|---|
| Chat | `POST` | `/v1/chat/` |
| Image | `GET` | `/v1/image` |
| Music | `GET` | `/v1/music` |
| Video | `GET` | `/v1/video` |

The default API origin is:

```text
https://jibay.ir
```

---

## 34. Service and SDK Separation

The Python package is a client library. It does not contain the JibayAI models and does not perform generation locally.

Requests are sent to the configured JibayAI API service.

Therefore:

- An internet connection is required.
- A valid API key is required.
- Service availability depends on the remote API.
- API limits and account permissions may apply.
- Generated output is determined by the remote service.
- The SDK version and the service version are managed separately.

---

## 35. License

Copyright © 2026 JibayAI. All applicable rights are reserved except where explicitly granted by the license below.

This project is licensed under:

**Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International**  
**CC BY-NC-ND 4.0**

Official license:

<https://creativecommons.org/licenses/by-nc-nd/4.0/>

Under this license, users may share exact, unmodified copies of the licensed material, provided that all license conditions are followed.

The principal conditions are:

1. **Attribution**  
   Appropriate credit must be provided to JibayAI, the license must be identified, and a link to the official license must be included.

2. **NonCommercial**  
   The material may not be used for commercial purposes without separate written authorization from the rights holder.

3. **NoDerivatives**  
   Modified, remixed, transformed, translated, adapted, or derivative versions may not be distributed without separate written authorization from the rights holder.

4. **No Additional Restrictions**  
   No legal or technological restriction may be applied that prevents recipients from exercising permissions granted by the license.

### Required attribution

A suitable attribution is:

```text
JibayAI Python SDK
Copyright © 2026 JibayAI
Licensed under CC BY-NC-ND 4.0
https://creativecommons.org/licenses/by-nc-nd/4.0/
https://jibay.ir/
```

### Commercial licensing and additional permissions

Commercial use, redistribution of modified versions, integration under incompatible licensing terms, sublicensing, or permissions beyond CC BY-NC-ND 4.0 require separate written authorization from JibayAI.

### Third-party components

Third-party libraries and services remain subject to their own respective licenses and terms. The JibayAI license does not replace or override the licenses of third-party dependencies.

### API service terms

Use of the JibayAI API may also be subject to separate platform terms, account rules, pricing, limits, and acceptable-use requirements.

---

# مستندات فارسی

## ۱. معرفی رسمی

کتابخانه `jibayai` رابط رسمی پایتون برای استفاده از سرویس‌های هوش مصنوعی جیبای است.

این بسته یک ساختار یکپارچه، اعتبارسنجی‌شده و مناسب توسعه‌دهندگان برای ارتباط با قابلیت‌های زیر فراهم می‌کند:

| سرویس | متد پایتون | کاربرد |
|---|---|---|
| چت | `client.chat()` | ارسال پیام، دستور سیستمی، تاریخچه گفتگو و تنظیمات تکمیلی |
| تصویر | `client.image()` | ساخت تصویر از توضیح متنی |
| موسیقی | `client.music()` | ساخت موسیقی از سبک، حس یا توضیح تولید |
| ویدیو | `client.video()` | ساخت ویدیو از پرامپت متنی |

این کتابخانه برای موارد زیر مناسب است:

- سرویس‌های بک‌اند
- اسکریپت‌های خودکار
- نرم‌افزارهای دسکتاپ
- ابزارهای خط فرمان
- پروژه‌های آموزشی
- نمونه‌های اولیه
- محیط Pydroid در اندروید
- محیط Termux در اندروید
- یکپارچه‌سازی سمت سرور

این SDK همگام است و در بخش ارتباط HTTP از کتابخانه `requests` استفاده می‌کند.

---

## ۲. منابع رسمی

| منبع | نشانی |
|---|---|
| صفحه PyPI | <https://pypi.org/project/jibayai/> |
| وب‌سایت جیبای | <https://jibay.ir/> |
| مستندات پلتفرم | <https://platform.jibay.ir/docs/> |
| مجوز | <https://creativecommons.org/licenses/by-nc-nd/4.0/> |

---

## ۳. قابلیت‌های اصلی

کتابخانه قابلیت‌های زیر را ارائه می‌کند:

- نصب عمومی از PyPI
- استفاده مجدد از اتصال‌های HTTP
- ارسال درخواست چت با JSON
- سازگاری با ارسال فرم قدیمی
- ساخت تصویر
- ساخت موسیقی
- ساخت ویدیو
- دریافت کلید API از آرگومان یا متغیر محیطی
- اعتبارسنجی پارامترها قبل از ارسال درخواست
- اعتبارسنجی منعطف یا سخت‌گیرانه مدل
- زمان انتظار قابل تنظیم
- تلاش مجدد خودکار
- خطاهای اختصاصی و ساختاریافته
- پردازش پاسخ JSON
- پشتیبانی از پاسخ متنی
- دانلود فایل‌های تولیدشده
- پشتیبانی از `with`
- توابع مستقیم سطح پکیج
- ابزار خط فرمان
- راهنمای آفلاین داخلی
- پشتیبانی از Python `3.9+`
- انتشار Pure Python و مستقل از سیستم‌عامل

---

## ۴. نصب

نصب آخرین نسخه از PyPI:

```bash
python -m pip install jibayai
```

دستور کوتاه‌تر:

```bash
pip install jibayai
```

به‌روزرسانی نسخه نصب‌شده:

```bash
python -m pip install --upgrade jibayai
```

به‌روزرسانی بدون استفاده از کش:

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

نصب یک نسخه مشخص:

```bash
python -m pip install jibayai==0.1.0
```

---

## ۵. بررسی نصب

در ترمینال:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

خروجی مورد انتظار برای این نسخه:

```text
0.1.0
```

داخل فایل پایتون:

```python
import jibayai

print(jibayai.__version__)
```

بررسی ابزار خط فرمان:

```bash
jibayai --version
```

نمایش راهنمای خط فرمان:

```bash
jibayai --help
```

---

## ۶. نیازمندی‌ها و سازگاری

### نسخه پایتون

حداقل نسخه موردنیاز:

```text
Python >= 3.9
```

بازه هدف پشتیبانی:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

### وابستگی اجرایی

```text
requests >= 2.31, < 3
```

### محیط‌های قابل استفاده

به‌دلیل انتشار به‌صورت Pure Python، کتابخانه در محیط‌های سازگار زیر قابل استفاده است:

- Windows
- Linux
- macOS
- Pydroid در Android
- Termux در Android
- محیط مجازی پایتون
- کانتینرها
- سرورها

---

## ۷. تنظیم کلید API

برای استفاده از سرویس‌ها، کلید معتبر جیبای لازم است.

### واردکردن مستقیم کلید

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")
```

### متغیر محیطی

برای محیط عملیاتی بهتر است کلید خصوصی در کد منبع نوشته نشود.

Linux، macOS یا Termux:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:JIBAYAI_API_KEY="YOUR_API_KEY"
```

Windows Command Prompt:

```cmd
set JIBAYAI_API_KEY=YOUR_API_KEY
```

سپس:

```python
from jibayai import JibayAI

client = JibayAI()
```

اگر `api_key` وارد نشده باشد، کتابخانه متغیر `JIBAYAI_API_KEY` را بررسی می‌کند.

---

## ۸. شروع سریع

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="جیبای را در یک پاراگراف معرفی کن.",
    model="jibay-5",
)

print(result)
```

نوع خروجی می‌تواند یکی از موارد زیر باشد:

- `dict` برای پاسخ JSON شیء
- `list` برای پاسخ JSON آرایه
- `str` برای پاسخ متنی
- سایر مقدارهای سازگار با JSON در صورت ارسال از سمت API

---

## ۹. استفاده از Client ثابت

برای چند درخواست از یک Client ثابت استفاده کنید:

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=60,
    retries=2,
)

chat_result = client.chat(
    "هوش مصنوعی را ساده توضیح بده.",
    model="jibay-5",
)

image_result = client.image(
    "یک مرکز مدرن پژوهش هوش مصنوعی"
)

music_result = client.music(
    "موسیقی الکترونیک سینمایی آرام با پیانو"
)

video_result = client.video(
    "شهر آینده‌نگر در شب با حرکت سینمایی دوربین"
)

print(chat_result)
print(image_result)
print(music_result)
print(video_result)

client.close()
```

استفاده مجدد از Client باعث استفاده مجدد از نشست HTTP و اتصال‌ها می‌شود.

---

## ۱۰. استفاده با `with`

```python
from jibayai import JibayAI

with JibayAI(api_key="YOUR_API_KEY") as client:
    result = client.chat(
        text="سلام.",
        model="jibay-5",
    )

    print(result)
```

بعد از خروج از بلوک `with`، نشست HTTP داخلی به‌صورت خودکار بسته می‌شود.

---

## ۱۱. تنظیمات Client

```python
from jibayai import JibayAI

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

| پارامتر | نوع | مقدار پیش‌فرض | توضیح |
|---|---|---|---|
| `api_key` | `str` یا `None` | متغیر محیطی | کلید API جیبای |
| `base_url` | `str` | `https://jibay.ir` | نشانی پایه API |
| `timeout` | عدد | `60.0` | زمان انتظار درخواست |
| `retries` | `int` | `2` | تعداد تلاش مجدد |
| `strict_models` | `bool` | `False` | فعال‌کردن فهرست محدود مدل‌ها |
| `supported_models` | iterable یا `None` | فهرست داخلی | مدل‌های مجاز در حالت سخت‌گیرانه |
| `chat_encoding` | `str` | `json` | نوع ارسال چت |
| `session` | `requests.Session` یا `None` | نشست داخلی | نشست HTTP سفارشی |

محدوده `timeout`:

```text
بیشتر از 0 و حداکثر 600 ثانیه
```

محدوده `retries`:

```text
عدد صحیح بین 0 تا 10
```

---

## ۱۲. چت هوش مصنوعی

### درخواست پایه

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="یادگیری ماشین چیست؟",
    model="jibay-5",
)

print(result)
```

### مدل پیش‌فرض

در صورت واردنکردن مدل:

```text
jibay-4.1
```

مثال:

```python
result = client.chat(
    "شبکه عصبی را توضیح بده."
)
```

### دستور سیستمی

```python
result = client.chat(
    text="شبکه عصبی را توضیح بده.",
    model="jibay-5",
    system="پاسخ رسمی، دقیق و مختصر باشد.",
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

در هر پیام می‌توان به‌جای `text` از `content` استفاده کرد:

```python
history = [
    {
        "role": "user",
        "content": "زبان برنامه‌نویسی موردعلاقه من پایتون است.",
    },
    {
        "role": "assistant",
        "content": "پایتون برای پروژه‌های هوش مصنوعی مناسب است.",
    },
]

result = client.chat(
    text="من چه زبانی را نام بردم؟",
    chats=history,
)
```

ارسال تاریخچه به‌صورت JSON متنی:

```python
history_json = """
[
  {
    "role": "user",
    "text": "اسم من سارا است."
  },
  {
    "role": "assistant",
    "text": "سلام سارا."
  }
]
"""

result = client.chat(
    text="اسم من چیست؟",
    chats=history_json,
)
```

### فعال‌کردن جستجوی وب

```python
result = client.chat(
    text="موضوع درخواستی را با قابلیت جستجوی وب بررسی کن.",
    model="jibay-5",
    search_web=True,
)
```

### حافظه‌های ذخیره‌شده

```python
result = client.chat(
    text="مطابق ترجیحات ذخیره‌شده پاسخ بده.",
    model="jibay-5",
    saved_memories={
        "language": "fa",
        "response_style": "formal",
    },
)
```

### گزینه‌های تکمیلی

```python
result = client.chat(
    text="سلام.",
    model="jibay-5",
    search_web=False,
    signal=False,
    mode_official=False,
)
```

### نمونه کامل چت

```python
from jibayai import JibayAI

client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=90,
    retries=2,
)

result = client.chat(
    text="یک معرفی کوتاه درباره هوش مصنوعی بنویس.",
    model="jibay-5",
    system="متن رسمی باشد و تکرار اضافی نداشته باشد.",
    chats=[
        {
            "role": "user",
            "text": "مخاطب متن توسعه‌دهندگان نرم‌افزار هستند.",
        },
        {
            "role": "assistant",
            "text": "متوجه شدم.",
        },
    ],
    search_web=False,
    signal=False,
    saved_memories={
        "preferred_language": "fa",
    },
    mode_official=False,
)

print(result)
```

### پارامترهای چت

| پارامتر | نوع قابل قبول | الزامی | توضیح |
|---|---|---:|---|
| `text` | `str` | بله | پیام فعلی کاربر |
| `model` | `str` | خیر | شناسه مدل |
| `system` | `str` یا `None` | خیر | دستور سیستمی |
| `chats` | فهرست، JSON یا `None` | خیر | تاریخچه پیام‌ها |
| `search_web` | boolean-like | خیر | فعال‌سازی جستجوی وب API |
| `signal` | boolean-like | خیر | گزینه Signal |
| `saved_memories` | متن، شیء، فهرست یا `None` | خیر | داده حافظه |
| `mode_official` | boolean-like | خیر | حالت رسمی |
| `encoding` | `json`، `form` یا `None` | خیر | نوع ارسال همین درخواست |

مقدارهای بولی قابل قبول:

```text
True / False
1 / 0
"true" / "false"
"T" / "F"
"yes" / "no"
"on" / "off"
```

---

## ۱۳. ارسال JSON و فرم قدیمی

حالت پیش‌فرض:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="json",
)
```

سازگاری با فرم قدیمی:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    chat_encoding="form",
)

result = client.chat(
    text="سلام.",
    model="jibay-5",
)
```

تغییر نوع ارسال فقط برای یک درخواست:

```python
result = client.chat(
    text="سلام.",
    model="jibay-5",
    encoding="form",
)
```

مقدارهای مجاز:

```text
json
form
```

---

## ۱۴. ساخت تصویر

### نمونه پایه

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.image(
    "یک شهر آینده‌نگر واقعی در شب با نورپردازی سینمایی"
)

print(result)
```

### شناسه دستگاه

سرویس تصویر به یک شناسه عددی مثبت نیاز دارد. اگر `device` وارد نشود، کتابخانه یک مقدار معتبر به‌صورت خودکار تولید می‌کند.

مقدار دستی:

```python
result = client.image(
    "یک آزمایشگاه مدرن هوش مصنوعی",
    device=12345,
)
```

محدوده معتبر:

```text
1 تا 2147483647
```

### پرامپت دقیق‌تر

```python
result = client.image(
    "آزمایشگاه واقع‌گرایانه هوش مصنوعی، معماری سفید و تمیز، "
    "سامانه‌های پردازشی پیشرفته، متریال واقعی، نور حرفه‌ای، نسبت 16:9"
)
```

---

## ۱۵. ساخت موسیقی

### نمونه پایه

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.music(
    "موسیقی سینمایی آرام با پیانو و ویولن"
)

print(result)
```

### پرامپت دقیق‌تر

```python
result = client.music(
    "قطعه بی‌کلام رسمی و سینمایی، ریتم آرام، پیانوی احساسی، "
    "سازهای زهی گرم، فضای الکترونیک ملایم، بدون خواننده"
)
```

پرامپت موسیقی می‌تواند شامل موارد زیر باشد:

- سبک
- حس
- سرعت
- سازها
- باکلام یا بی‌کلام
- شیوه تولید
- فضای صوتی
- کاربرد موردنظر

مثال:

```python
result = client.music(
    "موسیقی الکترونیک بی‌کلام و پرانرژی، ریتم سریع، فضای آینده‌نگر، "
    "بیس عمیق و مناسب ارائه فناوری"
)
```

---

## ۱۶. ساخت ویدیو

### نمونه پایه

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.video(
    "جنگل پاییزی سینمایی با حرکت آرام دوربین"
)

print(result)
```

### پرامپت دقیق‌تر

```python
result = client.video(
    "شهر آینده‌نگر در شب، حرکت هوایی دوربین، باران ملایم، "
    "بازتاب نورهای نئونی، معماری واقعی و حرکت روان"
)
```

پرامپت ویدیو می‌تواند شامل موارد زیر باشد:

- سوژه
- موقعیت
- زاویه دوربین
- حرکت دوربین
- نورپردازی
- آب‌وهوا
- سبک بصری
- نوع حرکت
- فضای کلی
- ترکیب‌بندی

---

## ۱۷. توابع مستقیم

برای اسکریپت‌های کوتاه:

```python
import jibayai

chat_result = jibayai.chat(
    text="سلام.",
    api_key="YOUR_API_KEY",
    model="jibay-5",
)

image_result = jibayai.image(
    text="یک شهر آینده‌نگر",
    api_key="YOUR_API_KEY",
)

music_result = jibayai.music(
    text="موسیقی سینمایی آرام",
    api_key="YOUR_API_KEY",
)

video_result = jibayai.video(
    text="یک جنگل سینمایی",
    api_key="YOUR_API_KEY",
)

print(chat_result)
print(image_result)
print(music_result)
print(video_result)
```

این توابع یک Client موقت می‌سازند و پس از پایان آن را می‌بندند.

برای چند درخواست، استفاده از یک نمونه ثابت `JibayAI` مناسب‌تر است.

---

## ۱۸. دانلود فایل تولیدشده

```python
saved_path = client.download(
    url="https://example.com/generated-file.mp4",
    destination="outputs/video.mp4",
)

print(saved_path)
```

### جایگزینی فایل موجود

```python
saved_path = client.download(
    url="https://example.com/generated-image.png",
    destination="outputs/image.png",
    overwrite=True,
)
```

عملکرد دانلود:

- اعتبارسنجی URL
- ساخت خودکار پوشه‌های لازم
- جلوگیری از بازنویسی فایل موجود
- دانلود جریانی
- ذخیره موقت با پسوند `.part`
- انتقال فایل کامل‌شده به مقصد
- حذف فایل ناقص در صورت بروز خطا
- استفاده از مدیریت timeout و خطاهای SDK

---

## ۱۹. اعتبارسنجی پارامترها

کتابخانه موارد زیر را قبل از ارسال بررسی می‌کند:

- کلید API
- URL پایه
- متن پرامپت
- دستور سیستمی
- شناسه مدل
- تاریخچه گفتگو
- پارامترهای بولی
- داده حافظه
- شناسه دستگاه
- نوع ارسال چت
- زمان انتظار
- تعداد تلاش مجدد
- URL دانلود
- مسیر فایل مقصد

### متن خالی

```python
from jibayai import JibayAI, ValidationError

client = JibayAI(api_key="YOUR_API_KEY")

try:
    client.music("")
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

### شناسه دستگاه نامعتبر

```python
try:
    client.image(
        "یک شهر",
        device=-10,
    )
except ValidationError as exc:
    print(exc)
```

### ساختار نام مدل

شناسه مدل می‌تواند شامل موارد زیر باشد:

```text
حروف
اعداد
نقطه
زیرخط
خط تیره
```

حداکثر طول:

```text
64 کاراکتر
```

---

## ۲۰. اعتبارسنجی مدل

### حالت منعطف

حالت پیش‌فرض:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    strict_models=False,
)
```

در این حالت ساختار نام مدل بررسی می‌شود، اما یک نام معتبر جدید فقط به دلیل نبودن در فهرست داخلی رد نمی‌شود.

### حالت سخت‌گیرانه

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

در این حالت مدل خارج از فهرست با `ValidationError` رد می‌شود.

مدل‌های شناخته‌شده داخلی:

```text
jibay-4
jibay-4.1
jibay-5
```

---

## ۲۱. تلاش مجدد خودکار

تعداد پیش‌فرض:

```text
2
```

کدهای HTTP قابل تلاش مجدد:

```text
408
429
500
502
503
504
```

در صورت وجود هدر `Retry-After`، کتابخانه آن را رعایت می‌کند.

غیرفعال‌کردن:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    retries=0,
)
```

افزایش تعداد:

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    retries=4,
)
```

در نرم‌افزارهای تعاملی از مقدارهای بسیار بالا استفاده نکنید.

---

## ۲۲. مدیریت خطا

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
    result = client.chat(
        text="سلام.",
        model="jibay-5",
    )

    print(result)

except ValidationError as exc:
    print("پارامتر نامعتبر:", exc.parameter)
    print(exc)

except AuthenticationError:
    print("کلید API وارد نشده، نامعتبر، منقضی یا غیرفعال است.")

except PermissionDeniedError:
    print("کلید اجازه دسترسی به این سرویس را ندارد.")

except RateLimitError as exc:
    print("محدودیت درخواست رد شده است.")
    print("Retry-After:", exc.retry_after)

except TimeoutError:
    print("زمان انتظار درخواست تمام شد.")

except NetworkError:
    print("ارتباط با API جیبای برقرار نشد.")

except ServerError as exc:
    print("سرور جیبای خطا برگرداند.")
    print("کد HTTP:", exc.status_code)

except InvalidResponseError:
    print("پاسخ سرور قابل تفسیر ایمن نبود.")

except JibayError as exc:
    print("خطای کتابخانه جیبای:", exc)
```

---

## ۲۳. ساختار خطاها

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

| خطا | توضیح |
|---|---|
| `JibayError` | خطای پایه همه خطاهای SDK |
| `ConfigurationError` | تنظیم ضروری وجود ندارد یا نامعتبر است |
| `ValidationError` | پارامتر قبل از ارسال درخواست نامعتبر است |
| `NetworkError` | خطای شبکه یا ارتباط |
| `TimeoutError` | پایان زمان انتظار |
| `InvalidResponseError` | پاسخ قابل تفسیر ایمن نیست |
| `APIError` | خطای پایه پاسخ‌های ناموفق API |
| `BadRequestError` | درخواست از نظر سرور نامعتبر است |
| `AuthenticationError` | احراز هویت ناموفق |
| `PermissionDeniedError` | دسترسی رد شده است |
| `NotFoundError` | مسیر یا منبع پیدا نشده است |
| `ConflictError` | تعارض با وضعیت فعلی |
| `RateLimitError` | عبور از محدودیت |
| `ServerError` | خطای پردازش سمت سرور |

---

## ۲۴. نگاشت کدهای HTTP

| کد HTTP | خطای کتابخانه |
|---:|---|
| `400` | `BadRequestError` |
| `401` | `AuthenticationError` |
| `403` | `PermissionDeniedError` |
| `404` | `NotFoundError` |
| `409` | `ConflictError` |
| `422` | `BadRequestError` |
| `429` | `RateLimitError` |
| `500–599` | `ServerError` |
| سایر پاسخ‌های ناموفق | `APIError` |

ویژگی‌های خطای API:

```python
exc.status_code
exc.response_body
exc.request_id
exc.headers
```

برای محدودیت درخواست:

```python
exc.retry_after
```

---

## ۲۵. راهنمای آفلاین داخلی

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

موضوع‌های موجود:

```text
overview
chat
image
music
video
download
models
errors
cli
```

---

## ۲۶. ابزار خط فرمان

### راهنمای کلی

```bash
jibayai --help
```

### نسخه

```bash
jibayai --version
```

### چت

```bash
jibayai chat "سلام." --model jibay-5
```

با دستور سیستمی:

```bash
jibayai chat "هوش مصنوعی را توضیح بده." \
  --model jibay-5 \
  --system "پاسخ رسمی و مختصر باشد."
```

با جستجوی وب:

```bash
jibayai chat "موضوع موردنظر را خلاصه کن." \
  --model jibay-5 \
  --search-web
```

با کلید مستقیم:

```bash
jibayai chat "سلام." \
  --model jibay-5 \
  --api-key "YOUR_API_KEY"
```

### تصویر

```bash
jibayai image "یک شهر آینده‌نگر در شب"
```

با شناسه دستگاه:

```bash
jibayai image "آزمایشگاه مدرن هوش مصنوعی" --device 12345
```

### موسیقی

```bash
jibayai music "موسیقی سینمایی آرام با پیانو"
```

### ویدیو

```bash
jibayai video "جنگل پاییزی سینمایی"
```

### راهنمای آفلاین

```bash
jibayai help
jibayai help chat
jibayai help image
jibayai help music
jibayai help video
jibayai help errors
```

گزینه‌های مشترک:

```text
--api-key
--base-url
--timeout
--retries
```

راهنمای هر دستور:

```bash
jibayai chat --help
jibayai image --help
jibayai music --help
jibayai video --help
```

---

## ۲۷. استفاده در Pydroid 3

در بخش Pip برنامه عبارت زیر را جستجو و نصب کنید:

```text
jibayai
```

یا در ترمینال داخلی:

```bash
pip install jibayai
```

داخل ادیتور پایتون:

```python
from jibayai import JibayAI

client = JibayAI(api_key="YOUR_API_KEY")

result = client.chat(
    text="سلام.",
    model="jibay-5",
)

print(result)
```

دستور زیر مخصوص ترمینال است و نباید داخل فایل `.py` نوشته شود:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

داخل فایل پایتون:

```python
import jibayai

print(jibayai.__version__)
```

---

## ۲۸. استفاده در Termux

نصب Python:

```bash
pkg update -y
pkg install python -y
```

نصب کتابخانه:

```bash
python -m pip install jibayai
```

بررسی:

```bash
python -c "import jibayai; print(jibayai.__version__)"
```

ثبت کلید:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

استفاده از CLI:

```bash
jibayai chat "سلام." --model jibay-5
```

---

## ۲۹. الزامات امنیتی

کلید API یک اطلاعات محرمانه است.

- کلید را در کد عمومی منتشر نکنید.
- کلید را در کانال یا تصویر منتشر نکنید.
- کلید خصوصی را داخل JavaScript عمومی قرار ندهید.
- کلید را داخل فایل ZIP عمومی پروژه قرار ندهید.
- در سرور از متغیر محیطی استفاده کنید.
- دسترسی فایل‌های تنظیمات را محدود کنید.
- کلید افشاشده را فوراً تعویض کنید.
- کلید کامل را در Log ننویسید.
- مقدار محرمانه را در پیام خطا برنگردانید.
- وابستگی‌ها را به‌روز نگه دارید.
- علاوه بر اعتبارسنجی SDK، ورودی کاربران برنامه را نیز بررسی کنید.

---

## ۳۰. رفع مشکلات رایج

### خطای نصب‌نبودن ماژول

```text
ModuleNotFoundError: No module named 'jibayai'
```

راه‌حل:

```bash
python -m pip install jibayai
```

بررسی محیط:

```bash
python --version
python -m pip --version
```

### نیاز به کلید API

```python
client = JibayAI(api_key="YOUR_API_KEY")
```

یا:

```bash
export JIBAYAI_API_KEY="YOUR_API_KEY"
```

### خطای احراز هویت

بررسی کنید:

- کلید کامل باشد.
- ابتدا یا انتهای کلید فاصله وجود نداشته باشد.
- کلید فعال باشد.
- حساب به سرویس موردنظر دسترسی داشته باشد.

### پایان زمان انتظار

```python
client = JibayAI(
    api_key="YOUR_API_KEY",
    timeout=180,
)
```

حداکثر:

```text
600 ثانیه
```

### محدودیت درخواست

```python
from jibayai import RateLimitError

try:
    result = client.chat("سلام.")
except RateLimitError as exc:
    print("Retry after:", exc.retry_after)
```

### پارامتر نامعتبر

```python
from jibayai import ValidationError

try:
    client.video("")
except ValidationError as exc:
    print(exc.parameter)
    print(exc)
```

### فایل مقصد از قبل وجود دارد

```python
client.download(
    url,
    "output/file.mp4",
    overwrite=True,
)
```

### به‌روزرسانی

```bash
python -m pip install --upgrade --no-cache-dir jibayai
```

---

## ۳۱. نمونه کامل برنامه

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
                text="توضیح کوتاهی درباره یک شهر آینده‌نگر بنویس.",
                model="jibay-5",
                system="متن رسمی باشد.",
            )
            print("نتیجه چت:")
            print(chat_result)

            image_result = client.image(
                "شهر آینده‌نگر واقع‌گرایانه در شب با نور سینمایی"
            )
            print("نتیجه تصویر:")
            print(image_result)

            music_result = client.music(
                "موسیقی الکترونیک سینمایی بی‌کلام با پیانو"
            )
            print("نتیجه موسیقی:")
            print(music_result)

            video_result = client.video(
                "نمای هوایی سینمایی از شهر آینده‌نگر در شب"
            )
            print("نتیجه ویدیو:")
            print(video_result)

        except ValidationError as exc:
            print("پارامتر نامعتبر:", exc.parameter)
            print(exc)

        except RateLimitError as exc:
            print("محدودیت درخواست.")
            print("Retry-After:", exc.retry_after)

        except JibayError as exc:
            print("خطای جیبای:")
            print(exc)


if __name__ == "__main__":
    main()
```

---

## ۳۲. مرجع API عمومی

### Client

```python
JibayAI(
    api_key=None,
    *,
    base_url="https://jibay.ir",
    timeout=60.0,
    retries=2,
    strict_models=False,
    supported_models=None,
    chat_encoding="json",
    session=None,
)
```

### چت

```python
client.chat(
    text,
    *,
    model="jibay-4.1",
    system=None,
    chats=None,
    search_web=False,
    signal=False,
    saved_memories=None,
    mode_official=False,
    encoding=None,
)
```

### تصویر

```python
client.image(
    text,
    *,
    device=None,
)
```

### موسیقی

```python
client.music(text)
```

### ویدیو

```python
client.video(text)
```

### دانلود

```python
client.download(
    url,
    destination,
    *,
    overwrite=False,
)
```

### راهنما

```python
client.help(topic=None)
```

### بستن

```python
client.close()
```

### توابع مستقیم

```python
jibayai.chat(...)
jibayai.image(...)
jibayai.music(...)
jibayai.video(...)
```

---

## ۳۳. مسیرهای API مورد استفاده

| قابلیت | متد HTTP | مسیر |
|---|---|---|
| چت | `POST` | `/v1/chat/` |
| تصویر | `GET` | `/v1/image` |
| موسیقی | `GET` | `/v1/music` |
| ویدیو | `GET` | `/v1/video` |

نشانی پایه پیش‌فرض:

```text
https://jibay.ir
```

---

## ۳۴. تفاوت SDK و سرویس هوش مصنوعی

این بسته یک کتابخانه کلاینت است. مدل‌های جیبای داخل این کتابخانه قرار ندارند و تولید محتوا به‌صورت محلی انجام نمی‌شود.

درخواست‌ها به API جیبای ارسال می‌شوند.

بنابراین:

- اتصال اینترنت لازم است.
- کلید API معتبر لازم است.
- دسترس‌پذیری به وضعیت سرویس وابسته است.
- محدودیت حساب یا سرویس ممکن است اعمال شود.
- خروجی توسط سرویس راه دور تولید می‌شود.
- نسخه SDK و نسخه سرویس مستقل مدیریت می‌شوند.

---

## ۳۵. مجوز

حق نشر © ۲۰۲۶ JibayAI. کلیه حقوقی که به‌صراحت در مجوز زیر واگذار نشده‌اند محفوظ هستند.

این پروژه تحت مجوز زیر ارائه می‌شود:

**Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International**  
**CC BY-NC-ND 4.0**  
**نسبت‌دادن — غیرتجاری — بدون‌اثر مشتق ۴.۰ بین‌المللی**

نشانی رسمی مجوز:

<https://creativecommons.org/licenses/by-nc-nd/4.0/>

بر اساس این مجوز، کاربران می‌توانند نسخه دقیق و بدون تغییر اثر را به اشتراک بگذارند؛ مشروط بر رعایت تمام شرایط مجوز.

شرایط اصلی:

1. **ذکر منبع**  
   باید نام JibayAI به‌عنوان صاحب اثر ذکر شود، نوع مجوز مشخص باشد و لینک مجوز رسمی ارائه شود.

2. **استفاده غیرتجاری**  
   استفاده تجاری بدون دریافت مجوز کتبی جداگانه از صاحب حقوق مجاز نیست.

3. **عدم انتشار نسخه تغییر‌یافته**  
   نسخه‌های ویرایش‌شده، ترجمه‌شده، بازنویسی‌شده، ترکیب‌شده، اقتباسی یا مشتق‌شده بدون اجازه کتبی جداگانه قابل انتشار نیستند.

4. **عدم ایجاد محدودیت اضافی**  
   استفاده‌کننده نباید محدودیت حقوقی یا فنی اضافه‌ای اعمال کند که مانع استفاده از مجوزهای اعطاشده شود.

### شیوه پیشنهادی ذکر منبع

```text
JibayAI Python SDK
Copyright © 2026 JibayAI
Licensed under CC BY-NC-ND 4.0
https://creativecommons.org/licenses/by-nc-nd/4.0/
https://jibay.ir/
```

### استفاده تجاری و مجوزهای تکمیلی

استفاده تجاری، انتشار نسخه تغییر‌یافته، ادغام تحت شرایط ناسازگار، صدور مجوز فرعی یا هر استفاده‌ای خارج از محدوده CC BY-NC-ND 4.0 به اجازه کتبی جداگانه از JibayAI نیاز دارد.

### اجزای شخص ثالث

کتابخانه‌ها، سرویس‌ها و اجزای شخص ثالث تابع مجوزها و شرایط مستقل خود هستند. مجوز جیبای جایگزین مجوز اجزای شخص ثالث نمی‌شود.

### شرایط سرویس API

استفاده از API جیبای ممکن است علاوه بر این مجوز، تابع قوانین حساب، محدودیت‌ها، تعرفه‌ها، شرایط پلتفرم و سیاست استفاده قابل قبول باشد.

---

## Copyright Notice | اعلام حق نشر

```text
Copyright © 2026 JibayAI
All rights reserved except as expressly granted under CC BY-NC-ND 4.0.
```

```text
حق نشر © ۲۰۲۶ JibayAI
تمام حقوق به‌جز مواردی که صریحاً تحت CC BY-NC-ND 4.0 اعطا شده‌اند محفوظ است.
```
