import sqlite3
import os
from datetime import datetime
from typing import Optional, List, Dict

class NovelDatabase:
    """Manages storage of generated novels in SQLite database."""
    
    def __init__(self, db_path: str = "novels.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS novels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                theme TEXT,
                setting TEXT,
                plot_outline TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chapters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                novel_id INTEGER NOT NULL,
                chapter_number INTEGER NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (novel_id) REFERENCES novels(id)
            )
        """)
        
        conn.commit()
        conn.close()
        print(f"Database initialized: {self.db_path}")
    
    def save_novel(self, title: str, theme: str, setting: str, plot_outline: str) -> int:
        """Save a novel and return its ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO novels (title, theme, setting, plot_outline)
            VALUES (?, ?, ?, ?)
        """, (title, theme, setting, plot_outline))
        
        novel_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"Saved novel: {title} (ID: {novel_id})")
        return novel_id
    
    def save_chapter(self, novel_id: int, chapter_number: int, content: str):
        """Save a chapter for a novel."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO chapters (novel_id, chapter_number, content)
            VALUES (?, ?, ?)
        """, (novel_id, chapter_number, content))
        
        conn.commit()
        conn.close()
        
        print(f"Saved chapter {chapter_number} for novel ID {novel_id}")
    
    def get_novel(self, novel_id: int) -> Optional[Dict]:
        """Retrieve a novel with all its chapters."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM novels WHERE id = ?", (novel_id,))
        novel = cursor.fetchone()
        
        if not novel:
            conn.close()
            return None
        
        cursor.execute("""
            SELECT * FROM chapters 
            WHERE novel_id = ? 
            ORDER BY chapter_number
        """, (novel_id,))
        chapters = cursor.fetchall()
        
        conn.close()
        
        return {
            'id': novel['id'],
            'title': novel['title'],
            'theme': novel['theme'],
            'setting': novel['setting'],
            'plot_outline': novel['plot_outline'],
            'created_at': novel['created_at'],
            'chapters': [dict(chapter) for chapter in chapters]
        }
    
    def list_novels(self) -> List[Dict]:
        """List all novels."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT n.*, COUNT(c.id) as chapter_count
            FROM novels n
            LEFT JOIN chapters c ON n.id = c.novel_id
            GROUP BY n.id
            ORDER BY n.created_at DESC
        """)
        
        novels = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return novels

if __name__ == "__main__":
    db = NovelDatabase()
    print("Database test successful!")
