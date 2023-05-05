import random
import time
from typing import List
import asyncio

class Company:
    def __init__(self, code: List[str], name: str):
        self.code = code
        self.name = name
    
companies = [Company([],"") for i in range(1,11)]

async def function_1(number: int):
    await asyncio.gather(asyncio.sleep(1), asyncio.sleep(1))
    companies[number-1].code = [f"{number}"]
    companies[number-1].name = f"{number}"

async def function_2():
    start = time.time()
    print(f'BEGIN {start}')
    results = await asyncio.gather( *(function_1(i) for i in range(1,11)))
    end = time.time()
    print(f"Thời gian để thực hiện là: {end-start} second")
    for company in companies:
        print(f'CompanyCode: {company.code} - CompanyName: {company.name}')
        

await function_2()
---
    await asyncio.sleep(1)
    return "hello_a"
async def func_b():
    await asyncio.sleep(1)
    return "hello_b"
a, b = await asyncio.gather(func_a(), func_b())
print(a)
print(b)
hello_a
hello_b
