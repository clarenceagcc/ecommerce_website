from app import app, db
from app.models import User, Product, Order

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add sample users
        user1 = User(username='john_doe', email='john@example.com', password='password123')
        user2 = User(username='jane_doe', email='jane@example.com', password='password123')
        db.session.add(user1)
        db.session.add(user2)

        # Add sample products
        product1 = Product(name='Laptop', price=999.99, description='A high-performance laptop.')
        product2 = Product(name='Smartphone', price=499.99, description='A latest-generation smartphone.')
        db.session.add(product1)
        db.session.add(product2)

        # Commit changes
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()