import openai

def read_api_key(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()

def select_GPT_3_model():
    prompt = "1 = text-davinci-003\n"
    prompt += "2 = text-curie-001\n"
    prompt += "3 = text-babbage-001\n"
    prompt += "4 = text-ada-001\n"
    prompt += "\n"
    prompt += "Choisir le modèle à utiliser : \n"
    model_id = int(input(prompt))
    models = {1: "text-davinci-003", 2: "text-curie-001", 3: "text-babbage-001", 4: "text-ada-001"}
    if model_id in models:
        return models[model_id]
        print("\n")
    else:
        print("Modèle non valide")
        print("\n")
        return None

def select_GPT_3_temperature():
    prompt = "Choisir le degré de créativité entre 0 (pas créatif) à 1 (très créatif) : \n"
    temperature = float(input(prompt))
    temperature = min(1, max(0, temperature))
    print("\n")
    return temperature

def select_GPT_3_token():
    prompt = "Choisir le nombre de tokens (défaut = 1024) - attention ce sera débité du crédit: \n"
    tokens = int(input(prompt))
    print("\n")
    return tokens

def main():
    api_key = read_api_key("openAI_KEY.txt")
    openai.api_key = api_key
    model_engine = select_GPT_3_model()
    if model_engine:
        temperature = select_GPT_3_temperature()
        tokens = select_GPT_3_token()
        ### Generate text
        prompt = str(input("Poses ta question : "))
        completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=tokens,n=1,stop=None,temperature=temperature)
        message=completions.choices[0].text
        print("\n")
        print("Proposition de chatGPT, avec le modele de langage",model_engine," ,la créatitivité à ",temperature*100," et une consommation de ",tokens,"tokens")
        print(message)
        print("\n")
        print("**************************************")
        print("Le code a consommé :",completions.usage)
        print("**************************************")

#########################################################

if __name__ == "__main__":
    main()




