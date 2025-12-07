from parser import main_parse


async def post_custom_currensy(id_of_currensy_1: int, id_of_currensy_2: int):
    
    for currensy in await main_parse():
        if currensy["id"] == id_of_currensy_1:
            currensy_1 = currensy
        elif currensy["id"] == id_of_currensy_2:
            currensy_2 = currensy
        
    if currensy_1 is None and currensy_2 is None:
        return "Валюты не найдены" 
    elif currensy_1 is None:
        return "Валюта 1 не найдена" 
    elif currensy_2 is None:
        return "Валюта 2 не найдена" 
    else:
        return {"id_1": currensy_1["id"],
                "id_2": currensy_2["id"],
                "exchange_1": currensy_1["exchange"],
                "exchange_2": currensy_2["exchange"],
                "name" : currensy_1["name"][:3] + "/" + currensy_2["name"][:3],
                "price" : round(currensy_1["price"] / currensy_2["price"], 4),
                "date" : currensy_1["date"]}

print(post_custom_currensy(0,3))

