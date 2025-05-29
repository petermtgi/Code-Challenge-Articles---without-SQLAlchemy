# Example: Run some queries for demonstration

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":
    # List all authors
    print("Authors:")
    for name in ["Alice", "Bob", "Carol"]:
        author = Author.find_by_name(name)
        if author:
            print(f"- {author.name} (id: {author.id})")

    # List all magazines
    print("\nMagazines:")
    for name in ["Tech Today", "Food Weekly", "Travel Explorer"]:
        mag = Magazine.find_by_name(name)
        if mag:
            print(f"- {mag.name} (id: {mag.id}, category: {mag.category})")

    # List all articles for Alice
    alice = Author.find_by_name("Alice")
    if alice:
        print(f"\nArticles by Alice:")
        for article in alice.articles():
            print(f"- {article.title}")

    # List contributors for Tech Today
    tech = Magazine.find_by_name("Tech Today")
    if tech:
        print(f"\nContributors to Tech Today:")
        for author in tech.contributors():
            print(f"- {author.name}")