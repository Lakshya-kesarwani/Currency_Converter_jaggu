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
    else:
        return render_template("index.html")
def fetch_conv_factor(source,target):
    result = client.latest(source, currencies=[target])
    value = result['data'][target]['value']
    return value
fetch_conv_factor('GBP','INR')
if __name__ == "__main__":
    app.run(debug=True)
