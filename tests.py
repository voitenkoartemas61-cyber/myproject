import logic

def test_logic():
    # Тестовий набір даних
    sample_records = [
        {"date": "2026-10-03", "category": "їжа", "amount": 250.0, "note": "обід"},
        {"date": "2026-10-04", "category": "транспорт", "amount": 40.0, "note": "метро"},
        {"date": "2026-10-05", "category": "їжа", "amount": 150.0, "note": "кава"},
        {"date": "2026-11-01", "category": "коробочка", "amount": 500.0, "note": "подарунок"},
    ]

    # 1. Тести find_by_category
    assert len(logic.find_by_category(sample_records, "їжа")) == 2
    assert len(logic.find_by_category(sample_records, "кіно")) == 0

    # 2. Тести total_by_category
    totals = logic.total_by_category(sample_records)
    assert totals["їжа"] == 400.0
    assert totals["транспорт"] == 40.0

    # 3. Тести get_monthly_report
    assert logic.get_monthly_report(sample_records, "2026-10") == 440.0
    assert logic.get_monthly_report(sample_records, "2026-12") == 0.0

    # 4. Тести get_largest_expense
    assert logic.get_largest_expense(sample_records)["amount"] == 500.0
    assert logic.get_largest_expense([]) is None

    print("Всі локальні тести успішно пройдено!")

if __name__ == "__main__":
    test_logic()
