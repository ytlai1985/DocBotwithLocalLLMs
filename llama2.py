import openai


class MyLLAMA:
    def __init__(self, host):
        openai.api_key = 'EMPTY'
        openai.api_base = f'http://{host}/v1'

    @staticmethod
    def get_result(input_prompt):
        return openai.ChatCompletion.create(
            model='llama2-7b',
            messages=[{"role": "user", "content": input_prompt}],
        )['choices'][0]['message']['content']


if __name__ == '__main__':
    bot = MyLLAMA('127.0.0.1:5566')
    prompt = 'who is the famous USA actor'

    res = bot.get_result(prompt)
    print(res)
