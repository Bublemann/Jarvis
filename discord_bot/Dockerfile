FROM python:3.10

WORKDIR /app

RUN pip install discord.py httpx

COPY app.py /app/app.py

ENV DISCORD_BOT_TOKEN="DEIN_DISCORD_TOKEN"
ENV PIP_ROOT_USER_ACTION=ignore

CMD ["python", "app.py"]
