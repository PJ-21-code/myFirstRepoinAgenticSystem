import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout
from typing import TypedDict,List,Dict,Any
from langgraph.graph import StateGraph,START,END


def fake_status_api(request_text: str):
    time.sleep(3)
    return {'status':'success'}

class StatusState(TypedDict):
    request: str
    api_status: Dict[str,Any]
    result: str
    trace: List[str]
    error: str

def run_with_timeout(fn, seconds: float,*args):
    with ThreadPoolExecutor(max_workers=1) as pool:
        future= pool.submit(fn,*args)
        return future.result(timeout=seconds)

def understand_request(state: StatusState):
    cleaned = state["request"].strip()  # Clean spaces
    return {
        "request": cleaned, 
        "trace": state["trace"] + ["understand_request"],  
        "error": "",  # Clear old errors at the start
    }

def fetch_status(state):
    try:  # Attempt the timed API call
        status = run_with_timeout(fake_status_api, 1.0, state["request"])  # 1 second limit
        return {
            "api_status": status,  # Save API payload
            "trace": state["trace"] + ["fetch_status"],  # Log success path
            "error": "",  # No error
        }
    except FutureTimeout:  # Timer rang before the API finished
        return {
            "api_status": "",  # No useful payload
            "trace": state["trace"] + ["fetch_status"],  # Still record the attempt
            "error": "Status service took too long. Please try again in a minute.",  # User-facing timeout message
        }

def write_result(state):
    if state["error"]:  
        message = state["error"]  
    elif state["api_status"]:  
        message = "Campus desk status: " + state["api_status"]  
    else:  
        message = "Could not read campus desk status."  
    return {
        "result": message,  
        "trace": state["trace"] + ["write_result"],  
    }

builder = StateGraph(StatusState)  
builder.add_node("understand_request", understand_request)  
builder.add_node("fetch_status", fetch_status)  
builder.add_node("write_result", write_result) 
builder.add_edge(START, "understand_request")  
builder.add_edge("understand_request", "fetch_status")  
builder.add_edge("fetch_status", "write_result")  
builder.add_edge("write_result", END)  


graph = builder.compile()

def solve(initial_state):
    final_state = graph.invoke(
      initial_state
    )

    return {
        "TRACE": final_state['trace'],
        "ERROR": final_state['error'],
        "RESULT": final_state['result']
    }

if __name__ == "__main__":
    sample_input = {
            "request": "Is the scholarship desk open?",  
            "api_status": "",  
            "result": "",  
            "trace": [],  
            "error": "",  
         }
    print(solve(sample_input))
