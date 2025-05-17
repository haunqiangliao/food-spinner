import streamlit as st
import random
import pandas as pd
from PIL import Image

# ----------------------
# 1. 初始化数据
# ----------------------
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
**不知道吃什么？让我们帮你随机选择！**  
点击按钮，随机获取美食推荐，并查看详细营养信息。
""")

# ----------------------
# 4. 随机选择和结果展示区域
# ----------------------
col1, col2 = st.columns([3, 2])

with col1:
    # 随机选择按钮
    if st.button("🍽️ 随机选餐", use_container_width=True, type="primary"):
        with st.spinner("正在随机选择..."):
            # 模拟思考时间
            st.session_state.spin_result = random.choice(st.session_state.foods)
            st.success("已为您随机选择了一道美食！")
    
    # 结果显示区域
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        
        # 显示结果卡片
        st.markdown(f"""
        <div class="bg-white rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg">
            <img src="{result['image']}" alt="{result['name']}" class="w-full h-48 object-cover">
            <div class="p-6">
                <h2 class="text-2xl font-bold text-gray-800 mb-2">{result['name']}</h2>
                <p class="text-gray-600 mb-4">{result['category']}</p>
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-gray-50 p-3 rounded-lg">
                        <div class="text-sm text-gray-500">热量</div>
                        <div class="text-lg font-semibold">{result['calories']} kcal</div>
                    </div>
                    <div class="bg-gray-50 p-3 rounded-lg">
                        <div class="text-sm text-gray-500">蛋白质</div>
                        <div class="text-lg font-semibold">{result['protein']} g</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("点击上方按钮开始随机选餐")

with col2:
    # 营养信息卡片
    st.markdown("### 🍳 营养信息")
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        st.markdown(f"""
        <div class="bg-white rounded-xl shadow-md p-5">
            <div class="flex items-center mb-4 pb-4 border-b border-gray-100">
                <img src="{nutrition_icons['calories']}" alt="热量" class="w-8 h-8 mr-3">
                <div>
                    <div class="text-sm text-gray-500">热量</div>
                    <div class="text-xl font-bold">{result['calories']} kcal</div>
                </div>
            </div>
            <div class="flex items-center mb-4 pb-4 border-b border-gray-100">
                <img src="{nutrition_icons['protein']}" alt="蛋白质" class="w-8 h-8 mr-3">
                <div>
                    <div class="text-sm text-gray-500">蛋白质</div>
                    <div class="text-xl font-bold">{result['protein']} g</div>
                </div>
            </div>
            <div class="flex items-center">
                <img src="{nutrition_icons['fat']}" alt="脂肪" class="w-8 h-8 mr-3">
                <div>
                    <div class="text-sm text-gray-500">脂肪</div>
                    <div class="text-xl font-bold">{round(result['calories'] * 0.3 / 9, 1)} g</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("随机选餐后显示详细营养信息")

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
