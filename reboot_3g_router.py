import requests

router_ip = "192.168.1.1"
headers = {	"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate", 
		"Referer": "http://192.168.1.1/html/home.htm", 
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
		"X-Requested-With": "XMLHttpRequest", 
		"Content-Length": "112", 
		"Connection": "close"
}

sess = requests.Session()
payload = "<?xml version='1.0' encoding='UTF-8'?><request><Username>admin</Username><Password>YWRtaW4=</Password></request>"
request = sess.post("http://" + router_ip + "/api/user/login", headers=headers, data=payload)

if "<response>OK</response>" in request.text:
	headers["Content-Length"] = "77"
	payload = "<?xml version='1.0' encoding='UTF-8'?><request><Control>1</Control></request>"
	request = sess.post("http://" + router_ip + "/api/device/control", headers=headers, data=payload)
