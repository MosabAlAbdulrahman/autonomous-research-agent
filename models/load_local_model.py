from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model():
    model_id = "microsoft/phi-2"  # use phi-3 or mistral from HF if needed
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe
