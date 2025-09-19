while True:
    ipadkids_input = input("введите число или 'стоп'")
    if ipadkids_input.lower() == "стоп":
        break
    try:
        number = float(ipadkids_input)
        print(f"Вы ввели число {number}")
    except ValueError:
        print("эррор")