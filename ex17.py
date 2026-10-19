import datetime

# تمرین ۱: زمان فعلی (ساعت:دقیقه)
now = datetime.datetime.now()
print("Current Time:", now.strftime("%H:%M"))

# تمرین ۲: تاریخ امروز (روز/ماه/سال)
print("Today's Date:", now.strftime("%d/%m/%Y"))

# تمرین ۳: تاریخ انقضا (۷ روز بعد)
future_date = now + datetime.timedelta(days=7)
print("Expire Date (7 days later):", future_date.strftime("%Y-%m-%d"))

# تمرین ۴: محاسبه سن
birth_date = datetime.datetime(2020, 5, 15)
age_days = (now - birth_date).days
age_years = age_days // 365  # تقسیم صحیح برای اینکه عدد اعشاری نگیریم
print(f"Age: {age_years} years")
