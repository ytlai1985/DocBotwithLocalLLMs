import gradio as gr
from bard import BardAgent
from langc import ChromaQA
from llama2 import MyLLAMA


bard_token = 'YwhrVv6pALiz8zfBx8r6c_OBFQ.'
local_host = '127.0.0.1:5566'
llm = BardAgent(bard_token)
llm_local = MyLLAMA(local_host)
data_dir = './uploads/'


def user(message, history):
    return "", history + [[message, None]]


def bot(bot_name, input_file, history, with_data):
    user_message = history[-1][0]
    cq = ChromaQA(input_file.name, user_message)
    results, temp = cq.get_result()
    if bot_name == 'Local LLM':
        results = llm_local.get_result(results)
    else:
        results = llm.get_result(results)['content']

    if with_data:
        results += f'\n\nSearch result:\n{temp}'

    response = [user_message, results]
    response = [(response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)]
    history[-1] = response[0]
    del cq
    return history


def upload_file(files):
    return files.name


with gr.Blocks() as demo:
    gr.Markdown('# Demo')

    with gr.Tab('Chat Bot'):
        file_output = gr.File()
        upload_button = gr.UploadButton("Click to Upload a File", file_types=[".pdf"])
        with gr.Row():
            with gr.Column():
                bot_list = gr.Dropdown(['Bard', 'Local LLM'], label='Language Model')
            with gr.Column():
                res_flag = gr.Checkbox(label="Sure", info="Return Search Result")

        chatbot = gr.Chatbot(height=500)
        msg = gr.Textbox()
        clear = gr.Button("Clear")

        upload_button.upload(upload_file, upload_button, file_output)
        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).\
            then(bot, [bot_list, upload_button, chatbot, res_flag], chatbot)
        clear.click(lambda: None, None, chatbot, queue=False)


if __name__ == "__main__":

    demo.queue().launch(
        # server_name='10.82.185.23',
        # server_port=8000,
        # inline=False
    )
