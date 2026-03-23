import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Mobile Addiction Analyzer", page_icon="📱", layout="wide")

# Load model
model = pickle.load(open("addiction_model.pkl", "rb"))

# Custom CSS for styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📱 Mobile Addiction Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Analyze your daily mobile usage habits</h4>", unsafe_allow_html=True)

st.write("---")

# Sidebar Inputs
st.sidebar.header("📊 Enter Your Daily Habits")
screen = st.sidebar.slider("Screen Time (hrs)", 0, 12)
social = st.sidebar.slider("Social Media Usage (hrs)", 0, 12)
sleep = st.sidebar.slider("Sleep Hours", 0, 12)
study = st.sidebar.slider("Study Hours", 0, 12)
notifications = st.sidebar.slider("Daily Notifications", 0, 200)

# Metrics Dashboard
st.subheader("📈 Daily Usage Summary")

col1, col2, col3 = st.columns(3)
col1.metric("📱 Screen Time", f"{screen} hrs")
col2.metric("📲 Social Media", f"{social} hrs")
col3.metric("😴 Sleep", f"{sleep} hrs")

col4, col5 = st.columns(2)
col4.metric("📚 Study", f"{study} hrs")
col5.metric("🔔 Notifications", f"{notifications}")

st.write("---")

# Visualization Section
st.subheader("📊 Usage Visualization")

colA, colB = st.columns(2)

# Pie Chart (Fixed)
with colA:
    st.write("### Time Distribution")
    labels = ['Screen', 'Social Media', 'Study', 'Sleep']
    values = [screen, social, study, sleep]

    if sum(values) == 0:
        st.warning("Enter values to display pie chart")
    else:
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%')
        ax1.axis('equal')
        st.pyplot(fig1)

# Bar Chart
with colB:
    st.write("### Daily Activity Comparison")
    activities = ['Screen', 'Social', 'Sleep', 'Study', 'Notifications']
    data = [screen, social, sleep, study, notifications]

    fig2, ax2 = plt.subplots()
    ax2.bar(activities, data)
    st.pyplot(fig2)

st.write("---")

# Prediction Section
st.subheader("🤖 Addiction Prediction")

if st.button("🔍 Check Addiction Level"):

    data = np.array([[screen, social, sleep, study, notifications]])
    result = model.predict(data)

    # Addiction Score
    score = (screen + social + notifications/50) / 3
    st.write("### Addiction Score")
    st.progress(min(int(score * 10), 100))
    st.write(f"Score: {round(score,2)} / 10")

    if result == 0:
        st.success("🟢 Normal Usage")
        st.info("Your mobile usage is balanced. Keep it up!")

    elif result == 1:
        st.warning("🟡 Risk of Addiction")
        st.info("Try reducing screen time and notifications.")

    else:
        st.error("🔴 High Addiction Level")
        st.info("Reduce mobile usage and improve sleep habits.")

    # Tips Section
    st.write("### 📌 Tips to Reduce Mobile Addiction")
    st.write("""
    - Turn off unnecessary notifications  
    - Avoid phone before sleep  
    - Set daily screen limits  
    - Do physical activities  
    - Use focus apps  
    """)

st.write("---")
st.caption("AI Mobile Addiction Analyzer | Streamlit + Machine Learning")