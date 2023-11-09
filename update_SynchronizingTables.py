def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    sort_ids, sort_salary = sorted(ids), sorted(salary)
    table_ids_and_salary = dict(zip(sort_ids, sort_salary))
    return [table_ids_and_salary[worker] for worker in ids]

