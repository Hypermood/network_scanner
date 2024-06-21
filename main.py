from gatherer import gatherer, threat_check

def main():
    connections = gatherer.get_network_connections()
    unique_ips = gatherer.get_unique_ips(connections)
    threat_reports = threat_check.check_threat_intelligence(unique_ips)

    print("Network Connections:", connections)
    print("Unique IPs:", unique_ips)
    print("Threat Reports:", threat_reports)

if __name__ == "__main__":
    main()