# Витрати

Консольний облік особистих витрат за категоріями.

## Для кого
Для мене, щоб бачити, куди йдуть гроші.

## Запуск
Додати новий запис:
```bash
python cli.py add 2026-10-03 їжа 250 обід
python cli.py add 2026-10-04 транспорт 40 метро
```

Показати всі записи:
```bash
python cli.py list
```

Пошук за категорією:
```bash
python cli.py find їжа
```

Згенерувати звіт:
```bash
python cli.py report
```

Запустити тести:
```bash
python tests.py
```

## Формат даних
Файл `data.txt`, один запис на рядок у форматі:
`дата;категорія;сума;коментар`
## Запуск вебсервісу та приклади запитів (API)

Запустити сервер:
```bash
python app.py
```

Додати запис:
```bash
curl -i -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"date": "2026-11-25", "category": "їжа", "amount": 250, "note": "обід"}'
```

Отримати всі записи:
```bash
curl -i http://localhost:5000/items
```

Отримати звіт за категоріями:
```bash
curl -i http://localhost:5000/report
```

Видалити запис:
```bash
curl -i -X DELETE http://localhost:5000/items/1
```
