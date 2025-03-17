def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(grey)
        return color_code
    except ValueError:
        return None

color_name = input('Enter color')
result_code = color_name_to_code(color_name)
print(result_code)
