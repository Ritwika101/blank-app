import streamlit as st
import networkx as nx

# Define the graph of Bhubaneswar tourist places
G = nx.Graph()

# Sample data: Nodes (places) and weighted edges (distances)
places = ["Lingaraj Temple", "Nandankanan Zoo", "Udayagiri Caves", "Khandagiri Caves", "Dhauli", "ISKCON Temple", "Rajarani Temple"]
edges = [
    ("Lingaraj Temple", "Udayagiri Caves", 5),
    ("Udayagiri Caves", "Khandagiri Caves", 1),
    ("Khandagiri Caves", "Nandankanan Zoo", 10),
    ("Lingaraj Temple", "ISKCON Temple", 4),
    ("ISKCON Temple", "Rajarani Temple", 2),
    ("Rajarani Temple", "Dhauli", 8),
    ("Dhauli", "Nandankanan Zoo", 12),
    ("Udayagiri Caves", "Dhauli", 7)
]

# Add nodes and edges to the graph
G.add_nodes_from(places)
G.add_weighted_edges_from(edges)

# Streamlit UI
st.title("Travel Planner - Bhubaneswar")
st.write("Find the shortest route between popular tourist places in Bhubaneswar.")

# Dropdowns for source and destination selection
source = st.selectbox("Select Starting Location:", places)
destination = st.selectbox("Select Destination:", places)

if st.button("Find Route"):
    if source == destination:
        st.warning("Source and destination cannot be the same!")
    else:
        try:
            shortest_path = nx.shortest_path(G, source=source, target=destination, weight='weight')
            total_distance = nx.shortest_path_length(G, source=source, target=destination, weight='weight')
            
            st.success(f"Shortest Route: {' → '.join(shortest_path)}")
            st.info(f"Total Distance: {total_distance} km")
        except nx.NetworkXNoPath:
            st.error("No path found between the selected locations.")

# Display graph structure
st.write("### Travel Map")
st.graphviz_chart(nx.nx_pydot.to_pydot(G).to_string())
