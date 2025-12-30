import streamlit as st
import base64
import os

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="محمية غلة الخير | M.F",
    page_icon="🐪",
    layout="wide"
)

# --- دالة حل مشكلة الشعار ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# تأكد أن ملف الصورة موجود بنفس المجلد وبنفس الاسم
logo_filename = "logo.png" 

if os.path.exists(logo_filename):
    encoded_logo = get_base64_of_bin_file(logo_filename)
    logo_html = f'<img src="data:image/png;base64,{encoded_logo}" class="logo-img">'
else:
    logo_html = "<h1 style='color:#d4af37;'>محمية غلة الخير</h1>"

# --- تصميم الـ CSS المتقدم ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Tajawal:wght@300;500;700&display=swap');

    /* تغيير الخلفية إلى البني العميق الفاخر */
    .stApp {{
        background: linear-gradient(135deg, #1e1510 0%, #3d2b1f 100%);
        color: #f4ece1;
        direction: rtl;
    }}

    /* تنسيق المحتوى ليكون من اليمين */
    div[data-testid="stVerticalBlock"] {{
        direction: rtl;
        text-align: right;
    }}

    /* تحسين شكل الشعار والتحكم في ألوانه بصرياً */
    .logo-container {{
        text-align: center;
        padding: 40px 0;
    }}
    .logo-img {{
        max-width: 350px;
        /* هذا الفلتر يحسن تباين الشعار الذهبي */
        filter: drop-shadow(0px 0px 15px rgba(212, 175, 55, 0.4)) contrast(1.1);
    }}

    /* البطاقات بتصميم جلدي فاخر */
    .vip-card {{
        background: rgba(255, 255, 255, 0.03);
        border-right: 4px solid #d4af37; /* خط ذهبي جهة اليمين */
        border-radius: 10px;
        padding: 30px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: 0.3s;
    }}
    .vip-card:hover {{
        background: rgba(212, 175, 55, 0.05);
        transform: scale(1.02);
    }}

    /* العناوين */
    h1, h2, h3 {{
        font-family: 'Amiri', serif !important;
        color: #d4af37 !important;
    }}
    
    /* أيقونات الأقسام */
    .icon-style {{
        font-size: 40px;
        margin-bottom: 15px;
        display: block;
    }}

    /* إخفاء واجهة ستريمليت الافتراضية */
    #MainMenu, header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- محتوى الموقع ---

# عرض الشعار
st.markdown(f'<div class="logo-container">{logo_html}</div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>مجلس الضيافة الخاص</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#f4ece1; font-size:1.2em;'>نتشرف بزيارتكم في محمية ومزرعة غلة الخير</p>", unsafe_allow_html=True)

st.write("---")

# توزيع الأقسام
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="vip-card">
        <span class="icon-style">🏛️</span>
        <h3>المجلس الملكي</h3>
        <p>خصوصية تامة وتجهيزات تليق بمقام ضيوفنا الكرام، في قلب الطبيعة الهادئة.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="vip-card">
        <span class="icon-style">🦌</span>
        <h3>المحمية الخاصة</h3>
        <p>جولة بين سلالات الإبل والمها العربي، تجربة برية فريدة بروح الأصالة.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="vip-card">
        <span class="icon-style">🌳</span>
        <h3>خيرات المزرعة</h3>
        <p>نقدم لضيوفنا أجود ما تنتجه مزارعنا من تمور وفواكه عضوية طازجة.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("##")

# قسم الصور (تأكد من استبدالها بصور حقيقية لاحقاً)
st.markdown("<h3>📸 لقطات من المحمية</h3>", unsafe_allow_html=True)
# استخدم صوراً عرضية (Landscape) لجمالية التصميم
img_url = "https://images.unsplash.com/photo-1542332213-31f87348057f?auto=format&fit=crop&w=1200&q=80"
st.image(img_url, caption="غروب الشمس في غلة الخير", use_column_width=True)

# سجل الزوار بتنسيق أنيق
st.write("---")
st.markdown("<h3 style='text-align:center;'>🤝 تواصل معنا</h3>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,2,1])
with c2:
    with st.form("visitor_form"):
        name = st.text_input("الاسم الكريم")
        contact = st.text_input("رقم الجوال / وسيلة التواصل")
        note = st.text_area("رسالة إلى المضيف")
        submitted = st.form_submit_button("إرسال البيانات")
        if submitted:
            st.success("تم استلام بياناتك بنجاح، نتشرف بك.")

# تذييل
st.markdown("<p style='text-align:center; color:#888; margin-top:50px;'>محمية غلة الخير - M.F © 2024</p>", unsafe_allow_html=True)
