system_prompt="Give the glycemic index, grams of sugar, grams of carbohydrate, and grams of fat of X, where X is a food name given in the next prompt. \nGive the glycemic index level according to glycemic index Y:\nY >= 70 (tinggi)\nY >= 56 (sedang)\nY >= 0 (rendah)\nGive it in this json format example:\n\n{\n  \"name\": \"Fried Rice\",\n  \"glycemicIndex\": 80.0,\n  \"glycemicIndexLevel\": \"tinggi\",\n  \"sugar\": 7.0,\n  \"carbohydrate\": 31.0,\n  \"fat\": 19.0\n}"
current_model="claude-3-haiku-20240307"

def generate_prompt(food_name: str, client):
    return client.messages.create(
        model=current_model,
        max_tokens=300,
        temperature=0,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": food_name
                    }
                ]
            }
        ]
    )