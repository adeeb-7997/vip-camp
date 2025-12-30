import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="المجلس الخاص | Royal Hospitality",
    page_icon="☕",
    layout="wide"
)

# 2. التنسيق الفاخر (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
    }
    
    .stApp {
        background-color: #1a1a1a;
        color: #e5c100; /* ذهبي */
    }
    
    h1, h2, h3 {
        color: #e5c100 !important;
        text-align: center;
    }
    
    /* تنسيق الحقول */
    .stTextInput > div > div > input {
        color: white;
        background-color: #333;
        border: 1px solid #e5c100;
    }

    /* إخفاء العناصر غير المرغوبة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة الترحيب
st.markdown("<h1 style='padding-top: 0;'>مخيم ومحمية (اسم العائلة/المالك)</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-weight: lighter; color: white !important;'>أهلاً وسهلاً بالضيوف الكرام في مجلسنا الخاص</h3>", unsafe_allow_html=True)
st.markdown("---")

# صورة ترحيبية (دلة قهوة أو مجلس)
st.image("https://images.unsplash.com/photo-1577056923223-2b2f63cb5736?auto=format&fit=crop&w=1920&q=80", use_column_width=True)

# 4. نبذة عن المكان (من منظور ضيافة)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🦌 المحمية والمزرعة")
    st.write("""
    نستقبل ضيوفنا الكرام في واحة تجمع بين أصالة الماضي ورفاهية الحاضر.
    المكان مجهز بمحمية خاصة ومزرعة إنتاجية لتقديم واجب الضيافة من خيرات الأرض مباشرة.
    """)

with col2:
    st.markdown("### ☕ المجلس الرئيسي")
    st.write("""
    تم تجهيز الموقع ليكون ملتقى للأحبة والأصدقاء، حيث تتوفر كافة سبل الراحة
    والخصوصية التامة لزوارنا الكرام.
    """)

st.markdown("---")

# 5. التواصل (بدلاً من الحجز)
st.markdown("### 📨 للتواصل وترتيب الزيارات")
st.write("نسعد بتواصلكم لترتيب زيارتكم وتشريفنا في الموقع.")

with st.form("guest_book"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("الاسم الكريم")
    with c2:
        phone = st.text_input("رقم التواصل")
    
    notes = st.text_area("ملاحظات أو تاريخ الزيارة المقترح")
    
    submit = st.form_submit_button("إرسال")
    if submit:
        st.success(f"حياك الله يا {name}، وصلت رسالتك وسيتم التواصل معك.")