from datetime import datetime
def cripta():
    cripta_dict = {}
    now = datetime.now()
    formatted_string_ru = now.strftime("%d.%m.%Y %H:%M")
    cripta_dict["USDT"] = {"price" : 100, "date" : formatted_string_ru}
    return cripta_dict
print(cripta())