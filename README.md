# 🚀 RocketBox Orchestrator 10Gbps Fabric Demo

A virtualized orchestration environment designed to simulate a physical **10Gbps USB-C Fabric** based on the **RocketBox architecture**.

This Streamlit dashboard proves the viability and efficiency of local edge compute orchestration for processing sensitive AI data. By simulating severe localized hardware constraints and comparing them against a strict bandwidth bridge, this tool visually demonstrates how local processing is vastly superior to relying on cloud dependencies.

## 🎯 Project Goals

- **Visualize 10Gbps Data Flow**: Watch 1GB payloads dynamically route and partition across multiple local compute nodes.
- **Enforce Constraints**: Simulate actual edge-compute environments with strict throttles:
  - 4 Nodes (1 Master / 3 Workers)
  - 2 CPU Cores & 1.5GB RAM per node
  - Strict 1250 MB/s limit and 0.5ms node hopping latency.
- **Generate Telemetry**: Live performance logging compiles system overhead and transfer speeds into downloadable CSV reports to pair with recorded video demos.

## 📦 Installation

Ensure you have Python 3.9+ installed.

1. Navigate to the project directory:
```bash
cd rocketbox-orchestrator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Generating the Video Demo

To effectively use this application for stakeholder presentations (Damian):

1. Start the Streamlit server:
```bash
streamlit run app.py
```
2. Open your browser to `http://localhost:8501`.
3. Start your screen-recording software.
4. Click the primary **🚀 Run 1GB File Transfer Simulation** button.
5. Capture the dynamic node telemetry, showing the metrics bouncing off the top-end bandwidth and hardware limits.
6. Once completed, stop the recording and click the **📥 Download Telemetry Report (CSV)** button.
7. Package the video file alongside the generated `.csv` metrics sheet.

## 🛠️ Stack

- **[Streamlit](https://streamlit.io/)**: Main interactive dashboard interface
- **[Plotly Graph Objects](https://plotly.com/python/graph-objects/)**: Dynamic real-time Star Topology Network rendering
- **[Pandas](https://pandas.pydata.org/)**: Telemetry data structuring and CSV exporting
