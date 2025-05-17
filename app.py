import streamlit as st
import random
import pandas as pd
from PIL import Image

# ----------------------
# 1. 初始化数据
# ----------------------
# 预设美食数据（结构化存储）
if 'foods' not in st.session_state:
    st.session_state.foods = [
        {"name": "番茄炒蛋", "category": "中餐", "calories": 145, "protein": 6.5, "image": "https://picsum.photos/seed/番茄炒蛋/300/200"},
        {"name": "照烧鸡腿饭", "category": "日式", "calories": 480, "protein": 22, "image": "https://picsum.photos/seed/照烧鸡腿饭/300/200"},
        {"name": "蔬菜沙拉", "category": "西餐", "calories": 120, "protein": 3, "image": "https://picsum.photos/seed/蔬菜沙拉/300/200"},
        {"name": "酸菜鱼", "category": "中餐", "calories": 320, "protein": 20, "image": "https://picsum.photos/seed/酸菜鱼/300/200"},
        {"name": "寿司拼盘", "category": "日式", "calories": 350, "protein": 18, "image": "https://picsum.photos/seed/寿司拼盘/300/200"},
        {"name": "黑椒牛柳意面", "category": "西餐", "calories": 420, "protein": 25, "image": "https://picsum.photos/seed/黑椒牛柳意面/300/200"},
    ]

# 营养图标
nutrition_icons = {
    "calories": "https://img.icons8.com/fluency/48/000000/calories.png",
    "protein": "https://img.icons8.com/fluency/48/000000/protein.png",
    "fat": "https://img.icons8.com/fluency/48/000000/fat.png",
    "carbs": "https://img.icons8.com/fluency/48/000000/carbs.png"
}

# ----------------------
# 2. 页面配置
# ----------------------
st.set_page_config(
    page_title="美食转盘", 
    page_icon="🍴", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------
# 3. 页面标题和介绍
# ----------------------
st.markdown("""
# 🍴 美食灵感转盘  
**不知道吃什么？让转盘帮你决定！**  
转动转盘，随机获取美食推荐，并查看详细营养信息。
""")

# ----------------------
# 4. 转盘动画和结果展示区域
# ----------------------
col1, col2 = st.columns([3, 2])

with col1:
    # 转盘容器
    with st.container():
        st.markdown("### 🎯 转动转盘")
        # 转盘展示区域
        if 'spin_result' not in st.session_state:
            st.markdown("""
            <div class="wheel-container" style="height: 300px; display: flex; align-items: center; justify-content: center; border: 2px dashed #eee; border-radius: 10px;">
                <p style="color: #888;">点击下方按钮开始转动</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # 展示转盘结果
            result = st.session_state.spin_result
            st.markdown(f"""
            <div class="result-container" style="height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 10px; background-color: #f9f9f9; padding: 20px;">
                <h3 style="color: #e74c3c;">🎉 推荐菜品: {result['name']}</h3>
                <img src="{result['image']}" alt="{result['name']}" style="max-height: 180px; border-radius: 8px; margin: 10px 0;">
                <p style="color: #555;">{result['category']} · 热量: {result['calories']} kcal</p>
            </div>
            """, unsafe_allow_html=True)
        
        # 转动按钮
        if st.button("🍽️ 开始随机选餐", use_container_width=True, type="primary"):
            with st.spinner("转盘转动中..."):
                # 模拟转盘动画
                for i in range(10):
                    temp_result = random.choice(st.session_state.foods)
                    st.session_state.spin_result = temp_result
                    st.experimental_rerun()
                
                # 最终结果
                final_result = random.choice(st.session_state.foods)
                st.session_state.spin_result = final_result
                st.experimental_rerun()

with col2:
    # 营养信息卡片
    st.markdown("### 🍳 营养信息")
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        st.markdown(f"""
        <div class="nutrition-card" style="background-color: #fff; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); padding: 20px;">
            <div class="nutrition-item" style="display: flex; align-items: center; margin-bottom: 15px;">
                <img src="{nutrition_icons['calories']}" alt="热量" style="width: 32px; margin-right: 10px;">
                <div>
                    <div style="font-size: 14px; color: #666;">热量</div>
                    <div style="font-size: 20px; font-weight: bold;">{result['calories']} kcal</div>
                </div>
            </div>
            <div class="nutrition-item" style="display: flex; align-items: center; margin-bottom: 15px;">
                <img src="{nutrition_icons['protein']}" alt="蛋白质" style="width: 32px; margin-right: 10px;">
                <div>
                    <div style="font-size: 14px; color: #666;">蛋白质</div>
                    <div style="font-size: 20px; font-weight: bold;">{result['protein']} g</div>
                </div>
            </div>
            <div class="nutrition-item" style="display: flex; align-items: center;">
                <img src="{nutrition_icons['fat']}" alt="脂肪" style="width: 32px; margin-right: 10px;">
                <div>
                    <div style="font-size: 14px; color: #666;">脂肪</div>
                    <div style="font-size: 20px; font-weight: bold;">{round(result['calories'] * 0.3 / 9, 1)} g</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("转动转盘后显示详细营养信息")

# ----------------------
# 5. 侧边栏：自定义食物列表
# ----------------------
with st.sidebar:
    st.markdown("### 📝 自定义食物列表")
    
    # 添加新食物
    with st.expander("添加新菜品", expanded=True):
        name = st.text_input("菜品名称")
        category = st.selectbox("菜系", ["中餐", "西餐", "日式", "韩式", "东南亚", "其他"])
        calories = st.number_input("热量 (kcal)", min_value=0)
        protein = st.number_input("蛋白质 (g)", min_value=0.0, step=0.1)
        image_url = st.text_input("图片URL (可选)", help="留空将使用默认图片")
        
        if st.button("➕ 添加到列表"):
            if not name:
                st.error("请输入菜品名称")
            else:
                new_food = {
                    "name": name,
                    "category": category,
                    "calories": calories,
                    "protein": protein,
                    "image": image_url if image_url else f"https://picsum.photos/seed/{name}/300/200"
                }
                st.session_state.foods.append(new_food)
                st.success(f"已添加: {name}")
    
    # 显示当前食物列表
    st.markdown("### 🍱 当前食物列表")
    for i, food in enumerate(st.session_state.foods):
        cols = st.columns([4, 1])
        cols[0].write(f"{i+1}. {food['name']} ({food['category']})")
        if cols[1].button("❌", key=f"delete_{i}"):
            st.session_state.foods.pop(i)
            st.experimental_rerun()
    
    # 重置功能
    if st.button("🔄 重置为默认食物"):
        st.session_state.foods = [
            {"name": "番茄炒蛋", "category": "中餐", "calories": 145, "protein": 6.5, "image": "https://picsum.photos/seed/番茄炒蛋/300/200"},
            {"name": "照烧鸡腿饭", "category": "日式", "calories": 480, "protein": 22, "image": "https://picsum.photos/seed/照烧鸡腿饭/300/200"},
            {"name": "蔬菜沙拉", "category": "西餐", "calories": 120, "protein": 3, "image": "https://picsum.photos/seed/蔬菜沙拉/300/200"},
            {"name": "酸菜鱼", "category": "中餐", "calories": 320, "protein": 20, "image": "https://picsum.photos/seed/酸菜鱼/300/200"},
            {"name": "寿司拼盘", "category": "日式", "calories": 350, "protein": 18, "image": "https://picsum.photos/seed/寿司拼盘/300/200"},
            {"name": "黑椒牛柳意面", "category": "西餐", "calories": 420, "protein": 25, "image": "https://picsum.photos/seed/黑椒牛柳意面/300/200"},
        ]
        st.success("已重置为默认食物列表")

# ----------------------
# 6. 页脚信息
# ----------------------
st.markdown("""
---
🍔 美食转盘 | 为选择困难症患者设计  
💡 提示：可在侧边栏自定义添加或删除食物  
📊 营养数据仅供参考，实际数值可能有差异
""")
