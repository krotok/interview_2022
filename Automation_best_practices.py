# Python Best Practices: 50+ Examples of Bad vs Good Code

# --- 1. Naming ---
# ❌ Bad
x = 10
def f(a): return a*a

# ✅ Good
user_count = 10
def square(number): return number * number

# --- 2. Type hints ---
# ❌ Bad
def greet(name): return "Hello " + name

# ✅ Good
def greet(name: str) -> str:
    return f"Hello {name}"

# --- 3. Magic numbers ---
# ❌ Bad
age = 17
if age > 18:
    pass

# ✅ Good
LEGAL_AGE = 18
if age > LEGAL_AGE:
    pass

# --- 4. Mutable default args ---
# ❌ Bad
def append_item(item, items=[]):
    items.append(item)
    return items

# ✅ Good
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# --- 5. Unclear error handling ---
# ❌ Bad
def risky_operation():
    pass
try:
    risky_operation()
except:
    pass

# ✅ Good
import logging
try:
    risky_operation()
except ValueError as e:
    logging.error(f"ValueError: {e}")

# --- 6. Logging instead of print ---
# ❌ Bad
print("Error occurred")

# ✅ Good
import logging
logging.error("Error occurred")

# --- 7. List comprehension instead of loop ---
# ❌ Bad
squares = []
for x in range(10):
    squares.append(x*x)

# ✅ Good
squares = [x*x for x in range(10)]

# --- 8. Use with for files ---
# ❌ Bad
f = open("file.txt")
data = f.read()
f.close()

# ✅ Good
with open("file.txt") as f:
    data = f.read()

# --- 9. Avoid deeply nested code ---
def do_something():
    pass

# ❌ Bad
if x:
    if y:
        if z:
            do_something()

# ✅ Good
if not x or not y or not z:
    return

do_something()

# --- 10. Use enumerations ---
# ❌ Bad
if status == "open":
    ...
elif status == "closed":
    ...

# ✅ Good
from enum import Enum
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"

if status == Status.OPEN:
    ...

# --- 11. Use generators for large data ---
# ❌ Bad
def get_numbers():
    return [x for x in range(1000000)]

# ✅ Good
def get_numbers():
    for x in range(1000000):
        yield x

# --- 12. Use Counter ---
# ❌ Bad
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

# ✅ Good
from collections import Counter
counts = Counter(items)

# --- 13. Use defaultdict ---
# ❌ Bad
grouped = {}
for key, value in data:
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(value)

# ✅ Good
from collections import defaultdict
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)

# --- 14. Avoid redundant ifs ---
# ❌ Bad
if x == True:
    ...

# ✅ Good
if x:
    ...

# --- 15. Use constants ---
# ❌ Bad
if role == "admin":
    ...

# ✅ Good
ROLE_ADMIN = "admin"
if role == ROLE_ADMIN:
    ...

# --- 16. Use dataclass ---
# ❌ Bad
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ✅ Good
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

# --- 17. Use comprehensions for dicts/sets ---
# ❌ Bad
squared = {}
for x in range(10):
    squared[x] = x*x

# ✅ Good
squared = {x: x*x for x in range(10)}

# --- 18. Use built-in functions ---
# ❌ Bad
result = []
for x in data:
    result.append(str(x))

# ✅ Good
result = list(map(str, data))

# --- 19. Use zip ---
# ❌ Bad
for i in range(len(names)):
    print(names[i], ages[i])

# ✅ Good
for name, age in zip(names, ages):
    print(name, age)

# --- 20. Use "any" and "all" ---
# ❌ Bad
found = False
for x in data:
    if x > 10:
        found = True

# ✅ Good
found = any(x > 10 for x in data)

# --- 21. Avoid repeated calculations ---
# ❌ Bad
if len(data) > 0 and len(data) < 100:
    ...

# ✅ Good
length = len(data)
if 0 < length < 100:
    ...

# --- 22. Use tuple unpacking ---
# ❌ Bad
x = coords[0]
y = coords[1]

# ✅ Good
x, y = coords

# --- 23. Use contextlib for custom context ---
# ❌ Bad
lock.acquire()
do_stuff()
lock.release()

# ✅ Good
from contextlib import contextmanager

@contextmanager
def acquire_lock(lock):
    lock.acquire()
    try:
        yield
    finally:
        lock.release()

with acquire_lock(lock):
    do_stuff()

# --- 24. Avoid complex one-liners ---
# ❌ Bad
result = func1(func2(func3(x)))

# ✅ Good
temp = func3(x)
temp = func2(temp)
result = func1(temp)

# --- 25. Use async/await properly ---
# ❌ Bad
def fetch():
    response = requests.get(url)

# ✅ Good
import aiohttp
async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

# --- 26. Use "else" with loops ---
# ❌ Bad
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    raise ValueError("Not found")

# ✅ Good
for item in items:
    if item == target:
        break
else:
    raise ValueError("Not found")

# --- 27. Use pathlib instead of os.path ---
# ❌ Bad
import os
path = os.path.join("dir", "file.txt")

# ✅ Good
from pathlib import Path
path = Path("dir") / "file.txt"

# --- 28. Use type checking tools ---
# ✅ Good practice
# Run: mypy script.py or use pyright

def add(a: int, b: int) -> int:
    return a + b

# --- 29. Avoid side effects in __init__ ---
# ❌ Bad
class Downloader:
    def __init__(self):
        self.data = download()

# ✅ Good
class Downloader:
    def __init__(self):
        self.data = None

    def load(self):
        self.data = download()

# --- 30. Prefer composition over inheritance ---
# ❌ Bad
class FlyingCar(Car):
    def fly(): pass

# ✅ Good
class FlyingCar:
    def __init__(self):
        self.car = Car()
        self.plane = Plane()

    def drive(self):
        self.car.drive()

    def fly(self):
        self.plane.fly()

# --- To be continued until 50+ examples... Let me know to proceed!

# Python Best Practices: 50+ Examples of Bad vs Good Code

# --- 1. Naming ---
# ❌ Bad
x = 10
def f(a): return a*a

# ✅ Good
user_count = 10
def square(number): return number * number

# --- 2. Type hints ---
# ❌ Bad
def greet(name): return "Hello " + name

# ✅ Good
def greet(name: str) -> str:
    return f"Hello {name}"

# --- 3. Magic numbers ---
# ❌ Bad
if age > 18:
    pass

# ✅ Good
LEGAL_AGE = 18
if age > LEGAL_AGE:
    pass

# --- 4. Mutable default args ---
# ❌ Bad
def append_item(item, items=[]):
    items.append(item)
    return items

# ✅ Good
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# --- 5. Unclear error handling ---
# ❌ Bad
try:
    risky_operation()
except:
    pass

# ✅ Good
try:
    risky_operation()
except ValueError as e:
    logging.error(f"ValueError: {e}")

# --- 6. Logging instead of print ---
# ❌ Bad
print("Error occurred")

# ✅ Good
import logging
logging.error("Error occurred")

# --- 7. List comprehension instead of loop ---
# ❌ Bad
squares = []
for x in range(10):
    squares.append(x*x)

# ✅ Good
squares = [x*x for x in range(10)]

# --- 8. Use with for files ---
# ❌ Bad
f = open("file.txt")
data = f.read()
f.close()

# ✅ Good
with open("file.txt") as f:
    data = f.read()

# --- 9. Avoid deeply nested code ---
# ❌ Bad
if x:
    if y:
        if z:
            do_something()

# ✅ Good
if not x or not y or not z:
    return

do_something()

# --- 10. Use enumerations ---
# ❌ Bad
if status == "open":
    ...
elif status == "closed":
    ...

# ✅ Good
from enum import Enum
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"

if status == Status.OPEN:
    ...

# --- 11. Use generators for large data ---
# ❌ Bad
def get_numbers():
    return [x for x in range(1000000)]

# ✅ Good
def get_numbers():
    for x in range(1000000):
        yield x

# --- 12. Use Counter ---
# ❌ Bad
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

# ✅ Good
from collections import Counter
counts = Counter(items)

# --- 13. Use defaultdict ---
# ❌ Bad
grouped = {}
for key, value in data:
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(value)

# ✅ Good
from collections import defaultdict
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)

# --- 14. Avoid redundant ifs ---
# ❌ Bad
if x == True:
    ...

# ✅ Good
if x:
    ...

# --- 15. Use constants ---
# ❌ Bad
if role == "admin":
    ...

# ✅ Good
ROLE_ADMIN = "admin"
if role == ROLE_ADMIN:
    ...

# --- 16. Use dataclass ---
# ❌ Bad
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ✅ Good
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

# --- 17. Use comprehensions for dicts/sets ---
# ❌ Bad
squared = {}
for x in range(10):
    squared[x] = x*x

# ✅ Good
squared = {x: x*x for x in range(10)}

# --- 18. Use built-in functions ---
# ❌ Bad
result = []
for x in data:
    result.append(str(x))

# ✅ Good
result = list(map(str, data))

# --- 19. Use zip ---
# ❌ Bad
for i in range(len(names)):
    print(names[i], ages[i])

# ✅ Good
for name, age in zip(names, ages):
    print(name, age)

# --- 20. Use "any" and "all" ---
# ❌ Bad
found = False
for x in data:
    if x > 10:
        found = True

# ✅ Good
found = any(x > 10 for x in data)



# ... (continue to 50+ examples)