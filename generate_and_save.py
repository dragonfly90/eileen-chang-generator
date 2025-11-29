import os
import sys
from datetime import datetime
from generator import EileenChangGenerator
from novel_database import NovelDatabase
from html_generator import HTMLGenerator

def generate_novel(theme: str, setting: str, title: str, num_chapters: int = 3, provider: str = "groq"):
    """
    Generate a complete novel and save to both database and HTML.
    
    Args:
        theme: Theme of the novel (e.g., "错过的爱情")
        setting: Setting of the novel (e.g., "1940年代上海")
        title: Title of the novel
        num_chapters: Number of chapters to generate (default: 3)
    """
    print(f"\n{'='*60}")
    print(f"开始生成小说：{title}")
    print(f"主题：{theme}")
    print(f"背景：{setting}")
    print(f"章节数：{num_chapters}")
    print(f"LLM提供商：{provider}")
    print(f"{'='*60}\n")
    
    # Initialize components
    generator = EileenChangGenerator(provider=provider)
    db = NovelDatabase()
    
    # Step 1: Generate plot outline
    print("📝 生成情节大纲...")
    plot_outline = generator.generate_plot(theme, setting)
    print(f"\n大纲生成完成 ({len(plot_outline)} 字)\n")
    
    # Step 2: Save novel to database
    novel_id = db.save_novel(title, theme, setting, plot_outline)
    
    # Step 3: Generate chapters
    chapters = []
    previous_context = ""
    
    for i in range(1, num_chapters + 1):
        print(f"✍️  生成第 {i} 章...")
        chapter_content = generator.generate_chapter(plot_outline, i, previous_context)
        print(f"第 {i} 章生成完成 ({len(chapter_content)} 字)\n")
        
        # Save chapter to database
        db.save_chapter(novel_id, i, chapter_content)
        
        chapters.append({
            'chapter_number': i,
            'content': chapter_content
        })
        
        # Update context for next chapter (use last 500 chars)
        previous_context = chapter_content[-500:] if len(chapter_content) > 500 else chapter_content
    
    # Step 4: Retrieve complete novel from database
    novel_data = db.get_novel(novel_id)
    
    # Step 5: Generate HTML output
    output_dir = "generated_novels"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_filename = f"{output_dir}/{title}_{timestamp}.html"
    
    print(f"📄 生成HTML文件...")
    HTMLGenerator.generate_novel_html(novel_data, html_filename)
    
    print(f"\n{'='*60}")
    print(f"✅ 小说生成完成！")
    print(f"{'='*60}")
    print(f"数据库ID: {novel_id}")
    print(f"HTML文件: {html_filename}")
    print(f"总字数: {len(plot_outline) + sum(len(ch['content']) for ch in chapters)}")
    print(f"{'='*60}\n")
    
    return novel_id, html_filename

if __name__ == "__main__":
    # Example usage - change provider as needed
    # Generate a 10-chapter novel
    generate_novel(
        theme="错过的爱情",
        setting="2020年代的旧金山湾区",
        title="异乡的鸢尾",
        num_chapters=10,
        provider="groq"  # Options: "groq", "deepseek", "qwen", "gemini"
    )
