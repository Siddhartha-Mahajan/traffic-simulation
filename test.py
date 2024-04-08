import csv

def save_to_csv(nodes, links, filename):
    # Save nodes and links to CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'longitude', 'latitude'])  # Write header for nodes
        writer.writerows(nodes)  # Write node data
        writer.writerow([])  # Write empty row to separate nodes and links
        writer.writerow(['name', 'start_node_id', 'end_node_id', 'attribute1', 'attribute2'])  # Write header for links
        writer.writerows(links)  # Write link data

def read_from_csv(filename):
    nodes = []
    links = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        nodes_section = True  # Flag to determine if we are reading nodes or links
        for row in reader:
            if not row:  # Skip empty rows
                nodes_section = False
                continue
            if nodes_section:
                nodes.append([float(row[0]), float(row[1]), float(row[2])])
            else:
                links.append([row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4])])
    return nodes, links
