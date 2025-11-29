from datetime import datetime
from typing import Dict, List

class HTMLGenerator:
    """Generates HTML output for novels."""
    
    @staticmethod
    def generate_novel_html(novel_data: Dict, output_path: str):
        """Generate a complete HTML file for a novel."""
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{novel_data['title']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Songti SC', 'SimSun', serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.8;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: 3px;
        }}
        
        .metadata {{
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            font-size: 0.95em;
        }}
        
        .metadata p {{
            margin: 8px 0;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .plot-outline {{
            background: #f8f9fa;
            padding: 30px;
            border-left: 4px solid #667eea;
            margin-bottom: 40px;
            border-radius: 4px;
        }}
        
        .plot-outline h2 {{
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.5em;
        }}
        
        .plot-outline p {{
            white-space: pre-wrap;
            color: #555;
        }}
        
        .chapter {{
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 1px solid #eee;
        }}
        
        .chapter:last-child {{
            border-bottom: none;
        }}
        
        .chapter h2 {{
            color: #333;
            margin-bottom: 25px;
            font-size: 1.8em;
            text-align: center;
            font-weight: 300;
        }}
        
        .chapter-content {{
            text-indent: 2em;
            color: #333;
            font-size: 1.1em;
            white-space: pre-wrap;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 30px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .header {{
                padding: 40px 20px;
            }}
            
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{novel_data['title']}</h1>
            <div class="metadata">
                <p><strong>主题：</strong>{novel_data['theme']}</p>
                <p><strong>背景：</strong>{novel_data['setting']}</p>
                <p><strong>创作时间：</strong>{novel_data['created_at']}</p>
                <p><strong>章节数：</strong>{len(novel_data['chapters'])}</p>
            </div>
        </div>
        
        <div class="content">
            <div class="plot-outline">
                <h2>情节大纲</h2>
                <p>{novel_data['plot_outline']}</p>
            </div>
            
"""
        
        # Add chapters
        for chapter in novel_data['chapters']:
            html += f"""            <div class="chapter">
                <h2>第 {chapter['chapter_number']} 章</h2>
                <div class="chapter-content">{chapter['content']}</div>
            </div>
            
"""
        
        html += f"""        </div>
        
        <div class="footer">
            <p>本作品由张爱玲风格生成器创作</p>
            <p>生成时间：{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"HTML generated: {output_path}")

if __name__ == "__main__":
    # Test with sample data
    sample_data = {
        'title': '测试小说',
        'theme': '爱情',
        'setting': '1940年代上海',
        'created_at': '2024-01-01 12:00:00',
        'plot_outline': '这是一个测试大纲...',
        'chapters': [
            {'chapter_number': 1, 'content': '第一章内容...'}
        ]
    }
    HTMLGenerator.generate_novel_html(sample_data, 'test_novel.html')
    print("HTML test successful!")
