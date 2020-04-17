from model2module.models import ModelTemplate

dataset = [
    "Nakakaasar nman! ahhh... ang dami dami kong gagawin... kulang time...",
    "Asar... Badtrip!",
    "May bagong bagyo ang namataan sa kanlurang bahagi ng bansa.",
    "Thank you po Lord Jesus at gumana din sya.",
    "Congrats po sa inyong lahat!",
    "Ano, sasagot ka pa? Ha?"
]

model = ModelTemplate()
pred = model.predict_dataset(dataset, raw_output=False, output_type=[
                             'emotion', 'sentiment'])
print(pred)
