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

# ================= CSS (RTL صحيح + خط ناعم) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500&display=swap');

:root{
  --text:#2b2b2b;
  --muted:#6b6b6b;
  --bg:#fbfbf8;
}

html, body {
  direction: rtl !important;
}

.stApp {
  background-color: var(--bg);
}

* {
  font-family: 'Alexandria', sans-serif !important;
  text-align: right;
}

#MainMenu, header, footer {visibility: hidden;}

/* ===== الشعار ===== */
.logo {
  text-align: center !important;
  margin: 60px 0 30px;
}
.logo img {
  max-width: 220px;
}

/* ===== العناوين ===== */
.title {
  text-align: center !important;
  font-size: 2.3rem;
  color: var(--text);
  margin-bottom: 10px;
}
.subtitle {
  text-align: center !important;
  font-size: 1.1rem;
  color: var(--muted);
  margin-bottom: 60px;
}

/* ===== الأقسام ===== */
.section {
  max-width: 1000px;
  margin: 0 auto 70px;
}
.section h3 {
  font-size: 1.6rem;
  margin-bottom: 12px;
}
.section p {
  font-size: 1.05rem;
  color: var(--muted);
  line-height: 2;
}
.section img {
  width: 100%;
  border-radius: 14px;
  margin: 25px 0;
}

.footer {
  text-align: center !important;
  color: #aaa;
  margin: 80px 0 30px;
}
</style>
""", unsafe_allow_html=True)

# ================= الشعار =================
if logo_base64:
    st.markdown(
        f'<div class="logo"><img src="data:image/png;base64,{logo_base64}"></div>',
        unsafe_allow_html=True
    )
else:
    st.markdown('<div class="logo"><h2>محمية غلة الخير</h2></div>', unsafe_allow_html=True)

# ================= العنوان =================
st.markdown('<div class="title">محمية غلة الخير</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">مكان مخصص لاستقبال الضيوف وتقديم الضيافة في أجواء طبيعية هادئة</div>', unsafe_allow_html=True)

# ================= الأقسام =================

# خيمة المرعي
st.markdown("""
<div class="section">
  <h3>خيمة المرعي (خيمة المجلس)</h3>
  <p>
    خيمة المجلس هي قلب المحمية، أُعدّت لاستقبال الضيوف في أجواء من الوقار والكرم،
    بجلسات فاخرة تجمع بين الأصالة والراحة، ومكان يليق بالضيوف والتشريف.
  </p>
  <img src="https://images.unsplash.com/photo-1510739859545-e7b9e979de86?q=80&w=1400">
</div>
""", unsafe_allow_html=True)

# خيرات المحمية
st.markdown("""
<div class="section">
  <h3>خيرات المحمية</h3>
  <p>
    نعتني بإنتاج خيرات المحمية من الخضار الطازجة والحليب ومشتقاته،
    لتُقدّم للضيوف بجودة عالية وطابع طبيعي يعكس بساطة المكان ونقاءه.
  </p>
  <img src="https://images.unsplash.com/photo-1506806732259-39c2d0268443?q=80&w=1400">
</div>
""", unsafe_allow_html=True)

# محمية الربيع
st.markdown("""
<div class="section">
  <h3>محمية الربيع</h3>
  <p>
    في موسم الربيع، تكتسي المحمية بالخضرة وتنبض بالحياة، حيث المساحات المفتوحة
    والمراعي الطبيعية التي تبعث الراحة والسكينة في النفوس.
  </p>
  <img src="https://images.unsplash.com/photo-1495107334309-fcf20504a5ab?q=80&w=1400">
</div>
""", unsafe_allow_html=True)

# ================= Footer =================
st.markdown('<div class="footer">محمية غلة الخير © 2025</div>', unsafe_allow_html=True)
