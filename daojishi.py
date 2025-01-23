from datetime import datetime
import streamlit as st
import time

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
        font-family: 'Helvetica Neue', sans-serif;
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
        color: #4A90E2;
        margin-bottom: 20px;
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


