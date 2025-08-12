import datetime

levels = {
    "info": "[INFO]",
    "warning": "[WARNING]",
    "error": "[ERROR]"
}

def get_time():
    return f"({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"


def create_log(content, level):
    level_text = levels[level]

    print(f"{get_time()}{level_text} - {content}")

create_log('test', 'info')