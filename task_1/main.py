from queue import Queue
import time

queue = Queue()
id = 1

def generate_request():
    global id
    queue.put(id)
    print("New request:", id)
    id += 1

def process_request():
    if queue.empty():
        print("Queue is empty")
        return
        
    req = queue.get()
    print("Processed request:", req)

def main():
    while True:
        generate_request()
        process_request()
        time.sleep(0.5)

        if id == 1000:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped")