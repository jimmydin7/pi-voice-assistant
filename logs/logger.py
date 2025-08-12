import datetime

levels = {
    "info": "[INFO]",
    "warning": "[WARNING]",
    "error": "[ERROR]",
    "speech": "[SPEECH]"
}

def get_time():
    return f"({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"


def log(content, level):
    level_text = levels[level]

    print(f"{get_time()}{level_text} - {content}")

