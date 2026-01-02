import json
import random

with open('resources/questions/questions.json', 'r', encoding='utf-8') as f:
    tests = json.load(f)

print(f"Jami {len(tests)} ta savol mavjud\n")

random_test = random.choice(tests)
print(f"Savol #{random_test['id']}: {random_test['question']}\n")

for i, choice in enumerate(random_test['choises'], 1):
    print(f"{i}. {choice['text']}")

print(f"\nTo'g'ri javob: ", end="")
for i, choice in enumerate(random_test['choises'], 1):
    if choice['answer']:
        print(f"{i}-variant")
        break

if random_test['media']['exist']:
    print(f"\nRasm: public/images/{random_test['media']['name']}.png")

print(f"\nIzoh: {random_test['description'][:100]}...")

media_count = sum(1 for t in tests if t['media']['exist'])
print(f"\n\nStatistika:")
print(f"- Jami savollar: {len(tests)}")
print(f"- Rasmi bor savollar: {media_count}")
print(f"- Rasmsiz savollar: {len(tests) - media_count}")
