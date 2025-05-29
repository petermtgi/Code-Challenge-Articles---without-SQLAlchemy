import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_create_article():
    author = Author.create("Article Author")
    mag = Magazine.create("Article Mag", "TestCat")
    article = Article.create("Test Article", author.id, mag.id)
    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Test Article"
    assert found.author_id == author.id
    assert found.magazine_id == mag.id