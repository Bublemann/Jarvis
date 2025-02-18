FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip git
RUN pip install fastapi uvicorn torch transformers accelerate sentencepiece
ENV PIP_ROOT_USER_ACTION=ignore

COPY app.py /app/app.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
