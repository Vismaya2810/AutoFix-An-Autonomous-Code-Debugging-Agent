from executor import execute_code
from error_classifier import classify_error

buggy_code = """
def divide(a, b):
    return a / b

print(divide(10, 0))
"""
result = execute_code(buggy_code)

if result["success"]:
    print("Code ran successfully")
else:
    print("Error detected")

    error_info = classify_error(result["error"])
    print("Classified error:", error_info)