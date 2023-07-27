import os
from bardapi import Bard


class BardAgent:
    def __init__(self, token):
        os.environ['_BARD_API_KEY'] = token
        self.agent = Bard()

    def get_result(self, input_text):
        return self.agent.get_answer(input_text)

