from datetime import datetime
import streamlit as st
import time

# 八音盒音乐文件（示例链接，使用公开音乐资源）
MUSIC_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


def countdown(target_date):
    # 设置背景图片和样式
    st.markdown("""
    <style>
    .stApp {
        background-image: url('https://github.com/lushui1/xiaohoutongxue/blob/main/微信图片_20250110152922.jpg?raw=true');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #333333;
        font-family: 'Dancing Script', cursive, 'Helvetica Neue', sans-serif;
    }
    .overlay {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        max-width: 600px;
        margin: auto;
        margin-top: 50px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #FF69B4;
        margin-bottom: 20px;
        text-shadow: 0 0 10px rgba(255, 105, 180, 0.8);
    }
    .subtitle {
        font-size: 20px;
        color: #50E3C2;
        margin-bottom: 30px;
    }
    .countdown {
        font-size: 48px;
        font-weight: bold;
        color: #FF6F61;
        margin-top: 20px;
        text-shadow: 0 0 10px rgba(255, 111, 97, 0.7);
    }
    .footer {
        font-size: 16px;
        color: #999999;
        margin-top: 40px;
    }
    .messages {
        font-size: 18px;
        color: #4A90E2;
        margin-top: 20px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # 动态背景音乐
    st.audio(MUSIC_URL, start_time=0)

    # 包装内容
    st.markdown('<div class="overlay">', unsafe_allow_html=True)
    st.markdown('<div class="title">💖 倒计时页面：期待乖乖的到来！</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">🌸 用爱装点的每一天，期待与你的相见 🌸</div>', unsafe_allow_html=True)

    # 记录心情留言
    message = st.text_input("今天你的心情是？", "期待满满 💕")
    st.write(f"❤️ 你的心情记录：{message}")

    # 提示动态更新内容
    st.markdown('<div class="subtitle">✨ 爱的日记簿 ✨</div>', unsafe_allow_html=True)
    messages = [
        "💌 第一天相遇的笑容，温暖了整个冬天。",
        "🎶 我们也约定，要一起幸福的走下去。",
        "🌹 期待见到你，我已准备好迎接你。",
        "🌈 每一天的倒计时，都是爱你的轨迹。",
        "💕 乖乖是我的全世界，我是乖乖的家！"
    ]

    for msg in messages:
        st.markdown(f'<div class="messages">{msg}</div>', unsafe_allow_html=True)
        time.sleep(1.5)  # 模拟滚动效果

    # 倒计时模块
    placeholder = st.empty()  # 创建占位符

    while True:
        now = datetime.now()
        time_diff = target_date - now

        if time_diff.total_seconds() <= 0:
            placeholder.empty()
            st.markdown('<div class="title">🎉 终于等到你！欢迎乖乖的到来 💕</div>', unsafe_allow_html=True)
            st.balloons()
            break

        # 提取天、小时、分钟、秒
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 动态更新倒计时内容
        with placeholder.container():
            st.markdown(
                f"""
                <div class="countdown">
                    ❤️ 距离乖乖到来还有：
                    <br>
                    <span>{days} 天</span>
                    <span>{hours:02} 小时</span>
                    <span>{minutes:02} 分钟</span>
                    <span>{seconds:02} 秒</span>
                </div>
                """, unsafe_allow_html=True
            )

        time.sleep(1)  # 每秒更新倒计时
        placeholder.empty()  # 清空占位符并准备下一次更新

    st.markdown('<div class="footer">感谢你的耐心等待，愿这份期待充满爱意！💕</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # 结束 overlay div


if __name__ == "__main__":
    # 提供自定义日期开关（默认隐藏）
    if st.sidebar.checkbox("显示自定义日期设置", value=False):
        user_date = st.sidebar.date_input("请输入你期待的日期：", datetime(2025, 2, 13).date())
        user_time = st.sidebar.time_input("请输入具体时间：", datetime(2025, 2, 13, 0, 0).time())
        target_date = datetime.combine(user_date, user_time)
    else:
        target_date = datetime(2025, 2, 13, 0, 0, 0)

    countdown(target_date)
