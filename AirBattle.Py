#Problem: https://quera.org/problemset/182271?tab=description
#Solution:
# ترکیب دو نیمه و شمارش اهداف استراتژیک برای هر جنگنده
def merge_and_count(heights, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    strategic_count = 0  # متغیری برای شمارش تعداد جنگنده‌های قابل هدف

    # ترکیب دو نیمه و شمارش تعداد اهداف استراتژیک
    while i <= mid and j <= right:
        if heights[i] <= heights[j]:
            temp[k] = heights[i]  # اگر ارتفاع سمت چپ کوچک‌تر یا مساوی باشد، آن را کپی می‌کنیم
            i += 1
        else:
            temp[k] = heights[j]  # اگر ارتفاع سمت راست کوچک‌تر باشد
            strategic_count += (mid - i + 1)  # تمام جنگنده‌های سمت چپ که ارتفاع بیشتری دارند قابل هدف هستند
            j += 1
        k += 1  # حرکت به عنصر بعدی در آرایه ترکیبی

    # کپی باقیمانده عناصر سمت چپ در آرایه ترکیبی
    while i <= mid:
        temp[k] = heights[i]
        i += 1
        k += 1

    # کپی باقیمانده عناصر سمت راست در آرایه ترکیبی
    while j <= right:
        temp[k] = heights[j]
        j += 1
        k += 1

    # انتقال عناصر از آرایه ترکیبی به آرایه اصلی
    for i in range(left, right + 1):
        heights[i] = temp[i]

    return strategic_count  # بازگرداندن تعداد اهداف استراتژیک برای این بخش از آرایه

# الگوریتم اصلی تقسیم و حل با استفاده از ادغام برای شمارش اهداف استراتژیک
def merge_sort_and_count(heights, temp, left, right):
    if left >= right:
        return 0  # اگر یک عنصر یا کمتر داریم، تعداد اهداف استراتژیک صفر است

    mid = (left + right) // 2  # پیدا کردن نقطه میانی برای تقسیم
    strategic_count = merge_sort_and_count(heights, temp, left, mid)  # حل بازگشتی نیمه چپ
    strategic_count += merge_sort_and_count(heights, temp, mid + 1, right)  # حل بازگشتی نیمه راست
    strategic_count += merge_and_count(heights, temp, left, mid, right)  # ترکیب نتایج دو نیمه و شمارش اهداف استراتژیک

    return strategic_count  # بازگرداندن مجموع اهداف استراتژیک کل

# تابع اصلی که الگوریتم را برای محاسبه مجموع اهداف استراتژیک اجرا می‌کند
def calculate_strategic_sum(n, heights):
    temp = [0] * n  # آرایه کمکی برای ترکیب
    return merge_sort_and_count(heights, temp, 0, n - 1)  # اجرای الگوریتم تقسیم و حل برای کل آرایه

# دریافت ورودی
n = int(input().strip())  # خواندن تعداد جنگنده‌ها
heights = list(map(int, input().strip().split()))  # خواندن ارتفاع‌ها به عنوان لیست اعداد صحیح

# محاسبه و چاپ نتیجه
print(calculate_strategic_sum(n, heights))  # چاپ مجموع اهداف استراتژیک
