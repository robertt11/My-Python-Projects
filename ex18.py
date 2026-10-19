# تمرین ۱ و ۲: ساخت پوشه و محیط مجازی
mkdir myproject
cd myproject
python -m venv venv
source venv/bin/activate

# تمرین ۳: نصب کتابخانه و بررسی
pip install requests
pip list

# خروج از محیط و بررسی مجدد
deactivate
pip list

# تمرین ۴: ساخت فایل requirements
source venv/bin/activate
pip freeze > requirements.txt
cat requirements.txt
