# MSDS 700 Database Management Systems
## Overview

- **Course:** Database Management Systems (MSDS 700)
- **Institution:** Meharry Medical College
- **Instructor:** Dr. M. Zakaria Kurdi
- **Focus:** Theory and practice of DBMS, SQL, data models, architecture, and security

---

## Key Concepts

### ANSI-SPARC Three-Level Architecture

| Level      | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| External   | Individual user/application views; relevant data subset                      |
| Conceptual | Community/global schema; central definitions and relationships               |
| Internal   | Physical storage; data organization and indexes                              |

**Objectives:**
- Immunity to changes between views and physical storage
- Access to consistent data for all users

### Data Independence

- **Logical Data Independence:** Changes to conceptual schema ≠ changes to user views
- **Physical Data Independence:** Changes to storage ≠ changes to schema or user views

### Database Languages

- **DDL (Data Definition Language):** Define database schemas and constraints
- **DML (Data Manipulation Language):** Manipulate/query data (procedural/non-procedural)
- **4GLs:** High-level languages, e.g., SQL

### Data Models

| Type          | Examples                                                                    |
|---------------|-----------------------------------------------------------------------------|
| Object-Based  | Entity-Relationship (ER), Semantic, Functional, Object-Oriented             |
| Record-Based  | Relational, Network, Hierarchical                                           |
| Physical      | Storage layouts, file organization                                          |

### Functions of a DBMS

- Data storage, retrieval, and update
- Metadata/catalog management
- Transaction and concurrency control
- Recovery and integrity services
- Authorization and security
- Utility functions

---

## System Catalog

Stores metadata such as:
- Data types, structures, and constraints
- Authorized users and access permissions
- Usage statistics

---

## DBMS Architectures

| Model         | Description                                             | Pros/Cons                         |
|---------------|--------------------------------------------------------|-----------------------------------|
| Teleprocessing| Mainframe and terminals                                | Simple, outdated                  |
| File-server   | Networked workstations with shared server              | Heavy network traffic             |
| 2-Tier        | Client UI+apps, Server with DBMS                       | Better performance, lower costs   |
| 3-Tier        | Thin client, middleware/business logic, DBMS server    | Scalable, centralized maintenance |

---

## Transaction Processing Monitors (TPMs)

- Middleware for managing consistent transactions between clients/servers
- Handles errors, ensures integrity, shares resources

---

## DBMS Environment: Roles

- **DA:** Data Administrator
- **DBA:** Database Administrator
- **Designers:** Logical/Physical Schema
- **Programmers:** Application Developers
- **End Users:** Naive/Sophisticated

---

## Advantages & Disadvantages

**Advantages:**
- Consistency, integrity, reduced redundancy
- Advanced recovery/backups
- Security and enforcement of standards

**Disadvantages:**
- Complexity, cost, resource requirements
- Conversion and performance issues

---

## Course Structure & Grading
- Assignments: 40%
- Participation: 10%
- Project: 30%
- Midterm: 20%

| Grade  | % Range |
|--------|---------|
| A      | >= 90   |
| B+     | 85-89   |
| B      | 80-84   |
| C+     | 75-79   |
| C      | 70-74   |
| F      | < 70    |

---
