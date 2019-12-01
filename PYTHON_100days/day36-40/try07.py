# redis

import redis

def main():
    client = redis.Redis(host='127.0.0.1', port=6379)
    client.set('username', 'admin')
    client.hset('student', 'name', 'hao')
    client.hset('student', 'age', 38)
    print(client.keys('*'))
    print(client.get('username'))
    print(client.hgetall('student'))

if __name__ == '__main__':
    main()
