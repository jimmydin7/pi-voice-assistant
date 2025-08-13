import os
import json

class TodoControl:
    def __init__(self, filename):
        self.todos = []
        self.filename = filename

    def _load_items(self):
        
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []
    
    def _save_items(self, item):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=1)

    def add_item(self, item):
        self.todos.append(item)
        self._save_items()

    def read_items(self):
        if not self.todos:
            return "empty todo list"
        
        else:
            return self.todos
        
    def remove_item(self, index):

        if 0 <= index - 1 < len(self.todos):

            removed = self.todos.pop(index - 1)
            self._save_items()
            return f"removed {removed}"
            
        else:
            return "invalid index"