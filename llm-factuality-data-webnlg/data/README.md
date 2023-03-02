# data format

fields: <br />
"prompt" - prompt presented to model, in the form "Explain A, including information about B, C" <br />
"output" - model generated ouptut <br />
"model" - model used (currently only text-davinci-003) <br />
"category" - category of entity A (food, athlete, etc.) <br />
"id" - original id number in web nlg dataset <br />
"orig_entity_info" - stores web nlg entity/info pairing as fields (ex. "birth_date" : "April 1, 2000") <br />
<br />
{ <br />
&nbsp;&nbsp;&nbsp;&nbsp;"prompt": "Explain A, including information about B, C", <br />
&nbsp;&nbsp;&nbsp;&nbsp;"output": "\n\nA is the...", <br />
&nbsp;&nbsp;&nbsp;&nbsp;"model": "model_name", <br />
&nbsp;&nbsp;&nbsp;&nbsp;"category": "category_name", <br />
&nbsp;&nbsp;&nbsp;&nbsp;"id": "Id#", <br />
&nbsp;&nbsp;&nbsp;&nbsp;"orig_entity_info": { <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"B": "B_entity_info", <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"C": "C_entity_info" <br />
&nbsp;&nbsp;&nbsp;&nbsp;} <br />
  } <br />
  
