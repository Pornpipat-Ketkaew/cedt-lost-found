# CEDT Lost & Found: Project Plan

## 1. Problem Statement

Students in the Computer Engineering and Digital Technology (CEDT) program at Chulalongkorn University often leave personal belongings in classrooms. At present, teaching assistants (TAs) announce found items in Discord channels. These announcements are easily buried by other messages, cannot be searched, and offer no way for a student to report an item they have lost.

**CEDT Lost & Found** is a web application that gives the community one searchable place to report lost and found items and to return them to their owners safely.

## 2. Users

| Role | Description |
|------|-------------|
| **Student** | Loses items, or finds items left behind by others. |
| **Staff / TA** | Finds items after class, manages returns, and verifies ownership. |

Any signed-in user may create both *lost* and *found* posts.

## 3. User Stories

1. As a **TA**, I want to post a photo of an item left in a classroom, so that its owner can see it and contact me.
2. As a **student** who finds an item after class, I want to post it, so that the owner knows who to contact.
3. As a **student** who lost an item, I want to post a photo of it, so that anyone who sees it knows who it belongs to.
4. As a **student** who has no photo of a lost item, I want to describe what it looks like and where I last saw it, so that others can still recognize it.
5. As a **student**, I want to search posts by keyword and category, so that I can quickly check whether my item has been found.
6. As a **student** who claims a found item, I want to submit proof of ownership, so that the finder can return it to me.
7. As a **finder**, I want to approve or reject claims, so that the item is returned to its real owner.
8. As a **student** who has received an item back, I want to mark the post as returned, so that nobody keeps searching for it.

## 4. Scope

### Minimum Viable Product (v1)

- User accounts (register, log in, log out)
- Create *lost* and *found* posts, with an optional photo
- Browse and search posts by keyword and category
- Claim a found item with a message and an optional proof photo
- Approve or reject claims
- Mark a post as returned

### Planned for Later

- Posting without an account (guest posting with moderation)
- Support for multiple organizations beyond CEDT
- Ownership confirmation by votes from other users
- A minimum waiting period before a claim can be approved

## 5. Ownership Verification

To prevent false claims, the finder may record a **secret detail** that is not shown publicly (for example, the contents of a wallet or a phone's wallpaper). A claimant must describe this detail, and may attach a photo as further proof. The finder checks the claimant's student ID when the item is handed over.

## 6. Data Model

```
User
  id, name, email, student_id, password_hash, discord, role (student | staff)

Post
  id, user_id -> User, type (LOST | FOUND), title, detail, category,
  photo (optional), place, pickup_point, secret_detail (FOUND only),
  status (open | returned), created_at

Claim
  id, post_id -> Post, claimer_id -> User, message, proof_photo (optional),
  status (pending | approved | rejected), created_at
```

`->` marks a **foreign key** (a reference to a row in another table).

## 7. Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | React |
| Backend | Python, FastAPI |
| Database | PostgreSQL |

## 8. Roadmap

1. Planning and data model
2. Development environment and repository setup
3. Database and first API endpoints
4. Authentication
5. Image upload and search
6. Frontend
7. Claim workflow
8. Automated tests and continuous integration
9. Deployment
10. Documentation
