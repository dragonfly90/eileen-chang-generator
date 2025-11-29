# Eileen Chang Novel Generator - Usage Guide

## Overview
This system generates novels in Eileen Chang's style and saves them to both a SQLite database and beautiful HTML files.

## Files Created
- `novel_database.py` - Database manager for storing novels
- `html_generator.py` - HTML template generator
- `generate_and_save.py` - Main generation script (requires API key)
- `demo_generation.py` - Demo script with sample data (no API key needed)

## Quick Start

### Option 1: Generate with AI (Requires GEMINI_API_KEY)
```bash
# Set your API key
export GEMINI_API_KEY="your-api-key-here"

# Run the generator
python3 generate_and_save.py
```

### Option 2: Run Demo (No API Key Required)
```bash
python3 demo_generation.py
```

## Database Schema

### novels table
- `id` - Primary key
- `title` - Novel title
- `theme` - Theme (e.g., "错过的爱情")
- `setting` - Setting (e.g., "1940年代上海")
- `plot_outline` - Plot summary
- `created_at` - Timestamp

### chapters table
- `id` - Primary key
- `novel_id` - Foreign key to novels
- `chapter_number` - Chapter number
- `content` - Chapter text
- `created_at` - Timestamp

## Output

### Database
All novels are stored in `novels.db` (SQLite)

### HTML Files
Generated in `generated_novels/` directory with format:
`{title}_{timestamp}.html`

## Customization

Edit `generate_and_save.py` to change:
- Theme
- Setting
- Title
- Number of chapters

Example:
```python
generate_novel(
    theme="家族恩怨",
    setting="1930年代香港",
    title="金色枷锁",
    num_chapters=5
)
```

## Viewing Novels

### HTML
Open any `.html` file in `generated_novels/` with your browser

### Database
Use SQLite browser or Python:
```python
from novel_database import NovelDatabase
db = NovelDatabase()
novels = db.list_novels()
for novel in novels:
    print(f"{novel['id']}: {novel['title']}")
```
