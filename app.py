import streamlit as st
import base64

# ================= إعدادات الصفحة =================
st.set_page_config(
    page_title="محمية غلة الخير",
    page_icon="🌿",
    layout="wide"
)

# ================= تحميل الشعار =================
def get_base64_of_bin_file(path):
    try:
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo_base64 = get_base64_of_bin_file("logo.png")

# ================= CSS (هادئ – ضيافة – بدون صناديق أو حجز) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500&display=swap');

:root{
  --text:#2f2f2f;
  --soft:#6f6f6f;
  --bg:#fbfbf9;
}

.stApp{
  background-color:var(--bg);
  direction:rtl;
}

html,body,[class*="css"]{
  font-family:'Alexandria', sans-serif !important;
  text-align:right;
}

#MainMenu,header,footer{visibility:hidden;}

/* ===== الشعار ===== */
.logo{
  text-align:center;
  margin:60px 0 40px;
}
.logo img{
  max-width:220px;
}

/* ===== العناوين ===== */
.title{
  text-align:center;
  font-size:2.4rem;
  color:var(--text);
  margin-bottom:10px;
}

.subtitle{
  text-align:center;
  font-size:1.1rem;
  color:var(--soft);
  margin-bottom:60px;
}

/* ===== أقسام نصية هادئة ===== */
.section{
  max-width:900px;
  margin:0 auto 60px;
  line-height:2;
  color:var(--text);
}

.section h3{
  font-size:1.5rem;
  margin-bottom:12px;
}

.section p{color:var(--soft); font-size:1.05rem}

/* ===== صور ===== */
.section img{
  width:100%;
  border-radius:14px;
  margin:25px 0;
}

.footer{
  text-align:center;
  color:#aaa;
  margin:80px 0 30px;
}
</style>
""", unsafe_allow_html=True)

# ================= الشعار =================
if logo_base64:
    st.markdown(f'<div class="logo"><img src="data:image/png;base64,{logo_base64}"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo"><h2>محمية غلة الخير</h2></div>', unsafe_allow_html=True)

# ================= العنوان =================
st.markdown('<div class="title">محمية غلة الخير</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">مكان للضيافة واستقبال الضيوف في أجواء طبيعية هادئة</div>', unsafe_allow_html=True)

# ================= المحتوى =================
st.markdown("""
<div class="section">
<h3>عن المحمية</h3>
<p>
محمية غلة الخير خُصصت لاستقبال الضيوف وتقديم الضيافة في بيئة طبيعية هادئة، بعيدًا عن مفهوم الإيجار أو الاستضافة التجارية.
نرحب بضيوفنا بروح الكرم والأصالة، حيث البساطة والراحة والخصوصية.
</p>
<img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1200">
</div>

<div class="section">
<h3>الأجواء</h3>
<p>
أجواء طبيعية مفتوحة، جلسات هادئة، ومكان يليق بالضيوف الباحثين عن السكينة والتقدير.
</p>
<img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200">
</div>
""", unsafe_allow_html=True)

# ================= Footer =================
st.markdown('<div class="footer">محمية غلة الخير © 2025</div>', unsafe_allow_html=True)
