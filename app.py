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

# ================= CSS (لوحة تعريف – بسيطة – RTL ثابت) =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500&display=swap');

html, body {
  direction: rtl !important;
}

* {
  font-family: 'Alexandria', sans-serif !important;
  text-align: right;
}

.stApp{
  background-color:#fbfbf8;
}

#MainMenu, header, footer {visibility:hidden;}

/* ===== الشعار ===== */
.logo{
  text-align:center !important;
  margin:70px 0 40px;
}
.logo img{max-width:220px;}

/* ===== العنوان ===== */
.title{
  text-align:center !important;
  font-size:2.2rem;
  color:#2b2b2b;
  margin-bottom:12px;
}
.subtitle{
  text-align:center !important;
  font-size:1.05rem;
  color:#6b6b6b;
  margin-bottom:70px;
}

/* ===== اللوحة ===== */
.panel{
  max-width:900px;
  margin:0 auto 80px;
}
.panel h3{
  font-size:1.5rem;
  margin-bottom:14px;
  color:#2b2b2b;
}
.panel p{
  font-size:1.05rem;
  color:#555;
  line-height:2.1;
}
.panel img{
  width:100%;
  border-radius:14px;
  margin:28px 0;
}

.footer{
  text-align:center !important;
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
st.markdown('<div class="subtitle">لوحة تعريفية لمكان خُصص لاستقبال الضيوف وتقديم الضيافة</div>', unsafe_allow_html=True)

# ================= لوحة التعريف =================
st.markdown("""
<div class="panel">
<h3>عن المحمية</h3>
<p>
...
</p>
</div>

<div class="panel">
<h3>خيمة المرعي (خيمة المجلس)</h3>
<p>
خيمة المجلس هي مقر استقبال الضيوف، أُعدّت بجلسات عربية فاخرة تعكس روح الكرم والأصالة،
وتُقام فيها المجالس واللقاءات في أجواء هادئة وخاصة.
</p>
<img src="https://images.unsplash.com/photo-1510739859545-e7b9e979de86?q=80&w=1400">
</div>

<div class="panel">
<h3>خيرات المحمية</h3>
<p>
تضم المحمية خيرات طبيعية من الخضار والحليب ومشتقاته،
وتُقدَّم للضيوف كجزء من الضيافة بما يعكس بساطة المكان وجودة إنتاجه.
</p>
<img src="https://images.unsplash.com/photo-1506806732259-39c2d0268443?q=80&w=1400">
</div>

<div class="panel">
<h3>الإبل</h3>
<p>
تحتضن المحمية عددًا من الإبل، وتُعد جزءًا من هوية المكان وتراثه،
وتُشاهد في بيئتها الطبيعية ضمن أجواء هادئة تحافظ على أصالتها.
</p>
<img src="https://images.unsplash.com/photo-1557223563-703333333a41?q=80&w=1400">
</div>

<div class="panel">
<h3>محمية الربيع</h3>
<p>
في موسم الربيع تكتسي المحمية بالخضرة، وتزدهر المراعي الطبيعية،
مما يضفي على المكان جمالًا وراحةً تعكس روح الطبيعة.
</p>
<img src="https://images.unsplash.com/photo-1495107334309-fcf20504a5ab?q=80&w=1400">
</div>
""", unsafe_allow_html=True)

# ================= Footer =================
st.markdown('<div class="footer">محمية غلة الخير © 2025</div>', unsafe_allow_html=True)
