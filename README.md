# llm-factuality-analysis

All dataset creation info stored under llm-factuality-data-webnlg folder.

llm-factuality-data-webnlg/src holds code for data generation - corpus-reader obtained from [Web-NLG corpus reader](https://gitlab.com/webnlg/corpus-reader/-/tree/master).

llm-factuality-data-webnlg/data holds data - original_nlg_data/train holds [Web-NLG training data](https://gitlab.com/shimorina/webnlg-dataset/-/tree/master/release_v3.0/en/train), webnlg-prompt-gen-dataset.json stores GPT3 generated data on WebNLG (about 136 json objects), webnlg-prompt-gen-large.json stores all the two triple prompts (about 1103 json objects) and webnlg-prompt-gen-small.json stores GPT3 generated data with less prompts (about 24 json objects).
