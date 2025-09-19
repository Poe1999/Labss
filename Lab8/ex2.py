import re

def anal_log(log):
    ipadd = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    finding1 = re.findall(ipadd,log)
    for ip in finding1:
        print(f'{ip}')
    print()

    date_time = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    finding2 = re.findall(date_time,log)
    for dt in finding2:
        print(f"{dt}")
    print()

    uppercase = r'\b[A-ZА-Я]{1,}\b'
    finding3 = re.findall(uppercase,log)
    for up in finding3:
        print(f'{up}')
    print()

    email = r'\b[a-zA-Z0-9_-]+@[a-zA-Z]+\.[a-zA-Z]{2,}\b'
    protected = re.sub(email, '[EMAIL_POTECTED]',log)
    print(protected)

    return {'ip_add': finding1, 'date_time': finding2, 'up_words': finding3, 'emails': protected}


if __name__ == "__main__":
    # Пример лог-данных
    log = """
2023-01-15 10:30:45 [INFO] User with email user@example.com logged from IP 192.168.1.1
2023-01-15 10:31:12 [ERROR] Connection failed to 8.8.8.8 from admin@company.org
2023-01-15 10:32:05 [WARNING] High memory usage detected by MONITORING system
2023-01-15 10:33:20 [INFO] Backup completed successfully by BACKUP_SERVICE
2023-01-15 10:34:00 [DEBUG] Received request from 10.0.0.5, user: support@domain.net
SERVER RESTARTED at 2023-01-15 10:35:00 due to CRITICAL ERROR
"""
    asss = anal_log(log)
