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
- *GET* /api/products/ - List products
- *GET* /api/warehouses/ - List warehouses
- *GET* /api/inventory/ - List inventory
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
- **Batches & Expiration Dates**
- **Product Variants**
- **Webhooks & Events**
- **Integration with e-commerce platforms**

---

## 🛠️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/sortegam29/warhouse_api.git 
cd warhouse

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
