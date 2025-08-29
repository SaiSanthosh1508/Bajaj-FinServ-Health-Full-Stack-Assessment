from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()

class DataModel(BaseModel):
    data: list[str]

@app.post("/bfhl")
def route_bfhl(body: DataModel):
    data = body.data
    if not data:
        raise HTTPException(status_code=400, detail = "Data list cannot be empty")

    odd_nums = []
    even_nums = []
    alphabets = []
    special_chars = []
    total_sum = 0

    for item in data:
        if item.isdigit():
            num = int(item)
            total_sum += num
            if num % 2 == 0:
                even_nums.append(item)
            else:
                odd_nums.append(item)
        elif item.isalpha():
            alphabets.append(item.upper())
        else:
            special_chars.append(item)

    only_alpha = [item for item in data if item.isalpha()]
    string = ''.join(only_alpha)[::-1]
    result = "".join([ch.upper() if i%2==0 else ch.lower() for i, ch in enumerate(string)])

    return {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd_nums,
        "even_numbers": even_nums,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(total_sum),
        "concat_string": result
    }
