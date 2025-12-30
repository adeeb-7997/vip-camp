import streamlit as st
import base64

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(
    page_title="محمية غلة الخير | M.F",
    page_icon="🐪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- دالة مساعدة لتحويل الصورة إلى كود (لتعمل الشعار بداخل التصميم) ---
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# حاول تحميل الشعار، إذا لم يوجد نستخدم نص بديل (لتجنب الخطأ)
try:
    logo_img = get_img_as_base64("logo.png")
    logo_html = f'<img src="data:image/png;base64,{logo_img}" class="logo-img">'
except:
    logo_html = "<h2>محمية غلة الخير</h2>"

# --- التصميم المتقدم (CSS Injection) ---
# هنا يكمن سر الفخامة والتحكم بالاتجاه
st.markdown(f"""
    <style>
    /* استيراد خطوط عربية فاخرة */
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Tajawal:wght@300;400;700&display=swap');

    /* تنسيق الصفحة بالكامل */
    .stApp {{
        background-color: #050505; /* أسود حالك */
        background-image: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #000000 100%);
    }}

    /* النصوص والخطوط */
    html, body, p, div, label, input, textarea, button {{
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl; /* إجبار الاتجاه من اليمين لليسار */
        text-align: right;
    }}

    h1, h2, h3 {{
        font-family: 'Amiri', serif !important; /* خط أميري للعناوين */
        color: #d4af37 !important; /* لون ذهبي */
        text-align: center;
    }}

    /* تنسيق الشعار في المنتصف */
    .logo-container {{
        display: flex;
        justify_content: center;
        align-items: center;
        padding: 20px 0;
        margin-bottom: 20px;
    }}
    .logo-img {{
        max-width: 300px; /* حجم الشعار */
        filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.3)); /* توهج ذهبي خفيف */
    }}

    /* البطاقات الشفافة (Glassmorphism) */
    .custom-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }}
    .custom-card:hover {{
        transform: translateY(-5px);
        border-color: rgba(212, 175, 55, 0.6);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    /* تنسيق حقول الإدخال لتكون من اليمين */
    .stTextInput input, .stTextArea textarea {{
        direction: rtl; 
        text-align: right;
        background-color: #1a1a1a;
        color: #d4af37;
        border: 1px solid #d4af37;
    }}
    
    /* تنسيق الزر */
    .stButton>button {{
        background: linear-gradient(45deg, #d4af37, #b8860b);
        color: black;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
    }}

    /* إخفاء القوائم العلوية */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- محتوى الصفحة ---

# 1. عرض الشعار
st.markdown(f'<div class="logo-container">{logo_html}</div>', unsafe_allow_html=True)

# 2. الترحيب (نص متحرك بسيط أو ثابت بفخامة)
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 style='font-size: 2.5em; margin-bottom: 10px;'>أهلاً بضيوف "غلة الخير"</h1>
        <p style='color: #cccccc; font-size: 1.2em;'>حيث الأصالة تعانق الطبيعة في ضيافة (M.F)</p>
    </div>
    <hr style='border-color: #d4af37; opacity: 0.3;'>
""", unsafe_allow_html=True)

# 3. الأقسام (باستخدام HTML مخصص داخل Markdown لضمان التصميم)
# نستخدم الأعمدة لترتيب البطاقات
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="custom-card">
        <h3 style="text-align: center;">🐪 أصالة الإبل</h3>
        <p style="color: #ddd; line-height: 1.8;">
        نعتز في "غلة الخير" بامتلاك سلالات نادرة من الإبل، رمز تراثنا وفخرنا (M.F)، حيث يمكن للضيوف الاستمتاع بمشاهدتها في بيئتها الطبيعية.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="custom-card">
        <h3 style="text-align: center;">🌴 المزرعة والخيرات</h3>
        <p style="color: #ddd; line-height: 1.8;">
        واحة غناء تضم أجود أنواع النخيل والمزروعات العضوية. نقدم لضيوفنا الكرام ما تجود به أرض المحمية من خيرات طازجة.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="custom-card">
        <h3 style="text-align: center;">☕ مجلس الضيافة</h3>
        <p style="color: #ddd; line-height: 1.8;">
        مجلس يجمع بين فخامة التجهيز وعبق الماضي، مجهز لاستقبال كبار الشخصيات والضيوف الأعزاء في جو من الخصوصية التامة.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. معرض صور (متحرك/سلايدر)
st.markdown("<h2 style='padding-top: 30px;'>من قلب المحمية</h2>", unsafe_allow_html=True)
# ملاحظة: استبدل الروابط بصور حقيقية من المحمية لاحقاً
images = [
    "https://images.unsplash.com/photo-1590634685366-0f72381f9645?auto=format&fit=crop&w=800&q=80", # صورة إبل
    "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=800&q=80", # صورة نخيل/مزرعة
    "https://images.unsplash.com/photo-1534068590799-09895a701e3e?auto=format&fit=crop&w=800&q=80", # صورة قهوة
]
st.image(images, width=None, caption=["شموخ الإبل", "خيرات المزرعة", "الضيافة العربية"], use_column_width=False)


# 5. سجل الزوار (النموذج)
st.markdown("<hr style='border-color: #d4af37; opacity: 0.3; margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<h3>📝 سجل كبار الزوار</h3>", unsafe_allow_html=True)

# وضع النموذج في المنتصف ليكون أنيقاً
empty1, form_col, empty2 = st.columns([1, 2, 1])

with form_col:
    with st.form("vip_guest_book"):
        st.markdown("<p style='text-align: center; color: #aaa;'>يسعدنا تدوين زيارتكم الكريمة</p>", unsafe_allow_html=True)
        name = st.text_input("الاسم الكريم")
        msg = st.text_area("كلمة للمكان وأهله")
        
        submitted = st.form_submit_button("تدوين الزيارة")
        if submitted:
            st.success(f"شرفت ونورت يا {name}، تدوينتك وسام على صدورنا.")

# تذييل الصفحة
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #555; font-size: 0.8em;'>
    تصميم خاص لـ محمية غلة الخير (M.F) | جميع الحقوق محفوظة
    </div>
""", unsafe_allow_html=True)
