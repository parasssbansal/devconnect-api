# DEVConnect API 🚀

A **social networking backend API** built using **FastAPI** that allows developers to create posts, follow other users, and interact through a RESTful API.
This project demonstrates backend development concepts like **authentication, database relationships, CRUD operations, and API deployment**.

---

## 🌐 Live API

API Documentation (Swagger UI):

```
https://devconnect-api-1-ezgx.onrender.com/docs
```

---

## ✨ Features

* User Signup & Login
* Get All Users
* Create and Delete Posts
* Get Posts by User
* Follow / Unfollow Users
* Followers and Following System
* Update User Bio
* RESTful API Design
* Automatic API documentation using Swagger

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Database ORM:** SQLAlchemy
* **Database:** SQLite
* **Language:** Python
* **API Testing:** Swagger UI / Postman
* **Deployment:** Render

---

## 📂 Project Structure

```
devconnect-api
│
├── routers
│   ├── auth.py
│   ├── posts.py
│   ├── follow.py
│   └── users.py
│
├── models
│   ├── user.py
│   ├── post.py
│   └── follow.py
│
├── schemas
│   ├── user_schema.py
│   ├── post_schema.py
│   └── follow_schema.py
│
├── database
│   └── db.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔗 API Endpoints

### Auth

```
POST /auth/signup        Register a new user
POST /auth/login         Login user
GET  /auth/allusers      Get all users
```

---

### Posts

```
POST   /posts/create               Create a post
GET    /posts/getallposts          Get all posts
GET    /posts/getpost/{user_id}    Get posts by a specific user
DELETE /posts/deletepost/{id}      Delete a post
```

---

### Follow System

```
POST   /follow/{user_id}              Follow a user
DELETE /unfollow/{following_id}       Unfollow a user
GET    /followers/{user_id}           Get followers
GET    /following/{user_id}           Get following users
```

---

### User

```
PATCH /changebio/{user_id}      Update user bio
```

---

## ⚙️ Running the Project Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/parasssbansal/devconnect-api.git
cd devconnect-api
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI server

```
uvicorn main:app --reload --port 8009
```

---

## 📖 API Documentation

Once the server starts, open:

```
http://127.0.0.1:8009/docs
```

This will open the **Swagger UI** where you can test all endpoints.

---

## 📸 API Preview

Swagger automatically generates interactive API documentation.

Example response:

<img width="392" height="97" alt="image" src="https://github.com/user-attachments/assets/43c2f8dc-a99a-4af1-b9e0-73a35a5c46a2" />


---

## 🚀 Deployment

The API is deployed using **Render** and is accessible online.

---

## 👨‍💻 Author

**Paras Bansal**

Backend Developer | Python | FastAPI

GitHub:
https://github.com/parasssbansal

---

## ⭐ Future Improvements

* Post Likes
* Comment System
* Feed Algorithm
* Profile Pictures
* Search Users

---
