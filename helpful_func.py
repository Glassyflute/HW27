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


def categories_json_restructured(json_file, model):

    with open(json_file, "r", encoding="utf-8") as json_f:
        data = json.load(json_f)

        result_list = []
        for element in data:
            result_list.append(
                {
                    "model": model,
                    "pk": element["id"],
                    "fields": {
                        "name": element["name"]
                    }
                }
            )

        return result_list


# def json_restructured(json_file, model):
#
#     with open(json_file, "r", encoding="utf-8") as json_f:
#         data = json.load(json_f)
#
#         result_list = []
#
#         fields_dict = []
#
#         for element in data:
#             for key in element.keys():
#
#
#             result_list.append(
#                 {
#                     "model": model,
#                     "pk": element["id"],
#                     "fields": {
#                         "name": element["name"]
#                     }
#                 }
#             )
#
#         return result_list


def data_to_json_file_ads(json_file, json_newfile, model):
    with open(json_newfile, "w", encoding="utf-8") as json_f_new:
        data = ads_json_restructured(json_file, model)
        json_f_new.write(json.dumps(data, ensure_ascii=False))


def data_to_json_file_cat(json_file, json_newfile, model):
    with open(json_newfile, "w", encoding="utf-8") as json_f_new:
        data = categories_json_restructured(json_file, model)
        json_f_new.write(json.dumps(data, ensure_ascii=False))


output = data_to_json_file_ads("ads_wn.json", "ads_wn_fixt.json", "ads.ad")
output2 = data_to_json_file_cat("categories.json", "categories_fixt.json", "ads.category")
