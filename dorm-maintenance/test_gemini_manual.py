
from requests_app.services.gemini import analyze_request

test_requests = [
    "My desk drawer is broken.",
    "The toilet on our floor is overflowing.",
    "Water is dripping onto an electrical outlet.",
    "My room's heater stopped working.",
    "There are cockroaches in the kitchen.",
    "The refrigerator is making a loud noise.",
    "My dorm room door won't lock.",
    "There is smoke coming from the ceiling."
]

for request in test_requests:
    print("\n" + "=" * 50)
    print("REQUEST:", request)

    try:
        result = analyze_request(request)

        print("CATEGORY:", result["category"])
        print("PRIORITY:", result["priority"])
        print("SAFETY FLAG:", result["safety_flag"])
        print("EXPLANATION:", result["explanation"])

    except Exception as error:
        print("ERROR:", error)
