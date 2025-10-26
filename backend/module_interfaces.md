# Phase 2 - Module Responsibilities and Interfaces

## 2.2. Module Responsibilities

### 🧠 **AuthModule**
**Responsibilities:**
- Handles user authentication and authorization.
- Manages `UserProfile` collection.
- Provides secure session handling and role-based access control.
  
**API Endpoints:**
- `POST /api/v1/auth/register` → Register a new user.
- `POST /api/v1/auth/login` → Authenticate a user and return JWT.
- `GET /api/v1/users/me` → Retrieve the authenticated user's profile.

---

### 💬 **QueryModule**
**Responsibilities:**
- Manages `SupportQuery`, `GeneratedResponse`, and `Citation` entities.
- Connects queries to LLM for intelligent responses.
- Tracks and retrieves personal query history.

**API Endpoints:**
- `POST /api/v1/query/submit` → Submit a query for response.
- `GET /api/v1/query/history` → Retrieve user-specific query history.
- `GET /api/v1/query/{id}` → Fetch specific query response.

---

### 👍 **FeedbackModule**
**Responsibilities:**
- Manages `Feedback` entity.
- Collects user feedback (thumbs up/down) for generated responses.

**API Endpoints:**
- `POST /api/v1/feedback` → Submit feedback for a response.
- `GET /api/v1/feedback/{query_id}` → Retrieve feedback for a given query.

---

### 📚 **KnowledgeModule**
**Responsibilities:**
- Handles data ingestion, chunking, vector embedding, and indexing.
- Manages `DataSourceConnector`, `KnowledgeArticle`, `DocumentChunk`, and `Embedding` entities.

**API Endpoints:**
- `POST /api/v1/knowledge/connectors` → Configure or register data connectors.
- `POST /api/v1/knowledge/ingest` → Trigger ingestion and embedding.
- `GET /api/v1/knowledge/status` → View ingestion or embedding job status.

---

### 🧑‍💼 **AdminModule**
**Responsibilities:**
- Administrative operations for connector management and user roles.
- Manages invitation, disabling users, and setting user permissions.

**API Endpoints:**
- `POST /api/v1/admin/users/invite` → Invite new users.
- `PATCH /api/v1/admin/users/{id}/disable` → Disable user access.
- `PATCH /api/v1/admin/users/{id}/role` → Update user roles.

---

## ⚙️ **Infrastructure Modules**

### **DatabaseModule**
Provides a consistent interface to connect and interact with MongoDB Atlas.  
Implements repository pattern for all entities ensuring abstraction in data access.

---

### **LLMModule**
Abstracts communication with external LLM and embedding providers.  
Centralized configuration guarantees uniform handling of prompt, completion, and embedding APIs.

---

### **SharedModule**
Provides reusable utilities, global configurations, and Pydantic schema definitions for consistent typing across the backend.

---

## 2.3. Core Module Design

### 🏗️ Folder Structure
```
root/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── context/
└── backend/
    ├── routers/
    ├── services/
    ├── models/
    ├── dependencies/
    ├── config/
    ├── database/
    ├── llm/
    └── ingestion/
```

### 🧩 Key Design Patterns

**Repository Pattern:**  
- Isolates database access in repository classes.
- Promotes a clean separation between API routes and data access.

**Service Layer:**  
- Contains business logic distinct from routing and repository layers.
- Used in all domain modules (e.g., AuthService, QueryService).

**Pydantic Models:**  
- Ensures data validation and serialization across request/response cycles.

**React Context (Frontend):**  
- Used for managing user session state and authentication tokens.

---

### ✅ Summary
All modules follow a **clean architecture** principle:
- Separation of concerns across routes, services, and repositories.
- Extensible and scalable design ready for distributed development.