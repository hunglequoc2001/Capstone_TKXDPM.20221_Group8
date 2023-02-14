import requests
import json
import hashlib
class Interbank:
    def __init__(self,baseurl):
        self.baseurl=baseurl
    def interbankPayment(self,cardCode, owner,cvvCode,dateExpired,command,transactionContent,amount,createdAt,appCode="",secretKey=""):
        return True
        data={"secretKey":secretKey,
            "transaction":{
                "cardCode":cardCode,
                "owner":owner,
                "cvvCode":cvvCode,
                "dateExpired":dateExpired,
                "command":command,
                "transactionContent":transactionContent,
                "amount":amount,
                "createdAt":createdAt
            }
        }
        encode=json.dumps(data).encode()
        md5=hashlib.md5()
        md5.update(encode)
        md5_hash=md5.hexdigest()
        body={
            'version':'1.0.1',
            "secretKey":secretKey,
            "transaction":{
                "cardCode":cardCode,
                "owner":owner,
                "cvvCode":cvvCode,
                "dateExpired":dateExpired,
                "command":command,
                "transactionContent":transactionContent,
                "amount":amount,
                "createdAt":createdAt
            },
            'appCode':appCode,
            'hashCode':md5_hash,
        }
        response= requests.patch(self.baseurl+'/api/card/processTransaction',data=body)
        return response
    def interbankReset(self,cardCode, owner, cvvCode, dateExpired):
        body={
            'cardCode':cardCode,
            'owner':owner,
            'cvvCode':cvvCode,
            'dateExpired':dateExpired
        }
        response=requests.patch(self.baseurl+'/api/card/reset-balance',data=body)
        return response
        
        
        """self.url="https://ecopark-system-api.herokuapp.com/"

        body={
            "version":"1.0.1",
            "transaction":{
                "cardCode":"",
                "owner":"",
                "cvvCode":"",
                "dateExpired":"",
                "command":"",
                "transactionContent":"",
                "amount":"",
                "createdAt":""
            },
            "appCode":"",
            "hashcode":""
        }
        data=json.dumps(dictionary)
        md5=hashlib.md5()
        print
        md5.update(data.encode())

        #request=requests.get("https://ecopark-system-api.herokuapp.com/api/card/processTransaction")
        #print(request.status_code)"""