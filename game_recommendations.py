```python
import random

class GameRecommendation:
    def __init__(self):
        self.game_database = [
            {"name": "Minecraft", "genre": "Sandbox, Survival"},
            {"name": "Among Us", "genre": "Party, Strategy"},
            {"name": "Valorant", "genre": "Shooter"},
            {"name": "Cyberpunk 2077", "genre": "RPG"},
            {"name": "The Witcher 3", "genre": "RPG"},
            {"name": "Fortnite", "genre": "Battle Royale, Shooter"},
            {"name": "League of Legends", "genre": "MOBA"},
            {"name": "Genshin Impact", "genre": "RPG"},
            {"name": "Fall Guys", "genre": "Party"},
            {"name": "FIFA 21", "genre": "Sports"},
        ]

    def recommend_game(self, user_profile):
        user_interests = user_profile.get('interests', [])
        recommended_games = []

        for game in self.game_database:
            if any(interest.lower() in game['genre'].lower() for interest in user_interests):
                recommended_games.append(game)

        if not recommended_games:
            recommended_games = self.game_database

        return random.choice(recommended_games)

def recommend_game(userProfile):
    game_rec = GameRecommendation()
    recommended_game = game_rec.recommend_game(userProfile)
    return f"I recommend you to play {recommended_game['name']}. It's a great {recommended_game['genre']} game."
```