# build_scratch_site.py
# تولیدکننده سایت آموزش اسکرچ و اسکرچ جونیور
# همه HTMLها داخل خود پایتون ساخته می‌شن

import os
import datetime

# ==========================================
# ۱. دیتای دوره‌ها
# ==========================================
COPYRIGHT_YEAR = datetime.datetime.now().year

# دوره‌های اسکرچ جونیور (۵ تا ۸ سال)
SCRATCHJR_COURSES = [
    {
        'id': 1,
        'title': 'آشنایی با اسکرچ جونیور',
        'level': 'مبتدی',
        'age': '۵ تا ۷ سال',
        'duration': '۴ جلسه',
        'price': 'رایگان',
        'description': 'آشنایی با محیط اسکرچ جونیور، شخصیت‌ها و ابزارهای اولیه',
        'topics': ['معرفی محیط برنامه', 'آشنایی با شخصیت‌ها', 'حرکت دادن شخصیت', 'اضافه کردن صدا', 'ذخیره کردن پروژه'],
        'color': '#FF6B6B',
        'emoji': '🎮',
        'video_link': 'https://www.aparat.com/v/bewg9bw'
    },
    {
        'id': 2,
        'title': 'ساخت انیمیشن ساده',
        'level': 'مبتدی',
        'age': '۶ تا ۸ سال',
        'duration': '۶ جلسه',
        'price': 'رایگان',
        'description': 'یادگیری ساخت انیمیشن‌های ساده با شخصیت‌های اسکرچ جونیور',
        'topics': ['حرکت‌های مختلف', 'تغییر ظاهر', 'ساخت صحنه‌های مختلف', 'تکنیک‌های انیمیشن‌سازی', 'پروژه نهایی'],
        'color': '#4ECDC4',
        'emoji': '🎬',
        'video_link': ''
    },
    {
        'id': 3,
        'title': 'بازی‌سازی با اسکرچ جونیور',
        'level': 'متوسط',
        'age': '۷ تا ۹ سال',
        'duration': '۸ جلسه',
        'price': '۱۹۹,۰۰۰ تومان',
        'description': 'ساخت بازی‌های تعاملی ساده با استفاده از بلوک‌های اسکرچ جونیور',
        'topics': ['مفهوم بازی‌سازی', 'ساخت بازی مسابقه', 'ساخت بازی جمع‌آوری', 'امتیازدهی', 'مراحل مختلف', 'پروژه نهایی'],
        'color': '#FFD93D',
        'emoji': '🎯',
        'video_link': ''
    }
]

# دوره‌های اسکرچ (۸ تا ۱۴ سال)
SCRATCH_COURSES = [
    {
        'id': 4,
        'title': 'مقدمات اسکرچ',
        'level': 'مبتدی',
        'age': '۸ تا ۱۰ سال',
        'duration': '۶ جلسه',
        'price': 'رایگان',
        'description': 'آشنایی با محیط اسکرچ، بلوک‌ها و ساخت اولین پروژه',
        'topics': ['معرفی محیط اسکرچ', 'بلوک‌های حرکتی', 'بلوک‌های ظاهری', 'صداها', 'اولین بازی ساده'],
        'color': '#667eea',
        'emoji': '🐱',
        'video_link': ''
    },
    {
        'id': 5,
        'title': 'ساخت بازی با اسکرچ',
        'level': 'متوسط',
        'age': '۹ تا ۱۲ سال',
        'duration': '۱۰ جلسه',
        'price': '۲۹۹,۰۰۰ تومان',
        'description': 'ساخت بازی‌های حرفه‌ای با اسکرچ شامل چندین مرحله و امتیاز',
        'topics': ['طراحی بازی', 'متغیرها و امتیاز', 'برخوردها', 'مراحل مختلف', 'ساخت بازی مار', 'پروژه نهایی'],
        'color': '#FF8A5C',
        'emoji': '🕹️',
        'video_link': ''
    },
    {
        'id': 6,
        'title': 'انیمیشن‌سازی با اسکرچ',
        'level': 'متوسط',
        'age': '۹ تا ۱۲ سال',
        'duration': '۸ جلسه',
        'price': '۲۴۹,۰۰۰ تومان',
        'description': 'ساخت انیمیشن‌های حرفه‌ای با اسکرچ و تکنیک‌های پیشرفته',
        'topics': ['اصول انیمیشن', 'حرکت‌های پیشرفته', 'تغییر لباس', 'ساخت کارتون', 'صداگذاری', 'پروژه نهایی'],
        'color': '#A66CFF',
        'emoji': '🎨',
        'video_link': ''
    },
    {
        'id': 7,
        'title': 'پروژه‌های خلاقانه اسکرچ',
        'level': 'پیشرفته',
        'age': '۱۰ تا ۱۴ سال',
        'duration': '۱۲ جلسه',
        'price': '۳۹۹,۰۰۰ تومان',
        'description': 'پروژه‌های بزرگ و خلاقانه با اسکرچ شامل بازی، انیمیشن و داستان',
        'topics': ['ساخت بازی چندمرحله‌ای', 'ساخت نقاشی دیجیتال', 'ساخت موزیک', 'ساخت داستان تعاملی', 'پروژه نهایی بزرگ'],
        'color': '#FF6B6B',
        'emoji': '🌟',
        'video_link': ''
    }
]

# ==========================================
# ۲. CSS یکپارچه
# ==========================================
CSS_STYLE = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Comic Sans MS', 'Vazir', 'Chalkboard SE', cursive;
    background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    color: #333;
    line-height: 1.6;
    padding-bottom: 60px;
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    border-bottom: 4px solid #FFD93D;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

nav h1 {
    font-size: 2rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

nav h1 span {
    display: inline-block;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

nav ul {
    display: flex;
    list-style: none;
    gap: 1.5rem;
    flex-wrap: wrap;
}

nav ul a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 1rem;
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
    transition: all 0.3s;
    background: rgba(255,255,255,0.1);
}

nav ul a:hover {
    background: rgba(255,255,255,0.3);
    transform: scale(1.05);
}

nav ul a.active {
    background: #FFD93D;
    color: #333;
}

.search-form {
    display: flex;
    gap: 0.5rem;
}

.search-form input {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 20px;
    font-size: 1rem;
    width: 200px;
    font-family: inherit;
}

.search-form input:focus {
    outline: 2px solid #FFD93D;
}

.search-form button {
    padding: 0.5rem 1.2rem;
    border: none;
    border-radius: 20px;
    background: #FFD93D;
    color: #333;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.3s;
}

.search-form button:hover {
    transform: scale(1.1);
    background: #FFC107;
}

.hero {
    text-align: center;
    padding: 3rem 0;
}

.hero h2 {
    font-size: 2.8rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: none;
}

.hero p {
    font-size: 1.3rem;
    margin-bottom: 2rem;
    color: #555;
}

.category-info {
    text-align: center;
    padding: 1.5rem;
    border-radius: 20px;
    margin: 1rem 0 2rem;
}

.category-info.jr {
    background: linear-gradient(135deg, #ffe6e6, #ffd4d4);
    border: 3px solid #FF6B6B;
}

.category-info.scratch {
    background: linear-gradient(135deg, #e6eeff, #d4e0ff);
    border: 3px solid #667eea;
}

.category-info h3 {
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
}

.category-info p {
    font-size: 1.1rem;
    color: #555;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.feature-box {
    background: white;
    padding: 1.8rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: all 0.3s;
    border: 3px solid transparent;
}

.feature-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.feature-box:nth-child(1) { border-color: #FF6B6B; }
.feature-box:nth-child(2) { border-color: #4ECDC4; }
.feature-box:nth-child(3) { border-color: #FFD93D; }

.feature-box h3 {
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
}

.course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.course-card {
    background: white;
    border-radius: 20px;
    padding: 1.8rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: all 0.3s;
    border-top: 6px solid #667eea;
    position: relative;
}

.course-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.course-card .emoji {
    font-size: 2.5rem;
    display: block;
    margin-bottom: 0.5rem;
}

.course-card h3 {
    color: #333;
    margin-bottom: 0.5rem;
    font-size: 1.2rem;
}

.course-card .level {
    font-weight: bold;
    margin: 0.3rem 0;
}

.course-card .age {
    color: #667eea;
    font-weight: bold;
}

.course-card .price {
    color: #FF6B6B;
    font-weight: bold;
    font-size: 1.1rem;
    margin: 0.5rem 0;
}

.course-card .description {
    color: #666;
    font-size: 0.9rem;
    margin: 0.5rem 0 1rem;
}

.course-card .category-tag {
    display: inline-block;
    padding: 0.2rem 0.8rem;
    border-radius: 15px;
    font-size: 0.7rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.tag-jr {
    background: #FF6B6B;
    color: white;
}

.tag-scratch {
    background: #667eea;
    color: white;
}

.btn-primary, .btn-secondary, .btn-success {
    display: inline-block;
    padding: 0.7rem 2rem;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s;
    margin: 0 0.3rem;
    cursor: pointer;
    border: none;
    font-size: 1rem;
    font-family: inherit;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.btn-primary:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
}

.btn-secondary {
    background: #FFD93D;
    color: #333;
    box-shadow: 0 4px 15px rgba(255, 217, 61, 0.4);
}

.btn-secondary:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 6px 25px rgba(255, 217, 61, 0.6);
}

.btn-success {
    background: #4ECDC4;
    color: white;
    box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
}

.btn-success:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 6px 25px rgba(78, 205, 196, 0.6);
}

.btn-small {
    padding: 0.4rem 1.2rem;
    font-size: 0.85rem;
}

.btn-disabled {
    background: #ccc;
    color: #888;
    cursor: not-allowed;
    box-shadow: none;
}

.btn-disabled:hover {
    transform: none;
    box-shadow: none;
}

.course-detail {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.course-detail .emoji-big {
    font-size: 4rem;
    display: block;
    text-align: center;
    margin-bottom: 1rem;
}

.course-detail h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 1.5rem;
}

.detail-meta {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    justify-content: center;
    margin: 1.5rem 0;
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 15px;
}

.detail-meta span {
    background: white;
    padding: 0.5rem 1.5rem;
    border-radius: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.detail-description, .detail-topics {
    margin: 2rem 0;
}

.detail-description h3, .detail-topics h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: #667eea;
}

.detail-topics ul {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 0.8rem;
}

.detail-topics li {
    padding: 0.8rem 1.2rem;
    background: #f8f9fa;
    border-radius: 15px;
    border-right: 4px solid #667eea;
    font-weight: 500;
}

.detail-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 2rem;
}

.register-page {
    background: white;
    padding: 3rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}

.register-page .success-icon {
    font-size: 5rem;
    display: block;
    margin-bottom: 1rem;
}

.register-page h2 {
    color: #4ECDC4;
    font-size: 2.2rem;
    margin-bottom: 1rem;
}

.register-page .message {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 1.5rem;
}

.register-page .course-name {
    font-size: 1.5rem;
    color: #667eea;
    font-weight: bold;
    margin: 1rem 0;
}

.register-page .video-section {
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
}

.register-page .video-section h3 {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 0.5rem;
}

.register-page .video-section .video-link {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.8rem 2rem;
    background: #FF6B6B;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s;
}

.register-page .video-section .video-link:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 20px rgba(255, 107, 107, 0.4);
}

.register-page .video-section .no-video {
    color: #999;
    font-size: 1.1rem;
    padding: 1rem;
}

footer {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    padding: 1.5rem 0;
    margin-top: 3rem;
    border-top: 4px solid #FFD93D;
}

.text-center {
    text-align: center;
    margin: 2rem 0;
}

.search-result {
    color: #764ba2;
    font-weight: bold;
    font-size: 1.1rem;
    margin: 1rem 0;
    padding: 1rem;
    background: #f0edff;
    border-radius: 15px;
    text-align: center;
}

.no-results {
    text-align: center;
    color: #666;
    font-size: 1.2rem;
    padding: 3rem 0;
}

h2 {
    margin: 2rem 0 1rem;
    color: #333;
    text-align: center;
}

@media (max-width: 768px) {
    nav {
        flex-direction: column;
        text-align: center;
    }
    
    nav ul {
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .search-form {
        width: 100%;
        justify-content: center;
    }
    
    .search-form input {
        width: 150px;
    }
    
    .hero h2 {
        font-size: 2rem;
    }
    
    .detail-meta {
        flex-direction: column;
        align-items: center;
    }
}
"""

# ==========================================
# ۳. توابع تولید صفحات
# ==========================================

def render_page(content, title="اسکرچ و اسکرچ جونیور", active_page=""):
    """تابع اصلی که همه صفحات رو با همون قالب میسازه"""
    
    active_home = 'active' if active_page == 'home' else ''
    active_jr = 'active' if active_page == 'jr' else ''
    active_scratch = 'active' if active_page == 'scratch' else ''
    active_about = 'active' if active_page == 'about' else ''
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {CSS_STYLE}
    </style>
</head>
<body>
    <header>
        <nav class="container">
            <h1>
                <span>🐱</span> کدآکادمی کودکان <span>✨</span>
            </h1>
            <ul>
                <li><a href="index.html" class="{active_home}">🏠 خانه</a></li>
                <li><a href="scratchjr.html" class="{active_jr}">🎮 اسکرچ جونیور</a></li>
                <li><a href="scratch.html" class="{active_scratch}">🐱 اسکرچ</a></li>
                <li><a href="about.html" class="{active_about}">❓ درباره ما</a></li>
            </ul>
            <form action="search.html" method="get" class="search-form">
                <input type="text" name="q" placeholder="🔍 جستجو..." required>
                <button type="submit">🔍</button>
            </form>
        </nav>
    </header>

    <main class="container">
        {content}
    </main>

    <footer>
        <div class="container">
            <p>🐱 © {COPYRIGHT_YEAR} کدآکادمی کودکان - آموزش اسکرچ و اسکرچ جونیور ❤️</p>
            <p style="font-size: 0.9rem; opacity: 0.8; margin-top: 0.5rem;">
                🎮 اسکرچ جونیور (۵-۸ سال) | 🐱 اسکرچ (۸-۱۴ سال)
            </p>
        </div>
    </footer>
</body>
</html>"""


def generate_index():
    """صفحه اصلی"""
    preview_jr = SCRATCHJR_COURSES[:2]
    preview_scratch = SCRATCH_COURSES[:2]
    
    # ساخت کارت‌های اسکرچ جونیور
    jr_cards = ""
    for course in preview_jr:
        jr_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-jr">🎮 اسکرچ جونیور</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <a href="course_{course['id']}.html" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    # ساخت کارت‌های اسکرچ
    scratch_cards = ""
    for course in preview_scratch:
        scratch_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-scratch">🐱 اسکرچ</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <a href="course_{course['id']}.html" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <section class="hero">
        <h2>🌟 به دنیای برنامه‌نویسی کودکان خوش آمدید! 🌟</h2>
        <p>🐱 اسکرچ و اسکرچ جونیور - یادگیری با بازی و خلاقیت</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="scratchjr.html" class="btn-primary">🎮 اسکرچ جونیور (۵-۸ سال)</a>
            <a href="scratch.html" class="btn-primary">🐱 اسکرچ (۸-۱۴ سال)</a>
        </div>
    </section>

    <section class="features">
        <div class="feature-box">
            <h3>🎮 یادگیری با بازی</h3>
            <p>برنامه‌نویسی به شکل بازی و سرگرمی</p>
        </div>
        <div class="feature-box">
            <h3>🎨 خلاقیت</h3>
            <p>ساخت انیمیشن، بازی و داستان</p>
        </div>
        <div class="feature-box">
            <h3>👶 مناسب کودکان</h3>
            <p>از ۵ تا ۱۴ سال با سطح‌های مختلف</p>
        </div>
    </section>

    <h2>🎮 دوره‌های اسکرچ جونیور</h2>
    <div class="course-grid">{jr_cards}</div>
    <div class="text-center">
        <a href="scratchjr.html" class="btn-secondary">📚 همه دوره‌های اسکرچ جونیور</a>
    </div>

    <h2>🐱 دوره‌های اسکرچ</h2>
    <div class="course-grid">{scratch_cards}</div>
    <div class="text-center">
        <a href="scratch.html" class="btn-secondary">📚 همه دوره‌های اسکرچ</a>
    </div>
    """
    
    return render_page(content, "خانه | اسکرچ و اسکرچ جونیور", "home")


def generate_scratchjr():
    """صفحه اسکرچ جونیور"""
    course_cards = ""
    for course in SCRATCHJR_COURSES:
        course_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-jr">🎮 اسکرچ جونیور</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <p class="description">{course['description'][:60]}...</p>
            <a href="course_{course['id']}.html" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <div class="category-info jr">
        <h3>🎮 اسکرچ جونیور</h3>
        <p>مناسب برای کودکان ۵ تا ۸ سال | آموزش برنامه‌نویسی با بلوک‌های تصویری</p>
    </div>
    <div class="course-grid">{course_cards}</div>
    """
    
    return render_page(content, "اسکرچ جونیور | کدآکادمی کودکان", "jr")


def generate_scratch():
    """صفحه اسکرچ"""
    course_cards = ""
    for course in SCRATCH_COURSES:
        course_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-scratch">🐱 اسکرچ</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <p class="description">{course['description'][:60]}...</p>
            <a href="course_{course['id']}.html" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <div class="category-info scratch">
        <h3>🐱 اسکرچ</h3>
        <p>مناسب برای کودکان ۸ تا ۱۴ سال | برنامه‌نویسی خلاقانه با اسکرچ</p>
    </div>
    <div class="course-grid">{course_cards}</div>
    """
    
    return render_page(content, "اسکرچ | کدآکادمی کودکان", "scratch")


def generate_course_detail(course):
    """صفحه جزئیات دوره"""
    topics_list = ""
    for topic in course['topics']:
        topics_list += f"<li>✅ {topic}</li>"
    
    category_name = "اسکرچ جونیور" if course['id'] <= 3 else "اسکرچ"
    video_link = course.get('video_link', '')
    
    if video_link:
        watch_button = f'<a href="{video_link}" target="_blank" class="btn-primary">🎥 جلسه اول را ببین</a>'
    else:
        watch_button = '<span class="btn-primary btn-disabled">🎥 جلسه اول به زودی</span>'
    
    content = f"""
    <div class="course-detail">
        <span class="emoji-big">{course['emoji']}</span>
        <h2>{course['title']}</h2>
        <div style="text-align: center; margin-bottom: 1rem;">
            <span class="category-tag {'tag-jr' if course['id'] <= 3 else 'tag-scratch'}">🎮 {category_name}</span>
        </div>
        <div class="detail-meta" style="border: 3px solid {course['color']};">
            <span>📊 سطح: {course['level']}</span>
            <span>👶 سن: {course['age']}</span>
            <span>⏱️ مدت: {course['duration']}</span>
            <span>💰 {course['price']}</span>
        </div>
        <div class="detail-description">
            <h3>📖 توضیحات دوره</h3>
            <p style="font-size: 1.1rem;">{course['description']}</p>
        </div>
        <div class="detail-topics">
            <h3>📌 سرفصل‌ها</h3>
            <ul>{topics_list}</ul>
        </div>
        <div class="detail-buttons">
            {watch_button}
            <a href="register_{course['id']}.html" class="btn-success">📝 ثبت‌نام در دوره</a>
            <a href="index.html" class="btn-secondary">🏠 بازگشت به خانه</a>
        </div>
    </div>
    """
    
    return render_page(content, f"{course['title']} | کدآکادمی کودکان")


def generate_register(course):
    """صفحه ثبت‌نام"""
    video_link = course.get('video_link', '')
    
    if video_link:
        video_section = f"""
        <div class="video-section">
            <h3>🎬 جلسه اول</h3>
            <p style="color: #666; margin-bottom: 1rem;">برای مشاهده جلسه اول روی دکمه زیر کلیک کنید:</p>
            <a href="{video_link}" target="_blank" class="video-link">▶️ مشاهده جلسه اول</a>
        </div>
        """
    else:
        video_section = f"""
        <div class="video-section">
            <h3>🎬 جلسه اول</h3>
            <p class="no-video">⏳ این دوره به زودی تکمیل می‌شود...</p>
            <p style="color: #999; font-size: 0.9rem;">لطفاً چند روز دیگر مراجعه کنید</p>
        </div>
        """
    
    content = f"""
    <div class="register-page">
        <span class="success-icon">🎉</span>
        <h2>ثبت‌نام شما با موفقیت انجام شد!</h2>
        <p class="message">به دوره زیر خوش آمدید:</p>
        <p class="course-name">{course['emoji']} {course['title']}</p>
        
        {video_section}
        
        <div style="margin-top: 2rem;">
            <a href="index.html" class="btn-secondary">🏠 بازگشت به خانه</a>
            <a href="course_{course['id']}.html" class="btn-primary">📖 بازگشت به صفحه دوره</a>
        </div>
    </div>
    """
    
    return render_page(content, f"ثبت‌نام | {course['title']}")


def generate_about():
    """صفحه درباره ما"""
    content = """
    <div style="background: white; padding: 2rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
        <h2>❓ درباره کدآکادمی کودکان</h2>
        <div style="font-size: 1.1rem; line-height: 2;">
            <p>🐱 <strong>کدآکادمی کودکان</strong> یک سایت آموزش برنامه‌نویسی برای کودکان است.</p>
            <p>🎯 هدف ما آموزش برنامه‌نویسی به کودکان ۵ تا ۱۴ سال با روشی ساده و سرگرم‌کننده است.</p>
            <p>🎮 <strong>اسکرچ جونیور:</strong> مناسب برای کودکان ۵ تا ۸ سال</p>
            <p>🐱 <strong>اسکرچ:</strong> مناسب برای کودکان ۸ تا ۱۴ سال</p>
            <br>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
                <span style="background: #f8f9fa; padding: 0.5rem 1.5rem; border-radius: 20px;">🎮 ۳+ دوره اسکرچ جونیور</span>
                <span style="background: #f8f9fa; padding: 0.5rem 1.5rem; border-radius: 20px;">🐱 ۴+ دوره اسکرچ</span>
                <span style="background: #f8f9fa; padding: 0.5rem 1.5rem; border-radius: 20px;">👶 ۵ تا ۱۴ سال</span>
            </div>
        </div>
        <div class="text-center" style="margin-top: 2rem;">
            <a href="index.html" class="btn-primary">🏠 بازگشت به خانه</a>
        </div>
    </div>
    """
    return render_page(content, "درباره ما | کدآکادمی کودکان", "about")


def generate_search():
    """صفحه جستجو (استاتیک - برای نمایش)"""
    content = """
    <div style="background: white; padding: 2rem; border-radius: 20px; margin: 2rem 0; text-align: center;">
        <h2>🔍 جستجوی دوره‌ها</h2>
        <p style="font-size: 1.1rem; color: #666; margin: 1rem 0;">
            برای جستجو، از کادر جستجو در بالای صفحه استفاده کنید.
        </p>
        <div style="display: flex; gap: 0.5rem; justify-content: center; max-width: 500px; margin: 0 auto;">
            <input type="text" placeholder="نام دوره را وارد کنید..." style="flex:1; padding: 0.7rem 1rem; border: 2px solid #ddd; border-radius: 20px; font-size: 1rem; font-family: inherit;">
            <button style="padding: 0.7rem 1.5rem; background: #667eea; color: white; border: none; border-radius: 20px; font-size: 1rem; cursor: pointer;">🔍</button>
        </div>
        <div style="margin-top: 2rem;">
            <a href="index.html" class="btn-secondary">🏠 بازگشت به خانه</a>
        </div>
    </div>
    """
    return render_page(content, "جستجو | کدآکادمی کودکان")


# ==========================================
# ۴. تابع اصلی
# ==========================================
def main():
    print("🐱 در حال تولید سایت آموزش اسکرچ و اسکرچ جونیور...")
    print("=" * 55)
    
    # ۱. صفحه اصلی
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_index())
    print("✅ index.html")
    
    # ۲. اسکرچ جونیور
    with open("scratchjr.html", "w", encoding="utf-8") as f:
        f.write(generate_scratchjr())
    print("✅ scratchjr.html")
    
    # ۳. اسکرچ
    with open("scratch.html", "w", encoding="utf-8") as f:
        f.write(generate_scratch())
    print("✅ scratch.html")
    
    # ۴. درباره ما
    with open("about.html", "w", encoding="utf-8") as f:
        f.write(generate_about())
    print("✅ about.html")
    
    # ۵. جستجو
    with open("search.html", "w", encoding="utf-8") as f:
        f.write(generate_search())
    print("✅ search.html")
    
    # ۶. صفحات جزئیات و ثبت‌نام برای هر دوره
    all_courses = SCRATCHJR_COURSES + SCRATCH_COURSES
    for course in all_courses:
        # صفحه جزئیات
        with open(f"course_{course['id']}.html", "w", encoding="utf-8") as f:
            f.write(generate_course_detail(course))
        print(f"✅ course_{course['id']}.html ({course['title']})")
        
        # صفحه ثبت‌نام
        with open(f"register_{course['id']}.html", "w", encoding="utf-8") as f:
            f.write(generate_register(course))
        print(f"✅ register_{course['id']}.html ({course['title']})")
    
    print("=" * 55)
    print(f"📍 مسیر فایل‌ها: {os.path.abspath('.')}")
    print("🌐 حالا می‌توانید فایل‌ها را در مرورگر باز کنید.")
    print("📂 فایل index.html را باز کنید تا سایت را ببینید.")


if __name__ == "__main__":
    main()