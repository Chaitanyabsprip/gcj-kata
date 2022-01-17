def get_cases(
    number_of_cases: int,
    cases: list[list[list[str]]] = [],
) -> list[list[list[str]]]:
    if number_of_cases == 0:
        return cases
    engines = get_engines(int(input('Enter number of engines: ')))
    queries = get_queries(int(input('Enter number of queries: ')))
    return get_cases(number_of_cases - 1, cases + [[engines, queries]])


def get_queries(number_of_queries: int, queries: list[str] = []) -> list[str]:
    if number_of_queries == 0:
        return queries
    return get_queries(
        number_of_queries - 1,
        queries + [input(f'Enter query #{len(queries) + 1}: ')],
    )


def get_engines(number_of_engines: int, engines: list[str] = []) -> list[str]:
    if number_of_engines == 0:
        return engines
    return get_engines(
        number_of_engines - 1,
        engines + [input(f'Enter engine #{len(engines) + 1}: ')],
    )
