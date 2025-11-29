import streamlit as st
import os
from generator import EileenChangGenerator

st.set_page_config(page_title="张爱玲风格小说生成器", page_icon="📖", layout="wide")

st.title("📖 张爱玲风格小说生成器")
st.markdown("""
> “生命是一袭华美的袍，爬满了虱子。”
""")

with st.sidebar:
    st.header("设置")
    api_key = st.text_input("Gemini API Key", type="password")
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        st.warning("请输入 API Key 或设置 GEMINI_API_KEY 环境变量")
        st.stop()
    
    generator = EileenChangGenerator(api_key=api_key)

st.header("1. 构思情节")
col1, col2 = st.columns(2)
with col1:
    theme = st.text_input("主题 (例如：错过的爱情，家族的衰落)", value="旧上海的爱恨情仇")
with col2:
    setting = st.text_input("背景 (例如：1940年代上海，现代香港)", value="1943年的上海")

if st.button("生成情节大纲"):
    with st.spinner("正在构思中..."):
        try:
            plot = generator.generate_plot(theme, setting)
            st.session_state['plot'] = plot
            st.success("情节大纲生成完毕")
        except Exception as e:
            st.error(f"生成失败: {e}")

if 'plot' in st.session_state:
    st.subheader("情节大纲")
    plot_text = st.text_area("编辑大纲", value=st.session_state['plot'], height=300)
    st.session_state['plot'] = plot_text

    st.header("2. 撰写正文")
    chapter_num = st.number_input("章节号", min_value=1, value=1)
    
    if st.button(f"生成第 {chapter_num} 章"):
        with st.spinner("正在以此去..."):
            try:
                chapter_content = generator.generate_chapter(st.session_state['plot'], chapter_num)
                st.session_state[f'chapter_{chapter_num}'] = chapter_content
                st.success("章节生成完毕")
            except Exception as e:
                st.error(f"生成失败: {e}")

    if f'chapter_{chapter_num}' in st.session_state:
        st.subheader(f"第 {chapter_num} 章")
        st.markdown(st.session_state[f'chapter_{chapter_num}'])
        
        if st.button("润色本章"):
             with st.spinner("正在润色..."):
                polished = generator.polish_text(st.session_state[f'chapter_{chapter_num}'])
                st.session_state[f'chapter_{chapter_num}'] = polished
                st.experimental_rerun()

