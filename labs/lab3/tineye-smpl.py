tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

# red channel of clay creek
red_value = tineye_sample["result"][0]["color"][0]
print(f"The red channel of Clay Creek has a value {red_value}")

# blue channel of seal Brown
blue_value = tineye_sample["result"][1]["color"][2]
print(f"The blue channel of Seal Brown has a value {blue_value}")                  


