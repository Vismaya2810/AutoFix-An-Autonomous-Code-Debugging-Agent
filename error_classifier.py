def classify_error(traceback_text: str):
    lines = traceback_text.strip().split("\n")
    last_line = lines[-1] # last line contains error message and error name
    error_type = last_line.split(":")[0]

    return {
        "error_type":error_type
    }