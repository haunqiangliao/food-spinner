import streamlit as st
import random
import pandas as pd

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

# 美食图片API
def get_food_image(food_name):
    """根据食物名称获取对应的美食图片"""
    food_image_map = {
        "番茄炒蛋": "https://picsum.photos/seed/egg-tomato/300/200",
        "照烧鸡腿饭": "https://picsum.photos/seed/teriyaki/300/200",
        "蔬菜沙拉": "https://picsum.photos/seed/salad/300/200",
        "酸菜鱼": "https://picsum.photos/seed/fish-soup/300/200",
        "寿司拼盘": "https://picsum.photos/seed/sushi/300/200",
        "黑椒牛柳意面": "https://picsum.photos/seed/pasta/300/200",
        "麻婆豆腐": "https://picsum.photos/seed/mapo-tofu/300/200",
        "宫保鸡丁": "https://picsum.photos/seed/kungpao/300/200",
        "汉堡": "https://picsum.photos/seed/burger/300/200",
        "披萨": "https://picsum.photos/seed/pizza/300/200",
        "饺子": "https://picsum.photos/seed/dumplings/300/200",
        "火锅": "https://picsum.photos/seed/hotpot/300/200",
    }
    
    if food_name in food_image_map:
        return food_image_map[food_name]
    
    return f"https://foodish-api.herokuapp.com/api/images/food?random={hash(food_name) % 1000}"

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
            if not st.session_state.foods:
                st.warning("请先添加一些食物到列表中！")
            else:
                st.session_state.spin_result = random.choice(st.session_state.foods)
                st.success("已为您随机选择了一道美食！")
    
    # 结果显示区域
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        
        if result not in st.session_state.foods:
            st.warning("您选择的菜品已被删除，请重新选择")
            del st.session_state.spin_result
        else:
            image_url = get_food_image(result['name'])
            
            st.markdown(f"""
            <div class="bg-white rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg">
                <img src="{image_url}" alt="{result['name']}" class="w-full h-48 object-cover">
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
            <div class="mb-4 pb-4 border-b border-gray-100">
                <div class="text-sm text-gray-500">热量</div>
                <div class="text-xl font-bold">{result['calories']} kcal</div>
            </div>
            <div>
                <div class="text-sm text-gray-500">蛋白质</div>
                <div class="text-xl font-bold">{result['protein']} g</div>
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
        
        if st.button("➕ 添加到列表"):
            if not name:
                st.error("请输入菜品名称")
            else:
                image_url = get_food_image(name)
                
                new_food = {
                    "name": name,
                    "category": category,
                    "calories": calories,
                    "protein": protein,
                    "image": image_url
                }
                st.session_state.foods.append(new_food)
                st.success(f"已添加: {name}")
    
    # 显示当前食物列表
    st.markdown("### 🍱 当前食物列表")
    if not st.session_state.foods:
        st.info("食物列表为空，请添加一些食物")
    else:
        for i, food in enumerate(st.session_state.foods):
            cols = st.columns([4, 1])
            cols[0].write(f"{i + 1}. {food['name']} ({food['category']})")
            if cols[1].button("❌", key=f"delete_{i}"):
                if 'spin_result' in st.session_state and st.session_state.spin_result == food:
                    del st.session_state.spin_result
                st.session_state.foods.pop(i)
                st.rerun()
    
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
        if 'spin_result' in st.session_state and st.session_state.spin_result in st.session_state.foods:
            pass
        else:
            if 'spin_result' in st.session_state:
                del st.session_state.spin_result
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
