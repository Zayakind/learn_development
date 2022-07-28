
def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    ids_sort, salary_sort = ids[:], salary[:]
    ids_sort.sort()
    salary_sort.sort()
    ids_salary_dict = {}
    for i in range(N):
        ids_salary_dict[ids_sort[i]] = salary_sort[i]
    result_salary = [ids_salary_dict.get(_id) for _id in ids]
    return result_salary
