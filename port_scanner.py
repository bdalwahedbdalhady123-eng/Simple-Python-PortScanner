import re
import sys

def check_password_strength(password):
    # المعايير الأمنية
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !@#$%^&*(),.?\":{}|<>_]", password) is None
    
    # حساب النتيجة
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False) # كلما قلّت الأخطاء زادت القوة
    
    print("-" * 40)
    print(f"Password Evaluated: {password}")
    print("-" * 40)
    
    # تحديد مستوى القوة
    if score == 5:
        return "🟢 Strength: VERY STRONG (Excellent!)"
    elif score == 4:
        return "🟡 Strength: STRONG (Good, but can be improved)"
    elif score == 3:
        return "🟠 Strength: MEDIUM (Vulnerable to attacks)"
    else:
        return "🔴 Strength: WEAK (Highly Insecure!)"

# تشغيل الأداة
try:
    while True:
        user_password = input("\nEnter a password to test (or type 'exit' to quit): ")
        if user_password.lower() == 'exit':
            print("Exiting tool. Stay safe!")
            sys.exit()
            
        result = check_password_strength(user_password)
        print(result)
        
except KeyboardInterrupt:
    print("\nExiting tool.")
    sys.exit()
