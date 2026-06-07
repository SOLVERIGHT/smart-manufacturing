## 🚀 Smart Factory OEE Analytics

### Tech Stack
- Databricks, Delta Lake, Databricks SQL, Azure Event Hub
<hr>

### Highlights
- Built OEE analytics pipeline using Medallion Architecture
- Calculated Availability, Performance, and Quality KPIs
- Developed Databricks SQL dashboards for production monitoring
- Automated ETL with Delta Lake
  
### Dashboard Preview
<img width="1181" height="735" alt="image" src="https://github.com/user-attachments/assets/284732f5-14db-418f-82e6-290f24ca09e6" />

### Solution Architecture
```mermaid
flowchart TB

    subgraph ShopFloor["Shop Floor"]
        Sensors["Sensors"]
        PLC["PLC / SCADA"]
        MES["MES"]
        Quality["Quality Logs"]
        Downtime["Downtime Logs"]
    end

    subgraph Ingestion["Ingestion"]
        EventHub["Kafka / Event Hub"]
        AutoLoader["Auto Loader"]
        Streaming["Structured Streaming"]
    end

    subgraph Lakehouse["Lakehouse"]
        Bronze["Bronze<br/>Raw Events"]
        Silver["Silver<br/>Production Data"]
        Gold["Gold<br/>OEE Metrics"]
    end

    subgraph Analytics["Analytics"]
        OEE["OEE Dashboard"]
        DowntimeRpt["Downtime Analysis"]
        YieldRpt["Yield Analysis"]
        CapacityRpt["Capacity View"]
    end

    Sensors --> EventHub
    PLC --> EventHub
    MES --> EventHub
    Quality --> AutoLoader
    Downtime --> AutoLoader

    EventHub --> Streaming
    AutoLoader --> Bronze
    Streaming --> Bronze

    Bronze --> Silver
    Silver --> Gold

    Gold --> OEE
    Gold --> DowntimeRpt
    Gold --> YieldRpt
    Gold --> CapacityRpt
```
