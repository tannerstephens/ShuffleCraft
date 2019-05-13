import glob, json, random, zipfile, os, io

dir_path = os.path.dirname(os.path.realpath(__file__))

def make_shuffled_datapack(version):
  recipes = {}
  results = {}
  items = []

  for file in glob.glob(dir_path + '/versions/' + version + '/*.json'):
    try:
      name = file.split('/')[-1][:-5]

      if name in ['crafting_table', 'furnace']:
        continue
      
      if 'planks' in name:
        continue

      with open(file) as f:
        data = json.load(f)

      if 'result' not in data:
        continue

      if 'crafting_shaped' in data['type']:
        recipe = dict(type=data['type'], pattern=data['pattern'], key=data['key'])
      elif 'crafting_shapeless' in data['type']:
        recipe = dict(type=data['type'], ingredients=data['ingredients'])
      elif 'stonecutting' in data['type']:
        continue
      else:
        recipe = dict(type=data['type'], ingredient=data['ingredient'], cookingtime=data['cookingtime'], experience=data['experience'])

      result = dict(result=data['result'], name=name)

      if 'group' in data:
        result['group'] = data['group']

      recipes[name] = recipe
      results[name] = result
      items.append(name)
    except Exception as e:
      print(file.split("\\")[-1].split("_")[-1])

  items2 = items[:]
  random.shuffle(items2)

  for s,d in zip(items, items2):
    recipes[s].update(results[d])
    if 'smelting' in recipes[s]['type']:
      if isinstance(recipes[s]['result'], dict):
        recipes[s]['result'] = recipes[s]['result']['item']
    else:
      if isinstance(recipes[s]['result'], str):
        recipes[s]['result'] = dict(item=recipes[s]['result'])
        

  output = io.BytesIO()
  zipo = zipfile.ZipFile(output, mode='w')

  zipo.writestr('pack.mcmeta', json.dumps({'pack': {'pack_format': 4, 'description': 'Tutorial Resource Pack'}}))

  for recipe in recipes:
    zipo.writestr('data/minecraft/recipes/' + recipes[recipe]['name'] + '.json', json.dumps(recipes[recipe]))

  zipo.close()

  output.seek(0)

  return output

def get_versions():
  versions = []
  for file in glob.glob(dir_path + '/versions/*'):
    versions.append(file.split("/")[-1])
  return versions


if __name__ == "__main__":
  with open("pack.zip", 'wb') as f:
    f.write(make_shuffled_datapack().read())
