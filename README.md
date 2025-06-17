# 📦 warhouse - Warehouse Management API

> **Universal warehouse API for managing stock, products, and locations. Built with Django + DRF.**

---

## 🧱 Features

- **Products**: SKU, variants, categories, unit types.
- **Warehouses**: Storage locations with unique codes.
- **Inventory**: Stock tracking per warehouse with minimum thresholds.
- **Docs**: Embedded HTML documentation for developers.

---

## 📡 Endpoints
### 🔐 Authentication
- *POST* /api/token/ - Obtain JWT access token
- *POST* /api/token/refresh/ - Refresh expired token
### 📦 Products
- *GET* /api/products/ - List products
- *POST* /api/products/ - Create product
- *GET* /api/products/<id>/ - View product details
### 🧱 Product Variants
- *GET* /api/product-variants/ - List variants
- *POST* /api/product-variants/ - Create variant with attributes
### 🏗️ Locations
- *GET* /api/locations/ - List hierarchical locations
- *POST* /api/locations/ - Create nested location (e.g., warehouse → shelf)
### 🏤 Warhouses
- *GET* /api/warehouses/ - List warehouses
### 🔄 Inventory
- *GET* /api/inventory/ - List inventory
- *POST* /api/movements/ - Register entry, exit, transfer, or adjustment
### 📦 Batches
- *GET* /api/batches/ - List product batches
- *POST* /api/batches/ - Create batch with lot number and expiration date
### 📝 Documentation
- *GET* /docs/ - Developer documentation

---

## 🔐 Authentication

This API uses **JWT tokens** for secure access. To use protected endpoints:

1. **Get a token**:
   ```bash
   POST /api/token/
   {
     "username": "your-username",
     "password": "your-password"
   }
   ```
2. **Use the token in protected endpoints:**:
   ```bash
   Authorization: Bearer <your-access-token>
   ```

2. **Refresh token when expired:**:
   ```bash
   POST /api/token/refresh/
   {
       "refresh": "<your-refresh-token>"
   }
   ```
**Tokens expire after 60 minutes (access) and 24 hours (refresh).**

---

## 📝 Documentation
Visit: http://localhost:8000/docs/

---

## 🚀 Future Features

- **Bulk Upload : Load inventory via CSV/Excel with validation and error reporting**
- **Webhooks : Notify external systems about stock changes or events**
- **Multi-Tenancy : Support multiple clients/companies in one instance**
- **GraphQL : Alternative query interface for complex requests**
- **Integration with e-commerce platforms**

---

## 🛠️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/sortegam29/warhouse_api.git 
cd warhouse_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Migrate and run server
python manage.py migrate
python manage.py runserver

```
## 📜 License
MIT

---

## 📌 Contributing
Contributions are welcome! Please read our contributing guidelines for details on how to contribute.

## 📬 Contact
For questions or feedback, reach out to sebastian.ortega29@inacapmail.cl or open an issue on GitHub.
