import json


def ads_json_restructured(json_file, model):

    with open(json_file, "r", encoding="utf-8") as json_f:
        data = json.load(json_f)

        result_list = []
        for element in data:
            result_list.append(
                {
                    "model": model,
                    "pk": element["id"],
                    "fields": {
                        "name": element["name"],
                        "author": element["author"],
                        "price": element["price"],
                        "description": element["description"],
                        "address": element["address"],
                        "is_published": element["is_published"]
                    }
                }
            )

        return result_list


def data_to_json_file(json_file, model):
    with open(json_file, "w", encoding="utf-8") as json_f_new:
        data = ads_json_restructured(json_file, model)
        json.dump(data, json_f_new)



ads_modified = ads_json_restructured("ads_wn.json", "model_name")
print(ads_modified)


data_to_json_file("ads_wn.json", "model_name")




# {
# "model": "ads.ad",
# "pk": "12",
# "fields": {
# "name": "Собака в добрые руки",
# "author": "Петр",
# "price": 1500,
# "description": "Весенняя и лукавая Норочка не унывает и терпеливо ждёт единственного и неповторимого хозяина! Нора - собака для тепла, любви и активного времяпрепровождения! Если Вы давно ищите компаньона и друга, то Нора очень Вас ждёт!",
# "address": "Москва, м. Библиотека имени Ленина",
# "is_published": true
# }
# },