#!/bin/bash
uvicorn llm_server:app --host 0.0.0.0 --port 8000 &

while true; do
    response=$(curl -s http://localhost:8000/health)
    status=$(echo "$response" | jq -r '.status')
    if [[ "$status" == "ok" ]]; then
        break
    fi
    sleep 2
done

python discord_bot.py
