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
        
        # 添加CSS动画样式（使用Tailwind风格的类名）
        st.markdown("""
        <style type="text/tailwindcss">
            @layer utilities {
                .content-auto {
                    content-visibility: auto;
                }
                .wheel-spin {
                    animation: spin 5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
                }
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(3600deg); }
                }
                .wheel-section {
                    position: absolute;
                    width: 50%;
                    height: 50%;
                    transform-origin: bottom right;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 24px;
                    clip-path: polygon(0 0, 100% 0, 100% 100%);
                }
                .wheel-pointer {
                    position: absolute;
                    top: -10px;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 0;
                    height: 0;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-bottom: 20px solid #e74c3c;
                    z-index: 10;
                }
            }
        </style>
        """, unsafe_allow_html=True)
        
        # 创建转盘动画（改进的HTML结构）
        st.markdown("""
        <div class="flex justify-center my-6">
            <div class="relative w-[300px] h-[300px]">
                <!-- 转盘 -->
                <div id="food-wheel" class="absolute w-full h-full rounded-full border-4 border-gray-200 overflow-hidden">
                    <!-- 6个扇区 -->
                    <div class="wheel-section bg-red-400/80" style="transform: rotate(0deg);">🍜</div>
                    <div class="wheel-section bg-green-400/80" style="transform: rotate(60deg);">🍔</div>
                    <div class="wheel-section bg-blue-400/80" style="transform: rotate(120deg);">🍣</div>
                    <div class="wheel-section bg-purple-400/80" style="transform: rotate(180deg);">🌯</div>
                    <div class="wheel-section bg-yellow-400/80" style="transform: rotate(240deg);">🍕</div>
                    <div class="wheel-section bg-orange-400/80" style="transform: rotate(300deg);">🥗</div>
                    
                    <!-- 中心图标 -->
                    <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md">
                        <div class="text-2xl">🍴</div>
                    </div>
                </div>
                
                <!-- 指针 -->
                <div class="wheel-pointer"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 转动按钮
        if st.button("🍽️ 开始随机选餐", use_container_width=True, type="primary"):
            # 使用JavaScript控制转盘动画
            st.markdown("""
            <script>
                // 获取转盘元素
                const wheel = document.getElementById('food-wheel');
                
                // 重置转盘状态
                wheel.classList.remove('wheel-spin');
                void wheel.offsetWidth; // 触发重绘
                
                // 添加旋转动画类
                wheel.classList.add('wheel-spin');
                
                // 选择随机结果
                const foods = [
                    {name: "番茄炒蛋", category: "中餐", calories: 145, protein: 6.5, image: "https://picsum.photos/seed/番茄炒蛋/300/200"},
                    {name: "照烧鸡腿饭", category: "日式", calories: 480, protein: 22, image: "https://picsum.photos/seed/照烧鸡腿饭/300/200"},
                    {name: "蔬菜沙拉", category: "西餐", calories: 120, protein: 3, image: "https://picsum.photos/seed/蔬菜沙拉/300/200"},
                    {name: "酸菜鱼", category: "中餐", calories: 320, protein: 20, image: "https://picsum.photos/seed/酸菜鱼/300/200"},
                    {name: "寿司拼盘", category: "日式", calories: 350, protein: 18, image: "https://picsum.photos/seed/寿司拼盘/300/200"},
                    {name: "黑椒牛柳意面", category: "西餐", calories: 420, protein: 25, image: "https://picsum.photos/seed/黑椒牛柳意面/300/200"},
                ];
                
                const randomFood = foods[Math.floor(Math.random() * foods.length)];
                
                // 动画结束后显示结果
                setTimeout(() => {
                    // 移除动画类
                    wheel.classList.remove('wheel-spin');
                    
                    // 更新Streamlit状态
                    parent.postMessage({
                        type: 'streamlit:setComponentValue',
                        value: randomFood
                    }, '*');
                    
                    // 显示结果通知
                    const notification = document.createElement('div');
                    notification.className = 'fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded shadow-lg z-50';
                    notification.textContent = `🎉 恭喜！您抽到了 ${randomFood.name}！`;
                    document.body.appendChild(notification);
                    
                    // 3秒后移除通知
                    setTimeout(() => {
                        notification.remove();
                    }, 3000);
                }, 5000);
            </script>
            """, unsafe_allow_html=True)
    
    # 结果显示区域
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        st.markdown(f"""
        ### 🎉 推荐菜品: {result['name']}
        <div class="flex items-center mt-4 gap-4">
            <img src="{result['image']}" alt="{result['name']}" class="w-1/3 h-auto rounded-lg shadow-md">
            <div class="flex-1">
                <div class="text-gray-600 text-lg">{result['category']}</div>
                <div class="grid grid-cols-2 gap-2 mt-2">
                    <div class="bg-gray-100 p-2 rounded">
                        <div class="text-xs text-gray-500">热量</div>
                        <div class="text-lg font-semibold">{result['calories']} kcal</div>
                    </div>
                    <div class="bg-gray-100 p-2 rounded">
                        <div class="text-xs text-gray-500">蛋白质</div>
                        <div class="text-lg font-semibold">{result['protein']} g</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # 营养信息卡片
    st.markdown("### 🍳 营养信息")
    if 'spin_result' in st.session_state:
        result = st.session_state.spin_result
        st.markdown(f"""
        <div class="bg-white rounded-xl shadow-md p-4">
            <div class="flex items-center mb-4">
                <img src="{nutrition_icons['calories']}" alt="热量" class="w-8 h-8 mr-3">
                <div>
                    <div class="text-sm text-gray-500">热量</div>
                    <div class="text-xl font-bold">{result['calories']} kcal</div>
                </div>
            </div>
            <div class="flex items-center mb-4">
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
