# app-privategpt-llm

# LLM to train your private data

LLM to train using your data...

## Installation

Recommend installing anaconda to create your virtual environment and install the libraries in your virtual env
```bash
pip3 install -r requirements.txt
```
```bash
download the LLM model and place it in a models directory:
- LLM: default to [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). If you prefer a different GPT4All-J compatible model, just download it and reference it in your `.env` file.
```
```bash
cp example.env .env
```

```bash
add all your train pdf files to source_documents folder
```

```bash
python ingest.py
```

```bash
python privateGPT.py
```

```bash
Enter a query: which companies have warren invested?```
