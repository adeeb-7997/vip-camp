import streamlit as st
import base64

# ================= إعدادات الصفحة =================
st.set_page_config(
    page_title="محمية غلة الخير | M.F",
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

# ================= CSS عصري (Glass + Minimal) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&family=Amiri:wght@700&display=swap');

:root{
  --green:#1b5e20;
  --soft-green:#2e7d32;
  --gold:#c9a44c;
  --bg:#f7f8f5;
  --card:rgba(255,255,255,0.75);
}

.stApp{
  background: linear-gradient(180deg,#fafafa,#f1f3ef);
  direction: rtl;
}

html,body,[class*="css"]{
  font-family:'Tajawal',sans-serif !important;
}

#MainMenu,header,footer{visibility:hidden;}

/* ===== Hero ===== */
.hero{
  background: linear-gradient(135deg,#1b5e20,#4caf50);
  color:white;
  padding:60px 30px;
  border-radius:28px;
  margin-bottom:50px;
  box-shadow:0 20px 40px rgba(0,0,0,.15);
}
.hero h1{font-family:'Amiri',serif; font-size:3rem;}
.hero p{font-size:1.2rem; opacity:.9}

/* ===== Logo ===== */
.logo{
  text-align:center;
  margin-bottom:25px;
}
.logo img{max-width:220px; filter:drop-shadow(0 10px 20px rgba(0,0,0,.25));}

/* ===== Cards ===== */
.card{
  background:var(--card);
  backdrop-filter: blur(14px);
  border-radius:22px;
  overflow:hidden;
  box-shadow:0 15px 35px rgba(0,0,0,.08);
  transition:.35s ease;
  border:1px solid rgba(255,255,255,.4);
}
.card:hover{transform:translateY(-8px) scale(1.01);}
.card img{width:100%; height:210px; object-fit:cover;}
.card .content{padding:22px; text-align:center;}
.card h3{color:var(--green); font-weight:700;}

/* ===== Buttons ===== */
.stButton>button{
  background: linear-gradient(135deg,var(--green),var(--soft-green));
  color:white;
  border-radius:14px;
  width:100%;
  border:none;
  padding:12px;
  font-size:1rem;
}
.stButton>button:hover{opacity:.9}

/* ===== Section titles ===== */
.section-title{
  text-align:center;
  font-family:'Amiri',serif;
  color:#2c3e50;
  margin:40px 0 25px;
}

.footer{
  text-align:center;
  color:#9e9e9e;
  margin-top:60px;
}
</style>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
  <div class="logo">
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<img src="data:image/png;base64,{logo_base64}">', unsafe_allow_html=True)

st.markdown("""
  </div>
  <h1>محمية غلة الخير</h1>
  <p>واحة الضيافة والأصالة… حيث تلتقي الطبيعة بالفخامة</p>
</div>
""", unsafe_allow_html=True)

# ================= الأقسام =================
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
      <img src="https://images.unsplash.com/photo-1510739859545-e7b9e979de86?q=80&w=800">
      <div class="content">
        <h3>⛺ خيمة المرعي</h3>
        <p>جلسات عربية راقية بلمسة عصرية، مثالية للاجتماعات والسمر.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
      <img src="https://images.unsplash.com/photo-1557223563-703333333a41?q=80&w=800">
      <div class="content">
        <h3>🦌 المحمية الخاصة</h3>
        <p>تجربة فريدة لمشاهدة النوق في بيئتها الطبيعية الهادئة.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
      <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?q=80&w=800">
      <div class="content">
        <h3>🌾 خيرات المزرعة</h3>
        <p>منتجات طازجة وعضوية من مزارعنا مباشرة إلى ضيافتكم.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ================= معرض الصور =================
st.markdown('<h2 class="section-title">📸 لقطات من المحمية</h2>', unsafe_allow_html=True)

g1,g2 = st.columns(2)
with g1:
    st.image("https://images.unsplash.com/photo-1493246507139-91e8bef99c17?q=80&w=900", use_container_width=True)
with g2:
    st.image("https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?q=80&w=900", use_container_width=True)

# ================= تواصل =================
st.markdown('<h2 class="section-title">🤝 تواصل معنا</h2>', unsafe_allow_html=True)

c1,c2,c3 = st.columns([1,2,1])
with c2:
    with st.form("contact"):
        name = st.text_input("الاسم الكريم")
        msg = st.text_area("رسالتك")
        send = st.form_submit_button("إرسال")
        if send:
            st.success("تم استلام رسالتك، نرحب بك دائماً 🌿")

# ================= Footer =================
st.markdown('<div class="footer">محمية غلة الخير © 2025</div>', unsafe_allow_html=True)
