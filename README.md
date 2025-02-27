# Face Recognition-Based User Registration System

This project is a **face recognition-based user registration system** using **Node.js, Python, and MySQL**. It allows users to register using a **unique code** and their **face**, which is processed and stored securely.

## 🛠 Tech Stack
- **Frontend:** React.js (Image conversion to Base64, API communication)
- **Backend:** Node.js (Express, MySQL)
- **Face Processing:** Python (MediaPipe, OpenCV, NumPy)
- **Database:** MySQL

---

## 📌 Features
- **Face-based Registration:** Users register using their real name, unique code, and face image.
- **Face Embedding Generation:** Extracts facial features using **MediaPipe**.
- **Secure Database Storage:** Stores user data and face embeddings in MySQL.
- **Unique Code Verification:** Ensures only authorized users can register.

---

## 📂 Project Structure
```
/Face-Recognition-Registration
│── frontend/             # React.js Frontend (To be built)
│── server.js            # Node.js backend (API, database handling)
│── face_processor.py    # Face processing script (Python, MediaPipe)
│── package.json         # Node.js dependencies
│── README.md            # Project documentation
└── database.sql         # SQL script to create tables
```

---

## ⚡ How It Works
1. **User selects an image in the frontend.**
2. **Frontend converts the image to Base64** and sends it to the backend.
3. **server.js** verifies the unique code and sends the image to **face_processor.py**.
4. **face_processor.py** detects the face and generates a **face embedding**.
5. **server.js** stores the processed data in **MySQL** and updates user details.

---

## 🚀 Future Plans
✔ **Complete Frontend with React.js**  
✔ **Real-time Face Scanning Animation**  
✔ **QR-Based Login using Face Authentication**  
✔ **Decentralized Access Control (Blockchain)**  
✔ **Improved AI-based Face Matching**  

---

## 🐜 Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/guider23/faceScannerForAuthentication.git
cd Face-Recognition-Registration
```

### **2️⃣ Install Dependencies**
```sh
npm install        # Install Node.js dependencies
pip install -r requirements.txt  # Install Python dependencies
```

### **3️⃣ Configure the Database**
- Create a MySQL database and import the **database.sql** file.
- Update `server.js` with your **database credentials**.

#### **SQL Table Creation**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    real_name VARCHAR(255) DEFAULT 'Pending',
    unique_code VARCHAR(50) NOT NULL UNIQUE,
    face_embedding JSON DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert placeholder unique codes for testing
INSERT INTO users (real_name, unique_code) VALUES ('Pending', 'ABC1234'), ('Pending', 'DEF5678'), ('Pending', 'GHI9101');
```

### **4️⃣ Start the Server**
```sh
node server.js
```

### **5️⃣ Test API with Postman or cURL**
Since the frontend is pending, you can test the API using **Postman** or **cURL**:

#### **Postman**
1. Open Postman and create a new `POST` request to `http://localhost:3000/register`.
2. Set the request body to `raw JSON`:
```json
{
  "real_name": "John Doe",
  "unique_code": "ABC1234",
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
}
```
3. Click **Send** and check the response.

#### **cURL**
Alternatively, you can use cURL in the terminal:
```sh
curl -X POST http://localhost:3000/register \
     -H "Content-Type: application/json" \
     -d '{
           "real_name": "John Doe",
           "unique_code": "ABC1234",
           "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
         }'
```

---

## 💡 Contribution
Feel free to contribute by improving the **face recognition model, frontend UI, or database optimization**. Open a PR! 🚀

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---

### 🌟 Star this repo if you like this project! ⭐


# Live Preview on Medium  

[![Read on Medium](https://img.shields.io/badge/📖%20Read%20on%20Medium-black?style=for-the-badge&logo=medium)](https://medium.com/@yourusername/face-recognition-based-user-registration-system-xyz123)

---

## 🔗 Quick Access  
Click the button above to read the full blog post on **Medium**! 🚀  
Get insights on **Face Recognition, AI, and Secure User Registration** with this project.

---
