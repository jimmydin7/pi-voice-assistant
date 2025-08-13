import requests

def get_joke(topic):
    url = f"https://v2.jokeapi.dev/joke/{topic}?blacklistFlags=nsfw,sexist&type=twopart&safe-mode"
    data = requests.get(url).json()

    if data.get("error") and data.get("code") == 106:
        print(f"no jokes found for '{topic}'. trying random category instead...")
        return get_joke("Any")

    if data["type"] == "twopart":
        print(data["setup"])
        print(data["delivery"])
    else:
        print(data["joke"])

