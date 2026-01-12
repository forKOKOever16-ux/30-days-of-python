## 🧠 شرح سريع (اختصارات)
#
# unittest
# مكتبة بايثون مخصصة لاختبار الكود تلقائيًا.
#
# add(a, b)
# دالة تجمع رقمين وترجع الناتج.
#
# TestAddition(unittest.TestCase)
# كلاس يحتوي على اختبارات
# لازم يرث من TestCase.
#
# test_add()
# أي دالة يبدأ اسمها بـ test_
# تعتبر اختبار تلقائي.
#
# assertEqual(x, y)
# يتأكد أن الناتج الفعلي = الناتج المتوقع
# ✔️ ينجح لو متساويين
# ❌ يفشل لو مختلفين.
#
# unittest.main()
# يشغّل جميع الاختبارات في الملف.


import unittest
def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  def test_add(self):
    result = add(3, 4)

    expected_result = 7
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()

