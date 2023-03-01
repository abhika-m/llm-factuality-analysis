import openai
import json
from api import api_key
from corpus_reader.benchmark_reader import Benchmark
from corpus_reader.benchmark_reader import select_files

openai.api_key = api_key

b = Benchmark()
files = select_files('./original_nlg_data/train')
b.fill_benchmark(files)
v = b.verbalisations()
# print("Number of entries: ", b.entry_count())
# print(b.filter(cat=["Food"]).unique_p_mtriples())
# for i in range(b.entry_count()):
#     e = b.entries[i]
#     print(e.unique_p_mtriples())
#     if len(e.relations()) == 3 and e.shape_type == "sibling":
#         print(v[i])
#         print(e.list_triples()[0])
#         #print(e.relations())
#     i += 5000
# entry = b.entries[514]
# print(entry.relations())

result = []

def retrieveOutputGPT3(prompt_input, model_input):
    response = openai.Completion.create(
        model=model_input,
        prompt=prompt_input,
        max_tokens=2048,
        temperature=0
    )
    
    return response.choices[0].text

def retrieveOutputChatGPT(prompt_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt_input}
        ]
    )   
    return response.choices[0].message.content

def create_prompt(subject, entities):
    parts = subject.split("_")
    subject = ""
    for p in parts:
        subject += " "
        subject += p
    prompt = "Explain" + subject +", including information about " 
    for i in range(len(entities) - 1):
        prompt += entities[i] 
        prompt += ", "
    
    prompt += entities[len(entities) - 1]
    return prompt

def create_json(dictionary):
    json_object = json.dumps(dictionary)
    with open("train.json", "w") as outfile:
        outfile.write(json_object)

def camelCaseFormat(word):
    if(word.lower() == word):
        return word
    else:
        words = [[word[0]]]
        for c in word[1:]:
            if words[-1][-1].islower() and c.isupper():
                words.append(list(c))
            else:
                words[-1].append(c)
 
        w = [''.join(word) for word in words]
        word = ""
        for i in range(len(w) - 1):
            word += w[i].lower()
            word += " "
        word += w[len(w) - 1].lower()
        return word

for i in range(0, b.entry_count()):
    e = b.entries[i]
    entities = []

    if e.shape_type == "sibling" and e.size == "2":
        triples = e.list_triples()
        es = triples[0].split(" | ")
        subject = es[0]
        e1 = camelCaseFormat(es[1])
        e1d = es[2]
        es = triples[1].split(" | ")
        e2 = camelCaseFormat(es[1])
        e2d = es[2]
        if(e1 != e2):
            entities.append(e1)
            entities.append(e2)
            prompt = create_prompt(subject, entities)
            outputGPT3 = retrieveOutputGPT3(prompt, "text-davinci-003")
            dict = {"prompt": prompt, "output": outputGPT3, "model": "text-davinci-003",  "category":e.category, "id":e.id, "orig_entity_info":{e1.replace(" ", "_"):e1d, e2.replace(" ", "_"):e2d}}
            result.append(dict)

for i in range(0, b.entry_count()):
    e = b.entries[i]
    entities = []

    if e.shape_type == "sibling" and e.size == "2":
        triples = e.list_triples()
        es = triples[0].split(" | ")
        subject = es[0]
        e1 = camelCaseFormat(es[1])
        e1d = es[2]
        es = triples[1].split(" | ")
        e2 = camelCaseFormat(es[1])
        e2d = es[2]
        if(e1 != e2):
            entities.append(e1)
            entities.append(e2)
            prompt = create_prompt(subject, entities)
            outputChatGPT = retrieveOutputChatGPT(prompt)
            dict = {"prompt": prompt, "output": outputChatGPT, "model": "gpt-3.5-turbo",  "category":e.category, "id":e.id, "orig_entity_info":{e1.replace(" ", "_"):e1d, e2.replace(" ", "_"):e2d}}
            result.append(dict)

create_json(result)