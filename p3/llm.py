from transformers import AutoTokenizer, AutoModelForCausalLM

model = "meta-llama/Llama-3.2-1b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model)