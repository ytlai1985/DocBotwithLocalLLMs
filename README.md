# Doc Bot with Local LLMs

## Preparation
```commandline
git clone https://github.com/ytlai1985/DocBotwithLocalLLMs.git
cd DocBotwithLocalLLMs
pip install -r requirements.txt
```

# Deploy your LLMs
## Controller
```commandline
python -m fastchat.serve.controller --host 127.0.0.1 --port 21001
```

## Worker
```commandline
python -m fastchat.serve.model_worker --model-name 'blah' --model-path path --host 127.0.0.1 --port 21002 --controller-address http://127.0.0.1:21001
```

## Openai API
```commandline
python -m fastchat.serve.openai_api_service --host 127.0.0.1 --port 5566 --controller-address http://127.0.0.1:21001
```

## Open Gradio
```commandline
python bot.py
```

You should set your Bard token in bot.py