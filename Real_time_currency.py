def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) :
  
    # importing required libraries
    import requests, json
  
    # base_url variable store base url 
    base_url = 'http://data.fixer.io/api/latest?access_key=7adaaa4eb2b8a810b661622e746eaf40'
  
    # main_url variable store complete url
    main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key
  
    # get method of requests module 
    # return response object 
    req_ob = requests.get(main_url)
  
    # json method return json format
    # data into python dictionary data type.
      
    # result contains list of nested dictionaries
    result = req_ob.json()
  
    print(" Result before parsing the json data :\n", result)
  
      
    print("\n After parsing : \n Realtime Currency Exchange Rate for",
          result(["Realtime Currency Exchange Rate"]["2. From_Currency Name"]), "TO",
          result(["Realtime Currency Exchange Rate"]["4. To_Currency Name"]), "is",
          result(["Realtime Currency Exchange Rate"]['5. Exchange Rate']), to_currency)
  
# Driver code
if __name__ == "__main__" :
  
    # currency code
    from_currency = "USA"
    to_currency = "INR"
  
    # enter your api key here 
    api_key = "7adaaa4eb2b8a810b661622e746eaf40"
  
    # function calling
    RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)