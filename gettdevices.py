import requests

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZjhlYjhhZDc1MTYxMjRlODczYTg0YmYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYxMTQxMDc3NiwiaWF0IjoxNjExNDA3MTc2LCJqdGkiOiJmMWI1NDZjZi0xNTg1LTQxZjMtYjhkZC0wOWQ0MDM5NWFkOWYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.mL0CETD1UBO9LU8TOq3ZH0Wgf3qQnH_9BIpenD4T-M0c_4Gkg1ja7LuKDLYPSB9hhqwgLSRvnS-5Az8KNFTzqdRGawLkaCEnjgHCJEhqMbSi58FN9K6tk_diUNpS5KKZ3UzEChgxF6-KaI2DntFVY9qKmDBTqLoVuYISY0rNy47QhHGsk0OMWkHGpybAVl2nOswrtEcpmMFiG95opFL-BS-hwu5rNxx98bUl5caSRLdrzjI11kwydYU8Ly_z0shLU6PCIzoaRCmHuOTd7nxoe0k9pfN_PBEFSynWZskbxK41SXodtYurlwFDfp8050CW4xw1GQIkGIBXeApeEnI19w',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
