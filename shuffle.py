import glob, json, random, zipfile, os

def zipdir(path, zip_path):
    ziph = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            aname = os.path.join(root, file)[15:]
            ziph.write(os.path.join(root, file), aname)
    ziph.close()


recipes = {}
results = {}
items = []

for file in glob.glob("./original_recipes/*"):
    with open(file) as f:
        data = json.load(f)

    name = file.split("\\")[-1][:-5]

    if data["type"] == "crafting_shaped":
        recipe = dict(type=data["type"], pattern=data["pattern"], key=data["key"])
    elif data["type"] == "crafting_shapeless":
        recipe = dict(type=data["type"], ingredients=data["ingredients"])
    else:
        recipe = dict(type=data["type"], ingredient=data["ingredient"], cookingtime=data["cookingtime"], experience=data["experience"])

    result = dict(result=data["result"])

    if "group" in data:
        result["group"] = data["group"]

    recipes[name] = recipe
    results[name] = result
    items.append(name)

items2 = items[:]
random.shuffle(items2)

for s,d in zip(items, items2):
    recipes[s].update(results[d])
    if recipes[s]["type"] == "smelting":
        if isinstance(recipes[s]["result"], dict):
            recipes[s]["result"] = recipes[s]["result"]["item"]
    else:
        if isinstance(recipes[s]["result"], str):
            recipes[s]["result"] = dict(item=recipes[s]["result"])
            
        

for recipe in recipes:
    with open("./ShuffleCraft/data/minecraft/recipes/" + recipe + ".json", "w") as f:
        json.dump(recipes[recipe], f)


zipdir("./ShuffleCraft", "./ShuffleCraft.zip")
