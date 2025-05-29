from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    alice = Author.create("Alice")
    bob = Author.create("Bob")
    carol = Author.create("Carol")

    tech = Magazine.create("Tech Today", "Technology")
    food = Magazine.create("Food Weekly", "Food")
    travel = Magazine.create("Travel Explorer", "Travel")

    Article.create("AI in 2024", alice.id, tech.id)
    Article.create("Best Pasta Recipes", bob.id, food.id)
    Article.create("Exploring Japan", carol.id, travel.id)
    Article.create("Quantum Computing", alice.id, tech.id)
    Article.create("Street Food Guide", bob.id, food.id)
    Article.create("Backpacking Europe", carol.id, travel.id)
    Article.create("Gadgets Review", alice.id, tech.id)
    Article.create("Healthy Salads", bob.id, food.id)
    Article.create("Desert Adventures", carol.id, travel.id)

if __name__ == "__main__":
    seed()
