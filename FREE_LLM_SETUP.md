# Free LLM Providers Setup Guide

This guide helps you get free API keys for DeepSeek and Qwen.

## DeepSeek (Recommended - Free & Fast)

### Get API Key
1. Visit https://platform.deepseek.com/
2. Sign up for a free account
3. Go to API Keys section
4. Create a new API key
5. Copy the key

### Set Environment Variable
```bash
export DEEPSEEK_API_KEY="your-key-here"
```

### Usage
```python
from generator import EileenChangGenerator
gen = EileenChangGenerator(provider="deepseek")
```

## Qwen (Alibaba Cloud)

### Get API Key
1. Visit https://dashscope.console.aliyun.com/
2. Sign up for Alibaba Cloud account
3. Activate DashScope service (free tier available)
4. Get your API key from the console

### Set Environment Variable
```bash
export QWEN_API_KEY="your-key-here"
# OR
export DASHSCOPE_API_KEY="your-key-here"
```

### Usage
```python
from generator import EileenChangGenerator
gen = EileenChangGenerator(provider="qwen")
```

## Gemini (Google)

### Get API Key
1. Visit https://makersuite.google.com/app/apikey
2. Create API key

### Set Environment Variable
```bash
export GEMINI_API_KEY="your-key-here"
```

### Usage
```python
from generator import EileenChangGenerator
gen = EileenChangGenerator(provider="gemini")
```

## Quick Test

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export DEEPSEEK_API_KEY="your-key"

# Run generation
python3 generate_and_save.py
```

## Cost Comparison

| Provider | Free Tier | Speed | Chinese Quality |
|----------|-----------|-------|-----------------|
| DeepSeek | ✅ Generous | Fast | Excellent |
| Qwen | ✅ Limited | Fast | Excellent |
| Gemini | ✅ Limited | Medium | Good |

**Recommendation**: Start with DeepSeek for the best free experience.
