from template import call_openai

prompt = "Hãy kể cho tôi một sự thật thú vị về Hà Nội."

for temp in [0.0, 0.7, 1.2, 1.8]:
    answer, latency = call_openai(prompt, temperature=temp)
    print(f"\n=== temperature={temp} | {latency:.2f}s ===")
    print(answer)