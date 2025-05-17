import streamlit as st
import random

# 预设美食数据（可自行修改/添加）
foods = [
    {"name": "番茄炒蛋", "category": "中餐", "calories": 145, "protein": 6.5},
    {"name": "照烧鸡腿饭", "category": "日式", "calories": 480, "protein": 22},
    {"name": "蔬菜沙拉", "category": "西餐", "calories": 120, "protein": 3},
    {"name": "酸菜鱼", "category": "中餐", "calories": 320, "protein": 20},
    {"name": "寿司拼盘", "category": "日式", "calories": 350, "protein": 18},
    {"name": "黑椒牛柳意面", "category": "西餐", "calories": 420, "protein": 25},
]

st.set_page_config(page_title="美食转盘", page_icon="🍴", layout="centered")
st.title("🍴 今日吃啥？一键转盘")

if st.button("转动转盘", use_container_width=True):
    selected = random.choice(foods)
    st.success(f"推荐：{selected['name']}（{selected['category']}）")
    st.write(f"热量：{selected['calories']} kcal | 蛋白质：{selected['protein']} g")

    # 简易转盘图示（用Emoji模拟）
    st.write("""
    🍜🍔🍕🍣🍛  
    🍳🥗🌭🍝🍲  
    """)