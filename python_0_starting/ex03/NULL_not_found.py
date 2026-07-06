def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print(f"Nothing: {object} {type(object)}")
            return 0
        case float() if object != object:
            print(f"Cheese: {object} {type(object)}")
            return 0
        case bool():
            print(f"Fake: {object} {type(object)}")
            return 0
        case 0:
            print(f"Zero: {object} {type(object)}")
            return 0
        case "":
            print(f"Empty: {object} {type(object)}")
            return 0
        case _:
            print("Type not Found")
            return 1
