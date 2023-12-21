# PAP REST API

## Converting CSV to JSON
Run parse.py to convert the data.csv file into a JSON file.
Script takes in two arguments:
- path to the CSV file
- the key for sorting the data (`name`, `phone`, `email` or `address`)
```bash
python3 parse.py --file ./data/data.json name
```

## Running the REST API Server
Start the REST API server by executing main.py with the path to the JSON file.
```bash
python3 main.py --file ./data/data.json
```
The server will start on localhost (default port 5000).

## Testing the API

Get all users: 
```bash
curl http://localhost:5000/users
```

Get a specific user by email: 
```bash
curl http://localhost:5000/user/user@example.com
```

Add a new user:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe", "email":"john.doe@example.com", "phone":"123-456-7890", "address":"123 Main St"}' http://localhost:5000/user
```

Update a user:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"John Updated", "email":"john.doe@example.com", "phone":"987-654-3210", "address":"321 New St"}' http://localhost:5000/user/user@example.com
```

Delete a user:
```bash
curl -X DELETE http://localhost:5000/user/user@example.com
```
