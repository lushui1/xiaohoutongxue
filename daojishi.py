from datetime import datetime
import streamlit as st
import time

def countdown(target_date):
    # 设置背景图片
    st.markdown("""
    <style>
    .stApp {
        background-image: url('https://github.com/lushui1/x-/raw/main/Snipaste_2025-01-02_16-27-40.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("💖 倒计时页面：期待乖乖的到来！")
    st.markdown("                         ")
    st.markdown("                         ")
    st.markdown("### 🌸 用爱装点的每一天，期待与你的相见 🌸")
    placeholder = st.empty()  # 创建占位符
    while True:
        now = datetime.now()
        time_diff = target_date - now

        if time_diff.total_seconds() <= 0:
            placeholder.empty()
            st.success("🎉 终于等到你！欢迎乖乖的到来 💕")
            st.balloons()
            break

        # 提取天、小时、分钟、秒
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 在占位符中动态更新内容
        with placeholder.container():
            st.markdown(
                f"""
                ❤️ **距离乖乖到来还有：**
                - **{days} 天**
                - **{hours:02} 小时**
                - **{minutes:02} 分钟**
                - **{seconds:02} 秒**
                """
            )

        time.sleep(1)
        placeholder.empty()  # 清空占位符并准备下一次更新

if __name__ == "__main__":
    target_date = datetime(2025, 2, 13, 0, 0, 0)
    countdown(target_date)
