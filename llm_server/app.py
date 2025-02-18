from fastapi import FastAPI
import transformers
import torch

app = FastAPI()

# Modell laden
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="cuda",
)

@app.post("/generate")
async def generate(prompt: str):
    message = [
        {"role": "user", "content": prompt},
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
