import os

def load(filename):
    """Повертає список словників з файла. Пошкоджені рядки пропускає."""
    records = []
    if not os.path.exists(filename):
        return records
        
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            try:
                record = {
                    "date": parts[0],
                    "category": parts[1],
                    "amount": float(parts[2]),
                    "note": parts[3],
                }
                records.append(record)
            except (IndexError, ValueError):
                print("пропущено пошкоджений рядок:", line)
                continue
    return records

def save(filename, records):
    """Записує всі записи у файл."""
    with open(filename, "w", encoding="utf-8") as f:
        for r in records:
            f.write(f"{r['date']};{r['category']};{r['amount']};{r['note']}\n")
