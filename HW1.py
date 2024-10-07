# تمرین 1:
# تابعی با نام  my_final_grade_calculation بنویسید که یک نام فایل دریافت کند و یک دیکشنری را برگرداند که بگوید یک دانش آموز براساس معیار های زیر در این دوره قبول شده یا ناموفق بوده است.
# هر خط از فایل فرمت زیرین را خواهد داشت:
#  name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final

# به طوری که :
# •  نام، یک رشته است
# • q1 تا q6 نمرات آزمون هستند (اعداد صحیح).
# • a1 تا a4 نمرات تکلیف هستند(مقادیر اعداد صحیح)
# • midterm، نمره میان ترم است. (عدد صحیح)
# • final، نمره امتحان نهایی است (عدد صحیح)
# برای مثال، اگر محتوای فایل مانند زیر به نظر برسد:

#  tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
# mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
# joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5

# توجه داشته باشید که ممکن است در هرخط، فضای اضافی بین ورودی وجود داشته باشد.
# تابع شما باید یک دیکشنری مانند نمونه زیر را برگرداند:

#  {"tom":"pass", "mary":"pass", "joan":"fail"} 

# نکات:
# • دوتا از پایین ترین نمرات باید از قلم انداخته شود و میانگین چهار آزمون باقی مانده 25% ارزش کل نمره است.
# • پایین ترین نمره تکلیف باید از قلم انداخته شود و میانگین سه تمرین باقی مانده 25% ارزش کل نمره است.
# • امتحان نهایی و میان ترم هر کدام 25% کل نمره هستند.
# • اسامی دانش آموزان در خروجی باید به حروف کوچک تبدیل شوند.
# مجموع نمرات دانش آموز را محاسبه کنید و اگر مجموع نمرات بزرگ تر یا برابر 60(مجموع نمرات >=60) باشد دراین صورت دانش آموز موفق شده است. توجه داشته باشید که کلید ها (نام ها) و مقادیر (قبولی یا شکست) دیکشنری باید تمام حروف کوچک بدون هیچ فاصله ای در آنها باشد.
# هیچگونه ماژولی را برای حل این مسأله وارد نکنید.

def my_final_grade_calculation(file_name):
    result = {}
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            # حذف فاصله‌های اضافی و تقسیم اطلاعات
            data = line.strip().split()
            name = data[0].lower()
            q_scores = list(map(int, data[1:7]))
            a_scores = list(map(int, data[7:11]))
            midterm = int(data[11])
            final = int(data[12])
            
            # حذف دو نمره پایین‌تر از آزمون‌ها
            q_scores.remove(min(q_scores))
            q_scores.remove(min(q_scores))
            avg_q = sum(q_scores) / len(q_scores)  # میانگین 4 نمره باقی‌مانده
            
            # حذف یک نمره پایین‌تر از تکالیف
            a_scores.remove(min(a_scores))
            avg_a = sum(a_scores) / len(a_scores)  # میانگین 3 نمره باقی‌مانده
            
            # محاسبه نمره نهایی
            final_score = (avg_q * 0.25) + (avg_a * 0.25) + (midterm * 0.25) + (final * 0.25)
            
            # بررسی قبول شدن یا رد شدن
            if final_score >= 60:
                result[name] = "pass"
            else:
                result[name] = "fail"
    
    return result

# توضیحات کد:

#     خواندن فایل: فایل ورودی با استفاده از open باز شده و هر خط جداگانه پردازش می‌شود.
#     پردازش نمرات: نمرات آزمون‌ها و تکالیف به‌صورت لیستی از اعداد صحیح ذخیره می‌شوند. سپس پایین‌ترین نمرات حذف می‌شود.
#     محاسبه نمره نهایی: هر بخش از نمره به نسبت تعیین‌شده (25%) محاسبه می‌شود.
#     نتیجه نهایی: دیکشنری شامل نام‌های دانش‌آموزان (به حروف کوچک) و وضعیت قبول یا رد آن‌ها است.
