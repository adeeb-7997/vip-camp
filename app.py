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

# ================= CSS =================
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
.logo{
  text-align:center !important;
  margin:70px 0 40px;
}
.logo img{max-width:220px;}
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
  margin-bottom:50px;
}
.panel{
  max-width:900px;
  margin:0 auto 60px;
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
st.markdown('<div class="title">حياكم الله في محمية غلة الخير</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">واحة الضيافة والأصالة في قلب الطبيعة</div>', unsafe_allow_html=True)

# ================= الأقسام =================
sections = [
    {
        'title': 'عن المحمية',
        'text': 'محمية غلة الخير أنشئت لتكون مجلسًا للضيف وراحة البال، بعيدًا عن الزحام والتكلّف.',
        'img': ''
    },
    {
        'title': 'خيمة المرعي (المجلس)',
        'text': 'مجلس الضيافة الرئيس في المحمية، فيه تُستقبل الوجوه الكريمة، وتُدار السوالف على نار هادئة، وتُقدَّم القهوة العربية التقليدية.',
        'img': 'data:image/jpeg;base64,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'
    },

    {
        'title': 'خيرات المحمية',
        'text': 'ما يُقدَّم من خيرات الأرض، خضار طازجة وحليب صافٍ ومشتقات طبيعية، يُقدَّم للضيف كما هو… بلا تكلّف.',
        'img': 'https://images.unsplash.com/photo-1506806732259-39c2d0268443?q=80&w=1400'
    },
    {
        'title': 'الإبل',
        'text': 'الإبل جزء من هوية المكان، شاهدة على تراث أصيل، وحاضرة كما كانت في حياة أهل البادية. نرجو عدم إزعاج الإبل أو إطعامها دون إذن.',
        'img': 'https://cnn-arabic-images.cnn.io/cloudinary/image/upload/w_1280,c_scale,q_auto/cnnarabic/2023/01/11/images/230397.jpg'
    },
    {
        'title': 'محمية الربيع',
        'text': 'عند اعتدال الجو، تكسو الأرض بالخضرة، وتزدهر المراعي الطبيعية، ليصبح المكان متنفسًا للنظر وراحة للنفس.',
        'img': 'https://images.unsplash.com/photo-1495107334309-fcf20504a5ab?q=80&w=1400'
    },
    {
        'title': 'خيمة الصباحية – قهوة الصباح',
        'text': 'تُقدّم القهوة على مهل لتبدأ اليوم بأجواء هادئة وعطرية.',
        'img': 'https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?q=80&w=1400'
    },
        {
        'title': ' coffee  ',
        'text': 'هنا تُحضّر القهوة المختصة بعناية، من حبوب مختارة، وبطريقة تليق بالضيف الكريم.',
        'img': 'https://cdn.salla.sa/DPYKd/d7f15aa2-0305-4058-8113-f48d201fad38-1000x1000-OAQqaie3rxgLcQ9vNTzA102ejR8xOb9VZRvZzpTT.png'
    },
    {
        'title': 'خيمة الألعاب',
        'text': 'مساحة آمنة للأطفال للمرح والتسلية     .',
        'img': 'https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?q=80&w=1400'
    }
]

for sec in sections:
    st.markdown(f"""
    <div class="panel">
        <h3>{sec['title']}</h3>
        <p>{sec['text']}</p>
        {'<img src="'+sec['img']+'">' if sec['img'] else ''}
    </div>
    """, unsafe_allow_html=True)

# ================= الخاتمة =================
st.markdown('<div class="footer">سعدنا بزيارتكم، حياكم الله في محمية غلة الخير © 2025</div>', unsafe_allow_html=True)


