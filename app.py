import json
import pandas as pd
import streamlit as st
from schema_validate import validate_json, format_validation_errors_st

# Set up page title and description
st.set_page_config(
    page_title='Metadata Validation App',
    layout='wide',
    initial_sidebar_state='collapsed',
    page_icon='📑'
)

# Set up title and description
# st.title('Metadata Management App')
st.markdown("<h1 style='text-align: center;'>Metadata Validation App</h1>", unsafe_allow_html=True)
st.subheader('Description')
st.markdown("""
            This application allows you to effortlessly validate your metadata files in JSON format. Simply upload your metadata file, and the app will automatically check it against a predefined schema, ensuring that your data is accurate and conforms to the required standards.
            """)

# Initialize slidebar
with st.sidebar:
    # File Upload Interface
    st.subheader("Metadata Upload")
    # File Upload Interface
    uploaded_file = st.file_uploader("Upload your metadata file", type=["json"])
    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1]
        if file_type == 'json':
            data = json.load(uploaded_file)
            # Declare session state variable for previewing metadata
            st.session_state['preview_meta_data'] = data


    # Use predefined schema
    st.subheader("Use predefined schema")
    predefined_schema_mets = st.checkbox("METS")
    predefined_schema_dc = st.checkbox("Dublin Core")

    if predefined_schema_mets:
        
        # load mets schema schema
        with open('schema/mets_schema.json', 'r', encoding='utf-8') as f:
            schema_mets = json.load(f)
            st.session_state['schema_mets'] = schema_mets

        # Validate mets data
        mets_val = validate_json(data, schema_mets)
        st.session_state['mets_val'] = mets_val

    elif predefined_schema_dc:

        # load dublin core schema
        with open('schema/dc_schema.json', 'r', encoding='utf-8') as f:
            schema_dc = json.load(f)
            st.session_state['schema_dc'] = schema_dc
    
        # Validate dv data
        mets_val = validate_json(data, schema_dc)
        st.session_state['mets_val'] = mets_val

    # Button to validate metadata
    validate_btn = st.button("Validate Metadata")
    if validate_btn:
        st.session_state['validate_btn'] = True
    else:
        st.session_state['validate_btn'] = False
    if not predefined_schema_dc and not predefined_schema_mets:
        st.warning("Please select a schema to validate your metadata.")

try:    
    if st.session_state['validate_btn']:
        if predefined_schema_dc:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Dublin Core Metadata Preview[JSON]')
                st.write(st.session_state['preview_meta_data'])
            # st.write(st.session_state['preview_meta_data'])
            # Convert metadata to dataframe
            df = pd.DataFrame.from_dict(st.session_state['preview_meta_data'], orient='index')
            with col2:
                st.subheader('Dublin Core Metadata Preview[DataFrame]')
                st.dataframe(df)
            
            cl1, cl2 = st.columns(2)
            with cl1:                
                st.subheader('Dublin Core Schema Preview[JSON]')
                sc = st.session_state['schema_dc']
                st.json(sc)
            # st.write(sc)
            with cl2:
                st.subheader('Dublin Core Schema Preview[DataFrame]')      
                # Extract properties into a DataFrame
                properties = sc["properties"]
                df_sc = pd.DataFrame.from_dict(properties, orient='index')
                st.dataframe(df_sc)

            _ , res_cl, _ = st.columns(3)
            with res_cl:
                st.title('Validation Result')
                st.markdown(format_validation_errors_st(st.session_state['mets_val']))

        elif predefined_schema_mets:
            st.subheader('METS Metadata Preview[JSON]')
            st.json(st.session_state['preview_meta_data'])

            st.subheader('METS Core Schema Preview[JSON]')
            sc = st.session_state['schema_mets']
            st.json(sc)

            st.title('Validation Result')
            st.markdown(st.session_state['mets_val'])

except KeyError:
    pass
