from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":
    alice = Author.find_by_name("Alice")
    print("Alice's articles:", [a.title for a in alice.articles()])
    print("Alice's magazines:", [m.name for m in alice.magazines()])
    print("Alice's topic areas:", alice.topic_areas())

    tech = Magazine.find_by_name("Tech Today")
    print("Tech Today contributors:", [a.name for a in tech.contributors()])
    print("Tech Today article titles:", tech.article_titles())
    print("Tech Today contributing authors (>2 articles):", [a.name for a in tech.contributing_authors()])