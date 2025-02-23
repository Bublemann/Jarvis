from fastapi import FastAPI
from pydantic import BaseModel
from torch import bfloat16
import transformers


MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=MODEL_ID,
    model_kwargs={"torch_dtype": bfloat16},
    device_map="cuda",
)

class PromptRequest(BaseModel):
    prompt: str

app = FastAPI()

@app.post("/generate")
async def generate(request: PromptRequest):
    message = [
        {"role": "user", "content": request.prompt},
    ]

    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    output = pipeline(
        message,
        max_new_tokens=2048,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

    return output[0]["generated_text"][-1]["content"]

@app.get("/health")
def health():
    return {"status": "ok"}
