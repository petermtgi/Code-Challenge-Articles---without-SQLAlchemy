from lib.db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, author_id, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (title, author_id, magazine_id)
        )
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return cls(id=article_id, title=title, author_id=author_id, magazine_id=magazine_id)

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'])
        return None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        articles = [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in cursor.fetchall()]
        conn.close()
        return articles

    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        articles = [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in cursor.fetchall()]
        conn.close()
        return articles

    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        articles = [cls(id=row['id'], title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id']) for row in cursor.fetchall()]
        conn.close()
        return articles
