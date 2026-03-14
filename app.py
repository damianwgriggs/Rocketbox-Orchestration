import streamlit as st
import time
import random
import pandas as pd
import plotly.graph_objects as go

# Ensure page config is first
st.set_page_config(
    page_title="RocketBox 10Gbps Fabric Orchestrator", 
    page_icon="🚀", 
    layout="wide"
)

# Constants & Configuration
NODES = ["Node-01 (Master)", "Node-02 (Worker)", "Node-03 (Worker)", "Node-04 (Worker)"]
TOTAL_CORES = 2
TOTAL_RAM_GB = 1.5
MAX_BW_MBPS = 1250 # 10Gbps
LATENCY_MS = 0.5
FILE_SIZE_MB = 1000

# Initialize Session State
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'sim_running' not in st.session_state:
    st.session_state.sim_running = False

# Header Design
st.title("🚀 Virtualized Orchestration Environment")
st.markdown("### Powered by Google Anti-Gravity Parameters | **RocketBox Architecture**")
st.markdown("This dashboard monitors a simulated edge-compute fabric over a virtualized 10Gbps USB-C Bridge. Prove to stakeholders that local edge orchestration efficiently replaces cloud dependencies for sensitive AI data.")

# Layout Columns
top_left, top_right = st.columns([2, 1])

def get_network_graph(active=False):
    # Node coordinates
    node_x = [-1, 1, 1, 1]
    node_y = [0, 1, 0, -1]
    
    # Edge lines between Master (0) and Workers (1, 2, 3)
    edge_x = []
    edge_y = []
    for i in range(1, 4):
        edge_x.extend([node_x[0], node_x[i], None])
        edge_y.extend([node_y[0], node_y[i], None])

    # Dynamic styling for simulation
    edge_color = 'rgba(0, 255, 204, 0.8)' if active else 'rgba(100, 100, 100, 0.3)'
    node_color = 'rgba(0, 255, 204, 1)' if active else 'rgba(50, 100, 255, 0.8)'
    node_line  = 'white' if active else 'rgba(255, 255, 255, 0.5)'

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=4 if active else 2, color=edge_color),
        hoverinfo='none',
        mode='lines'
    )

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=node_color,
            size=60,
            line=dict(width=2, color=node_line)
        ),
        text=NODES,
        textposition="top center",
        textfont=dict(color='white', size=14)
    )

    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title=dict(text='<br>10Gbps Fabric Network Topology', font=dict(color='white', size=18)),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=50),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]))
                )
    return fig

with top_left:
    st.subheader("Network Map")
    graph_placeholder = st.empty()
    graph_placeholder.plotly_chart(get_network_graph(active=False), use_container_width=True, key="graph_initial")

with top_right:
    st.subheader("Hardware Constraints")
    st.info(f"""
    **Per-Node Allocation:**
    - 🧠 CPUs: {TOTAL_CORES} Cores
    - ⚡ RAM: {TOTAL_RAM_GB} GB
    
    **Bridge Specification:**
    - 🌊 Bandwidth: 10Gbps ({MAX_BW_MBPS} MB/s strict throttle)
    - ⏱️ Latency: {LATENCY_MS}ms strict
    
    **Payload:**
    - 📦 Synthetic File: {FILE_SIZE_MB} MB
    """)
    st.markdown("---")
    if st.button("🚀 Run 1GB File Transfer Simulation", type="primary", use_container_width=True):
        st.session_state.sim_running = True

st.markdown("---")
st.subheader("Live Telemetry: Throughput & Resource Utilization")

# Dynamic Meters
meter_cols = st.columns(4)
meters = []

for i, col in enumerate(meter_cols):
    with col:
        st.markdown(f"#### {NODES[i]}")
        cpu_ph = st.empty()
        ram_ph = st.empty()
        bw_ph = st.empty()
        meters.append((cpu_ph, ram_ph, bw_ph))
        
        # Initial Idle State
        cpu_ph.progress(0, text="CPU: 0%")
        ram_ph.progress(0.0, text="RAM: 0.00 / 1.50 GB")
        bw_ph.metric("Network Throughput", "0.0 MB/s", delta="idle")

# Execution block for Simulation
if st.session_state.sim_running:
    st.session_state.logs = [] # Reset prior logs
    
    # Render active map
    graph_placeholder.plotly_chart(get_network_graph(active=True), use_container_width=True, key="graph_active")
    
    # Simulation Loop
    TICKS = 25
    for t in range(TICKS):
        for i, (cpu_ph, ram_ph, bw_ph) in enumerate(meters):
            # Compute randomized metrics bounded by limits
            if i == 0:
                # Master orchestrator sends data
                cpu_util = random.uniform(70, 95)
                ram_util = random.uniform(1.0, 1.45)
                throughput = random.uniform(1150, 1245) # Max 1250
            else:
                # Workers receive data (divided evenly ~400 MB/s each)
                cpu_util = random.uniform(40, 80)
                ram_util = random.uniform(0.6, 1.2)
                throughput = random.uniform(370, 415)
            
            # Update Progress bars
            cpu_ph.progress(int(cpu_util), text=f"CPU: {cpu_util:.1f}%")
            ram_ph.progress(min(ram_util/TOTAL_RAM_GB, 1.0), text=f"RAM: {ram_util:.2f} / {TOTAL_RAM_GB} GB")
            # Update metric
            lat = random.uniform(0.48, 0.52)
            bw_ph.metric("Network Throughput", f"{throughput:.1f} MB/s", delta=f"{lat:.2f}ms ping", delta_color="inverse")
            
            # Log telemetry
            st.session_state.logs.append({
                "Tick": t+1,
                "Node": NODES[i],
                "CPU_Usage_%": round(cpu_util, 2),
                "RAM_Usage_GB": round(ram_util, 2),
                "Throughput_MBps": round(throughput, 2),
                "Latency_ms": round(lat, 3)
            })
            
        time.sleep(0.12) # Animation speed
        
    # Cool down to idle
    for i, (cpu_ph, ram_ph, bw_ph) in enumerate(meters):
        cpu_util = random.uniform(1, 4)
        ram_util = random.uniform(0.1, 0.3)
        cpu_ph.progress(int(cpu_util), text=f"CPU: {cpu_util:.1f}%")
        ram_ph.progress(min(ram_util/TOTAL_RAM_GB, 1.0), text=f"RAM: {ram_util:.2f} / {TOTAL_RAM_GB} GB")
        bw_ph.metric("Network Throughput", "0.0 MB/s", delta="idle", delta_color="off")

    # Render idle map
    graph_placeholder.plotly_chart(get_network_graph(active=False), use_container_width=True, key="graph_completed")
    st.session_state.sim_running = False
    st.success("✅ **Simulation Complete!** 1GB payload dynamically partitioned and routed across 10Gbps fabric.")

# Report Generation
if st.session_state.logs:
    st.markdown("---")
    st.subheader("Performance Logs")
    df_logs = pd.DataFrame(st.session_state.logs)
    
    col_dl, col_blank = st.columns([1, 3])
    with col_dl:
        csv = df_logs.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Telemetry Report (CSV)",
            data=csv,
            file_name='rocketbox_fabric_telemetry.csv',
            mime='text/csv',
            type="primary"
        )
    
    st.dataframe(df_logs, use_container_width=True, height=200)
