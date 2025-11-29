import os
from typing import Optional
from corpus_manager import CorpusManager

class EileenChangGenerator:
    """
    Multi-provider Eileen Chang style novel generator.
    Supports: DeepSeek (free), Qwen (free), Gemini
    """
    
    def __init__(self, provider: str = "groq", api_key: Optional[str] = None):
        """
        Initialize generator with specified provider.
        
        Args:
            provider: "groq", "deepseek", "qwen", or "gemini"
            api_key: API key (optional, will check environment variables)
        """
        self.provider = provider.lower()
        
        # Initialize corpus manager
        self.corpus_manager = CorpusManager()
        self.corpus_manager.download_corpus()
        self.corpus_manager.load_corpus()
        
        # Initialize the appropriate client
        if self.provider == "groq":
            self._init_groq(api_key)
        elif self.provider == "deepseek":
            self._init_deepseek(api_key)
        elif self.provider == "qwen":
            self._init_qwen(api_key)
        elif self.provider == "gemini":
            self._init_gemini(api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}. Use 'groq', 'deepseek', 'qwen', or 'gemini'")
    
    def _init_groq(self, api_key: Optional[str]):
        """Initialize Groq client (OpenAI-compatible, very fast)."""
        from openai import OpenAI
        
        key = api_key or os.environ.get("GROQ_API_KEY")
        if not key:
            raise ValueError("Groq API key not found. Set GROQ_API_KEY or pass api_key parameter.")
        
        self.client = OpenAI(
            api_key=key,
            base_url="https://api.groq.com/openai/v1"
        )
        # Use Llama 3.3 70B for best quality and Chinese support
        self.model_name = "llama-3.3-70b-versatile"
        print(f"✓ Initialized Groq (model: {self.model_name})")
    
    def _init_deepseek(self, api_key: Optional[str]):
        """Initialize DeepSeek client (OpenAI-compatible)."""
        from openai import OpenAI
        
        key = api_key or os.environ.get("DEEPSEEK_API_KEY")
        if not key:
            raise ValueError("DeepSeek API key not found. Set DEEPSEEK_API_KEY or pass api_key parameter.")
        
        self.client = OpenAI(
            api_key=key,
            base_url="https://api.deepseek.com"
        )
        self.model_name = "deepseek-chat"
        print(f"✓ Initialized DeepSeek (model: {self.model_name})")
    
    def _init_qwen(self, api_key: Optional[str]):
        """Initialize Qwen client (OpenAI-compatible)."""
        from openai import OpenAI
        
        key = api_key or os.environ.get("QWEN_API_KEY") or os.environ.get("DASHSCOPE_API_KEY")
        if not key:
            raise ValueError("Qwen API key not found. Set QWEN_API_KEY or DASHSCOPE_API_KEY.")
        
        self.client = OpenAI(
            api_key=key,
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
        )
        self.model_name = "qwen-plus"  # or "qwen-turbo" for faster/cheaper
        print(f"✓ Initialized Qwen (model: {self.model_name})")
    
    def _init_gemini(self, api_key: Optional[str]):
        """Initialize Gemini client."""
        import google.generativeai as genai
        
        key = api_key or os.environ.get("GEMINI_API_KEY")
        if not key:
            raise ValueError("Gemini API key not found. Set GEMINI_API_KEY.")
        
        genai.configure(api_key=key)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.model_name = "gemini-1.5-pro"
        print(f"✓ Initialized Gemini (model: {self.model_name})")
    
    def _generate_with_openai_compatible(self, prompt: str) -> str:
        """Generate text using OpenAI-compatible API (DeepSeek/Qwen)."""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "你是一位精通张爱玲文学风格的作家。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=2000
        )
        return response.choices[0].message.content
    
    def _generate_with_gemini(self, prompt: str) -> str:
        """Generate text using Gemini API."""
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_plot(self, theme: str, setting: str) -> str:
        """Generate plot outline."""
        prompt = f"""请模仿张爱玲的风格，构思一个短篇小说的情节大纲。

主题：{theme}
背景：{setting}

要求：
1. 故事应包含张爱玲式的苍凉感和对人性的深刻洞察。
2. 人物关系错综复杂，往往带有悲剧色彩。
3. 请提供主要人物介绍和故事起承转合的梗概。
"""
        
        if self.provider == "gemini":
            return self._generate_with_gemini(prompt)
        else:
            return self._generate_with_openai_compatible(prompt)
    
    def generate_chapter(self, plot_outline: str, chapter_number: int, previous_context: str = "") -> str:
        """Generate a chapter."""
        style_reference = self.corpus_manager.get_random_snippet(length=300)
        
        prompt = f"""请根据以下情节大纲，模仿张爱玲的笔触撰写第 {chapter_number} 章。

参考风格（来自张爱玲作品片段）：
{style_reference}

情节大纲：
{plot_outline}

前情提要（如果有）：
{previous_context}

写作风格要求：
1. **感官描写**：大量使用细腻的感官描写，特别是对色彩、气味、声音的捕捉。
2. **服饰与环境**：详细描绘人物的衣着和周围的环境，用物质细节来暗示人物心理。
3. **比喻**：使用新奇、尖锐甚至略带刻薄的比喻。
4. **苍凉基调**：保持一种冷静、旁观、甚至有些无情的叙述语调，透出世态炎凉。
5. **语言**：使用半文半白的民国白话风，或者现代汉语中夹杂着旧式优雅的词汇。

请开始撰写：
"""
        
        if self.provider == "gemini":
            return self._generate_with_gemini(prompt)
        else:
            return self._generate_with_openai_compatible(prompt)
    
    def polish_text(self, text: str) -> str:
        """Polish text to match Eileen Chang's style."""
        prompt = f"""请润色以下文字，使其更接近张爱玲的风格。重点加强比喻的独特性和环境描写的细腻度，去除过于现代或平淡的表达。

原文：
{text}
"""
        
        if self.provider == "gemini":
            return self._generate_with_gemini(prompt)
        else:
            return self._generate_with_openai_compatible(prompt)

if __name__ == "__main__":
    # Test with DeepSeek (free)
    print("Testing DeepSeek provider...")
    try:
        gen = EileenChangGenerator(provider="deepseek")
        print("DeepSeek initialized successfully!")
    except Exception as e:
        print(f"DeepSeek error: {e}")
