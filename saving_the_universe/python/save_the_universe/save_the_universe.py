import input_parser as ip


def should_switch(current_engine: str, query: str) -> bool:
    return current_engine == query


def count_switches(engines: list[str],
                   queries: list[str],
                   switch_count: int = 0) -> int:
    if len(engines) == 0 or len(queries) == 0:
        return switch_count
    if should_switch(engines[0], queries[0]):
        switch_count += 1
        engines = engines[1:]
    return count_switches(engines, queries[1:], switch_count)


def count_min_switches(
    engines: list[str],
    queries: list[str],
    switch_count: int,
    n: int,
) -> int:
    if n == 0:
        return switch_count
    switch_count_new = count_switches(engines, queries)
    if switch_count > switch_count_new:
        switch_count = switch_count_new
    return count_min_switches(
        engines[-1:] + engines[:-1],
        queries,
        switch_count,
        n - 1,
    )


def save_the_universe():
    cases = ip.get_cases(int(input('Enter the number of cases: ')))
    for index, case in enumerate(cases):
        switches = count_min_switches(
            case[0],
            case[1],
            len(case[1]),
            len(case[0]),
        )
        print(f'Case #{index}: {switches}')
