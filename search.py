```python
import re
from chat_history import chatHistory

class Search:
    def __init__(self):
        self.searchBar = None

    def create_search_bar(self):
        # Code to create a search bar using a GUI library like tkinter or PyQt
        pass

    def search_chat(self, keyword, filter_options=None):
        results = []
        for chat in chatHistory:
            if re.search(keyword, chat['message'], re.I):
                if filter_options:
                    if self.apply_filters(chat, filter_options):
                        results.append(chat)
                else:
                    results.append(chat)
        return results

    def apply_filters(self, chat, filter_options):
        for key, value in filter_options.items():
            if key == 'date':
                if chat['date'] != value:
                    return False
            elif key == 'file_type':
                if chat['file_type'] != value:
                    return False
        return True
```