import sys
import storage
import logic

FILE = "data.txt"

def main():
    if len(sys.argv) < 2:
        print("використання: python cli.py add|list|find|report ...")
        return

    command = sys.argv[1]
    records = storage.load(FILE)

    if command == "add":
        if len(sys.argv) < 5:
            print("використання: python cli.py add ДАТА КАТЕГОРІЯ СУМА [КОМЕНТАР]")
            return
        
        date = sys.argv[2]
        category = sys.argv[3]
        try:
            amount = float(sys.argv[4])
        except ValueError:
            print("сума має бути числом")
            return
        note = sys.argv[5] if len(sys.argv) > 5 else ""

        records.append({"date": date, "category": category, "amount": amount, "note": note})
        storage.save(FILE, records)
        print("додано")

    elif command == "list":
        if not records:
            print("Немає записів.")
            return
        for r in records:
            print(f"{r['date']}  {r['category']:<12} {r['amount']:>8.2f}  {r['note']}")

    elif command == "find":
        if len(sys.argv) < 3:
            print("використання: python cli.py find КАТЕГОРІЯ")
            return
        found = logic.find_by_category(records, sys.argv[2])
        if not found:
            print("Нічого не знайдено.")
            return
        for r in found:
            print(f"{r['date']}  {r['category']:<12} {r['amount']:>8.2f}  {r['note']}")

    elif command == "report":
        print("--- Сума за категоріями ---")
        for cat, total in logic.total_by_category(records).items():
            print(f"{cat:<12} {total:>8.2f}")
        
        largest = logic.get_largest_expense(records)
        if largest:
            print("\n--- Найбільша витрата ---")
            print(f"{largest['date']}  {largest['category']}  {largest['amount']:.2f} ({largest['note']})")

    else:
        print("невідома команда:", command)

if __name__ == "__main__":
    main()
