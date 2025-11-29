# Eileen Chang Novel Generator

AI-powered novel generator that creates stories in the style of Eileen Chang (张爱玲), the renowned Chinese author.

## Features

- 🤖 **Multi-Provider LLM Support**: Groq, DeepSeek, Qwen, Gemini
- 📚 **Corpus-Based Learning**: Uses authentic Eileen Chang excerpts for style reference
- 💾 **SQLite Database**: Persistent storage of all generated novels
- 🎨 **Beautiful HTML Output**: Responsive, elegant web pages
- 🆓 **Free to Use**: Works with free LLM providers

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set API Key
```bash
# Groq (recommended - fast and free)
export GROQ_API_KEY="your-key-here"

# Or use DeepSeek, Qwen, or Gemini
export DEEPSEEK_API_KEY="your-key"
export QWEN_API_KEY="your-key"
export GEMINI_API_KEY="your-key"
```

### 3. Generate a Novel
```bash
python3 generate_and_save.py
```

## Output

- **HTML Files**: `generated_novels/*.html` - Beautiful web pages
- **Database**: `novels.db` - SQLite database with all novels

## Example Novels

See the `generated_novels/` directory for example outputs.

## Customization

Edit `generate_and_save.py` to customize:
- Theme (e.g., "家族恩怨", "战争中的爱情")
- Setting (e.g., "1940年代上海", "1930年代香港")
- Number of chapters
- LLM provider

## LLM Providers

| Provider | Speed | Chinese Quality | Free Tier |
|----------|-------|-----------------|-----------|
| Groq | ⚡ Very Fast | Excellent | ✅ Yes |
| DeepSeek | Fast | Excellent | ✅ Yes |
| Qwen | Fast | Excellent | ✅ Limited |
| Gemini | Medium | Good | ✅ Limited |

## Project Structure

```
eileen_chang_agent/
├── generator.py          # Multi-provider LLM generator
├── corpus_manager.py     # Manages text corpus
├── novel_database.py     # SQLite database manager
├── html_generator.py     # HTML template generator
├── generate_and_save.py  # Main generation script
├── corpus/               # Eileen Chang text samples
├── generated_novels/     # Output HTML files
└── novels.db            # SQLite database
```

## License

MIT

## Author

Generated with ❤️ using AI
