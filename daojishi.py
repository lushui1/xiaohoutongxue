from datetime import datetime
import streamlit as st
import time

def countdown(target_date):
    # 设置背景图片和样式
    st.markdown("""
    <style>
    .stApp {
        background-image: url('https://github.com/lushui1/x-/raw/main/Snipaste_2025-01-02_16-27-40.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
    }
    .overlay {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #FFC107;
        text-shadow: 2px 2px 5px #000000;
        margin-bottom: 20px;
        animation: glow 1.5s infinite;
    }
    .subtitle {
        font-size: 25px;
        font-weight: 500;
        color: #FFD700;
        margin-bottom: 30px;
    }
    .countdown {
        font-size: 60px;
        font-weight: bold;
        color: #FFFFFF;
        text-shadow: 4px 4px 8px #000000;
        margin-top: 20px;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    @keyframes glow {
        0% { text-shadow: 0 0 5px #FFD700, 0 0 10px #FFD700; }
        50% { text-shadow: 0 0 15px #FFD700, 0 0 30px #FFD700; }
        100% { text-shadow: 0 0 5px #FFD700, 0 0 10px #FFD700; }
    }
    .footer {
        font-size: 18px;
        color: #BBBBBB;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

    # 包装内容
    st.markdown('<div class="overlay">', unsafe_allow_html=True)
    st.markdown('<div class="title">💖 倒计时页面：期待乖乖的到来！</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">🌸 用爱装点的每一天，期待与你的相见 🌸</div>', unsafe_allow_html=True)

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

        time.sleep(1)
        placeholder.empty()  # 清空占位符并准备下一次更新

    st.markdown('<div class="footer">感谢你的耐心等待，愿这份期待充满爱意！💕</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # 结束 overlay div

if __name__ == "__main__":
    target_date = datetime(2025, 2, 13, 0, 0, 0)
    countdown(target_date)
