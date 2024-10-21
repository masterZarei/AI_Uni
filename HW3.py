#Problem: https://quera.org/problemset/3433
#Solution:

def maximum_prizes(p):
    total_prize = 0
    while len(p) > 1:
        n = len(p)
        mid = n // 2
        
        # تقسیم به دو دسته
        first_half = p[:mid]
        second_half = p[mid:]
        
        # پیدا کردن بیشترین قدرت در هر دسته
        max_first = max(first_half)
        max_second = max(second_half)
        
        # انتخاب دسته برای خداحافظی
        if max_first > max_second:
            total_prize += max_first
            p = second_half  # خداحافظی با دسته اول
        else:
            total_prize += max_second
            p = first_half   # خداحافظی با دسته دوم
            
    # اضافه کردن قدرت تیم آخر
    total_prize += p[0]
    
    return total_prize

# مثال
powers = [1, 6, 1, 7, 1, 8, 1, 4]
print(maximum_prizes(powers))  # خروجی: 22
