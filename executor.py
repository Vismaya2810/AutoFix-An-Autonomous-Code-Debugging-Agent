import traceback

def execute_code(code: str):
    try:
        exec(code, {})

        return{
            "success": True,
            error: None
        }
    except Exception:
        error_trace = traceback.format_exc()
        return {
            "success": False,
            "error":error_trace
        }