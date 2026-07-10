from openai import OpenAI


class LocalLLM:

    def __init__(self):
        self.client = OpenAI(
            base_url="http://127.0.0.1:11434/v1",
            api_key="not-needed",
        )

        # Discover the loaded model automatically
        models = self.client.models.list()
        self.model = models.data[0].id

    def ask(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert options trader and quantitative "
                        "analyst. Explain your reasoning clearly and avoid "
                        "making unsupported claims."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
            max_tokens=500,
        )

        return response.choices[0].message.content
