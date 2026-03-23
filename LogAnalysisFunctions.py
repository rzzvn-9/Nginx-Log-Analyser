import re
from collections import Counter

class LogAnalyser:

    log_pattern = re.compile(
        r'^(?P<ip>\S+) '                     # IP
        r'(?P<ident>\S+) '                   # ident
        r'(?P<authuser>\S+) '                # auth user
        r'\[(?P<timestamp>[^\]]+)\] '        # [date]
        r'"(?P<request>[^"]*)" '             # "GET / HTTP/1.1"
        r'(?P<status>\d{3}) '                # status
        r'(?P<size>\S+) '                    # size
        r'"(?P<referer>[^"]*)" '             # referer
        r'"(?P<user_agent>[^"]*)"$'          # user-agent
    )

    def parse_log_line(self,line: str) -> dict | None:
        line = line.strip() # Clean blank spaces from the start and end
        match = self.log_pattern.match(line)

        if not match:
            return None

        data = match.groupdict()

        request_parts = data["request"].split()
        if len(request_parts) == 3:
            data["method"] = request_parts[0]
            data["path"] = request_parts[1]
            data["protocol"] = request_parts[2]
        else:
            data["method"] = None
            data["path"] = None
            data["protocol"] = None

        data["status"] = int(data["status"])
        data["size"] = 0 if data["size"] == "-" else int(data["size"])

        return data

    def create_log_dict(self,log_file_path: str) -> dict:
        i = 0
        log_dict = {}
        with open(log_file_path, "r", encoding="utf-8") as f:
            for l in f:
                log_dict[i] = self.parse_log_line(l)
                i = i + 1
        return log_dict

    def top5_ip_addresses(self,log_dict: dict) -> list:
        ip_addresses = []
        for item in log_dict:
            ip_addresses.append(log_dict[item]["ip"])
        # Return the 5 most common addresses
        return Counter(ip_addresses).most_common(5)

    def top5_requested_paths(self,log_dict: dict) -> list:
        r_paths = []
        for item in log_dict:
            try:
                r_paths.append(log_dict[item]["request"].split(" ")[1])
            except IndexError:
                continue
        # Return the 5 most common paths
        return Counter(r_paths).most_common(5)

    def top5_status_codes(self,log_dict: dict) -> list:
        status_codes = []
        for item in log_dict:
            try:
                status_codes.append(log_dict[item]["status"])
            except IndexError:
                continue
        # Return the 5 most common paths
        return Counter(status_codes).most_common(5)

    def top5_user_agent(self,log_dict: dict) -> list:
        user_agents = []
        for item in log_dict:
            try:
                user_agents.append(log_dict[item]["user_agent"])
            except IndexError:
                continue
        # Return the 5 most common paths
        return Counter(user_agents).most_common(5)

