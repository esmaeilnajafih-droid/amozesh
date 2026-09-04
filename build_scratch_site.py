# build_scratch_site.py
# تولیدکننده سایت آموزش اسکرچ و اسکرچ جونیور
# با پنل مدیریت مخفی (فقط با آدرس مستقیم قابل دسترس)

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

/* ===== صفحه ثبت‌نام با کد ===== */
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

/* ===== بخش کد ===== */
.code-section {
    background: #f0f4ff;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    border: 2px dashed #667eea;
}

.code-section .code-title {
    font-size: 1.3rem;
    color: #333;
    margin-bottom: 0.5rem;
}

.code-section .code-desc {
    color: #666;
    margin-bottom: 1.5rem;
}

.code-section .code-input-group {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.code-section .code-input-group input {
    padding: 0.8rem 1.5rem;
    border: 2px solid #ddd;
    border-radius: 30px;
    font-size: 1.1rem;
    width: 250px;
    text-align: center;
    font-family: inherit;
    transition: border-color 0.3s;
    direction: ltr;
}

.code-section .code-input-group input:focus {
    border-color: #667eea;
    outline: none;
}

.code-section .code-input-group .btn-verify {
    padding: 0.8rem 2.5rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 30px;
    font-size: 1.1rem;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
    font-family: inherit;
}

.code-section .code-input-group .btn-verify:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
}

.code-section .code-error {
    color: #FF6B6B;
    font-weight: bold;
    margin-top: 1rem;
    display: none;
}

.code-section .code-success {
    color: #4ECDC4;
    font-weight: bold;
    margin-top: 1rem;
    display: none;
}

.code-section .no-code {
    margin-top: 1.5rem;
    padding: 1rem;
    background: #fff3cd;
    border-radius: 12px;
    border-right: 4px solid #FFD93D;
}

.code-section .no-code p {
    color: #856404;
    margin: 0.3rem 0;
}

.code-section .no-code .ble-link {
    display: inline-block;
    margin-top: 0.5rem;
    padding: 0.5rem 1.5rem;
    background: #4ECDC4;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s;
}

.code-section .no-code .ble-link:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
}

.code-section .no-code .ble-id {
    background: #e8e8e8;
    padding: 0.2rem 0.8rem;
    border-radius: 10px;
    font-weight: bold;
    color: #333;
    font-size: 1.2rem;
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

/* ===== پنل مدیریت (مخفی) ===== */
.admin-panel {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.admin-panel h2 {
    color: #333;
    margin-bottom: 1rem;
}

.admin-panel .admin-subtitle {
    color: #666;
    margin-bottom: 1rem;
}

.admin-panel .admin-warning {
    color: #999;
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
    padding: 0.5rem 1rem;
    background: #fff3cd;
    border-radius: 8px;
    border-right: 4px solid #FFD93D;
}

.admin-panel .add-section {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
}

.admin-panel .add-section h3 {
    margin-bottom: 1rem;
    color: #333;
}

.admin-panel .add-section .add-group {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    align-items: center;
}

.admin-panel .add-section .add-group input {
    padding: 0.7rem 1rem;
    border: 2px solid #ddd;
    border-radius: 12px;
    font-size: 1rem;
    font-family: inherit;
    width: 200px;
    direction: ltr;
}

.admin-panel .add-section .add-group input:focus {
    border-color: #667eea;
    outline: none;
}

.admin-panel .add-section .add-group .btn-add {
    padding: 0.7rem 2rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
    font-family: inherit;
}

.admin-panel .add-section .add-group .btn-add:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.admin-panel .add-section .add-message {
    margin-top: 0.5rem;
    display: none;
}

.admin-panel .add-section .add-message.success {
    color: #4ECDC4;
    display: block;
}

.admin-panel .add-section .add-message.error {
    color: #FF6B6B;
    display: block;
}

.admin-panel .codes-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.admin-panel .codes-table th {
    background: #667eea;
    color: white;
    padding: 12px;
    text-align: center;
}

.admin-panel .codes-table td {
    padding: 10px;
    text-align: center;
    border-bottom: 1px solid #eee;
}

.admin-panel .codes-table tr:hover {
    background: #f8f9fa;
}

.admin-panel .codes-table .code-box {
    font-family: monospace;
    font-size: 1.2rem;
    font-weight: bold;
    color: #333;
}

.admin-panel .codes-table .status-active {
    color: #4ECDC4;
    font-weight: bold;
}

.admin-panel .codes-table .btn-remove {
    padding: 0.3rem 1rem;
    background: #FF6B6B;
    color: white;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
    font-family: inherit;
}

.admin-panel .codes-table .btn-remove:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
}

.admin-panel .admin-buttons {
    margin-top: 2rem;
    text-align: center;
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.admin-panel .admin-buttons .btn-reset {
    padding: 0.7rem 2rem;
    background: #FFD93D;
    color: #333;
    border: none;
    border-radius: 30px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
    font-family: inherit;
    text-decoration: none;
}

.admin-panel .admin-buttons .btn-reset:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(255, 217, 61, 0.4);
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
    
    .code-section .code-input-group input {
        width: 100%;
    }
    
    .admin-panel .add-section .add-group {
        flex-direction: column;
        align-items: stretch;
    }
    
    .admin-panel .add-section .add-group input {
        width: 100%;
    }
    
    .admin-panel .codes-table {
        font-size: 0.9rem;
    }
    
    .admin-panel .codes-table th,
    .admin-panel .codes-table td {
        padding: 8px;
    }
}
"""

# ==========================================
# ۳. توابع تولید صفحات
# ==========================================

def render_page(content, title="اسکرچ و اسکرچ جونیور", active_page=""):
    """تابع اصلی که همه صفحات رو با همون قالب میسازه - بدون لینک مدیریت"""
    
    active_home = 'active' if active_page == 'home' else ''
    active_jr = 'active' if active_page == 'jr' else ''
    active_scratch = 'active' if active_page == 'scratch' else ''
    active_about = 'active' if active_page == 'about' else ''
    # active_admin حذف شد - کاربران مدیریت رو نمی‌بینن
    
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
                <!-- لینک مدیریت مخفی شده - کاربران نمی‌بینن -->
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
    """صفحه ثبت‌نام با کد (بدون نمایش کدها)"""
    
    # فقط برای دوره اول (آشنایی با اسکرچ جونیور) فرم کد نمایش داده میشه
    if course['id'] == 1:
        return generate_register_with_code(course)
    else:
        return generate_register_simple(course)


def generate_register_with_code(course):
    """صفحه ثبت‌نام با فرم ورود کد (ویژه دوره اول) - بدون نمایش کدها"""
    
    video_link = course.get('video_link', 'https://www.aparat.com/v/bewg9bw')
    
    content = f"""
    <div class="register-page">
        <span class="success-icon">🔐</span>
        <h2 style="color: #667eea;">ثبت‌نام در دوره</h2>
        <p class="course-name">{course['emoji']} {course['title']}</p>
        
        <div class="code-section">
            <div class="code-title">📝 کد ثبت‌نام خود را وارد کنید</div>
            <p class="code-desc">برای دسترسی به جلسه اول، کد را وارد کنید</p>
            
            <div class="code-input-group">
                <input type="text" id="codeInput" placeholder="کد را وارد کنید..." maxlength="10" dir="ltr">
                <button class="btn-verify" onclick="verifyCode()">✅ تایید کد</button>
            </div>
            
            <div id="codeError" class="code-error">❌ کد وارد شده صحیح نیست!</div>
            <div id="codeSuccess" class="code-success">✅ کد صحیح است! در حال انتقال به جلسه اول...</div>
            
            <div class="no-code">
                <p>🔑 <strong>کد ندارید؟</strong></p>
                <p>به پیامرسان <strong>بله</strong> بروید و به آیدی زیر پیام دهید:</p>
                <p style="font-size: 1.3rem; margin: 0.5rem 0;">
                    <span class="ble-id">@sobhan101095</span>
                </p>
                <a href="https://ble.ir/sobhan101095" target="_blank" class="ble-link">🚀 رفتن به پیامرسان بله</a>
            </div>
        </div>
        
        <div id="videoSection" class="video-section" style="display: none;">
            <h3>🎬 جلسه اول</h3>
            <p style="color: #666; margin-bottom: 1rem;">تبریک! کد شما تأیید شد. حالا می‌توانید جلسه اول را ببینید:</p>
            <a href="{video_link}" target="_blank" class="video-link">▶️ مشاهده جلسه اول</a>
        </div>
        
        <div style="margin-top: 2rem;">
            <a href="index.html" class="btn-secondary">🏠 بازگشت به خانه</a>
            <a href="course_{course['id']}.html" class="btn-primary">📖 بازگشت به صفحه دوره</a>
        </div>
    </div>
    
    <script>
        // ===== بارگذاری کدها از LocalStorage =====
        function loadCodes() {{
            const saved = localStorage.getItem('scratchCodes');
            if (saved) {{
                return JSON.parse(saved);
            }}
            const defaultCodes = ["1234", "5678", "9012", "3456", "7890"];
            localStorage.setItem('scratchCodes', JSON.stringify(defaultCodes));
            return defaultCodes;
        }}
        
        const VALID_CODES = loadCodes();
        
        function verifyCode() {{
            const input = document.getElementById('codeInput');
            const errorDiv = document.getElementById('codeError');
            const successDiv = document.getElementById('codeSuccess');
            const videoSection = document.getElementById('videoSection');
            const code = input.value.trim();
            
            errorDiv.style.display = 'none';
            successDiv.style.display = 'none';
            videoSection.style.display = 'none';
            
            if (code === "") {{
                errorDiv.textContent = '❌ لطفاً کد را وارد کنید!';
                errorDiv.style.display = 'block';
                return;
            }}
            
            if (VALID_CODES.includes(code)) {{
                successDiv.style.display = 'block';
                setTimeout(function() {{
                    videoSection.style.display = 'block';
                    videoSection.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }}, 1000);
            }} else {{
                errorDiv.textContent = '❌ کد وارد شده اشتباه است! لطفاً دوباره امتحان کنید.';
                errorDiv.style.display = 'block';
                input.value = '';
                input.focus();
            }}
        }}
        
        document.getElementById('codeInput').addEventListener('keypress', function(e) {{
            if (e.key === 'Enter') {{
                verifyCode();
            }}
        }});
    </script>
    """
    
    return render_page(content, f"ثبت‌نام | {course['title']}")


def generate_register_simple(course):
    """صفحه ثبت‌نام ساده برای دوره‌های دیگر"""
    
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
    """صفحه جستجو (استاتیک)"""
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
# ۴. پنل مدیریت (مخفی)
# ==========================================

def generate_admin():
    """صفحه پنل مدیریت کدها - فقط با آدرس مستقیم قابل دسترس"""
    
    content = """
    <div class="admin-panel">
        <h2>🔑 پنل مدیریت کدها</h2>
        <p class="admin-subtitle">مدیریت کدهای دسترسی به دوره‌ها (ذخیره در مرورگر)</p>
        <div class="admin-warning">
            ⚠️ این صفحه فقط با آدرس مستقیم قابل دسترسی است و در منوی سایت نمایش داده نمی‌شود.
        </div>
        
        <div class="add-section">
            <h3>➕ اضافه کردن کد جدید</h3>
            <div class="add-group">
                <input type="text" id="newCode" placeholder="کد جدید را وارد کنید..." dir="ltr">
                <button class="btn-add" onclick="addCode()">➕ اضافه کن</button>
            </div>
            <div id="addMessage" class="add-message"></div>
        </div>
        
        <h3>📋 لیست کدهای فعال</h3>
        <table class="codes-table">
            <thead>
                <tr>
                    <th>کد</th>
                    <th>وضعیت</th>
                    <th>عملیات</th>
                </tr>
            </thead>
            <tbody id="codesTableBody">
            </tbody>
        </table>
        
        <div class="admin-buttons">
            <button class="btn-reset" onclick="resetCodes()">🔄 ریست به حالت پیش‌فرض</button>
            <a href="index.html" class="btn-secondary" style="padding: 0.7rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold;">🏠 بازگشت به خانه</a>
        </div>
    </div>
    
    <script>
        // ===== مدیریت کدها در LocalStorage =====
        
        function loadCodes() {
            const saved = localStorage.getItem('scratchCodes');
            if (saved) {
                return JSON.parse(saved);
            }
            const defaultCodes = ["1234", "5678", "9012", "3456", "7890"];
            localStorage.setItem('scratchCodes', JSON.stringify(defaultCodes));
            return defaultCodes;
        }
        
        function saveCodes(codes) {
            localStorage.setItem('scratchCodes', JSON.stringify(codes));
            renderTable();
        }
        
        function renderTable() {
            const codes = loadCodes();
            const tbody = document.getElementById('codesTableBody');
            
            if (codes.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="3" style="padding: 20px; color: #999;">هیچ کدی وجود ندارد!</td>
                    </tr>
                `;
                return;
            }
            
            let html = '';
            codes.forEach(code => {
                html += `
                    <tr>
                        <td><span class="code-box">${code}</span></td>
                        <td><span class="status-active">✅ فعال</span></td>
                        <td>
                            <button class="btn-remove" onclick="removeCode('${code}')">🗑️ حذف</button>
                        </td>
                    </tr>
                `;
            });
            tbody.innerHTML = html;
        }
        
        function addCode() {
            const input = document.getElementById('newCode');
            const message = document.getElementById('addMessage');
            const code = input.value.trim();
            
            if (code === "") {
                message.textContent = '❌ لطفاً کد را وارد کنید!';
                message.className = 'add-message error';
                return;
            }
            
            let codes = loadCodes();
            if (codes.includes(code)) {
                message.textContent = '❌ این کد قبلاً وجود دارد!';
                message.className = 'add-message error';
                return;
            }
            
            codes.push(code);
            saveCodes(codes);
            message.textContent = '✅ کد با موفقیت اضافه شد!';
            message.className = 'add-message success';
            input.value = '';
            
            setTimeout(() => {
                message.className = 'add-message';
            }, 3000);
        }
        
        function removeCode(code) {
            if (!confirm(`آیا از حذف کد "${code}" مطمئن هستید؟`)) return;
            
            let codes = loadCodes();
            codes = codes.filter(c => c !== code);
            saveCodes(codes);
        }
        
        function resetCodes() {
            if (!confirm('همه کدها به حالت پیش‌فرض ریست می‌شوند! مطمئن هستید؟')) return;
            
            const defaultCodes = ["1234", "5678", "9012", "3456", "7890"];
            localStorage.setItem('scratchCodes', JSON.stringify(defaultCodes));
            renderTable();
            
            const message = document.getElementById('addMessage');
            message.textContent = '✅ کدها با موفقیت ریست شدند!';
            message.className = 'add-message success';
            
            setTimeout(() => {
                message.className = 'add-message';
            }, 3000);
        }
        
        // بارگذاری اولیه
        renderTable();
    </script>
    """
    
    return render_page(content, "مدیریت کدها | کدآکادمی کودکان")


# ==========================================
# ۵. تابع اصلی
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
    
    # ۶. پنل مدیریت (مخفی - فقط با آدرس مستقیم)
    with open("admin.html", "w", encoding="utf-8") as f:
        f.write(generate_admin())
    print("✅ admin.html (پنل مدیریت - مخفی)")
    
    # ۷. صفحات جزئیات و ثبت‌نام برای هر دوره
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
    print("🔑 پنل مدیریت مخفی: admin.html (فقط با آدرس مستقیم)")
    print("💡 کدها در LocalStorage مرورگر ذخیره می‌شوند.")
    print("=" * 55)


if __name__ == "__main__":
    main()
