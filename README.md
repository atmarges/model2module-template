# Model2Module Template
Deploy your trained deep learning models for NLP as simple python module.

*Note: Only applicable for NLP models trained using Keras*

## Quickstart
Create an instance of `ModelTemplate` and initialize it with the path of the following files:

- `json_file` - the .json file that contains the structure of your deep neural network model
- `weight_file` - the file containing the weights of your trained model
- `words_file` - a .tsv file containing a list of your word tokens. The first column should be the index of each word followed by the actual word tokens
- `classes_file` - a .tsv file containing a list of the class labels used on your model. You can include multiple labels by creating multiple columns. The first row will be the headers which will be later used to switch between different class labels.

Below is a sample code using a machine learing model trained for emotion classification:

```python
from model2module.models import ModelTemplate

dataset = [
    "Nakakaasar nman! ahhh... ang dami dami kong gagawin... kulang time...",
    "Asar... Badtrip!",
    "May bagong bagyo ang namataan sa kanlurang bahagi ng bansa.",
    "Thank you po Lord Jesus at gumana din sya.",
    "Congrats po sa inyong lahat!",
]

json_file='C:/location/of/model/json_file.json',
weight_file='C:/location/of/model/weight_file.h5',
words_file='C:/location/of/model/words.tsv',
classes_file='C:/location/of/model/classes.tsv'

model = ModelTemplate(json_file=json_file, weight_file=weight_file,
                       words_file=words_file, classes_file=classes_file)
pred = model.predict_dataset(dataset, output_type='emotion')
print(pred)

```

You can set `raw_output=True` in the `ModelTemplate.predict_dataset()` function to retrieve output in vector form.

Below is what **classes_file.tsv** looks like. The first row contains the header which can be used in the `output_type` parameter of the `ModelTemplate.predict_dataset()` function

```bash
index	emoji	emotion	sentiment
0	📝	neutral	neutral
1	😄	happy	positive
2	😌	relief	positive
3	😑	unammused	negative
4	😘	love	positive
5	😜	playful	positive
6	😞	sad	negative
7	😡	angry	negative
8	😱	shocked	negative
9	😷	sick	negative
10	🤔	pondering	neutral
```

The file **words_file.tsv** looks like this. The first column contains the indexes of the tokens followed by the actual words.

```bash
1	aacts
2	aad
3	aada
4	aadal
5	aadalan
6	aadapt
7	aadc
8	aadd
9	aaddict
10	aadfghjkl
```
