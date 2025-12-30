import streamlit as st
import base64
import os

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="محمية غلة الخير | M.F",
    page_icon="🌿",
    layout="wide"
)

# --- دالة معالجة الشعار ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

logo_base64 = get_base64_of_bin_file("logo.png")

# --- CSS التنسيق العصري الفاتح ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Tajawal:wght@400;500;700&display=swap');

    /* الخلفية فاتحة وعصرية */
    .stApp {{
        background-color: #fcfaf7;
        color: #4a4a4a;
        direction: rtl;
    }}

    /* تحسين الخطوط والاتجاه */
    html, body, [class*="css"] {{
        font-family: 'Tajawal', sans-serif !important;
        text-align: right;
    }}

    /* تصميم الشعار */
    .logo-container {{
        text-align: center;
        padding: 20px 0;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 40px;
    }}
    .logo-img {{
        max-width: 280px;
        filter: brightness(1.1); /* تفتيح الشعار إذا كان غامقاً */
    }}

    /* بطاقات الأقسام (تصميم نظيف وعصري) */
    .section-card {{
        background: white;
        border-radius: 20px;
        padding: 0px;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
        overflow: hidden;
        transition: 0.3s;
    }}
    .section-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }}
    .card-content {{
        padding: 20px;
        text-align: center;
    }}

    /* العناوين */
    h1, h2, h3 {{
        font-family: 'Amiri', serif !important;
        color: #2c3e50 !important;
    }}
    .gold-text {{ color: #d4af37 !important; }}

    /* أزرار وحقول النموذج */
    .stButton>button {{
        background: #2e7d32; /* أخضر طبيعي */
        color: white;
        border-radius: 10px;
        width: 100%;
        border: none;
    }}
    
    #MainMenu, header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر والشعار ---
if logo_base64:
    st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" class="logo-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="logo-container"><h1>محمية غلة الخير</h1></div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>مرحباً بكم في <span class='gold-text'>غلة الخير</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2em; color:#7f8c8d;'>واحة الضيافة والأصالة في قلب الطبيعة</p>", unsafe_allow_html=True)

st.write("##")

# --- الأقسام الرئيسية مع الصور ---
col1, col2, col3 = st.columns(3)

with col1:
    # صورة خيمة فخمة (خيمة المرعي)
    st.markdown(f"""
    <div class="section-card">
        <img src="https://images.unsplash.com/photo-1510739859545-e7b9e979de86?q=80&w=800" style="width:100%; height:200px; object-fit:cover;">
        <div class="card-content">
            <h3>⛺ خيمة المرعي</h3>
            <p>جلسات عربية أصيلة بلمسات عصرية، مجهزة لاستقبالكم في أجواء من الفخامة والهدوء.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # صورة ناقة في مكان ربيع
    st.markdown(f"""
    <div class="section-card">
        <img src="https://images.unsplash.com/photo-1557223563-703333333a41?q=80&w=800" style="width:100%; height:200px; object-fit:cover;">
        <div class="card-content">
            <h3>🦌 المحمية الخاصة</h3>
            <p>شاهدوا جمال النوق في مرعاها الأخضر وسط الطبيعة البكر والربيع المزهر.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # صورة خيرات المزرعة
    st.markdown(f"""
    <div class="section-card">
        <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?q=80&w=800" style="width:100%; height:200px; object-fit:cover;">
        <div class="card-content">
            <h3>🌾 خيرات المزرعة</h3>
            <p>نحصد لكم يومياً أجود أنواع الخضار والقمح العضوي من قلب مزارعنا لتصل لضيافتكم.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- معرض الصور (لقطات من المخيم) ---
st.write("---")
st.markdown("<h2 style='text-align:center;'>📸 لقطات من المخيم</h2>", unsafe_allow_html=True)

img_col1, img_col2 = st.columns(2)
with img_col1:
    st.image("https://images.unsplash.com/photo-1493246507139-91e8bef99c17?q=80&w=800", caption="المناظر الطبيعية حول المخيم", use_container_width=True)
with img_col2:
    st.image("https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?q=80&w=800", caption="أجواء المساء والسمر", use_container_width=True)

# --- سجل الزوار ---
st.write("---")
st.markdown("<h3 style='text-align:center;'>🤝 يسعدنا تواصلكم</h3>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,2,1])
with c2:
    with st.form("contact"):
        name = st.text_input("الاسم الكريم")
        msg = st.text_area("رسالة للمضيف")
        submitted = st.form_submit_button("إرسال")
        if submitted:
            st.success("شكراً لك، تم استلام رسالتك.")

# تذييل
st.markdown("<p style='text-align:center; color:#bdc3c7; margin-top:50px;'>محمية غلة الخير - M.F © 2025</p>", unsafe_allow_html=True)
