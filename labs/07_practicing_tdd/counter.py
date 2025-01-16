from flask import Flask
import status

app = Flask(__name__)

COUNTERS = {}

@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Creates a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS

    if name in COUNTERS: # Checks if counters exist
        return {"message":f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return { name: COUNTERS[name] }, status.HTTP_201_CREATED

@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Checks if there's an existing counter by name to update"""
    app.logger.info(f"Request to update counters: {name}")
    
    global COUNTERS
    COUNTERS[name] += 1

    app.logger.info(f"Counter: {name} is now {COUNTERS[name]}")
    return { name: COUNTERS[name] }, status.HTTP_200_OK

@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """It should read a counter"""
    app.logger.info(f"Request to read counter: {name}")

    counter = COUNTERS[name]

    app.logger.info(f"Counter: {name} is {counter}")
    return { name: counter }, status.HTTP_200_OK

@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """It should delete a counter by name"""
    app.logger.info(f"Request to delete counter: {name}")

    del(COUNTERS[name])

    app.logger.info(f"Counter: {name} has been deleted")
    return '', status.HTTP_204_NO_CONTENT