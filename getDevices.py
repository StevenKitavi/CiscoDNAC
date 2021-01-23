def get_device_from_dnac(device_ip):
    response = requests.get(
        'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token',
    )