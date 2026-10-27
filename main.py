from fastapi import FastAPI
from enum import Enum
app = FastAPI()


class AvailableCuisines(str, Enum):
    italian = "italian"
    mexican = "mexican"
    indian = "indian"
    

food_items = {
    "italian": ["Pizza", "Pasta", "Gelato"],
    "mexican": ["Tacos", "Burritos", "Chiles Rellenos"],
    "indian": ["Biryani", "Butter Chicken", "Samosa"]
}

valid_cuisines = food_items.keys()
@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine.value)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{coupon_id}")
async def get_coupon(coupon_id: int):
    return {'discount_amount': coupon_code.get(coupon_id)}

