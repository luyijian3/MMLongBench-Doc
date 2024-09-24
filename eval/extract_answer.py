from openai import OpenAI
client = OpenAI(api_key="sk-FHMGSN9J5GDLn9QX0a0c1a049a054bC181Ff15A31f74Bd62",
            base_url="https://svip.xty.app/v1")


def extract_answer(question, output, prompt, model_name="gpt-4o"):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
                {
                "role": "assistant",
                "content": "\n\nQuestion:{}\nAnalysis:{}\n".format(question, output)
                }
            ],
            temperature=0.0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = response.choices[0].message.content
    except:
        response = "Failed"
    
    return response