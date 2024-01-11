```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class UserProfile(QWidget):
    def __init__(self):
        super().__init__()

        self.userProfile = {
            "name": "",
            "avatar": "",
            "bio": ""
        }

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name")
        self.name_input = QLineEdit()
        self.name_input.textChanged.connect(self.update_name)

        self.avatar_label = QLabel("Avatar")
        self.avatar_input = QLineEdit()
        self.avatar_input.textChanged.connect(self.update_avatar)

        self.bio_label = QLabel("Bio")
        self.bio_input = QLineEdit()
        self.bio_input.textChanged.connect(self.update_bio)

        self.save_button = QPushButton("Save Profile")
        self.save_button.clicked.connect(self.save_profile)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.avatar_label)
        layout.addWidget(self.avatar_input)
        layout.addWidget(self.bio_label)
        layout.addWidget(self.bio_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def update_name(self, text):
        self.userProfile["name"] = text

    def update_avatar(self, text):
        self.userProfile["avatar"] = text

    def update_bio(self, text):
        self.userProfile["bio"] = text

    def save_profile(self):
        # Here you can add code to save the profile data to a database or file
        pass
```