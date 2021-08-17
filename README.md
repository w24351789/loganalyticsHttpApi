# loganalyticsHttpApi

## 概述

因應第三方PaaS服務無法透過安裝Agent的方式取得監控資訊，此時可以透過 API 取得第三方服務中的 log資訊，透過Azure Function定期call API 取得資訊後傳送至Log Analytics 進行後續分析。

## 步驟

1. Azure Function 定期按照Log間隔執行程式 
2. Model Function get api result 做為body
3. 取得Log Analytics space id 和Key
4. 將get 來的body post 到 Log Analytics

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74dc782b-580d-427c-ad2d-76bc98c6d357/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74dc782b-580d-427c-ad2d-76bc98c6d357/Untitled.png)

幣安API

[https://binance-docs.github.io/apidocs/spot/cn/#24hr](https://binance-docs.github.io/apidocs/spot/cn/#24hr)

範例程式github

[https://github.com/w24351789/loganalyticsHttpApi](https://github.com/w24351789/loganalyticsHttpApi)



## 參考資料

[https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
