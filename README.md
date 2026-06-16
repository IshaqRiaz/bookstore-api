📚✨ Bookstore API 🚀
A simple RESTful API for managing a 📖 book collection. Built with 🌶️ Flask and 🗄️ SQLAlchemy.
________________________________________
✨🔥 Features
-	📖 Book Management – Store and manage book records 🗂️
-	➕ Create Books – Add new books to the collection 📚
-	📚 View All Books – Retrieve all available books 📦
-	🔍 Get Single Book – Fetch book details by ID 🆔
-	✏️ Update Books – Modify existing book information 🛠️
-	🗑️ Delete Books – Remove books from the database ❌
-	🗄️ SQLite Database – Lightweight storage system 💾
-	🌐 RESTful API Design – Clean and structured endpoints ⚡
```
## 🛠️💻 Technologies Used
-	🐍 Python 3.x
-	🌶️ Flask – Web framework 🌐
-	🗄️ Flask-SQLAlchemy – Database ORM 🔗
-	💾 SQLite – Database engine 📦
-	🔐 python-dotenv – Environment variables config ⚙️
```
⚙️🚀 How to Run Locally
📋 Prerequisites 🧾
•	🐍 Python 3.x installed
•	📦 pip (Python package manager)
________________________________________
📝 Step-by-Step Guide
1️⃣ Clone the repository 📥
git clone
cd bookstore-api
________________________________________
2️⃣ Create virtual environment 🧪
python -m venv venv

# 🪟 Windows:
venv\Scripts\activate

# 🍎 Mac/Linux:
source venv/bin/activate
________________________________________
3️⃣ Install dependencies 📦
pip install -r requirements.txt
________________________________________
4️⃣ Create .env file 🔐
DATABASE_URL=sqlite:///books.db
________________________________________
5️⃣ Run the application ▶️
python app.py
________________________________________
6️⃣ Access the API 🌐
http://127.0.0.1:5000/books
________________________________________
📡⚡ API Endpoints
________________________________________
➕📖 Create a Book
POST /books
📥 Sample Input
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 15.99,
    "isbn": "9780735211292",
    "publishedDate": "2018-10-16"
}
📤 Response (201 ✅ Created 🎉)
{
    "id": 1
}
________________________________________
📚📦 Get All Books
GET /books
📤 Response (200 ✅ OK)
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
________________________________________
🔍📖 Get Single Book
GET /books/{id}
📥 Request
GET /books/1
📤 Response (200 ✅ OK)
{
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 15.99,
    "isbn": "9780735211292",
    "publishedDate": "2018-10-16"
}
❌ Response (404 Not Found 🚫)
{
    "error": "Book not found"
}
________________________________________
✏️🛠️ Update a Book
PUT /books/{id}
📥 Input
{
    "price": 12.99
}
📤 Response (200 ✅ Updated 🎉)
{
    "message": "Updated"
}
________________________________________
🗑️❌ Delete a Book
DELETE /books/{id}
📤 Response (200 ✅ Deleted)
{
    "message": "Deleted"
}
________________________________________
🧪⚡ Testing with VS Code
1.	📦 Install REST Client extension
2.	📄 Create test.http
3.	▶️ Click Send Request
4.	🔄 Test all endpoints step-by-step
________________________________________
📁🗂️ Project Structure
bookstore-api/
├── 📄 app.py              # Main application 🚀
├── 🧩 extensions.py       # Database setup 🗄️
├── 📚 models.py           # Book model 📖
├── 🌐 routes.py           # API routes ⚡
├── 📦 requirements.txt    # Dependencies 📥
├── 🔐 .env                # Environment variables
├── 🧪 test.http           # API testing file
└── 📘 README.md           # Documentation
________________________________________
📊✅ Evaluation Criteria
Criteria	Status
🏗️ API Design	✅ RESTful structure ⚡
🗄️ Database	✅ SQLite + SQLAlchemy 💾
📖 Documentation	✅ Fully documented 📘
🧪 Testing	✅ REST Client + Postman 📡
💻 Code Quality	✅ Clean & modular 🧩
________________________________________
📚🧠 What I Learned
•	🌶️ Flask API development
•	🗄️ SQLAlchemy ORM usage
•	📡 RESTful API design principles
•	🧱 Database modeling
•	⚠️ Error handling & validation
•	🧪 API testing techniques
•	📂 Project structuring
•	🚀 Deployment basics
________________________________________
👨‍💻💼 Author
Muhammad Ishaq 👨‍💻
📧 Email: ishaqriaz12345@gmail.com
🔗 GitHub: https://github.com/IshaqRiaz
________________________________________
⭐🔥 Support
•	⭐ Star this repo
•	🍴 Fork it
•	📢 Share it
________________________________________
📄 License 📜
This project is for learning purposes only 🎓
________________________________________
Built with ❤️ as Internship Task for DevelopersHub Corporation🚀

