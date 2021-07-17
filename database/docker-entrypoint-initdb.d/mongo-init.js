print("[START] Create collections ------------------------------------------------")

db = db.getSiblingDB('api_dev_db');
db.createUser(
  {
    user: 'interview',
    pwd: 'interview',
    roles: [{ role: 'readWrite', db: 'api_dev_db' }],
  },
);
db.createCollection('dogs');

print("[END] Create databases ------------------------------------------------")
