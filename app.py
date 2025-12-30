import streamlit as st
import base64

# ================= إعدادات الصفحة =================
st.set_page_config(
    page_title="محمية غلة الخير | M.F",
    page_icon="🌾",
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

# ================= CSS (فاخر – هادئ – بدون أيقونات مزعجة) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;600&family=Reem+Kufi:wght@500;700&display=swap');

:root{
  --primary:#6b7d4a;   /* زيتوني أنيق */
  --dark:#2f3a2e;
  --bg:#f4f5f2;
  --card:#ffffff;
}

.stApp{
  background-color:var(--bg);
  direction:rtl;
}

html,body,[class*="css"]{
  font-family:'IBM Plex Sans Arabic', sans-serif !important;
}

#MainMenu,header,footer{visibility:hidden;}

/* ===== Header ===== */
.header{
  background:#ffffff;
  border-radius:24px;
  padding:50px 30px;
  margin-bottom:60px;
  text-align:center;
  box-shadow:0 20px 40px rgba(0,0,0,.06);
}
.header h1{
  font-family:'Reem Kufi', sans-serif;
  font-size:2.8rem;
  color:var(--dark);
  margin-bottom:10px;
}
.header p{
  font-size:1.1rem;
  color:#6d6d6d;
}

.logo img{
  max-width:200px;
  margin-bottom:20px;
}

/* ===== Sections ===== */
.section{
  background:var(--card);
  border-radius:22px;
  padding:30px;
  margin-bottom:40px;
  box-shadow:0 15px 35px rgba(0,0,0,.05);
}
.section h3{
  font-family:'Reem Kufi', sans-serif;
  color:var(--primary);
  margin-bottom:12px;
}
.section p{color:#555; line-height:1.8}

.section img{
  width:100%;
  border-radius:18px;
  margin-bottom:18px;
}

/* ===== Form ===== */
.stButton>button{
  background:var(--primary);
  color:white;
  border-radius:14px;
  border:none;
  padding:12px;
}

.footer{
  text-align:center;
  color:#999;
  margin-top:70px;
}
</style>
""", unsafe_allow_html=True)

# ================= Header =================
st.markdown('<div class="header">', unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div class="logo"><img src="data:image/png;base64,{logo_base64}"></div>', unsafe_allow_html=True)

st.markdown("""
<h1>محمية غلة الخير</h1>
<p>تجربة ريفية هادئة بطابع فاخر بعيدًا عن الضجيج</p>
</div>
""", unsafe_allow_html=True)

# ================= الأقسام =================
col1,col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="section">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=900">
      <h3>المجالس الريفية</h3>
      <p>مساحات جلوس واسعة بتصميم هادئ، مناسبة للعائلات والضيوف الباحثين عن الخصوصية والسكينة.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="section">
      <img src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=900">
      <h3>الطبيعة المفتوحة</h3>
      <p>مساحات خضراء وإطلالات طبيعية تمنحك صفاء الذهن ومتعة الاسترخاء.</p>
    </div>
    """, unsafe_allow_html=True)

# ================= تجربة الضيف =================
st.markdown("""
<div class="section">
  <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200">
  <h3>تجربة متكاملة</h3>
  <p>من لحظة الوصول وحتى المغادرة، نحرص على تقديم تجربة هادئة تعكس كرم الضيافة وروح المكان.</p>
</div>
""", unsafe_allow_html=True)

# ================= تواصل =================
st.markdown('<div class="section">', unsafe_allow_html=True)

with st.form("contact"):
    name = st.text_input("الاسم")
    msg = st.text_area("رسالتك")
    send = st.form_submit_button("إرسال")
    if send:
        st.success("تم استلام رسالتك، نرحب بك دائمًا")

st.markdown('</div>', unsafe_allow_html=True)

# ================= Footer =================
st.markdown('<div class="footer">محمية غلة الخير © 2025</div>', unsafe_allow_html=True)
