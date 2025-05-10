# test_main.py
import pytest
from main import جمع, تفریق, ضرب # توابع را مستقیم از main.py وارد می‌کنیم

def test_تابع_جمع():
    assert جمع(2, 3) == 5
    assert جمع(-1, 1) == 0
    assert جمع(-5, -5) == -10
    assert جمع(0, 0) == 0
    assert جمع(1.5, 2.5) == 4.0

def test_تابع_تفریق():
    assert تفریق(5, 3) == 2
    assert تفریق(3, 5) == -2
    assert تفریق(0, 0) == 0
    assert تفریق(-1, -1) == 0
    assert تفریق(5.5, 2.5) == 3.0

def test_تابع_ضرب():
    assert ضرب(2, 3) == 6
    assert ضرب(-1, 5) == -5
    assert ضرب(0, 100) == 0
    assert ضرب(7, 1) == 7
    assert ضرب(2.5, 2) == 5.0

# برای اجرای تست‌ها، در ترمینال در ریشه پروژه دستور `pytest` را وارد کنید.
# مطمئن شوید که pytest نصب شده است: pip install pytest