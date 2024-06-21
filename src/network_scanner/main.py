from src.network_scanner import gatherer
from src.network_scanner import threat_check


def main():
    connections = gatherer.get_network_connections()
    unique_ips = gatherer.get_unique_ips(connections)
    threat_reports = threat_check.check_threat_intelligence(unique_ips)


if __name__ == "__main__":
    main()