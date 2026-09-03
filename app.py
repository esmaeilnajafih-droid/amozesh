from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# ========== دیتای دوره‌های اسکرچ جونیور (۵ تا ۸ سال) ==========
scratchjr_courses = [
    {
        'id': 1,
        'category': 'scratchjr',
        'title': 'آشنایی با اسکرچ جونیور',
        'level': 'مبتدی',
        'age': '۵ تا ۷ سال',
        'duration': '۴ جلسه',
        'price': 'رایگان',
        'description': 'آشنایی با محیط اسکرچ جونیور، شخصیت‌ها و ابزارهای اولیه',
        'topics': ['معرفی محیط برنامه', 'آشنایی با شخصیت‌ها', 'حرکت دادن شخصیت', 'اضافه کردن صدا', 'ذخیره کردن پروژه'],
        'color': '#FF6B6B',
        'emoji': '🎮',
        'video_link': 'https://www.aparat.com/v/bewg9bw'  # لینک اختصاصی برای این دوره
    },
    {
        'id': 2,
        'category': 'scratchjr',
        'title': 'ساخت انیمیشن ساده',
        'level': 'مبتدی',
        'age': '۶ تا ۸ سال',
        'duration': '۶ جلسه',
        'price': 'رایگان',
        'description': 'یادگیری ساخت انیمیشن‌های ساده با شخصیت‌های اسکرچ جونیور',
        'topics': ['حرکت‌های مختلف', 'تغییر ظاهر', 'ساخت صحنه‌های مختلف', 'تکنیک‌های انیمیشن‌سازی', 'پروژه نهایی'],
        'color': '#4ECDC4',
        'emoji': '🎬',
        'video_link': ''  # لینک خالی - کاربر پیام می‌بیند
    },
    {
        'id': 3,
        'category': 'scratchjr',
        'title': 'بازی‌سازی با اسکرچ جونیور',
        'level': 'متوسط',
        'age': '۷ تا ۹ سال',
        'duration': '۸ جلسه',
        'price': '۱۹۹,۰۰۰ تومان',
        'description': 'ساخت بازی‌های تعاملی ساده با استفاده از بلوک‌های اسکرچ جونیور',
        'topics': ['مفهوم بازی‌سازی', 'ساخت بازی مسابقه', 'ساخت بازی جمع‌آوری', 'امتیازدهی', 'مراحل مختلف', 'پروژه نهایی'],
        'color': '#FFD93D',
        'emoji': '🎯',
        'video_link': ''  # لینک خالی - کاربر پیام می‌بیند
    }
]

# ========== دیتای دوره‌های اسکرچ (۸ تا ۱۴ سال) ==========
scratch_courses = [
    {
        'id': 4,
        'category': 'scratch',
        'title': 'مقدمات اسکرچ',
        'level': 'مبتدی',
        'age': '۸ تا ۱۰ سال',
        'duration': '۶ جلسه',
        'price': 'رایگان',
        'description': 'آشنایی با محیط اسکرچ، بلوک‌ها و ساخت اولین پروژه',
        'topics': ['معرفی محیط اسکرچ', 'بلوک‌های حرکتی', 'بلوک‌های ظاهری', 'صداها', 'اولین بازی ساده'],
        'color': '#667eea',
        'emoji': '🐱',
        'video_link': ''  # لینک خالی
    },
    {
        'id': 5,
        'category': 'scratch',
        'title': 'ساخت بازی با اسکرچ',
        'level': 'متوسط',
        'age': '۹ تا ۱۲ سال',
        'duration': '۱۰ جلسه',
        'price': '۲۹۹,۰۰۰ تومان',
        'description': 'ساخت بازی‌های حرفه‌ای با اسکرچ شامل چندین مرحله و امتیاز',
        'topics': ['طراحی بازی', 'متغیرها و امتیاز', 'برخوردها', 'مراحل مختلف', 'ساخت بازی مار', 'پروژه نهایی'],
        'color': '#FF8A5C',
        'emoji': '🕹️',
        'video_link': ''  # لینک خالی
    },
    {
        'id': 6,
        'category': 'scratch',
        'title': 'انیمیشن‌سازی با اسکرچ',
        'level': 'متوسط',
        'age': '۹ تا ۱۲ سال',
        'duration': '۸ جلسه',
        'price': '۲۴۹,۰۰۰ تومان',
        'description': 'ساخت انیمیشن‌های حرفه‌ای با اسکرچ و تکنیک‌های پیشرفته',
        'topics': ['اصول انیمیشن', 'حرکت‌های پیشرفته', 'تغییر لباس', 'ساخت کارتون', 'صداگذاری', 'پروژه نهایی'],
        'color': '#A66CFF',
        'emoji': '🎨',
        'video_link': ''  # لینک خالی
    },
    {
        'id': 7,
        'category': 'scratch',
        'title': 'پروژه‌های خلاقانه اسکرچ',
        'level': 'پیشرفته',
        'age': '۱۰ تا ۱۴ سال',
        'duration': '۱۲ جلسه',
        'price': '۳۹۹,۰۰۰ تومان',
        'description': 'پروژه‌های بزرگ و خلاقانه با اسکرچ شامل بازی، انیمیشن و داستان',
        'topics': ['ساخت بازی چندمرحله‌ای', 'ساخت نقاشی دیجیتال', 'ساخت موزیک', 'ساخت داستان تعاملی', 'پروژه نهایی بزرگ'],
        'color': '#FF6B6B',
        'emoji': '🌟',
        'video_link': ''  # لینک خالی
    }
]

# ========== استایل CSS ==========
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

/* Header */
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

/* Hero */
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

/* Category Info */
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

/* Features */
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

/* Course Grid */
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

/* Course Detail */
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

/* Buttons Container */
.detail-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 2rem;
}

/* Register Page */
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

/* Footer */
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

/* Responsive */
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

# ========== تابع کمکی برای ساخت صفحه ==========
def render_page(content, title="اسکرچ و اسکرچ جونیور"):
    return f"""
<!DOCTYPE html>
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
                <li><a href="/" class="{'active' if request.path == '/' else ''}">🏠 خانه</a></li>
                <li><a href="/scratchjr" class="{'active' if '/scratchjr' in request.path else ''}">🎮 اسکرچ جونیور</a></li>
                <li><a href="/scratch" class="{'active' if '/scratch' in request.path else ''}">🐱 اسکرچ</a></li>
                <li><a href="/about">❓ درباره ما</a></li>
            </ul>
            <form action="/search" method="get" class="search-form">
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
            <p>🐱 © ۲۰۲۶ کدآکادمی کودکان - آموزش اسکرچ و اسکرچ جونیور ❤️</p>
            <p style="font-size: 0.9rem; opacity: 0.8; margin-top: 0.5rem;">
                🎮 اسکرچ جونیور (۵-۸ سال) | 🐱 اسکرچ (۸-۱۴ سال)
            </p>
        </div>
    </footer>
</body>
</html>
    """

# ========== صفحه اصلی ==========
@app.route('/')
def index():
    # نمایش ۲ دوره از هر دسته
    preview_jr = scratchjr_courses[:2]
    preview_scratch = scratch_courses[:2]
    
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
            <a href="/course/{course['id']}" class="btn-secondary btn-small">👀 مشاهده</a>
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
            <a href="/course/{course['id']}" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <section class="hero">
        <h2>🌟 به دنیای برنامه‌نویسی کودکان خوش آمدید! 🌟</h2>
        <p>🐱 اسکرچ و اسکرچ جونیور - یادگیری با بازی و خلاقیت</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="/scratchjr" class="btn-primary">🎮 اسکرچ جونیور (۵-۸ سال)</a>
            <a href="/scratch" class="btn-primary">🐱 اسکرچ (۸-۱۴ سال)</a>
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
        <a href="/scratchjr" class="btn-secondary">📚 همه دوره‌های اسکرچ جونیور</a>
    </div>

    <h2>🐱 دوره‌های اسکرچ</h2>
    <div class="course-grid">{scratch_cards}</div>
    <div class="text-center">
        <a href="/scratch" class="btn-secondary">📚 همه دوره‌های اسکرچ</a>
    </div>
    """
    
    return render_page(content, "خانه | اسکرچ و اسکرچ جونیور")

# ========== دوره‌های اسکرچ جونیور ==========
@app.route('/scratchjr')
def scratchjr_list():
    course_cards = ""
    for course in scratchjr_courses:
        course_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-jr">🎮 اسکرچ جونیور</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <p class="description">{course['description'][:60]}...</p>
            <a href="/course/{course['id']}" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <div class="category-info jr">
        <h3>🎮 اسکرچ جونیور</h3>
        <p>مناسب برای کودکان ۵ تا ۸ سال | آموزش برنامه‌نویسی با بلوک‌های تصویری</p>
    </div>
    <div class="course-grid">{course_cards}</div>
    """
    
    return render_page(content, "اسکرچ جونیور | کدآکادمی کودکان")

# ========== دوره‌های اسکرچ ==========
@app.route('/scratch')
def scratch_list():
    course_cards = ""
    for course in scratch_courses:
        course_cards += f"""
        <div class="course-card" style="border-top-color: {course['color']};">
            <span class="emoji">{course['emoji']}</span>
            <span class="category-tag tag-scratch">🐱 اسکرچ</span>
            <h3>{course['title']}</h3>
            <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
            <p class="age">👶 {course['age']}</p>
            <p class="price">{course['price']}</p>
            <p class="description">{course['description'][:60]}...</p>
            <a href="/course/{course['id']}" class="btn-secondary btn-small">👀 مشاهده</a>
        </div>
        """
    
    content = f"""
    <div class="category-info scratch">
        <h3>🐱 اسکرچ</h3>
        <p>مناسب برای کودکان ۸ تا ۱۴ سال | برنامه‌نویسی خلاقانه با اسکرچ</p>
    </div>
    <div class="course-grid">{course_cards}</div>
    """
    
    return render_page(content, "اسکرچ | کدآکادمی کودکان")

# ========== جستجو ==========
@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect('/')
    
    # جستجو در هر دو دسته
    results = []
    for course in scratchjr_courses + scratch_courses:
        if query.lower() in course['title'].lower() or query.lower() in course['description'].lower():
            results.append(course)
    
    if results:
        course_cards = ""
        for course in results:
            tag_class = "tag-jr" if course['category'] == 'scratchjr' else "tag-scratch"
            tag_text = "🎮 اسکرچ جونیور" if course['category'] == 'scratchjr' else "🐱 اسکرچ"
            course_cards += f"""
            <div class="course-card" style="border-top-color: {course['color']};">
                <span class="emoji">{course['emoji']}</span>
                <span class="category-tag {tag_class}">{tag_text}</span>
                <h3>{course['title']}</h3>
                <p class="level" style="color: {course['color']};">سطح: {course['level']}</p>
                <p class="age">👶 {course['age']}</p>
                <p class="price">{course['price']}</p>
                <a href="/course/{course['id']}" class="btn-secondary btn-small">👀 مشاهده</a>
            </div>
            """
        
        content = f"""
        <p class="search-result">🎯 نتایج جستجو برای: "{query}" ({len(results)} مورد)</p>
        <div class="course-grid">{course_cards}</div>
        """
    else:
        content = f"""
        <p class="no-results">😅 هیچ دوره‌ای برای "{query}" پیدا نشد!</p>
        <div class="text-center">
            <a href="/" class="btn-secondary">🏠 بازگشت به خانه</a>
        </div>
        """
    
    return render_page(content, "جستجو | کدآکادمی کودکان")

# ========== صفحه ثبت‌نام ==========
@app.route('/register/<int:course_id>')
def register(course_id):
    # پیدا کردن دوره
    all_courses = scratchjr_courses + scratch_courses
    course = None
    for c in all_courses:
        if c['id'] == course_id:
            course = c
            break
    
    if not course:
        content = """
        <div class="text-center" style="padding: 4rem 0;">
            <h2>😅 دوره پیدا نشد!</h2>
            <a href="/" class="btn-primary">🏠 بازگشت به خانه</a>
        </div>
        """
        return render_page(content, "خطا | کدآکادمی کودکان"), 404
    
    # دریافت لینک ویدیو
    video_link = course.get('video_link', '')
    
    # اگر لینک ویدیو وجود داشت، دکمه نمایش داده میشه، در غیر این صورت پیام "به زودی"
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
            <a href="/" class="btn-secondary">🏠 بازگشت به خانه</a>
            <a href="/course/{course['id']}" class="btn-primary">📖 بازگشت به صفحه دوره</a>
        </div>
    </div>
    """
    
    return render_page(content, f"ثبت‌نام | {course['title']}")

# ========== جزئیات دوره ==========
@app.route('/course/<int:course_id>')
def course_detail(course_id):
    # پیدا کردن دوره در هر دو دسته
    all_courses = scratchjr_courses + scratch_courses
    course = None
    for c in all_courses:
        if c['id'] == course_id:
            course = c
            break
    
    if not course:
        content = """
        <div class="text-center" style="padding: 4rem 0;">
            <h2>😅 دوره پیدا نشد!</h2>
            <a href="/" class="btn-primary">🏠 بازگشت به خانه</a>
        </div>
        """
        return render_page(content, "خطا | کدآکادمی کودکان"), 404
    
    # ساخت لیست سرفصل‌ها
    topics_list = ""
    for topic in course['topics']:
        topics_list += f"<li>✅ {topic}</li>"
    
    category_name = "اسکرچ جونیور" if course['category'] == 'scratchjr' else "اسکرچ"
    
    # دریافت لینک ویدیو
    video_link = course.get('video_link', '')
    
    # اگر لینک ویدیو وجود داشت، دکمه فعال نمایش داده میشه، در غیر این صورت دکمه غیرفعال
    if video_link:
        watch_button = f'<a href="{video_link}" target="_blank" class="btn-primary">🎥 جلسه اول را ببین</a>'
    else:
        watch_button = '<span class="btn-primary btn-disabled">🎥 جلسه اول به زودی</span>'
    
    content = f"""
    <div class="course-detail">
        <span class="emoji-big">{course['emoji']}</span>
        <h2>{course['title']}</h2>
        <div style="text-align: center; margin-bottom: 1rem;">
            <span class="category-tag {'tag-jr' if course['category'] == 'scratchjr' else 'tag-scratch'}">🎮 {category_name}</span>
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
            <a href="/register/{course['id']}" class="btn-success">📝 ثبت‌نام در دوره</a>
            <a href="/" class="btn-secondary">🏠 بازگشت به خانه</a>
        </div>
    </div>
    """
    
    return render_page(content, f"{course['title']} | کدآکادمی کودکان")

# ========== درباره ما ==========
@app.route('/about')
def about():
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
            <a href="/" class="btn-primary">🏠 بازگشت به خانه</a>
        </div>
    </div>
    """
    return render_page(content, "درباره ما | کدآکادمی کودکان")

# ========== اجرا ==========
if __name__ == '__main__':
    print("🐱 کدآکادمی کودکان - آموزش اسکرچ و اسکرچ جونیور")
    print("=" * 55)
    print("📍 آدرس: http://127.0.0.1:5000")
    print("🎮 اسکرچ جونیور: ۵ تا ۸ سال")
    print("🐱 اسکرچ: ۸ تا ۱۴ سال")
    print("✨ از یادگیری لذت ببر!")
    print("=" * 55)
    app.run(debug=True, host='0.0.0.0', port=5000)