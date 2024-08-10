import json
from typing import List, Tuple
from jsonschema import Draft7Validator, exceptions


def format_error_message(errors: List[exceptions.ValidationError]) -> str:
    """Format the error messages from JSON validation."""
    return "\n".join(
        f"Validation failed at {'/'.join(map(str, error.path))}: {error.message}"
        for error in errors
    )

def format_validation_errors_st(error_message):
    # Remove any unwanted leading or trailing whitespace
    error_message = error_message.strip()
    
    # Check if there are validation errors
    if 'valid' in error_message:
        return "Metadata is valid according to Dublin Core schema."
    
    # Initialize the formatted message with a title
    formatted_message = "**Errors found in Metadata:**\n\n"
    
    # Split the message into individual validation errors
    errors = error_message.split('Validation failed at : ')
    
    # Iterate over each error and format it
    for error in errors[1:]:  # Skip thnote first item as it's the initial part of the string
        formatted_message += f"- **Validation failed at : {error.strip()}**\n"
    
    return formatted_message

def format_validation_errors_mt(error_message: str) -> str:
    # Check if the message contains 'Validation failed'
    if 'valid' in error_message:
        return "Metadata is valid according to METS schema."

    # Split the error message into lines
    error_lines = error_message.split('Validation failed at')

    # Initialize a dictionary to hold error details
    error_dict = {}

    for line in error_lines:
        if line.strip():  # Ignore empty lines
            # Split line into location and error details
            location, details = line.split(':', 1)
            location = location.strip()
            details = details.strip()

            # If the location is already in the dictionary, append the error
            if location in error_dict:
                error_dict[location].append(details)
            else:
                error_dict[location] = [details]

    # Build a readable error message
    formatted_message = "Errors found in Metadata:\n"
    for location, errors in error_dict.items():
        formatted_message += f"\n- At '{location}':\n"
        for error in errors:
            formatted_message += f"  * {error}\n"

    return formatted_message

def validate_json(meta_data: dict, schema_data: dict) -> str:
    """Validate a JSON file against a given schema."""
    try:
        validator = Draft7Validator(schema_data)
        errors = sorted(validator.iter_errors(meta_data), key=lambda e: e.path)

        if not errors:
            return "JSON is valid according to the schema."
        else:
            return f"Errors found in Metadata:\n{format_error_message(errors)}"
    
    except exceptions.SchemaError as e:
        return f"Schema Error: {e.message}"
    
    except json.JSONDecodeError as e:
        return f"JSON Decode Error: {e.msg}"
    
    except FileNotFoundError as e:
        return f"File not found: {e.filename}"
    
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


if __name__ == '__main__':
    json_file = '/content/invalid.json'
    schema_file = '/content/dc_schema.json'
    print(validate_json(json_file, schema_file))
