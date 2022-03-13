import json
import sendmessage as tg
def analytics(name, f):
    server_name = str(name)
    with open(f) as json_file:
        data = json.load(json_file)
    
    download_speed = data['download'] / 1000000
    upload_speed = data['upload'] / 1000000
    ping = data['ping']
    server_location = str(data['server']['name'])
    server_country = str(data['server']['cc'])
    server_location += ", " + server_country
    server_isp = str(data['server']['sponsor'])
    timestamp = str(data['timestamp'])
    upload_data = data['bytes_sent'] / 1000000
    download_data = data['bytes_received'] / 1000000
    shared = str(data['share'])
    client_isp = str(data['client']['isp'])
    ip = str(data['client']['ip'])
    client_country = str(data['client']['country'])

    cap = """
    Server: {} 
    ISP: {} 
    IP: {} 
    Country: {} 
    Speedtest Server: {} 
    Speedtest Server Location: {} 
    ==============================
    Ping: {} ms 
    Upload: {} Mbps 
    Download: {} Mbps 
    Bytes Sent: {} MB 
    Bytes Received: {} MB 
    Shared Link: {} 
    Timestamp: {} 
    ==============================
    Powered by Central Speedtest by Frank Ruan.
    """.format(server_name, client_isp, ip, client_country, server_isp, server_location, str(ping), str(upload_speed), str(download_speed), str(upload_data), str(download_data), shared, timestamp)

    tg.send(cap, shared)

    return True
