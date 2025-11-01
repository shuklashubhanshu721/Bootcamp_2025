# 🧩 Debugging Development Plan — MongoDB Integration (Auth Module)

## 🔍 Issue Summary
**Problem:**  
User registration and login routes fall back to mock (in-memory) users instead of using MongoDB.  
**Root Cause:**  
The MongoDB URI in `.env` does not include a database name, so `get_database()` returns `None`, and all DB operations fail silently.

---

## 🧠 Diagnosis Steps
1. Examined [`app/auth/routes.py`](app/auth/routes.py:22) to confirm registration uses `database_module.get_db()`.
2. Verified [`app/infrastructure/database/mongo_client.py`](app/infrastructure/database/mongo_client.py:12) where `self.db = self.client.get_database()` relies on the URI to determine the DB name.
3. Detected `.env` value `DATABASE_URL=mongodb+srv://.../` without a specific database.
4. Confirmed fallback to mock data in the absence of active DB (`active_db is None`).
5. Validated reason using [`test_mongo_connection.py`](test_mongo_connection.py:7) which tests connectivity but not a database reference.

---

## 🧩 Root Cause
❌ **Missing database name in connection string.**  
The pymongo client requires a database name either in the connection string or in `get_database("name")`.  
Without it, the DB object is `None`.

---

## ⚙️ Proposed Fix
1. Update `.env` file to include DB name:
   ```
   DATABASE_URL=mongodb+srv://shubhanshus_db_user:xWgHHQaS9xER5G4T@cluster0.7cca3c5.mongodb.net/bootcamp_2025?appName=Cluster0
   ```
2. Optionally harden code:
   Replace in [`app/infrastructure/database/mongo_client.py`](app/infrastructure/database/mongo_client.py:12):
   ```python
   self.db = self.client.get_database("bootcamp_2025")
   ```
   ensuring fallback to the intended DB even if omitted in URI.

---

## ✅ Verification Plan
1. Run `python test_mongo_connection.py` to confirm successful connection and visible database list.
2. Register a new user through `/register` endpoint → verify insertion in MongoDB `users` collection.
3. Attempt `/login` for same credentials → ensure fetch from Mongo and JWT issued properly.
4. Inspect that mock path (`storage: "in-memory"`) no longer appears in response.

---

## 📊 Debugging Tasks Status

| Step | Task | Status |
|------|-------|--------|
| 1 | Review registration and login logic for DB dependency | ✅ Completed |
| 2 | Validate DatabaseModule connection initialization | ✅ Completed |
| 3 | Read environment variables for Mongo URI | ✅ Completed |
| 4 | Identify root cause (missing DB name) | ✅ Completed |
| 5 | Document fix steps and verification plan | ✅ Completed |
| 6 | Apply patch and test DB flow | ⏳ Pending |

---

## 🧾 Next Steps
- [ ] Update `.env` database URI to include the name.
- [ ] Optionally modify `DatabaseModule` to call `get_database("bootcamp_2025")`.
- [ ] Re-run registration and login tests to confirm persistence.
- [ ] Commit fix with message: `"fix(auth-db): ensure Mongo database name included for persistent user storage"`.