def find_by_category(records, category):
    """Повертає список записів, які відповідають заданій категорії."""
    return [r for r in records if r["category"].lower() == category.lower()]

def total_by_category(records):
    """Повертає словник {категорія: сума}."""
    totals = {}
    for r in records:
        cat = r["category"]
        totals[cat] = totals.get(cat, 0.0) + r["amount"]
    return totals

def get_monthly_report(records, year_month):
    """Повертає загальну суму витрат за вказаний місяць (формат РРРР-ММ)."""
    total = 0.0
    for r in records:
        if r["date"].startswith(year_month):
            total += r["amount"]
    return total

def get_largest_expense(records):
    """Повертає запис з найбільшою сумою або None, якщо список порожній."""
    if not records:
        return None
    return max(records, key=lambda r: r["amount"])
