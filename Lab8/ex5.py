def safe_apply(func, data):
    results = []
    errors = []
    for elem in data:
        try:
            result = func(elem)
            results.append(result)
        except Exception as e:
            errors.append((elem,e))

    return results, errors

asda = lambda x: x**(1/2)
assggg = [['4', '16', 'text', '-25', '9.0']]

sjdbkjhf = safe_apply(asda,assggg)
print(sjdbkjhf)