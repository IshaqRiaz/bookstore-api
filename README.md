Got it — you want the **same structure pattern as your Portfolio README**, just with emojis added cleanly and no duplication or extra changes.

Here is your **final clean README.md version (copy-paste ready):**

````markdown
# 📚 Bookstore API

A simple RESTful API for managing a book collection. Built with Flask and SQLAlchemy.

```

## ✨ Features

- 📖 **Book Management** – Store and manage book records
- ➕ **Create Books** – Add new books to the collection
- 📚 **Get All Books** – Retrieve all available books
- 🔍 **Get Single Book** – Fetch book details by ID
- ✏️ **Update Book** – Modify existing book information
- 🗑️ **Delete Book** – Remove books from the database
- 🗄️ **SQLite Database** – Lightweight local database
- 🌐 **RESTful API Design** – Clean and structured endpoints

```

## 🛠️ Technologies Used

- 🐍 **Python 3.x**
- 🌶️ **Flask** – Web framework
- 🗃️ **Flask-SQLAlchemy** – Database ORM
- 💾 **SQLite** – Database
- 🔐 **python-dotenv** – Environment variables

```

## 🚀 How to Run Locally

### 📋 Prerequisites

- 🐍 Python 3.x installed
- 📦 pip (Python package manager)

```

### 📝 Steps

### 1️⃣ Clone the repository

```bash
git clone
cd bookstore-api
````

```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

```

### 4️⃣ Create .env file

```env
DATABASE_URL=sqlite:///books.db
```

```

### 5️⃣ Run the application

```bash
python app.py
```

```

### 6️⃣ Access API

```text
http://127.0.0.1:5000/books
```

```

## 📡 API Endpoints

```

### ➕ Create a Book

**POST** `/books`

#### 📥 Request

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 15.99,
  "isbn": "9780735211292",
  "publishedDate": "2018-10-16"
}
```

#### 📤 Response (201 ✅)

```json
{
  "id": 1
}
```

---

### 📚 Get All Books

**GET** `/books`

#### 📤 Response (200 ✅)

```json
[
  {
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 15.99,
    "isbn": "9780735211292",
    "publishedDate": "2018-10-16"
  }
]
```

```

### 🔍 Get Book by ID

**GET** `/books/{id}`

#### 📤 Response (200 ✅)

```json
{
  "id": 1,
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 15.99,
  "isbn": "9780735211292",
  "publishedDate": "2018-10-16"
}
```

#### ❌ Not Found (404)

```json
{
  "error": "Book not found"
}
```

---

### ✏️ Update Book

**PUT** `/books/{id}`

#### 📥 Request

```json
{
  "price": 12.99
}
```

#### 📤 Response (200 ✅)

```json
{
  "message": "Updated"
}
```

---

### 🗑️ Delete Book

**DELETE** `/books/{id}`

#### 📤 Response (200 ✅)

```json
{
  "message": "Deleted"
}
```

```

## 🧪 Testing with VS Code

* 📦 Install **REST Client** extension
* 📄 Create `test.http`
* ▶️ Click **Send Request**

```

## 📁 Project Structure

```
bookstore-api/
├── app.py
├── extensions.py
├── models.py
├── routes.py
├── requirements.txt
├── .env
├── test.http
└── README.md
```

```

## 🌐 Deployment (Render)

* 🔗 Create account on Render
* 📦 New → Web Service
* 🔗 Connect GitHub repo
* ⚙️ Build Command: `pip install -r requirements.txt`
* 🚀 Start Command: `gunicorn app:app`

```

## 📚 What I Learned

* 🌶️ Flask API development
* 🗄️ SQLAlchemy ORM
* 📡 REST API design
* ⚠️ Error handling
* 🧪 API testing
* 📂 Project structuring
* 🚀 Deployment basics

```

## 👨‍💻 Author

**Muhammad Ishaq**

📧 Email: [ishaqriaz12345@gmail.com](mailto:ishaqriaz12345@gmail.com)
🔗 GitHub: [https://github.com/IshaqRiaz](https://github.com/IshaqRiaz)

```

## ⭐ Support

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share it

```

**Built with ❤️ for learning purposes**

```

