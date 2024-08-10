# Metadata Validation App

This repository contains a Streamlit-based web application designed to validate metadata files in JSON format. The app checks your metadata against predefined schemas such as METS and Dublin Core, ensuring that your data meets the necessary standards and formats.

## Features

- **User-Friendly Interface**: A clean and intuitive interface for uploading and validating metadata files.
- **Schema Validation**: Automatically validate metadata against predefined schemas, including METS and Dublin Core.
- **Preview and Compare**: View both the metadata and the corresponding schema in JSON format and DataFrame format, allowing for easy comparison and analysis.
- **Validation Feedback**: Get detailed feedback on any validation errors or issues detected in your metadata.

## Installation

To run this app locally, you'll need to have Python installed. Follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload Metadata File**: Use the sidebar to upload your metadata file in JSON format.
2. **Select Schema**: Choose between METS or Dublin Core schemas for validation.
3. **Validate**: Click the "Validate Metadata" button to start the validation process.
4. **View Results**: The app will display your metadata and schema in both JSON and DataFrame formats, along with the validation results.

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- JSON
- `schema_validate` module for custom validation logic

## Customization

You can modify or add schemas by placing them in the `schema/` directory. The app is designed to easily extend validation capabilities for additional schemas.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
