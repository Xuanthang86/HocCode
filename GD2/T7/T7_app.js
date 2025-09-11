// // app.js
// const express = require('express');
// const fs = require('fs');
// const path = require('path');
// const sqlite3 = require('sqlite3').verbose();

// const app = express();
// const PORT = process.env.PORT || 3000;

// // --- Middleware: parse JSON
// app.use(express.json());

// // --- Middleware: request logger -> append to access.log
// const accessLogPath = path.join(__dirname, 'access.log');
// function logger(req, res, next) {
//   const line = `[${new Date().toISOString()}] ${req.method} ${req.url}\n`;
//   // appendFileSync is simple for demo; for high load use streams/rotating logs
//   fs.appendFileSync(accessLogPath, line);
//   console.log(line.trim());
//   next();
// }
// app.use(logger);

// // --- Simple auth middleware (demo): check header x-auth === "true"
// function authMiddleware(req, res, next) {
//   // Demo: client should send header x-auth: true
//   const isAuth = (req.headers['x-auth'] === 'true');
//   if (isAuth) return next();
//   // if ajax/json request, return 401; else redirect to /login
//   if (req.headers.accept && req.headers.accept.includes('application/json')) {
//     return res.status(401).json({ error: 'Unauthorized' });
//   }
//   return res.redirect('/login');
// }

// // --- Database (file-based SQLite)
// const DB_FILE = path.join(__dirname, 'db.sqlite');
// const db = new sqlite3.Database(DB_FILE, (err) => {
//   if (err) {
//     console.error('Cannot open DB', err);
//     process.exit(1);
//   }
// });
// db.serialize(() => {
//   db.run(`CREATE TABLE IF NOT EXISTS users (
//     id INTEGER PRIMARY KEY AUTOINCREMENT,
//     name TEXT NOT NULL,
//     age INTEGER
//   )`);
// });

// // --- Routes

// // root
// app.get('/', (req, res) => {
//   res.send('Chào mừng bạn - Backend Tuần 7 (Middleware + DB)');
// });

// // simple login page (demo)
// app.get('/login', (req, res) => {
//   res.send('Trang login (demo). Gửi header x-auth:true để truy cập các route bảo vệ.');
// });

// // CRUD: create user
// app.post('/users', (req, res) => {
//   const { name, age } = req.body;
//   if (!name) return res.status(400).json({ error: 'Name is required' });
//   const stmt = db.prepare('INSERT INTO users(name, age) VALUES(?, ?)');
//   stmt.run(name, age || null, function (err) {
//     if (err) return res.status(500).json({ error: 'DB insert error' });
//     return res.status(201).json({ id: this.lastID, name, age: age || null });
//   });
//   stmt.finalize();
// });

// // read all users (protected by auth middleware)
// app.get('/users', authMiddleware, (req, res) => {
//   db.all('SELECT * FROM users', [], (err, rows) => {
//     if (err) return res.status(500).json({ error: 'DB read error' });
//     res.json(rows);
//   });
// });

// // read one user
// app.get('/users/:id', authMiddleware, (req, res) => {
//   const id = parseInt(req.params.id, 10);
//   db.get('SELECT * FROM users WHERE id = ?', [id], (err, row) => {
//     if (err) return res.status(500).json({ error: 'DB read error' });
//     if (!row) return res.status(404).json({ error: 'User not found' });
//     res.json(row);
//   });
// });

// // update user
// app.put('/users/:id', authMiddleware, (req, res) => {
//   const id = parseInt(req.params.id, 10);
//   const { name, age } = req.body;
//   db.run('UPDATE users SET name = COALESCE(?, name), age = COALESCE(?, age) WHERE id = ?', [name, age, id], function (err) {
//     if (err) return res.status(500).json({ error: 'DB update error' });
//     if (this.changes === 0) return res.status(404).json({ error: 'User not found' });
//     db.get('SELECT * FROM users WHERE id = ?', [id], (err2, row) => {
//       if (err2) return res.status(500).json({ error: 'DB read error' });
//       res.json(row);
//     });
//   });
// });

// // delete user
// app.delete('/users/:id', authMiddleware, (req, res) => {
//   const id = parseInt(req.params.id, 10);
//   db.run('DELETE FROM users WHERE id = ?', [id], function (err) {
//     if (err) return res.status(500).json({ error: 'DB delete error' });
//     if (this.changes === 0) return res.status(404).json({ error: 'User not found' });
//     res.json({ message: 'Deleted' });
//   });
// });

// // error handler (fallback)
// app.use((err, req, res, next) => {
//   console.error('Unhandled error:', err);
//   res.status(500).json({ error: 'Internal server error' });
// });

// // start server
// app.listen(PORT, () => {
//   console.log(`Server running at http://localhost:${PORT}`);
//   console.log(`DB file: ${DB_FILE}`);
// });

















// Import thư viện
const express = require("express");
const app = express();
const port = 3000;

// ------------------- Bài 1: Hello Express -------------------
app.get("/", (req, res) => {
    res.send("Xin chào, đây là bài Hello Express (Tuần 7)!");
});

// ------------------- Bài 2: Middleware -------------------
const myMiddleware = (req, res, next) => {
    console.log("Middleware đang chạy:", req.method, req.url);
    next(); // chuyển tiếp sang bước tiếp theo
};
app.use(myMiddleware);

// ------------------- Bài 3: Router -------------------
const router = express.Router();

router.get("/gioithieu", (req, res) => {
    res.send("Đây là trang giới thiệu (sử dụng Router).");
});

router.get("/lienhe", (req, res) => {
    res.send("Đây là trang liên hệ (sử dụng Router).");
});

app.use("/trang", router);

// ------------------- Bài 4: Static files -------------------
// Tạo thư mục public để chứa ảnh, CSS, JS
app.use(express.static("public"));

// ------------------- Bài 5: Error Handling -------------------
app.use((req, res, next) => {
    res.status(404).send("404 - Không tìm thấy trang!");
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send("500 - Lỗi server!");
});

// ------------------- Khởi động server -------------------
app.listen(port, () => {
    console.log(`Server chạy tại: http://localhost:${port}`);
});
