# Articles Code Challenge

## Setup

1. Install dependencies (if any)
2. Run the database setup:
    ```
    python scripts/setup_db.py
    ```
3. Seed the database:
    ```
    python lib/db/seed.py
    ```
4. Run debug session:
    ```
    python lib/debug.py
    ```

## Project Structure

- `lib/models/`: Model classes for Author, Article, Magazine
- `lib/db/`: Database connection, schema, and seed scripts
- `scripts/`: Setup and query scripts
- `tests/`: Pytest test files

## Features

- Add/find authors, magazines, articles
- Relationship methods (articles by author, contributors, etc.)
- Aggregate queries (topic areas, contributing authors, etc.)

## Testing

Run all tests with:
```
pytest
```