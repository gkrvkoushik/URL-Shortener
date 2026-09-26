import uuid

#long url - short
#short url - long  

class URLShortener:
    def __init__(self):
        self.url_mapping={}
        self.uid_mapping={}

    def shorten_url(self,url):
        uid=uuid.uuid5(uuid.NAMESPACE_URL,url).int
        if uid in self.uid_mapping:
            return self.uid_mapping[uid]
        short_url="https://mytinyurl.com/"
        short_url+=self._generate_url(uid)
        self.url_mapping[short_url]=url
        self.uid_mapping[uid]=short_url
        return short_url

    def redirect(self,url):
        if url in self.url_mapping:
            return self.url_mapping[url]
        return None

    def _generate_url(self,uid):

        crc={}
        for i in range(0,10):
            crc[i]=f'{i}'

        it=0
        for i in range(10,36):
            crc[i]=chr(ord('a')+it)
            it+=1

        it=0
        for i in range(36,62):
            crc[i]=chr(ord('A')+it)
            it+=1

        ans=""

        while uid>0:
            rem=uid%62
            ans+=crc[rem]
            uid=uid//62

        return ans


