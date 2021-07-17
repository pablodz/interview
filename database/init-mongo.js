db.auth('admin', 'password')

db = db.getSiblingDB('webapp')

db.createUser({
    user: 'interview',
    pwd: 'interview',
    roles: [{
        role: 'readWrite',
        db: 'webapp'
    }],
});


db.createCollection('cats');
