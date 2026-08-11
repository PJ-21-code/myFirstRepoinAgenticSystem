import random
from datetime import datetime, timezone
import json

records = {
    "amazon": {"status": "ready for pickup", "location": "gate number two"},
    "flipkart": {"status": "held", "location": "hostel desk"},
}

def create_trace_id():
    return random.randint(1000,10000)

def log_event(trace_id, step, message, log):
    # TODO: build a JSON-serializable record with trace_id, ISO timestamp, step, message
    # TODO: append it to `log`
    timestamp= datetime.now(timezone.utc).isoformat()
    log.append(
        {"trace ID": trace_id, "TIMESTAMP": timestamp, "Record info": message}
    )


def handle_query(retailer, log):
    # TODO: implement retrieve -> reason -> act using the same trace_id for all three steps
    # TODO: return the final response string
    trace_id= create_trace_id()
    if retailer in records:   
        message= f"{retailer} parcel is {records[retailer]['status']} at {records[retailer]['location']}"
    else:
        message= f"{retailer} parcel not found!"

    log_event(trace_id=trace_id,step=1,message=message,log=log) 

    if retailer in records:
        reason= f"Parcel is found and its current status is {records[retailer]['status']}"
    else:
        reason= f"{retailer} parcel not found!"

    log_event(trace_id=trace_id,step=2,message=f"Reasoning: {reason}",log=log)

    if retailer in records:
        response= message
    else:
        response=f"Sorry I cannot find {retailer} parcel" 

    log_event(trace_id=trace_id,step=3,message=f"Final response: {response}", log=log) 

    return response             

if __name__ == "__main__":
    log = []
    print(handle_query("amazon", log))
    print(handle_query("mintra", log))

    with open("tracing_parcel.log","a") as f:
        for event in log:
            f.write(json.dumps(event)+ "\n")
    

    
