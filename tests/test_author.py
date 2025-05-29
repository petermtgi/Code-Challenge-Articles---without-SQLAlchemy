from lib.models.author import Author

def test_create_and_find_author():
    author = Author.create("Test Author")
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "Test Author"

def test_find_by_name():
    author = Author.create("Unique Name")
    found = Author.find_by_name("Unique Name")
    assert found is not None
    assert found.name == "Unique Name"
