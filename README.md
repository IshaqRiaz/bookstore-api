Here's the complete README with emojis:

```markdown
# 📚 Bookstore API

A simple RESTful API for managing a book collection. Built with Flask and SQLAlchemy.

## 🛠️ Technologies Used

- 🐍 **Python** 3.x
- 🌶️ **Flask** - Web framework
- 🗄️ **Flask-SQLAlchemy** - Database ORM
- 💾 **SQLite** - Database
- 🔐 **python-dotenv** - Environment variables

## 🚀 How to Run Locally

### 📋 Prerequisites
- Python 3.x installed
- pip (Python package manager)

### 📝 Steps

1. **Clone the repository**
```bash
git clone 
cd bookstore-api
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```
DATABASE_URL=sqlite:///books.db
```

5. **Run the application**
```bash
python app.py
```

6. **Access the API**
```
http://127.0.0.1:5000/books
```

## 📡 API Endpoints

### 1️⃣ Create a Book
**POST** `/books`

**Sample Input:**
```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 15.99,
    "isbn": "9780735211292",
    "publishedDate": "2018-10-16"
}
```

**Sample Output (201 ✅ Created):**
```json
{
    "id": 1
}
```

---

### 2️⃣ Get All Books
**GET** `/books`

**Sample Output (200 ✅ OK):**
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

---

### 3️⃣ Get a Single Book
**GET** `/books/{id}`

**Sample Request:** `GET /books/1`

**Sample Output (200 ✅ OK):**
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

**Sample Output (404 ❌ Not Found):**
```json
{
    "error": "Book not found"
}
```

---

### 4️⃣ Update a Book
**PUT** `/books/{id}`

**Sample Input:**
```json
{
    "price": 12.99
}
```

**Sample Output (200 ✅ OK):**
```json
{
    "message": "Updated"
}
```

---

### 5️⃣ Delete a Book
**DELETE** `/books/{id}`

**Sample Output (200 ✅ OK):**
```json
{
    "message": "Deleted"
}
```

## 🧪 Testing with VS Code

1. Install **REST Client** extension in VS Code
2. Create a `test.http` file with the requests
3. Click **"Send Request"** above each request to test

## 📁 Project Structure

```
bookstore-api/
├── app.py              # Main application file
├── extensions.py       # Database initialization
├── models.py           # Book model
├── routes.py           # API routes
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── test.http          # Test requests (optional)
└── README.md          # This file
```

## 🌐 Bonus: Deploy on Render

1. Create a free account on [Render](https://render.com)
2. Click **"New +"** > **"Web Service"**
3. Connect your GitHub repository
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable: `DATABASE_URL=sqlite:///books.db`
6. Click **"Create Web Service"**

Your API will be live at `https://your-app-name.onrender.com/books` 🎉

## 📄 License

This project is for learning purposes. Feel free to use and modify!
```

