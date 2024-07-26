import streamlit as st
import requests

from flask import Flask,request,jsonify,render_template
app = Flask(__name__)
import currencyapicom

client = currencyapicom.Client('cur_live_uMDMy3Yq0QRIwyJYxD0Yu5P63p5PTE5RDB4KTysE')


@app.route('/',methods = ['POST','GET'])
def index():
    if request.is_json:
        data = request.get_json()
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        cv = fetch_conv_factor(source_currency,target_currency)
        final_amount = round(cv*amount,2)
        # print("want to convert",source_currency,amount,"to" ,target_currency)
        # print("Answer is ",final_amount)
        response = {
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
        }
        return jsonify(response)
def main():
    st.set_page_config(page_title="Currency Converter Chatbot", page_icon="💱", layout="centered")
    custom_css = """
       <style>
       #MainMenu {visibility: hidden;}
       footer {visibility: hidden;}
       .block-container {padding-top: 1rem !important;}
       h1 {margin-top: -0.5rem !important;}
       </style>"""
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("Currency Converter Chatbot")

    # CSS to inject contained in a string
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Your chatbot iframe URL
    chatbot_url = "YOUR_CHATBOT_IFRAME_URL_HERE"

    # Embed the iframe using HTML
    st.markdown(f'<iframe src="https://console.dialogflow.com/api-client/demo/embedded/93cd30a7-8d34-4012-91b0-c7fe25a6c846" width="100%" height="500" style="border: none;"></iframe>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("Currency Converter Chatbot, July 2024. Made with ❤️ by Lakshya")

if __name__ == "__main__":
    main()
