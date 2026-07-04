import json
import re
from typing import Tuple

REQUIRED_KEYS = ["category", "priority", "summary", "needs_human", "suggested_reply"]
ALLOWED_CATEGORIES = {"billing", "shipping", "product", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def strip_markdown_fences(text: str) -> str:
    cleaned = text.strip()
    match = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", cleaned, flags=re.IGNORECASE)
    return match.group(1).strip() if match else cleaned


def extract_json_object(text: str) -> str:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object braces found in model output.")
    return text[start : end + 1]


def safe_parse_model_json(raw: str) -> dict:
    step1 = strip_markdown_fences(raw)
    step2 = extract_json_object(step1)
    data = json.loads(step2)
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON must be an object (dict).")
    return data


# TODO: Implement validate_ticket
def validate_ticket(data: dict) -> tuple[bool, str]:
  for key in REQUIRED_KEYS:
    if key not in data:
        return False, f"Missing Required field: {key}"
  if data['category'] not in ALLOWED_CATEGORIES:
      return False, f"Unidentified category: {data['category']}"
  if data['priority'] not in ALLOWED_PRIORITIES:
      return False, f"Wrong Priority: {data['priority']}"
  if not isinstance(data['summary'], str) or len(data['summary'].strip()) <5:
      return False, "Not valid summary of data"
  if not isinstance(data['needs_human'],bool):
      return False, "Invalid type of data for this needs_human field"
     
  return True, "ok"
  
     


# TODO: Implement validate_or_raise
def validate_or_raise(data: dict) -> tuple[dict,str]:
  ok, message = validate_ticket(data)
  if not ok:
    return ValueError(message), '\n\n Invalid Ticket-FAILED'
  if ok:
    return data, '\n\n Valid Ticket-SUCCESS'


TEST_CASES = [
    # Case 1 — valid ticket (should print SUCCESS)
    '{"category": "shipping", "priority": "medium", "summary": "Order 4412 arrived late", '
    '"needs_human": false, "suggested_reply": "We are tracking your parcel."}',
    # Case 2 — wrong priority casing (should print FAILED)
    '{"category": "billing", "priority": "HIGH", "summary": "Duplicate charge", '
    '"needs_human": false, "suggested_reply": "Refund initiated."}',
]


# TODO: Implement main
def main() -> None:
   for case in TEST_CASES:
      final_dict= safe_parse_model_json(case)
      print(validate_or_raise(final_dict))


if __name__ == "__main__":
    main()
