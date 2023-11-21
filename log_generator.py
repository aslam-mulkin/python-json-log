import json
import random
import time

def generate_apache_log():
    timestamp = time.strftime('%d/%b/%Y:%H:%M:%S %z')
    ip_address = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    # Generate a random HTTP status code
    http_status_codes = [200, 401, 403, 404, 500, 501, 503]
    status_code = random.choice(http_status_codes)

    log_entry = f'{ip_address} - - [{timestamp}] "GET /" {status_code} - "{user_agent}"'
    json_log = {'log_entry': log_entry}

    # Print JSON log to stdout
    print(json.dumps(json_log))

if __name__ == '__main__':
    while True:
        generate_apache_log()
        time.sleep(5)
