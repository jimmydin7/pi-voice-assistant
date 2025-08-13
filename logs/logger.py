import datetime

levels = {
    "info": "[INFO]",
    "warning": "[WARNING]",
    "error": "[ERROR]",
    "speech": "[SPEECH]"
}


colors = {
    "info": "\033[94m",  
    "warning": "\033[93m",  
    "error": "\033[91m", 
    "speech": "\033[92m"
}

def get_time():
    return f"({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"


def log(content, level):
    level_text = levels[level]
    colour = colors[level]

    print(f"{colour}{get_time()}{level_text} - {content}")

