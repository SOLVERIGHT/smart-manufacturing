## 🚀 Smart Factory OEE Analytics

### 🛠️ Tech Stack
- Databricks, Delta Lake, Databricks SQL, Azure Event Hub

### 📌 Highlights
- Built OEE analytics pipeline using Medallion Architecture
- Calculated Availability, Performance, and Quality KPIs
- Developed Databricks SQL dashboards for production monitoring
- Automated ETL with Delta Lake
  
### 📊 Dashboard Preview
<img width="1181" height="735" alt="image" src="https://github.com/user-attachments/assets/284732f5-14db-418f-82e6-290f24ca09e6" />

### 🏗️ Solution Architecture
```mermaid
flowchart TB

    subgraph OT["Operational Technology"]
        OPC["OPC UA Simulator"]
        KEP["Kepware"]
    end

    subgraph Ingestion[" "]
        EH["Azure Event Hub"]
        STREAM["Databricks Structured Streaming"]
    end

    subgraph Lakehouse["Databricks Lakehouse"]
        Bronze["Bronze<br/>Raw Telemetry"]
        Silver["Silver<br/>Curated Telemetry"]
        Gold["Gold<br/>Production KPIs"]
    end

    subgraph Analytics["Analytics"]
        OEE["OEE Dashboard"]
        Downtime["Downtime Analysis"]
        Throughput["Throughput Metrics"]
        Quality["Quality KPIs"]
    end

    OPC --> KEP
    KEP --> EH
    EH --> STREAM

    STREAM --> Bronze
    Bronze --> Silver
    Silver --> Gold

    Gold --> OEE
    Gold --> Downtime
    Gold --> Throughput
    Gold --> Quality
```
