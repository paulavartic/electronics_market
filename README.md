Django Electronics Sales Network

A Django-based application for managing a hierarchical network of electronics sales, including factories, retail stores, and individual entrepreneurs. The project supports an admin panel for managing the network and a RESTful API for interacting with the data programmatically.

---

Features

- Hierarchical Network Management:
  - Supports three levels: factories, retail stores, and individual entrepreneurs.
  - Each node references its supplier and tracks hierarchical levels dynamically.
  
- Admin Panel:
  - Create, update, and delete network nodes.
  - Filter nodes by city or country.
  - Clear debts using a custom admin action.
  - Display links to supplier nodes for easy navigation.

- RESTful API:
  - Full CRUD functionality for managing nodes.
  - Supports filtering by country and searching by city.
  - Ensures debts are read-only in the API.
  - Restricts access to authenticated and active users.

---

Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework (DRF)
- Django Filters

---

Installation

1. Clone the Repository:
   git clone https://github.com/your-username/electronics-sales-network.git
   cd electronics-sales-network
2. Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies:
   pip install -r requirements.txt
4. Apply Migrations:
   python manage.py migrate
5. Run the Development Server:
   python manage.py runserver
6. Access the App:
Admin Panel: http://127.0.0.1:8000/admin
