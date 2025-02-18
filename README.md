# Jarvis

Jarvis is an advanced AI-powered Discord bot built to interact with a large language model (LLM) to provide intelligent, human-like responses. Inspired by Iron Man's AI assistant, Jarvis, this bot allows users to ask questions or give prompts, and receive thoughtful, AI-generated responses.

The bot communicates with an LLM model hosted on a server, capable of generating text based on a variety of prompts. Whether you're looking for casual conversations or more complex problem-solving assistance, Jarvis is designed to provide useful and engaging interactions.


I used docker compose to run in but it has a private token so here just the skeleton:
```
services:
  llm_server:
    build:
      context: ./llm_server
    ports:
      - "8000:8000"
    container_name: llm_server
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility


  discord_bot:
    build: ./discord_bot
    container_name: discord_bot
    environment:
      - DISCORD_BOT_TOKEN=DISCORD_BOT_TOKEN
    depends_on:
      - llm_server
```
