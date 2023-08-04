## Usage
### On the server side:
Clone:
`git clone https://github.com/marianna13/tracker.git`.

Start the server with uvicorn
```
cd tracker && uvicorn main:app --reload
```

### On the client side:

```python
from tracker import Tracker

client = Tracker('http://127.0.0.1:8000')
client.add(item='s3://commoncrawl/crawl-data/CC-MAIN-2023-23', status='processing')

# Check if item exists in the tracker:

print(client.get_item('s3://commoncrawl/crawl-data/CC-MAIN-2023-23')) # True

# Update status:

client.update(item='s3://commoncrawl/crawl-data/CC-MAIN-2023-23', status='completed')
```
