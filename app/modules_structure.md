# Bootcamp_2025 Backend - Phase 2: Application Anatomy & Design

## 🧩 Domain Modules
### 1. AuthModule
Handles:
- User registration
- Login/logout and session management
- Role-based access control
**Folder:** `app/auth/`

### 2. QueryModule
Handles:
- Query creation and response generation
- Citations and personal query history
**Folder:** `app/query/`

### 3. FeedbackModule
Handles:
- Feedback submission and retrieval for generated responses
**Folder:** `app/feedback/`

### 4. KnowledgeModule
Handles:
- Knowledge ingestion, chunking, embedding, vector indexing
- Data source connectors
**Folder:** `app/knowledge/`

### 5. AdminModule
Handles:
- Connector configuration
- User management and system admin operations
**Folder:** `app/admin/`

---

## ⚙️ Infrastructure Modules
### 1. DatabaseModule
Responsible for MongoDB connection and ORM/ODM setup.  
**Folder:** `app/infrastructure/database/`

### 2. LLMModule
Handles connection and requests to external language/embedding models.  
**Folder:** `app/infrastructure/llm/`

### 3. SharedModule
Contains shared utilities, data models (Pydantic), and configuration helpers.  
**Folder:** `app/shared/`

---

## Project Directory Layout
```
app/
├── __init__.py
├── main.py
├── auth/
│   ├── routes.py
│   ├── models.py
│   └── service.py
├── query/
│   ├── routes.py
│   ├── models.py
│   └── service.py
├── feedback/
│   ├── routes.py
│   ├── models.py
│   └── service.py
├── knowledge/
│   ├── routes.py
│   ├── models.py
│   └── service.py
├── admin/
│   ├── routes.py
│   ├── models.py
│   └── service.py
└── infrastructure/
    ├── database/
    │   └── mongo_client.py
    ├── llm/
    │   └── llm_client.py
    └── shared/
        ├── utils.py
        ├── schemas.py
        └── config.py
```

Each module includes:
- `routes.py` → API endpoints
- `models.py` → Pydantic models or database schemas
- `service.py` → Core logic and business services

This design ensures scalability, module isolation, and clean dependency management.