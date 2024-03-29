import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    GenerationConfig,
)


def generate(
    model_name="replit/replit-code-v1_5-3b", hint="def fibonacci(n):", bnb_quan=True
):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    generation_config = GenerationConfig.from_pretrained(model_name, max_length=1024)
    if bnb_quan:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            quantization_config=quantization_config,
            device_map="auto",
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            device_map="auto",
        )

    inputs = tokenizer.encode(hint, return_tensors="pt").cuda()
    sample = model.generate(inputs, generation_config=generation_config)

    return tokenizer.decode(sample[0])


if __name__ == "__main__":
    code = generate(
        # "Salesforce/codegen25-7b-multi",
        # bnb_quan=False,
    )
    print("======================================================")
    print(code)
    print("======================================================")
