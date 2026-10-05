# CLI-chatbot

A small interactive command-line chatbot powered by Groq. It is configured to
act as a helpful coding tutor and explain concepts simply. Conversation history
is sent with each request so the bot can follow the current chat.

## Requirements

- Python 3.12 or newer
- A Groq API key with access to the configured model, `openai/gpt-oss-20b`

## Configure the API key

The app reads the key from the `GROQ_API_KEY` environment variable. In Replit,
add it under **Tools → Secrets**. Do not put the key in `main.py`, this README,
or source control.

For a local environment, set `GROQ_API_KEY` in your shell or your preferred
secret manager before starting the app.

## Install and run

Install the Python dependency:

```bash
python -m pip install groq
```

Start the chatbot from the project root:

```bash
python main.py
```

When it starts, enter a message at the `You:` prompt. Type `quit` to end the
conversation. You can also stop it with `Ctrl+C`.

## Project files

- `main.py` — interactive chat loop and Groq API calls
- `pyproject.toml` — Python version and dependency metadata

## Troubleshooting

- **Missing `GROQ_API_KEY`:** Add the secret to the environment, then restart
  the run process.
- **Authentication or access error:** Check that the key is valid and that the
  Groq account can access the configured model.
- **Model not found:** Update the `model` value in `main.py` to a model ID
  available to your Groq account.
