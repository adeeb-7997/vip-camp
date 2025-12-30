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
'img': 'https://ar.tripadvisor.com/Hotel_Review-g294209-d943370-Reviews-Porini_Lion_Camp-Maasai_Mara_National_Reserve_Rift_Valley_Province.html'
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
        'img': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Niels_Feijen_NL.JPG'
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







